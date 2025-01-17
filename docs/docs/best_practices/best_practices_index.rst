
Best Practices
==============


General Concepts
----------------
.. toctree::
   :maxdepth: 2
   :hidden:
   
   Alternative_Standards
   Authentication
   CORS
   Required_and_Additional_Fields
   RESTfulness
   Versioning
   
The :doc:`BrAPI Community </docs/community/BrAPI_Community>` has developed a set of Best Practices when working with :doc:`BrAPI </docs/get_started/BrAPI>` implementations.

-  :doc:`Alternative Standards <Alternative_Standards>` - Notes on conversions and mappings to other existing standards including MIAPPE, ICASA, MCPD, GeoJSON, and GA4GH Variants Schema
-  :doc:`Authentication <Authentication>` - Notes on Authentication and Authorization, focusing on OAuth2
-  :doc:`Cross-Origin Resource Sharing (CORS) <CORS>` - Notes on common :doc:`CORS <CORS>` errors and how to deal with them
-  :doc:`Required and Additional Fields <Required_and_Additional_Fields>` - Notes on Fields and Parameters when they are Required, Added, and Deprecated
-  :doc:`RESTfulness <RESTfulness>` - General REST best practices, including notes on HTTP verbs, HTTP status codes, and URL construction.
-  :doc:`Versioning <Versioning>` - Notes on BrAPI Versioning Scheme

Implementation Notes
--------------------

.. toctree::
   :maxdepth: 2
   :hidden:
   
   Dates_and_Times
   Object_Identifiers
   Error_Handling
   Location_Coordinates
   Observation_Levels
   Pagination
   Pedigree_Tree
   Search_Services
   
These are notes on how to correctly implement certain specific concepts in BrAPI.

-  :doc:`Dates and Times <Dates_and_Times>` - Notes on encoding Dates and Times
-  :doc:`Object Identifiers <Object_Identifiers>` - Notes on DbIds, Names, PUIs, DOIs, and External References
-  :doc:`Error Handling <Error_Handling>` - Notes on handling Errors
-  :doc:`Location Coordinates <Location_Coordinates>` - Notes on use GPS Coordinates and GeoJSON
-  :doc:`Observation Levels <Observation_Levels>` - Notes on how to represent different types of Observation Units (ie, field, plot, plant, etc)
-  :doc:`Pagination <Pagination>` - Notes on Pagination
-  :doc:`Pedigree Tree Implementation <Pedigree_Tree>` - Guidelines for implementing a Pedigree Tree in BrAPI
-  :doc:`Search Services <Search_Services>` - Notes on Search implementations