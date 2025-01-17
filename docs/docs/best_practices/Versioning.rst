Versioning
==========

Major Versions
--------------
Major versions of the BrAPI spec are accompanied by broad changes to the whole specification. Major versions are not backward compatible with each other. 
When a new major version is built, all the deprecated fields are permanently removed, allowing for a clean slate to start again. 
This is why it is important to indicate the major version in the URL for every BrAPI call. If a server needs to support multiple major versions of the spec,
each version will be implemented under a different base path. 

Minor Versions
--------------
Minor versions are typically smaller updates to the spec, fixing a group of smaller github issues like new search parameters, additional data fields, and mistakes not following best practice. 
Minor versions are backward compatible, so a single response can have all the data fields necessary to support the needs of multiple minor versions. 


Deprecation
-----------
Deprecated fields, parameters, and endpoints indicate that something has been removed or replaced in a minor version update. 

