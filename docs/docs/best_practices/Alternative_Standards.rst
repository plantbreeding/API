Alternative Standards
=====================

MIAPPE
------
.. toctree::
   :maxdepth: 2
   :hidden:
   
   MIAPPE
   
Here is the complete list of :doc:`MIAPPE to BrAPI Field Mappings <MIAPPE>`

BrAPI V2 endpoints required to fully support MIAPPE data:

-  GET /trials
-  GET /studies
-  GET /locations
-  GET /germplasm
-  GET /observationunits
-  GET /events
-  GET /samples
-  GET /variables

ICASA
-----

In BrAPI V2.1, the `/events` endpoint was made compatible with the International Consortium for Agricultural Systems Applications (ICASA) controlled vocabulary. This common standard connects BrAPI to agronomy focused software projects including `ARDN <https://agmip.github.io/ARDN/>`__ and `DSSAT <https://github.com/DSSAT/dssat-csm-os>`__. Visit the `ICASA Data Dictionary <https://docs.google.com/spreadsheets/u/0/d/1MYx1ukUsCAM1pcixbVQSu49NU-LfXg-Dtt-ncLBzGAM/pub?output=html#>`__ for more information about the ICASA agronomy data model.

MCPD
----

Multi-Crop Passport Descriptors (MCPD) "is a widely used international standard to facilitate germplasm passport information exchange" (`BioversityInternational.org <https://www.bioversityinternational.org/e-library/publications/detail/faobioversity-multi-crop-passport-descriptors-v21-mcpd-v21/>`__). In BrAPI, the primary way to share Germplasm data is through the "GET /germplasm" endpoint. This endpoint has 24 fields out of the available 41 MCPD fields. The BrAPI specification also defines the endpoint "GET /germplasm/{germplasmDbId}/mcpd". This alternate endpoint allows a user to access all 41 MCPD compliant data points when looking at a specific germplasm entry. 

GeoJSON
-------

`GeoJSON <https://geojson.org/>`__ is a standard format for defining GPS coordinates and areas. It provides a specific JSON structure that is commonly used in other APIs across industries, including digital maps, satellite imagery, and navigation. BrAPI has adopted the GeoJSON standard for Images, Locations, and Observation Units. The full GeoJSON specification defines many different types of locations and areas that could be recorded, BrAPI has adopted a slightly simplified version. The only types of GPS data BrAPI cares about are point like objects (ie the source of an image) and simple polygon areas (ie the outline of a plot.

Please see best practices document :doc:`"Location Coordinates" <Location_Coordinates>` for more information. 

GA4GH Variants Schema
---------------------

The `Global Alliance for Genomics and Health (GA4GH) <https://www.ga4gh.org/>`__ developed an API schema for managing genotyping data. This `Variants API schema <https://ga4gh-schemas.readthedocs.io/en/latest/api/variants.html>`__ forms the basis for the BrAPI-Genotyping module, with additions based on community input. The schema is originally based on the VCF file format, and represents all the concepts presented in a VCF. The Variants API is very thorough and robust, however the BrAPI community has found it to be somewhat inefficient for medium to large variant datasets. Community working groups have made an effort to augment the schema with some more performant endpoints, while staying compliant to the original GA4GH specification. 



