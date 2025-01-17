Client Implementation
=====================

A client application will have a set of functions available to communicate data back and forth with a server. These functions 
might be triggered by some user action, or they might be automated to perform actions in the background. They might be 
chained together into a series of API requests to perform a more complex action. In general, each API function must perform the 
following steps:

- Determine an HTTP Method and URL for the desired server endpoint.
- Construct a list of query parameters, or construct a JSON object to be the body.
- If required, add an Authorization token header to the request.
- Send the HTTP request, wait for a response.
- When the response arrives, check the HTTP Status for error codes.
- If there are no errors, convert the JSON response object into a language specific data structure.

Libraries
---------

For several popular programming languages, there are BrAPI client code libraries available, with the functions described above 
for every BrAPI call. The BrAPI community has built client libraries for R, JavaScript, Java, and Drupal (PHP). These libraries 
are available at brapi.org/libraries. They are all open source, community run projects, so please consider contributing back to 
them if you use it.

Alternatively, SwaggerHub has a built in tool called swagger-code-gen. This tool allows you to generate a client library for a 
variety of languages, and download it directly from the SwaggerHub documentation page. On any BrAPI SwaggerHub Page, click the 
"Export" menu in the top right corner, hover over "Client SDK", then select from the list of languages/frameworks.

Note on generated code. Swagger-code-gen is a useful tool for converting API specs into code, but it is not perfect. Generated 
libraries will not be perfect, so be sure to review and test them before using in production.

Testing
-------
The BrAPI Test Server is the primary resource for testing new BrAPI compatible client applications. The BrAPI Test Server has a 
complete implementation of every BrAPI endpoint with every version of the specification. It does not require authorization, but 
has a simple authorization system available for testing if needed. There is a Docker image available on DockerHub, so a 
development team could run the server independently for CI/CD testing.

All the data in the BrAPI Test Server is fake, and in some cases, unrealistic. If you are looking to test against realistic 
data, there are several server implementations within the BrAPI community with real data. Contact the BrAPI Slack channel to 
connect with another group in the community with the data you are looking for.

Authorization
-------------
The BrAPI Community made a decision that the BrAPI standard is not responsible for how different groups implement security. Your
user authentication, authorization, and user management systems are your own responsibility. However, the community agreed that 
an OAuth-like pattern is a best practice for communicating data over an API between systems. Every BrAPI endpoint definition 
includes an “Authorization” header parameter. This header is used by things like OAuth/OpenID for passing an authorization token 
from the client to the server. It was added to support authorization best practices in BrAPI, but it is never required for BrAPI 
compliance.

A client application will get an authorization token (BrAPI does not care how), then make a BrAPI request with that token in the 
“Authorization” header. The server can validate the token (again, BrAPI does not care how this happens) and decide to return a 
response or not. That token might also be used to identify a specific user, so the server will only return the users specific data.

There are many resources/tools online for setting up an OAuth/OpenID pattern. Some basic material has been gathered in this 
BrAPI Wiki article. Reach out to the BrAPI Coordinator or the community Slack channel to discuss options and security patterns 
in more detail.

Example
-------
The brapi-intro-class github is a repository with example BrAPI implementations. All implementations follow the same use case 
where a user is browsing through Programs, Trials, and Studies. The code for getting Programs is included, but the critical code 
for Trials and Studies is missing. Choose a programming language you are most familiar with, and then fill in the missing code to 
complete the use case. 

