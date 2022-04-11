# Group Crossing Projects






### Get - /crossingprojects [GET /brapi/v2/crossingprojects{?crossingProjectDbId}{?crossingProjectName}{?includePotentialParents}{?commonCropName}{?programDbId}{?externalReferenceID}{?externalReferenceId}{?externalReferenceSource}{?page}{?pageSize}]

Get a filtered list of Crossing Projects.



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|additionalInfo|object|Additional arbitrary info|
|commonCropName|string|the common name of a crop (for multi-crop systems)|
|crossingProjectDbId|string|The unique identifier for a crossing project|
|crossingProjectDescription|string|the description for a crossing project|
|crossingProjectName|string|The human readable name for a crossing project|
|externalReferences|array[object]|An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.|
|referenceID|string|**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.|
|referenceId|string|The external reference ID. Could be a simple string or a URI.|
|referenceSource|string|An identifier for the source system or database of this reference|
|potentialParents|array[object]|A list of all the potential parents in the crossing block, available in the crossing project <br/> If the parameter 'includePotentialParents' is false, the array 'potentialParents' should be empty, null, or excluded from the response object.|
|germplasmDbId|string|the unique identifier for a germplasm|
|germplasmName|string|the human readable name for a germplasm|
|observationUnitDbId|string|the unique identifier for an observation unit|
|observationUnitName|string|the human readable name for an observation unit|
|parentType|string|The type of parent ex. 'MALE', 'FEMALE', 'SELF', 'POPULATION', etc.|
|programDbId|string|the unique identifier for a program|
|programName|string|the human readable name for a program|


 

+ Parameters
    + crossingProjectDbId (Optional, ) ... Search for Crossing Projects with this unique id
    + crossingProjectName (Optional, ) ... The human readable name for a crossing project
    + includePotentialParents (Optional, ) ... If the parameter 'includePotentialParents' is false, the array 'potentialParents' should be empty, null, or excluded from the response object.
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
                "commonCropName": "Cassava",
                "crossingProjectDbId": "ce0e1c29",
                "crossingProjectDescription": "Crosses between germplasm X and germplasm Y in male nursery study X_2018 and female nursery study Y_2018",
                "crossingProjectName": "Crosses_2018",
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
                "potentialParents": [
                    {
                        "germplasmDbId": "d34b10c3",
                        "germplasmName": "TME_419",
                        "observationUnitDbId": "2e1926a7",
                        "observationUnitName": "my_Plot_9001",
                        "parentType": "MALE"
                    }
                ],
                "programDbId": "a088176c",
                "programName": "IITA Cassava"
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




### Post - /crossingprojects [POST /brapi/v2/crossingprojects]

Create new Crossing Project entities on this server

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|additionalInfo|object|Additional arbitrary info|
|commonCropName|string|the common name of a crop (for multi-crop systems)|
|crossingProjectDescription|string|the description for a crossing project|
|crossingProjectName|string|The human readable name for a crossing project|
|externalReferences|array[object]|An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.|
|referenceID|string|**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.|
|referenceId|string|The external reference ID. Could be a simple string or a URI.|
|referenceSource|string|An identifier for the source system or database of this reference|
|potentialParents|array[object]|A list of all the potential parents in the crossing block, available in the crossing project <br/> If the parameter 'includePotentialParents' is false, the array 'potentialParents' should be empty, null, or excluded from the response object.|
|germplasmDbId|string|the unique identifier for a germplasm|
|germplasmName|string|the human readable name for a germplasm|
|observationUnitDbId|string|the unique identifier for an observation unit|
|observationUnitName|string|the human readable name for an observation unit|
|parentType|string|The type of parent ex. 'MALE', 'FEMALE', 'SELF', 'POPULATION', etc.|
|programDbId|string|the unique identifier for a program|
|programName|string|the human readable name for a program|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|additionalInfo|object|Additional arbitrary info|
|commonCropName|string|the common name of a crop (for multi-crop systems)|
|crossingProjectDbId|string|The unique identifier for a crossing project|
|crossingProjectDescription|string|the description for a crossing project|
|crossingProjectName|string|The human readable name for a crossing project|
|externalReferences|array[object]|An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.|
|referenceID|string|**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.|
|referenceId|string|The external reference ID. Could be a simple string or a URI.|
|referenceSource|string|An identifier for the source system or database of this reference|
|potentialParents|array[object]|A list of all the potential parents in the crossing block, available in the crossing project <br/> If the parameter 'includePotentialParents' is false, the array 'potentialParents' should be empty, null, or excluded from the response object.|
|germplasmDbId|string|the unique identifier for a germplasm|
|germplasmName|string|the human readable name for a germplasm|
|observationUnitDbId|string|the unique identifier for an observation unit|
|observationUnitName|string|the human readable name for an observation unit|
|parentType|string|The type of parent ex. 'MALE', 'FEMALE', 'SELF', 'POPULATION', etc.|
|programDbId|string|the unique identifier for a program|
|programName|string|the human readable name for a program|


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
[
    {
        "additionalInfo": {},
        "commonCropName": "Cassava",
        "crossingProjectDescription": "Crosses between germplasm X and germplasm Y in male nursery study X_2018 and female nursery study Y_2018",
        "crossingProjectName": "Crosses_2018",
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
        "potentialParents": [
            {
                "germplasmDbId": "d34b10c3",
                "germplasmName": "TME_419",
                "observationUnitDbId": "2e1926a7",
                "observationUnitName": "my_Plot_9001",
                "parentType": "MALE"
            }
        ],
        "programDbId": "a088176c",
        "programName": "IITA Cassava"
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
                "commonCropName": "Cassava",
                "crossingProjectDbId": "ce0e1c29",
                "crossingProjectDescription": "Crosses between germplasm X and germplasm Y in male nursery study X_2018 and female nursery study Y_2018",
                "crossingProjectName": "Crosses_2018",
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
                "potentialParents": [
                    {
                        "germplasmDbId": "d34b10c3",
                        "germplasmName": "TME_419",
                        "observationUnitDbId": "2e1926a7",
                        "observationUnitName": "my_Plot_9001",
                        "parentType": "MALE"
                    }
                ],
                "programDbId": "a088176c",
                "programName": "IITA Cassava"
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




### Get - /crossingprojects/{crossingProjectDbId} [GET /brapi/v2/crossingprojects/{crossingProjectDbId}]

Get a filtered list of Crossing Projects.



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|additionalInfo|object|Additional arbitrary info|
|commonCropName|string|the common name of a crop (for multi-crop systems)|
|crossingProjectDbId|string|The unique identifier for a crossing project|
|crossingProjectDescription|string|the description for a crossing project|
|crossingProjectName|string|The human readable name for a crossing project|
|externalReferences|array[object]|An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.|
|referenceID|string|**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.|
|referenceId|string|The external reference ID. Could be a simple string or a URI.|
|referenceSource|string|An identifier for the source system or database of this reference|
|potentialParents|array[object]|A list of all the potential parents in the crossing block, available in the crossing project <br/> If the parameter 'includePotentialParents' is false, the array 'potentialParents' should be empty, null, or excluded from the response object.|
|germplasmDbId|string|the unique identifier for a germplasm|
|germplasmName|string|the human readable name for a germplasm|
|observationUnitDbId|string|the unique identifier for an observation unit|
|observationUnitName|string|the human readable name for an observation unit|
|parentType|string|The type of parent ex. 'MALE', 'FEMALE', 'SELF', 'POPULATION', etc.|
|programDbId|string|the unique identifier for a program|
|programName|string|the human readable name for a program|


 

+ Parameters
    + crossingProjectDbId (Required, ) ... The unique identifier for a crossing project
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
        "commonCropName": "Cassava",
        "crossingProjectDbId": "ce0e1c29",
        "crossingProjectDescription": "Crosses between germplasm X and germplasm Y in male nursery study X_2018 and female nursery study Y_2018",
        "crossingProjectName": "Crosses_2018",
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
        "potentialParents": [
            {
                "germplasmDbId": "d34b10c3",
                "germplasmName": "TME_419",
                "observationUnitDbId": "2e1926a7",
                "observationUnitName": "my_Plot_9001",
                "parentType": "MALE"
            }
        ],
        "programDbId": "a088176c",
        "programName": "IITA Cassava"
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




### Put - /crossingprojects/{crossingProjectDbId} [PUT /brapi/v2/crossingprojects/{crossingProjectDbId}/]

Update an existing Crossing Project entity on this server

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|additionalInfo|object|Additional arbitrary info|
|commonCropName|string|the common name of a crop (for multi-crop systems)|
|crossingProjectDescription|string|the description for a crossing project|
|crossingProjectName|string|The human readable name for a crossing project|
|externalReferences|array[object]|An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.|
|referenceID|string|**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.|
|referenceId|string|The external reference ID. Could be a simple string or a URI.|
|referenceSource|string|An identifier for the source system or database of this reference|
|potentialParents|array[object]|A list of all the potential parents in the crossing block, available in the crossing project <br/> If the parameter 'includePotentialParents' is false, the array 'potentialParents' should be empty, null, or excluded from the response object.|
|germplasmDbId|string|the unique identifier for a germplasm|
|germplasmName|string|the human readable name for a germplasm|
|observationUnitDbId|string|the unique identifier for an observation unit|
|observationUnitName|string|the human readable name for an observation unit|
|parentType|string|The type of parent ex. 'MALE', 'FEMALE', 'SELF', 'POPULATION', etc.|
|programDbId|string|the unique identifier for a program|
|programName|string|the human readable name for a program|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|additionalInfo|object|Additional arbitrary info|
|commonCropName|string|the common name of a crop (for multi-crop systems)|
|crossingProjectDbId|string|The unique identifier for a crossing project|
|crossingProjectDescription|string|the description for a crossing project|
|crossingProjectName|string|The human readable name for a crossing project|
|externalReferences|array[object]|An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.|
|referenceID|string|**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.|
|referenceId|string|The external reference ID. Could be a simple string or a URI.|
|referenceSource|string|An identifier for the source system or database of this reference|
|potentialParents|array[object]|A list of all the potential parents in the crossing block, available in the crossing project <br/> If the parameter 'includePotentialParents' is false, the array 'potentialParents' should be empty, null, or excluded from the response object.|
|germplasmDbId|string|the unique identifier for a germplasm|
|germplasmName|string|the human readable name for a germplasm|
|observationUnitDbId|string|the unique identifier for an observation unit|
|observationUnitName|string|the human readable name for an observation unit|
|parentType|string|The type of parent ex. 'MALE', 'FEMALE', 'SELF', 'POPULATION', etc.|
|programDbId|string|the unique identifier for a program|
|programName|string|the human readable name for a program|


 

+ Parameters
    + crossingProjectDbId (Required, ) ... Search for Crossing Projects with this unique id
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "additionalInfo": {},
    "commonCropName": "Cassava",
    "crossingProjectDescription": "Crosses between germplasm X and germplasm Y in male nursery study X_2018 and female nursery study Y_2018",
    "crossingProjectName": "Crosses_2018",
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
    "potentialParents": [
        {
            "germplasmDbId": "d34b10c3",
            "germplasmName": "TME_419",
            "observationUnitDbId": "2e1926a7",
            "observationUnitName": "my_Plot_9001",
            "parentType": "MALE"
        }
    ],
    "programDbId": "a088176c",
    "programName": "IITA Cassava"
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
        "additionalInfo": {},
        "commonCropName": "Cassava",
        "crossingProjectDbId": "ce0e1c29",
        "crossingProjectDescription": "Crosses between germplasm X and germplasm Y in male nursery study X_2018 and female nursery study Y_2018",
        "crossingProjectName": "Crosses_2018",
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
        "potentialParents": [
            {
                "germplasmDbId": "d34b10c3",
                "germplasmName": "TME_419",
                "observationUnitDbId": "2e1926a7",
                "observationUnitName": "my_Plot_9001",
                "parentType": "MALE"
            }
        ],
        "programDbId": "a088176c",
        "programName": "IITA Cassava"
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

