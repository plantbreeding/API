Object Identifiers
==================

DbIds
-----

All objects represented in BrAPI have a ``xxxDbId`` field. This field
represents a primary key which will uniquely identify that object
*within the database being queried.* It is NOT guaranteed to be unique
across multiple systems, though it could be. DbIds should primarily be
used to link data together within a system.

For example, in a given call, an Observation Unit object is returned
with the ``studyDbId``. In a subsequent call to the same system, you
should be able to retrieve the Study Object directly based on the
``studyDbId``.

**DbIds Special Case**

There was a special case raised in `GitHub Issue #85 <https://github.com/plantbreeding/API/issues/85>`__ where the DbId
string was a URL (a DOI url in this specific case, but any url will have
the same problem). URLs generally contains the ``/`` character which
makes them difficult to use as parts of the path in a REST call.

Recommendation: If possible, avoid using URLs as DbIds. There are other fields available for communicating a variety of
URLs to a client, reserve the DbId field for a convenient primary key for linking to other objects.

If you must use a URL as a DbId, you must encode it in some way to hide the slashes. Your system will need to accept the encoded string in a
request and decode it before querying the database. Likewise, when responding to a request, your system will need to retrieve the URL from
the database and encode it before returning. The specific encoding schema doesn't matter, as long as it produces consistent results within
your system. `GitHub Issue #85 <https://github.com/plantbreeding/API/issues/85>`__ describes a double URL symbol encoding scheme which works. 

::

  Example: `%252F` is decoded as the slash character 
  .../brapi/v1/germplasm/https%253A%252F%252Fdoi.org%252F10.15454%252F1.4489666216568333E1

Hexadecimal or Base64 encoding are other good options, where the URL becomes an alphanumeric value without slashes. Encoding and decoding this way 
is easy and fast, though the value of the ``DbId`` will lose meaning to any human readers.

::

  Example: The DOI is hex encoded 
  .../brapi/v1/germplasm/68747470733A2F2F646F692E6F72672F31302E31353435342F312E343438393636363231363536383333334531

  Example: The DOI is base64 encoded
  .../brapi/v1/germplasm/aHR0cHM6Ly9kb2kub3JnLzEwLjE1NDU0LzEuNDQ4OTY2NjIxNjU2ODMzM0Ux

PUIs
----

Several BrAPI entities have a ``xxxPUI`` field for a Permanent
Unique Identifier. This is meant to be a global identifier
shared across different data sources. PUIs usually take the form of a
URI, with a combination of identifying authority and unique identity
value. For example, the `Digital Object Identifier (DOI) <https://www.doi.org/>`__ system is often used to assign PUIs.

Unlike DbIds, PUIs are never used in BrAPI paths, so there is no problem
if a PUI contains slashes. In several cases, PUIs can be used as query
parameters, so it can be helpful to use the encoding ``%2F`` to replace
an slash characters in URL query parameters.

.. _external_references:

External References
-------------------

Every BrAPI V2 entity has a list of ``externalReferences``. These are
meant to record additional identifiers for a data object, usually
originating from other tools and systems. This can assist with linking
to different systems, without altering the DbIds or PUIs. A particularly
important use case for using ``externalReferences`` comes from uploading
data to a database. When uploading data, the original DbId is not
preserved by default because it is assumed that each system will assign
a new primary key for new data. The ``externalReferences`` allow the
originating system to preserve a DbId while uploading. This is often
very useful for maintaining links between data.

Names
-----

Most objects represented in BrAPI have a ``xxxName`` field. This field
is meant to be a short, human readable summary of the object. It is NOT
guaranteed to be unique in ANY WAY. Names are a convenient way to
interact with users by printing on a screen or searching. Names may be
created by a human user or generated automatically by some concatenation
of other data points. Name fields should not be used to pass any data
other than the intended human readable reference string. For example,
the name ``Field_Trial_abc123`` should **never** be parsed to extract
``abc123`` as a usable DbId or piece of data.
