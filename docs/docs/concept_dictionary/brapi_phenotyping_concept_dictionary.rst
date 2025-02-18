BrAPI-Core Concept Dictionary
==============

Events
-----

An event is discrete occurrence at a particular time in the experiment. Events may be 
the realization of Treatments or parts of Treatments, or may be confounding to 
Treatments. Can be applied at the whole study level or to only a subset of observation 
units.

ICASA Management Events allow for the following types: planting, fertilizer, 
irrigation, tillage, organic_material, harvest, bed_prep, inorg_mulch, inorg_mul_rem, 
chemicals, mowing, observation, weeding, puddling, flood_level, other

[also see the MIAPPE definition]


Images
-----

Calls for retrieving, storing, and updating images and image metadata

Implementation Notes:

The Images endpoints support a GeoJSON object structure for describing their location. 
The BrAPI spec for GeoJSON only supports two of the possible geometries: Points and 
Polygons.

With most images, the Point geometry should be used, and it should indicate the 
longitude and latitude of the camera.

For top down images (ie from drones, cranes, etc), the Point geometry may be used to 
indicate the longitude and latitude of the centroid of the image content, and the 
Polygon geometry may be used to indicate the border of the image content.

An example use case is available on the BrAPI Wiki -> https://wiki.brapi.org/index.php/Image_Upload


Methods
--------

API to manage the details of observation variable Methods. An observation variable is 
composed by the unique combination of one Trait, one Method and one Scale. A Method 
describes the way an observation should be collected. For example, an Observation 
Variable might be defined with a Trait of "plant height", a Scale of "meters", and a 
Method of "tape measure". This Variable would be distinct from a Variable with the 
Method "estimation" or "drone image processing".


Observation Units
------

API to retrieve and submit data regarding Observation Units. An Observation Unit is 
anything that is being observed. Typically, this is a Plot or a Plant, but it could 
include things like Fields or Samples. The Observation Level defines the type of 
Observation Unit. For more information on Observation Levels, please review the 
Observation Levels documentation.


Observation Variables
------

API to retrieve list and details of observation variables. An observation variable 
is composed by the unique combination of one Trait, one Method and one Scale.


Observations
------

API to manage the details of basic phenotypic Observations. An Observation is a 
value assigned for a specific ObservationVariable when observing a specific 
ObservationUnit.



Ontologies
------

API to manage the details of stored Ontologies. This could be a reference a local 
Ontology or a remote public Ontology.



Scales
-----

API to manage the details of observation variable Scales. An observation variable is 
composed by the unique combination of one Trait, one Method and one Scale. A Scale 
describes the units and acceptable values for a Variable. For example, an 
Observation Variable might be defined with a Trait of "plant height", a Scale of 
"meters", and a Method of "tape measure". This Variable would be distinct from a 
Variable with the Scale "inches" or "pixels".


Traits
------

API to manage the details of observation variable Traits. An observation variable is 
composed by the unique combination of one Trait, one Method and one Scale. A Trait 
describes what property is being observed. For example, an Observation Variable might 
be defined with a Trait of "plant height", a Scale of "meters", and a Method of "tape 
measure". This Variable would be distinct from a Variable with the Trait "Leaf length" 
or "Flower height".
