RESTfulness
===========


URL Structure
-------------

API requests are structured as

``https://<host>/brapi/v2/<endpoint>``

where ``<host>`` is the base URL of the API host server, ``v2`` is the major
version number of the supported BrAPI spec, and ``<endpoint>`` is the path of the desired BrAPI endpoint.

Example: ``https://test-server.brapi.org/brapi/v2/germplasm/2939``

To distinguish between multiple databases available from the same
server, include the database name as part of the identifier. An
arbitrary number of levels can be inserted between the domain name and
the brapi level, if needed.

Example:
``https://test-server.brapi.org/maize_db_01/brapi/v2/germplasm/2939``

Example:
``https://test-server.brapi.org/cornell/cals/wheat_db/brapi/v2/germplasm/2939``


Old Notes
---------

-  URL nouns: should be plural. Keep verbs to minimum.
-  Parameter Names : Use camel case, use appropriate suffix e.g. for a
   field that uniquely identifies a study, it should be named studyId.
-  Response codes: Use http error codes for protocol errors. Use
   application specific codes for business domain validation messages.
-  Identifiers
-  In addition to the response fields that are required, additional
   fields may be included in a BRAPI-compliant response.
-  Use HTTP verbs (GET, POST, PUT, DELETE) instead of other verbs in the
   URL wherever possible.
-  HTTP compression should be enabled in the web server if possible.
-  Services should always return all the keys/fields defined in the API
   and set the value to NULL (e.g., not remove keys that don't contain
   any values).
-  Optional parameters error code handling: For some calls there are a
   lot of parameters. It is not necessary to implement all of them in
   all servers. If a not implemented parameters is send to a server, it
   should return an **http error 501** : "not implemented"
