Authentication
==============

It is HIGHLY recommended that every implementation of BrAPI uses some
form of authentication to protect its end points. As long as a common
authentication scheme used for all the tools within an organization, it
is not BrAPI's responsibility to enforce any particular scheme.

However, if all tools within the `BrAPI Community <BrAPI_Community>`__
can use compatible authentication schemes, it will make tool development
and integration development much easier.

To accomplish this, the `BrAPI Community <BrAPI_Community>`__ has
decided to standardize on an `OAuth
2 <https://tools.ietf.org/html/rfc6749>`__ authentication scheme.

**Disclaimer**

This article is intended to show a common authentication pattern which
BrAPI implementors can consider using to help with interconnections
between applications. This article is not meant to be prescribed or
enforced as a fixed standard.

Do your own research and choose the authentication tools and techniques
that work best for you, your tools, and your situation.

.. _oauth_2_basics:

`OAuth 2 <https://tools.ietf.org/html/rfc6749>`__ Basics
--------------------------------------------------------

Resource Owner : An entity capable of granting access to a protected resource. This is usually a real Person, but can also refer to a service account used by an automated process.
Client Application : An application making protected resource requests on behalf of the resource owner and with its authorization. The term "client" does not imply any particular implementation characteristics (e.g. a server, a desktop, a web browser, etc). BrAPI calls are made from here.
Resource Server : The server hosting the protected resources, capable of handling resource requests with access tokens. `BrAPI <BrAPI>`__ server implementation lives here
Authorization Server : The server issuing access tokens to the client after successfully authenticating the resource owner and obtaining authorization.
Access Token : A string token used to prove the resource owner has been authenticated successfully. It is then sent to the Resource Server with every request to be verified.
Grant Type : The method used to exchange the Resource Owner's credentials for an Access Token. This includes the type of credentials, which entities have access to those credentials, and which entities have access to the Access Token.

OAuth 2 is an authorization protocol developed by the IETF OAuth WG
published in 2012. The goal of `OAuth
2 <https://tools.ietf.org/html/rfc6749>`__ is to provide 3rd party
applications with protected user data, without exposing the users
credentials to the 3rd party application. It has grown to become a
standard way to protect public API's, as well as an easy way for
creating accounts using existing credentials from large trusted
authentication providers like Google, Amazon, and Facebook.

In general, OAuth 2 works by exchanging a Resource Owner's secure
credentials with a short lived Access Token. This means a Resource
Owners authenticity can be verified as often as needed but the Resource
Owner does not need to present their credentials every time. The OAuth 2
specification outlines four acceptable methods for exchanging the
credentials for a token. These methods are called Grant Types and they
are outlined in the section below.

**General Recommendations**

-  Use a reputable, 3rd party, tried and tested tool for your
   Authorization Server.
   Do not attempt to build your own. There are many options with a
   variety of prices and features available. One more time for good
   measure: Do not attempt to build your own

-  The Authorization Server should exists as a separate entity from the
   Resource Server.
   The Authorization Server may need to be maintained and secured
   differently than a Resources Server. Also, it is generally bad
   practice to keep user credential information in the same database as
   high traffic business data.

-  The Authorization server should represent a specific group of users,
   not a specific application
   Often, you will have one Authorization Server connected to a user
   management database for an organization. The users in that
   organization might have access to several different Resource Servers
   and Client tools.

.. _grant_types:

Grant Types
-----------

**Grant Type** refers to the type credentials and method used by the
Resource Owner to prove themselves to the Authorization Server. OAuth2
outlines four different Grant Types, each with different strengths and
weaknesses.

.. _authorization_code_grant:

Authorization Code Grant
^^^^^^^^^^^^^^^^^^^^^^^^

.. image:: images/OAuth_Authorization_Code_Grant.png
   :width: 800
   :alt: Authorization Code Grant

Authorization Code Grant is recommended
  when the Resource Owner is a real person and the Client Application
  can not be trusted with the Resource Owners credentials, such as a web
  application. This is the recommended Grant Type for most BrAPI use
  cases which involve a user retrieving data.

.. _client_credentials_grant:

Client Credentials Grant
^^^^^^^^^^^^^^^^^^^^^^^^

.. image:: images/OAuth_Client_Credentials_Grant.png
   :width: 800
   :alt: Client Credentials Grant

Client Credentials Grant is recommended
  when the Client Application is the Resource Owner (such as a script or
  automatic process) and can be trusted with its own credentials. These
  credentials could be a service account username and password, a shared
  private key, or a public/private key pair. This is the recommended
  Grant Type for any BrAPI use cases which involve a tools passing data
  automatically.

.. _implicit_grant:

Implicit Grant
^^^^^^^^^^^^^^

.. image:: images/OAuth_Implicit_Grant.png
   :width: 800
   :alt: Implicit Grant

ImplicitGrant.png Implicit Grant is a simplified version of
  Authorization Code Grant. It is recommended to use Authorization Code
  Grant hen possible, but Implicit Grant is acceptable when necessary.

.. _resource_owner_password_credentials_grant:

Resource Owner Password Credentials Grant
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. image:: images/OAuth_Resource_Owner_Password_Credentials_Grant.png
   :width: 800
   :alt: Resource Owner Password Credentials Grant

ResourceOwnerPasswordCredentialsGrant.png Resource Owner Password
  Credentials Grant involves giving the Resource Owner credentials
  directly to the Client so that the Client can obtain a token. This
  Grant Type is generally not advised if one of the other options is
  available. The Client must be completely trusted by the Resource Owner
  and the Authorization Server to handle confidential password data.

Tokens
------

.. _simple_tokens:

Simple Tokens
^^^^^^^^^^^^^

Simple Tokens are short, alpha-numeric strings which represent the
Resources Owner's authenticated status. They should be relatively short
compared to Signed Tokens, but long enough to remain unique for the
duration of their existence. They should be cryptographically random,
meaning you can not guess the next one from the previous one.

When a Simple Token is passed to a Resource Server during a request, the
server must immediately make a call to the Authorization Server to
verify the token. If the token is valid and has not reached its time out
limit, The Authorization Server may respond with basic account
information for the Resource Owner. The account information should have
an account identifier for identifying the Resource Owner and may also
include scope information. This scope tells the Resource Server which
resources are allowed to be returned.

.. _signed_tokens:

Signed Tokens
^^^^^^^^^^^^^

Signed Tokens are variable length, alpha-numeric strings which represent
the Resources Owner's authenticated status. Signed Tokens are typically
longer than Simple Tokens because they have data encoded inside them.
`JSON Web Tokens (JWT) <https://jwt.io/introduction/>`__ are the popular
standard for signed tokens right now. JWTs work by building a JSON
object with the relevant information, then encrypting a copy of the same
JSON string. This encrypted copy forms the signature. The original JSON
and signature are then concatenated together and the whole thing is
encoded using Base64. This Base64 encoded string is the token.

When a JWT is passed to a Resource Server, the server can verify it
without contacting the Authorization Server. The Resource server must
un-encrypt the signature to confirm the token is legitimate, then it
must compare the original JSON string with the un-encrypted signature to
prove nothing has been altered in transit. Finally, the Resource Server
can extract the token time out and scope information directly from the
JSON object. This scope tells the Resource Server which resources are
allowed to be returned.

It is recommended to use Signed Tokens with BrAPI endpoints whenever
possible.

Scenarios
---------

.. _scenario_1_global_resource_server:

- **Scenario #1: Global Resource Server**

|  In this scenario, there is one centralized Resource Server which
   contains all the data from several different organizations. This
   Resource Server has its own web client and several external tools which
   can access the data.


- **Scenario #2: Local Resource Server**

- **Scenario #3: Server to Server**

- **Scenario #4: Web Client Hosted Locally**

- **Scenario #5: Web Client Hosted Globally**

- **Scenario #6: Desktop or Mobile Application**

- **Scenario #7: Experimental Scripts, Generic Clients**

.. _auth_external_resources:

External Resources
------------------

-  RFC 6749 (OAuth2) -- https://tools.ietf.org/html/rfc6749
-  OAuth.net -- https://oauth.net/2/
-  JSON Web Token -- https://jwt.io/introduction/
