Required and Additional Fields
==============================

Required Fields and Parameters
------------------------------
From the perspective of the BrAPI Specification, most data fields are not required. Data fields and parameters that are required by the BrAPI specification are marked in 

Additional Fields and Parameters
--------------------------------
Additional data can be added to any response. Most response objects have an `additionalInfo` section which is a free form JSON object. 

Deprecated Fields and Parameters
--------------------------------
Deprecated endpoints and fields should be included only if the given server wants to support backwards compatibility. 
Deprecated fields can be removed from a response if there is no need to support an earlier version any more. See the section on Versioning for more information.



Hi, I can’t find a response implementation best practice for handling fields not available in a given database. Should we remove the unavailable field from the response or keep it with a null value? I would favor the latest, but I can’t find this in the spec (I might have’nt looked for it enough, sorry)

I think we said it was default NULL.

But it should appear in the specs.

If you use BRAVA, it complains when a field is missing if I'm right (but not if it is null)

that is a good point, I began writing a best practice document addressing this ... but I never finished it
As a response object, it shouldn't really matter if you exclude a field or return null. The client application should interpret both as a lack of data for that field and act accordingly. I make this point in the pagination best practice page when addressing what to do when pagination is not applicable.
However, it does matter when uploading data, particularly when using PUT to edit existing data. In a request object, an excluded field should be ignored, but an explicit null should be accepted to over-write that data field with nothing in the database 

I'll see if I can finish a quick write up this week to document it properly