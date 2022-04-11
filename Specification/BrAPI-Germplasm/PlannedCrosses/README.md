# Group Planned Crosses






### Get - /plannedcrosses [GET /brapi/v2/plannedcrosses{?crossingProjectDbId}{?crossingProjectName}{?plannedCrossDbId}{?status}{?commonCropName}{?programDbId}{?externalReferenceID}{?externalReferenceId}{?externalReferenceSource}{?page}{?pageSize}]

Get a filtered list of Planned Cross entities.



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|additionalInfo|object|Additional arbitrary info|
|crossType|string|the type of cross|
|crossingProjectDbId|string|the unique identifier for a crossing project|
|crossingProjectName|string|the human readable name for a crossing project|
|externalReferences|array[object]|An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.|
|referenceID|string|**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.|
|referenceId|string|The external reference ID. Could be a simple string or a URI.|
|referenceSource|string|An identifier for the source system or database of this reference|
|parent1|object||
|germplasmDbId|string|the unique identifier for a germplasm|
|germplasmName|string|the human readable name for a germplasm|
|observationUnitDbId|string|the unique identifier for an observation unit|
|observationUnitName|string|the human readable name for an observation unit|
|parentType|string|The type of parent ex. 'MALE', 'FEMALE', 'SELF', 'POPULATION', etc.|
|parent2|object||
|germplasmDbId|string|the unique identifier for a germplasm|
|germplasmName|string|the human readable name for a germplasm|
|observationUnitDbId|string|the unique identifier for an observation unit|
|observationUnitName|string|the human readable name for an observation unit|
|parentType|string|The type of parent ex. 'MALE', 'FEMALE', 'SELF', 'POPULATION', etc.|
|plannedCrossDbId|string|the unique identifier for a planned cross|
|plannedCrossName|string|the human readable name for a planned cross|
|status|string|The status of this planned cross. Is it waiting to be performed ('TODO'), has it been completed successfully ('DONE'), or has it not been done on purpose ('SKIPPED').|


 

+ Parameters
    + crossingProjectDbId (Optional, ) ... Search for Crossing Projects with this unique id
    + crossingProjectName (Optional, ) ... The human readable name for a crossing project
    + plannedCrossDbId (Optional, ) ... Search for Planned Cross with this unique id
    + status (Optional, ) ... The status of this planned cross. Is it waiting to be performed ('TODO'), has it been completed successfully ('DONE'), or has it not been done on purpose ('SKIPPED').
    + commonCropName (Optional, ) ... The BrAPI Common Crop Name is the simple, generalized, widely accepted name of the organism being researched. It is most often used in multi-crop systems where digital resources need to be divided at a high level. Things like 'Maize', 'Wheat', and 'Rice' are examples of common crop names.Use this parameter to only return results associated with the given crop. Use `GET /commoncropnames` to find the list of available crops on a server.
    + programDbId (Optional, ) ... Use this parameter to only return results associated with the given Program unique identifier. <br/>Use `GET /programs` to find the list of available Programs on a server.
    + externalReferenceID (Optional, ) ... **Deprecated in v2.1** Please use `externalReferenceId`. Github issue number #460 An external reference ID. Could be a simple string or a URI. (use with `externalReferenceSource` parameter)
    + externalReferenceId (Optional, ) ... An external reference ID. Could be a simple string or a URI. (use with `externalReferenceSource` parameter)
    + externalReferenceSource (Optional, ) ... An identifier for the source system or database of an external reference (use with `externalReferenceId` parameter)
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
                "crossType": "BIPARENTAL",
                "crossingProjectDbId": "696d7c92",
                "crossingProjectName": "my_Crosses_2018",
                "externalReferences": [
                    {
                        "referenceId": "doi:10.155454/12341234",
                        "referenceSource": "DOI"
                    },
                    {
                        "referenceId": "75a50e76",
                        "referenceSource": "Remote Data Collection Upload Tool"
                    }
                ],
                "parent1": {
                    "germplasmDbId": "d34b10c3",
                    "germplasmName": "TME_419",
                    "observationUnitDbId": "2e1926a7",
                    "observationUnitName": "my_Plot_9001",
                    "parentType": "MALE"
                },
                "parent2": {
                    "germplasmDbId": "d34b10c3",
                    "germplasmName": "TME_419",
                    "observationUnitDbId": "2e1926a7",
                    "observationUnitName": "my_Plot_9001",
                    "parentType": "MALE"
                },
                "plannedCrossDbId": "c8905568",
                "plannedCrossName": "my_Crosses_2018_01",
                "status": "TODO"
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




### Post - /plannedcrosses [POST /brapi/v2/plannedcrosses]

Create new Planned Cross entities on this server

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|additionalInfo|object|Additional arbitrary info|
|crossType|string|the type of cross|
|crossingProjectDbId|string|the unique identifier for a crossing project|
|crossingProjectName|string|the human readable name for a crossing project|
|externalReferences|array[object]|An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.|
|referenceID|string|**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.|
|referenceId|string|The external reference ID. Could be a simple string or a URI.|
|referenceSource|string|An identifier for the source system or database of this reference|
|parent1|object||
|germplasmDbId|string|the unique identifier for a germplasm|
|germplasmName|string|the human readable name for a germplasm|
|observationUnitDbId|string|the unique identifier for an observation unit|
|observationUnitName|string|the human readable name for an observation unit|
|parentType|string|The type of parent ex. 'MALE', 'FEMALE', 'SELF', 'POPULATION', etc.|
|parent2|object||
|germplasmDbId|string|the unique identifier for a germplasm|
|germplasmName|string|the human readable name for a germplasm|
|observationUnitDbId|string|the unique identifier for an observation unit|
|observationUnitName|string|the human readable name for an observation unit|
|parentType|string|The type of parent ex. 'MALE', 'FEMALE', 'SELF', 'POPULATION', etc.|
|plannedCrossName|string|the human readable name for a planned cross|
|status|string|The status of this planned cross. Is it waiting to be performed ('TODO'), has it been completed successfully ('DONE'), or has it not been done on purpose ('SKIPPED').|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|additionalInfo|object|Additional arbitrary info|
|crossType|string|the type of cross|
|crossingProjectDbId|string|the unique identifier for a crossing project|
|crossingProjectName|string|the human readable name for a crossing project|
|externalReferences|array[object]|An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.|
|referenceID|string|**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.|
|referenceId|string|The external reference ID. Could be a simple string or a URI.|
|referenceSource|string|An identifier for the source system or database of this reference|
|parent1|object||
|germplasmDbId|string|the unique identifier for a germplasm|
|germplasmName|string|the human readable name for a germplasm|
|observationUnitDbId|string|the unique identifier for an observation unit|
|observationUnitName|string|the human readable name for an observation unit|
|parentType|string|The type of parent ex. 'MALE', 'FEMALE', 'SELF', 'POPULATION', etc.|
|parent2|object||
|germplasmDbId|string|the unique identifier for a germplasm|
|germplasmName|string|the human readable name for a germplasm|
|observationUnitDbId|string|the unique identifier for an observation unit|
|observationUnitName|string|the human readable name for an observation unit|
|parentType|string|The type of parent ex. 'MALE', 'FEMALE', 'SELF', 'POPULATION', etc.|
|plannedCrossDbId|string|the unique identifier for a planned cross|
|plannedCrossName|string|the human readable name for a planned cross|
|status|string|The status of this planned cross. Is it waiting to be performed ('TODO'), has it been completed successfully ('DONE'), or has it not been done on purpose ('SKIPPED').|


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
[
    {
        "additionalInfo": {},
        "crossType": "BIPARENTAL",
        "crossingProjectDbId": "696d7c92",
        "crossingProjectName": "my_Crosses_2018",
        "externalReferences": [
            {
                "referenceId": "doi:10.155454/12341234",
                "referenceSource": "DOI"
            },
            {
                "referenceId": "75a50e76",
                "referenceSource": "Remote Data Collection Upload Tool"
            }
        ],
        "parent1": {
            "germplasmDbId": "d34b10c3",
            "germplasmName": "TME_419",
            "observationUnitDbId": "2e1926a7",
            "observationUnitName": "my_Plot_9001",
            "parentType": "MALE"
        },
        "parent2": {
            "germplasmDbId": "d34b10c3",
            "germplasmName": "TME_419",
            "observationUnitDbId": "2e1926a7",
            "observationUnitName": "my_Plot_9001",
            "parentType": "MALE"
        },
        "plannedCrossName": "my_Crosses_2018_01",
        "status": "TODO"
    }
]
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
                "crossType": "BIPARENTAL",
                "crossingProjectDbId": "696d7c92",
                "crossingProjectName": "my_Crosses_2018",
                "externalReferences": [
                    {
                        "referenceId": "doi:10.155454/12341234",
                        "referenceSource": "DOI"
                    },
                    {
                        "referenceId": "75a50e76",
                        "referenceSource": "Remote Data Collection Upload Tool"
                    }
                ],
                "parent1": {
                    "germplasmDbId": "d34b10c3",
                    "germplasmName": "TME_419",
                    "observationUnitDbId": "2e1926a7",
                    "observationUnitName": "my_Plot_9001",
                    "parentType": "MALE"
                },
                "parent2": {
                    "germplasmDbId": "d34b10c3",
                    "germplasmName": "TME_419",
                    "observationUnitDbId": "2e1926a7",
                    "observationUnitName": "my_Plot_9001",
                    "parentType": "MALE"
                },
                "plannedCrossDbId": "c8905568",
                "plannedCrossName": "my_Crosses_2018_01",
                "status": "TODO"
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




### Put - /plannedcrosses [PUT /brapi/v2/plannedcrosses/]

Update existing Planned Cross entities on this server

**Request Fields** 

|Field|Type|Description|
|---|---|---| 


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|additionalInfo|object|Additional arbitrary info|
|crossType|string|the type of cross|
|crossingProjectDbId|string|the unique identifier for a crossing project|
|crossingProjectName|string|the human readable name for a crossing project|
|externalReferences|array[object]|An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.|
|referenceID|string|**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.|
|referenceId|string|The external reference ID. Could be a simple string or a URI.|
|referenceSource|string|An identifier for the source system or database of this reference|
|parent1|object||
|germplasmDbId|string|the unique identifier for a germplasm|
|germplasmName|string|the human readable name for a germplasm|
|observationUnitDbId|string|the unique identifier for an observation unit|
|observationUnitName|string|the human readable name for an observation unit|
|parentType|string|The type of parent ex. 'MALE', 'FEMALE', 'SELF', 'POPULATION', etc.|
|parent2|object||
|germplasmDbId|string|the unique identifier for a germplasm|
|germplasmName|string|the human readable name for a germplasm|
|observationUnitDbId|string|the unique identifier for an observation unit|
|observationUnitName|string|the human readable name for an observation unit|
|parentType|string|The type of parent ex. 'MALE', 'FEMALE', 'SELF', 'POPULATION', etc.|
|plannedCrossDbId|string|the unique identifier for a planned cross|
|plannedCrossName|string|the human readable name for a planned cross|
|status|string|The status of this planned cross. Is it waiting to be performed ('TODO'), has it been completed successfully ('DONE'), or has it not been done on purpose ('SKIPPED').|


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "<plannedCrossDbId_1>": {
        "additionalInfo": {},
        "crossAttributes": [
            {
                "crossAttributeName": "string",
                "crossAttributeValue": "string"
            }
        ],
        "crossType": "BIPARENTAL",
        "crossingProjectDbId": "696d7c92",
        "crossingProjectName": "my_Crosses_2018",
        "parent1": {
            "germplasmDbId": "d34b10c3",
            "germplasmName": "TME_419",
            "observationUnitDbId": "3f0a1798",
            "observationUnitName": "my_Plot_9001",
            "parentType": "FEMALE"
        },
        "parent2": {
            "germplasmDbId": "776a609c",
            "germplasmName": "TME_419",
            "observationUnitDbId": "2e1926a7",
            "observationUnitName": "my_Plot_9002",
            "parentType": "MALE"
        },
        "plannedCrossName": "my_Crosses_2018_01",
        "pollinationTimeStamp": "2019-08-15T18:49:00.327Z"
    },
    "<plannedCrossDbId_2>": {
        "additionalInfo": {},
        "crossAttributes": [
            {
                "crossAttributeName": "string",
                "crossAttributeValue": "string"
            }
        ],
        "crossType": "BIPARENTAL",
        "crossingProjectDbId": "696d7c92",
        "crossingProjectName": "my_Crosses_2018",
        "parent1": {
            "germplasmDbId": "c43a2fd2",
            "germplasmName": "TME_419",
            "observationUnitDbId": "3f2a37b8",
            "observationUnitName": "my_Plot_9013",
            "parentType": "FEMALE"
        },
        "parent2": {
            "germplasmDbId": "124b10ad",
            "germplasmName": "TME_419",
            "observationUnitDbId": 27194637,
            "observationUnitName": "my_Plot_9014",
            "parentType": "MALE"
        },
        "plannedCrossName": "my_Crosses_2018_02",
        "pollinationTimeStamp": "2019-08-15T18:49:00.327Z"
    }
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
                "crossType": "BIPARENTAL",
                "crossingProjectDbId": "696d7c92",
                "crossingProjectName": "my_Crosses_2018",
                "externalReferences": [
                    {
                        "referenceId": "doi:10.155454/12341234",
                        "referenceSource": "DOI"
                    },
                    {
                        "referenceId": "75a50e76",
                        "referenceSource": "Remote Data Collection Upload Tool"
                    }
                ],
                "parent1": {
                    "germplasmDbId": "d34b10c3",
                    "germplasmName": "TME_419",
                    "observationUnitDbId": "2e1926a7",
                    "observationUnitName": "my_Plot_9001",
                    "parentType": "MALE"
                },
                "parent2": {
                    "germplasmDbId": "d34b10c3",
                    "germplasmName": "TME_419",
                    "observationUnitDbId": "2e1926a7",
                    "observationUnitName": "my_Plot_9001",
                    "parentType": "MALE"
                },
                "plannedCrossDbId": "c8905568",
                "plannedCrossName": "my_Crosses_2018_01",
                "status": "TODO"
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

