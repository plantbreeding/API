Dates and Times
===============

Date and timestamp fields are coded in the `ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601>`__ standard, extended format. 
If a given field in the spec has a type `string(date)`, then it is acceptable to only include the date portion, for example "2017-06-16". 
If a given field in the spec has a type `string(date-time)`, then the full date, time, and time zone information needs to be provided, as in this example: "2017-06-16T14:47:23-0600". 

In BrAPI V1, milliseconds are not supported. But in BrAPI V2, milliseconds are 
highly recommended, particularly in cases like Observations and Events when it is 
possible for multiple things to occur in less than a second.  

============================ ======================== ============================
\                            Format                   Example
============================ ======================== ============================
Date                         yyyy-MM-dd               2017-06-16
Timestamp UTC                yyyy-MM-ddThh:mm:ssZ     2017-06-16T20:47:23Z
Timestamp w/ zone            yyyy-MM-ddThh:mm:ssz     2017-06-16T14:47:23-0600
Timestamp w/ milliseconds    yyyy-MM-ddThh:mm:ss.SSSz 2017-06-16T14:47:23.339-0600
============================ ======================== ============================
