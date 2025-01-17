Observation Levels
==================

Definitions
-----------

-  **Observation Unit**: An Observation Unit is anything that is being
   observed. Typically, this is a Plot or a Plant, but it could include
   things like Fields or Samples.
-  **Observation Level**: The Observation Level describes the level of
   an Observation Unit within a field layout hierarchy. This describes
   the type of thing and Observation Unit represents.

Motivation
----------

The concept of Observation Levels is important to the BrAPI community
because of the diverse way observations can be grouped. Different
breeding programs and the software that support those programs can
organize their fields and their data in different ways. For example,
while most systems have the concept of a Plot level observations, not
all systems support a Sub-Plot level observation or a Field level
observation.

Observation Levels also act as a way to add positional information to an
Observation Unit. For example, using levels, you can define a particular
Observation Unit to be located at Field:2, Block: 14, Rep: 4, Plot:35.

Accepted Levels
---------------

According to the current BrAPI spec, the accepted values for Observation
Level are listed below. An implementation might use additional levels
not listed here, but please try to conform to these accepted values
whenever possible.

-  study
-  field
-  entry
-  rep
-  block
-  sub-block
-  plot
-  sub-plot
-  plant
-  pot
-  sample


Implementation Notes
--------------------

GET /observationlevels
^^^^^^^^^^^^^^^^^^^^^^

The ``GET /observationlevels`` endpoint is designed to list all the
available Observation Levels available in a server AND give them an
ordered hierarchy. The response field ``levelName`` is the name of that
level (see Accepted Levels above). The response field ``levelOrder``
defines where that level exists in the hierarchy of levels. Lower
numbers are at the top of the hierarchy (ie field -> 1) and higher
numbers are at the bottom of the hierarchy (ie plant -> 9). The query
parameters ``programDbId``, ``trialDbId``, and ``studyDbId`` allow this
list to be filtered to show Observation Levels only used by particular
programs, trials, or studies.

*Example*

This example shows that this server only uses 5 observation levels. The
``levelOrder`` shows the nested hierarchy of the levels.


.. code-block:: json

   {
      "result": {
         "data": [
            {
               "levelName": "field",
               "levelOrder": 1
            },
            {
               "levelName": "block",
               "levelOrder": 2
            },
            {
               "levelName": "plot",
               "levelOrder": 3
            },
            {
               "levelName": "sub-plot",
               "levelOrder": 4
            },
            {
               "levelName": "plant",
               "levelOrder": 5
            }
         ]
      }
   }

.. _get_studies:

GET /studies
^^^^^^^^^^^^

The ``Study`` object also contains a list of Observation Levels. This
structure is exactly the same as ``GET /observationlevels`` above, but
instead of applying to the whole server, it only applies to the attached
``Study`` object. The list included in the ``Study`` object should be a
sub-set of the list for the whole server.

.. _get_observationunits:

GET /observationunits
^^^^^^^^^^^^^^^^^^^^^

``Observation Unit`` objects each contain a few important fields related
to Observation Levels.

-  ``observationLevel`` describes the level of the attached Observation
   Unit. This includes the level name and hierarchy order value as
   before. It also includes a ``levelCode`` value to apply to the
   particular Observation Unit. ``levelCode`` is an unrestricted text
   field, so the value could be a number or alphanumeric ID of any kind.

Example: if the ``levelName`` is "plot", then the ``levelCode`` might be
"Plot_00123" representing the plot number represented by that
Observation Unit.


.. code-block:: json

   {
      "observationLevel": {
         "levelCode": "Plot_00123",
         "levelName": "plot",
         "levelOrder": 3
      }
   }

-  ``observationLevelRelationships`` is a list of level tags for the
   attached Observation Unit. This should include a ``levelCode`` for
   every level above the current ``observationLevel``. This is where
   things like Field number, Block, Rep, etc should be recorded for an
   Observation Unit. If a level has an ``ObservationUnit`` associated
   with it, include the ``observationUnitDbId``. This is intended to
   construct a strict hierarchy of observationUnits. If there is no
   ``ObservationUnit`` associated with this level, the 
   ``observationUnitDbId`` field can set to NULL or omitted from the
   response.

Example: With the ``observationLevel`` above declaring this Observation
Unit to be a Plot, then the Field and Block numbers might be defined
like this. In this example, the Block level has an associated
``ObservationUnit`` so the ``observationUnitDbId`` is included, while
the Field level has no associated ``ObservationUnit``, so the
``observationUnitDbId`` is null for the Field level.


.. code-block:: json

   {
      "observationLevelRelationships": [
         {
            "levelCode": "Field_01",
            "levelName": "field",
            "levelOrder": 1,
            "observationUnitDbId": null
         },
         {
            "levelCode": "Block_012",
            "levelName": "block",
            "levelOrder": 2,
            "observationUnitDbId": "017f17d5-c420-4723-94ea-64d4379975b2"
         }
      ]
   }
