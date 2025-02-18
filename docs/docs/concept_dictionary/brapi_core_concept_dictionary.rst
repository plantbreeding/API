BrAPI-Core Concept Dictionary
==============================

Crop
-----

For multi crop systems this is a useful call to list all the supported crops.


List
-----

Generic lists of item IDs


Location
--------

Physical locations


People
------

Maintaining information about people


Program
-------

A BrAPI Program represents the high level organization or group who is responsible for conducting 
trials and studies. Things like Breeding Programs and Funded Projects are considered BrAPI Programs. 
A Program can contain multiple Trials. A Trial can contain multiple Studies.


Season
------

A season is made of 2 parts; the primary year and a term which defines a segment of the year. This 
could be a traditional season, like "Spring" or "Summer" or this could be a month, like "May" or 
"June" or this could be an arbitrary season name which is meaningful to the breeding program like 
"PlantingTime_3" or "Season E".


Study
------

Study is defined as a phenotyping experiment conducted at a single geographic location. One Trial 
can have multiple studies conducted (e.g. multi location international trials). A "study" in BrAPI 
represents a "study" in MIAPPE (Minimal Information about a Plant Phenotyping Experiment).


Trial
-----

Services related to trials. Trials comprise of multiple studies. A "trial" in BrAPI represents an 
"investigation" in MIAPPE (Minimal Information about a Plant Phenotyping Experiment).
