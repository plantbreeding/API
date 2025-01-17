
import requests
import webbrowser
from threading import Lock
from fastapi import FastAPI
import uvicorn
from pyoauth2.client import OAuth2AuthorizationFlow, FileStorage, OAuth2APIRequest
import contextlib
import time
import threading
import uvicorn

class Server(uvicorn.Server):
    def install_signal_handlers(self):
        pass

    @contextlib.contextmanager
    def run_in_thread(self):
        thread = threading.Thread(target=self.run)
        thread.start()
        try:
            while not self.started:
                time.sleep(1e-3)
            yield
        finally:
            self.should_exit = True
            thread.join()

class BrAPIRequest(OAuth2APIRequest):
    def __init__(self, access_token):
        OAuth2APIRequest.__init__(self, access_token)
        self.authorization_header = {"Authorization": "Bearer %s" % self.access_token}

code_lock = Lock()
code_val = {"code": ""}

async def root(code: str):
    code_val["code"] = code
    code_lock.release()

async def lifespan_func(app: FastAPI):
     code_lock.acquire()
     print("temp server start")
     yield
     print("temp server shutdown")
    
def redirect_function(url):
    print("hello?")
    app = FastAPI(lifespan=lifespan_func)
    app.add_api_route("/login/redirect", root)

    config = uvicorn.Config(app=app, host="127.0.0.1", port=8000, log_level="info")
    server = Server(config=config)
    with server.run_in_thread():
        webbrowser.open_new_tab(url)
        with code_lock:
            print(code_val["code"] )

    return code_val["code"] 


def retrieve_authorization_code(required_params,
                                       extra_auth_params,
                                       extra_token_params, redirect_func=None):
        """ retrieve authorization code to get access token
        """
        
        request_param = {
            "client_id": required_params['client_id'],
            "redirect_uri": required_params['redirect_uri'],
            'scope' : required_params['scope']
        }

        if extra_auth_params:
            request_param.update(extra_auth_params)

        r = requests.get(required_params['auth_uri'], params=request_param,
                         allow_redirects=False)
        url = r.url
        return url      

if __name__ == '__main__':

    yt_feed_uri = r"https://test-server.brapi.org/brapi/v2/studies"

    required_params = {
        'client_id': "exampleClient",
        'client_secret': "pnosdgBScMmNVc2vpY1cEwBYjsImpAZn",
        'auth_uri': "https://auth.brapi.org/realms/brapi/protocol/openid-connect/auth",
        'token_uri': "https://test-server.brapi.org/realms/brapi/protocol/openid-connect/token",
        'scope': [r'openid profile'],
        'redirect_uri': "http://localhost:8000/login/redirect"
        }

    extra_auth_params = {
        'response_type': "code",
        'access_type': "offline"
        }

    extra_token_params = {
        'grant_type': "authorization_code",
        }

    # storage = FileStorage('/example_client.dat')
    # credentials = storage.get()
    credentials = None
    input("proceed?")
    if credentials is None:
        flow = OAuth2AuthorizationFlow(required_params,
                                       extra_auth_params,
                                       extra_token_params,
                                       False)
        

        code = flow.retrieve_authorization_code(redirect_func=redirect_function)
        flow.set_authorization_code(code)
        credentials = flow.retrieve_token()
        # storage.save(credentials)
    
    access_token = credentials['access_token']
    
    req = BrAPIRequest(access_token)
    data = req.request(yt_feed_uri)
    print(data)


