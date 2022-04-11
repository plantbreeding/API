
# Group Genome Maps

Retrieving genetic or physical maps
- type: [Genetic | Physical]
- unit: [cM | Mb]
- linkageGroup: may be scaffold (i.e. linkageGroupCount may consist of chromosomes or scaffolds or a combination of the two)
- For genetic maps, map naming convention should tell whether it is a consensus or mapping population (name of population) map for genetic maps
- For physical maps, map naming convention should tell whether it is a reference genome (name of line) or pan-genome





### Get - /maps [GET /brapi/v2/maps{?mapDbId}{?mapPUI}{?scientificName}{?type}{?trialDbId}{?studyDbId}{?commonCropName}{?programDbId}{?page}{?pageSize}]

Get list of maps



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|additionalInfo|object|Additional arbitrary info|
|comments|string|Additional comments|
|commonCropName|string|The common name of the crop|
|documentationURL|string (uri)|A URL to the human readable documentation of this object|
|linkageGroupCount|integer|The number of linkage groups present in this genomic map|
|mapDbId|string|The ID which uniquely identifies this genomic map|
|mapName|string|A human readable name for this genomic map|
|mapPUI|string|The DOI or other permanent identifier for this genomic map|
|markerCount|integer|The number of markers present in this genomic map|
|publishedDate|string (date-time)|The date this genome was published|
|scientificName|string|Full scientific binomial format name. This includes Genus, Species, and Sub-species|
|type|string|The type of map this represents, usually "Genetic"|
|unit|string|The units used to describe the data in this map|


 

+ Parameters
    + mapDbId (Optional, ) ... The primary DbId for this genomic map
    + mapPUI (Optional, ) ... The DOI or other permanent identifier for this genomic map
    + scientificName (Optional, ) ... Full scientific binomial format name. This includes Genus, Species, and Sub-species
    + type (Optional, ) ... Type of map
    + trialDbId (Optional, ) ... Unique Id to filter by Trial
    + studyDbId (Optional, ) ... Unique Id to filter by Study
    + commonCropName (Optional, ) ... The BrAPI Common Crop Name is the simple, generalized, widely accepted name of the organism being researched. It is most often used in multi-crop systems where digital resources need to be divided at a high level. Things like 'Maize', 'Wheat', and 'Rice' are examples of common crop names.Use this parameter to only return results associated with the given crop. Use `GET /commoncropnames` to find the list of available crops on a server.
    + programDbId (Optional, ) ... Use this parameter to only return results associated with the given Program unique identifier. <br/>Use `GET /programs` to find the list of available Programs on a server.
    + page (Optional, ) ... Used to request a specific page of data to be returned.The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.
    + pageSize (Optional, ) ... The size of the pages to be returned. Default is `1000`.
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>




+ Response 200 (application/json)
```
{
    "@context": [
        "https://brapi.org/jsonld/context/metadata.jsonld"
    ],
    "metadata": {
        "datafiles": [],
        "pagination": {
            "currentPage": 0,
            "pageSize": 1000,
            "totalCount": 10,
            "totalPages": 1
        },
        "status": [
            {
                "message": "Request accepted, response successful",
                "messageType": "INFO"
            }
        ]
    },
    "result": {
        "data": [
            {
                "additionalInfo": {},
                "comments": "Comments about this map",
                "commonCropName": "Paw Paw",
                "documentationURL": "https://brapi.org",
                "linkageGroupCount": 5,
                "mapDbId": "142cffd5",
                "mapName": "Genome Map 1",
                "mapPUI": "doi:10.3207/2959859860",
                "markerCount": 1100,
                "publishedDate": "2018-01-01T14:47:23-0600",
                "scientificName": "Zea mays",
                "type": "Genetic",
                "unit": "cM"
            }
        ]
    }
}
```

+ Response 400 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - Malformed JSON Request Object\n\nERROR - 2018-10-08T18:15:11Z - Invalid query parameter\n\nERROR - 2018-10-08T18:15:11Z - Required parameter is missing"
```

+ Response 401 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - Missing or expired authorization token"
```

+ Response 403 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - User does not have permission to perform this action"
```




### Get - /maps/{mapDbId} [GET /brapi/v2/maps/{mapDbId}]

Provides the number of markers on each linkageGroup and the max position on the linkageGroup



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|additionalInfo|object|Additional arbitrary info|
|comments|string|Additional comments|
|commonCropName|string|The common name of the crop|
|documentationURL|string (uri)|A URL to the human readable documentation of this object|
|linkageGroupCount|integer|The number of linkage groups present in this genomic map|
|mapDbId|string|The ID which uniquely identifies this genomic map|
|mapName|string|A human readable name for this genomic map|
|mapPUI|string|The DOI or other permanent identifier for this genomic map|
|markerCount|integer|The number of markers present in this genomic map|
|publishedDate|string (date-time)|The date this genome was published|
|scientificName|string|Full scientific binomial format name. This includes Genus, Species, and Sub-species|
|type|string|The type of map this represents, usually "Genetic"|
|unit|string|The units used to describe the data in this map|


 

+ Parameters
    + mapDbId (Required, ) ... The internal db id of a selected map
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>




+ Response 200 (application/json)
```
{
    "@context": [
        "https://brapi.org/jsonld/context/metadata.jsonld"
    ],
    "metadata": {
        "datafiles": [],
        "pagination": {
            "currentPage": 0,
            "pageSize": 1000,
            "totalCount": 10,
            "totalPages": 1
        },
        "status": [
            {
                "message": "Request accepted, response successful",
                "messageType": "INFO"
            }
        ]
    },
    "result": {
        "additionalInfo": {},
        "comments": "Comments about this map",
        "commonCropName": "Paw Paw",
        "documentationURL": "https://brapi.org",
        "linkageGroupCount": 5,
        "mapDbId": "142cffd5",
        "mapName": "Genome Map 1",
        "mapPUI": "doi:10.3207/2959859860",
        "markerCount": 1100,
        "publishedDate": "2018-01-01T14:47:23-0600",
        "scientificName": "Zea mays",
        "type": "Genetic",
        "unit": "cM"
    }
}
```

+ Response 400 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - Malformed JSON Request Object\n\nERROR - 2018-10-08T18:15:11Z - Invalid query parameter\n\nERROR - 2018-10-08T18:15:11Z - Required parameter is missing"
```

+ Response 401 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - Missing or expired authorization token"
```

+ Response 403 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - User does not have permission to perform this action"
```

+ Response 404 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - The requested object DbId is not found"
```




### Get - /maps/{mapDbId}/linkagegroups [GET /brapi/v2/maps/{mapDbId}/linkagegroups{?page}{?pageSize}]

Get the Linkage Groups of a specific Genomic Map. A Linkage Group is the BrAPI generic term for a named section of a map. A Linkage Group can represent a Chromosome, Scaffold, or Linkage Group.



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|additionalInfo|object|Additional arbitrary info|
|linkageGroupName|string|The Uniquely Identifiable name of this linkage group|
|markerCount|integer|The number of markers associated with this linkage group|
|maxPosition|integer|The maximum position of a marker within this linkage group|


 

+ Parameters
    + mapDbId (Required, ) ... The internal db id of a selected map
    + page (Optional, ) ... Used to request a specific page of data to be returned.The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.
    + pageSize (Optional, ) ... The size of the pages to be returned. Default is `1000`.
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>




+ Response 200 (application/json)
```
{
    "@context": [
        "https://brapi.org/jsonld/context/metadata.jsonld"
    ],
    "metadata": {
        "datafiles": [],
        "pagination": {
            "currentPage": 0,
            "pageSize": 1000,
            "totalCount": 10,
            "totalPages": 1
        },
        "status": [
            {
                "message": "Request accepted, response successful",
                "messageType": "INFO"
            }
        ]
    },
    "result": {
        "data": [
            {
                "additionalInfo": {},
                "linkageGroupName": "Chromosome 3",
                "markerCount": 150,
                "maxPosition": 2500
            }
        ]
    }
}
```

+ Response 400 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - Malformed JSON Request Object\n\nERROR - 2018-10-08T18:15:11Z - Invalid query parameter\n\nERROR - 2018-10-08T18:15:11Z - Required parameter is missing"
```

+ Response 401 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - Missing or expired authorization token"
```

+ Response 403 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - User does not have permission to perform this action"
```

+ Response 404 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - The requested object DbId is not found"
```




### Get - /markerpositions [GET /brapi/v2/markerpositions{?mapDbId}{?linkageGroupName}{?variantDbId}{?minPosition}{?maxPosition}{?page}{?pageSize}]

Get marker position information, based on Map, Linkage Group, and Marker ID



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|additionalInfo|object|Additional arbitrary info|
|linkageGroupName|string|The Uniquely Identifiable name of this linkage group|
|mapDbId|string|The unique ID of the map|
|mapName|string|The human readable name of the map|
|position|integer|The position of a marker within a linkage group|
|variantDbId|string|Internal db identifier|
|variantName|string|The human readable name for a marker|


 

+ Parameters
    + mapDbId (Optional, ) ... unique id of a map
    + linkageGroupName (Optional, ) ... The chromosome identifier or the generic linkage group identifier if the chromosome is not applicable.
    + variantDbId (Optional, ) ... The unique id for a marker
    + minPosition (Optional, ) ... The minimum position
    + maxPosition (Optional, ) ... The maximum position
    + page (Optional, ) ... Used to request a specific page of data to be returned.The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.
    + pageSize (Optional, ) ... The size of the pages to be returned. Default is `1000`.
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>




+ Response 200 (application/json)
```
{
    "@context": [
        "https://brapi.org/jsonld/context/metadata.jsonld"
    ],
    "metadata": {
        "datafiles": [],
        "pagination": {
            "currentPage": 0,
            "pageSize": 1000,
            "totalCount": 10,
            "totalPages": 1
        },
        "status": [
            {
                "message": "Request accepted, response successful",
                "messageType": "INFO"
            }
        ]
    },
    "result": {
        "data": [
            {
                "additionalInfo": {},
                "linkageGroupName": "Chromosome 3",
                "mapDbId": "3d52bdf3",
                "mapName": "Genome Map 1",
                "position": 2390,
                "variantDbId": "a1eb250a",
                "variantName": "Marker_2390"
            }
        ]
    }
}
```

+ Response 400 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - Malformed JSON Request Object\n\nERROR - 2018-10-08T18:15:11Z - Invalid query parameter\n\nERROR - 2018-10-08T18:15:11Z - Required parameter is missing"
```

+ Response 401 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - Missing or expired authorization token"
```

+ Response 403 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - User does not have permission to perform this action"
```




### Post - /search/markerpositions [POST /brapi/v2/search/markerpositions]

Submit a search request for `MarkerPositions`<br/>
Search requests allow a client to send a complex query for data. However, the server may not respond with the search results immediately. 
If a server needs more time to process the request, it might respond with a `searchResultsDbId`. 
Use the corresponding `GET /search/markerpositions/{searchResultsDbId}` to retrieve the results of the search. <br/> 
Review the <a target="_blank" href="https://wiki.brapi.org/index.php/Search_Services#POST_Search_Entity">Search Services documentation</a> for additional implementation details.

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|linkageGroupNames|array[string]|The Uniquely Identifiable name of this linkage group|
|mapDbIds|array[string]|The unique ID of the map|
|maxPosition|integer|The maximum position|
|minPosition|integer|The minimum position|
|page|integer|Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.|
|pageSize|integer|The size of the pages to be returned. Default is `1000`.|
|variantDbIds|array[string]|Internal db identifier|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|additionalInfo|object|Additional arbitrary info|
|linkageGroupName|string|The Uniquely Identifiable name of this linkage group|
|mapDbId|string|The unique ID of the map|
|mapName|string|The human readable name of the map|
|position|integer|The position of a marker within a linkage group|
|variantDbId|string|Internal db identifier|
|variantName|string|The human readable name for a marker|


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "linkageGroupNames": [
        "Chromosome 2",
        "Chromosome 3"
    ],
    "mapDbIds": [
        "7e6fa8aa",
        "bedc418c"
    ],
    "maxPosition": 4000,
    "minPosition": 250,
    "page": 0,
    "pageSize": 1000,
    "variantDbIds": [
        "a0caa928",
        "f8894a26"
    ]
}
```



+ Response 200 (application/json)
```
{
    "@context": [
        "https://brapi.org/jsonld/context/metadata.jsonld"
    ],
    "metadata": {
        "datafiles": [],
        "pagination": {
            "currentPage": 0,
            "pageSize": 1000,
            "totalCount": 10,
            "totalPages": 1
        },
        "status": [
            {
                "message": "Request accepted, response successful",
                "messageType": "INFO"
            }
        ]
    },
    "result": {
        "data": [
            {
                "additionalInfo": {},
                "linkageGroupName": "Chromosome 3",
                "mapDbId": "3d52bdf3",
                "mapName": "Genome Map 1",
                "position": 2390,
                "variantDbId": "a1eb250a",
                "variantName": "Marker_2390"
            }
        ]
    }
}
```

+ Response 202 (application/json)
```
{
    "@context": [
        "https://brapi.org/jsonld/context/metadata.jsonld"
    ],
    "metadata": {
        "datafiles": [],
        "pagination": {
            "currentPage": 0,
            "pageSize": 1000,
            "totalCount": 10,
            "totalPages": 1
        },
        "status": [
            {
                "message": "Request accepted, response successful",
                "messageType": "INFO"
            }
        ]
    },
    "result": {
        "searchResultsDbId": "551ae08c"
    }
}
```

+ Response 400 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - Malformed JSON Request Object\n\nERROR - 2018-10-08T18:15:11Z - Invalid query parameter\n\nERROR - 2018-10-08T18:15:11Z - Required parameter is missing"
```

+ Response 401 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - Missing or expired authorization token"
```

+ Response 403 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - User does not have permission to perform this action"
```




### Get - /search/markerpositions/{searchResultsDbId} [GET /brapi/v2/search/markerpositions/{searchResultsDbId}{?page}{?pageSize}]

Get the results of a `MarkerPositions` search request <br/>
Clients should submit a search request using the corresponding `POST /search/markerpositions` endpoint.
Search requests allow a client to send a complex query for data. However, the server may not respond with the search results immediately. 
If a server needs more time to process the request, it might respond with a `searchResultsDbId`. 
Use this endpoint to retrieve the results of the search. <br/> 
Review the <a target="_blank" href="https://wiki.brapi.org/index.php/Search_Services#POST_Search_Entity">Search Services documentation</a> for additional implementation details.



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|additionalInfo|object|Additional arbitrary info|
|linkageGroupName|string|The Uniquely Identifiable name of this linkage group|
|mapDbId|string|The unique ID of the map|
|mapName|string|The human readable name of the map|
|position|integer|The position of a marker within a linkage group|
|variantDbId|string|Internal db identifier|
|variantName|string|The human readable name for a marker|


 

+ Parameters
    + searchResultsDbId (Required, ) ... Unique identifier which references the search results
    + page (Optional, ) ... Used to request a specific page of data to be returned.The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.
    + pageSize (Optional, ) ... The size of the pages to be returned. Default is `1000`.
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>




+ Response 200 (application/json)
```
{
    "@context": [
        "https://brapi.org/jsonld/context/metadata.jsonld"
    ],
    "metadata": {
        "datafiles": [],
        "pagination": {
            "currentPage": 0,
            "pageSize": 1000,
            "totalCount": 10,
            "totalPages": 1
        },
        "status": [
            {
                "message": "Request accepted, response successful",
                "messageType": "INFO"
            }
        ]
    },
    "result": {
        "data": [
            {
                "additionalInfo": {},
                "linkageGroupName": "Chromosome 3",
                "mapDbId": "3d52bdf3",
                "mapName": "Genome Map 1",
                "position": 2390,
                "variantDbId": "a1eb250a",
                "variantName": "Marker_2390"
            }
        ]
    }
}
```

+ Response 202 (application/json)
```
{
    "@context": [
        "https://brapi.org/jsonld/context/metadata.jsonld"
    ],
    "metadata": {
        "datafiles": [],
        "pagination": {
            "currentPage": 0,
            "pageSize": 1000,
            "totalCount": 10,
            "totalPages": 1
        },
        "status": [
            {
                "message": "Request accepted, response successful",
                "messageType": "INFO"
            }
        ]
    },
    "result": {
        "searchResultsDbId": "551ae08c"
    }
}
```

+ Response 400 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - Malformed JSON Request Object\n\nERROR - 2018-10-08T18:15:11Z - Invalid query parameter\n\nERROR - 2018-10-08T18:15:11Z - Required parameter is missing"
```

+ Response 401 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - Missing or expired authorization token"
```

+ Response 403 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - User does not have permission to perform this action"
```

