
# Group Plates

API methods for tracking/managing `Plates` which contain `Samples` and related meta-data. A `Plate` is usually a plastic tray full of `Samples`, or a collection of test tubes grouped together.





### Get - /plates [GET /brapi/v2/plates{?sampleDbId}{?sampleName}{?sampleGroupDbId}{?observationUnitDbId}{?plateDbId}{?plateName}{?commonCropName}{?programDbId}{?trialDbId}{?studyDbId}{?germplasmDbId}{?externalReferenceID}{?externalReferenceId}{?externalReferenceSource}{?page}{?pageSize}]

Get a filtered list of `Plates`. Each `Plate` is a collection of `Samples` that are physically grouped together.



**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">plateDbId</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>The ID which uniquely identifies a `Plate`</td></tr>
<tr><td><span style="font-weight:bold;">plateName</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>A human readable name for a `Plate`</td></tr>
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">plateBarcode</span></td><td>string</td><td>A unique identifier physically attached to a `Plate`</td></tr>
<tr><td><span style="font-weight:bold;">plateFormat</span></td><td>string</td><td>Enum for plate formats, usually "PLATE_96" for a 96 well plate or "TUBES" for plateless format</td></tr>
<tr><td><span style="font-weight:bold;">programDbId</span></td><td>string</td><td>The ID which uniquely identifies a `Program` within the given database server</td></tr>
<tr><td><span style="font-weight:bold;">sampleType</span></td><td>string</td><td>The type of samples taken. ex. 'DNA', 'RNA', 'Tissue', etc</td></tr>
<tr><td><span style="font-weight:bold;">studyDbId</span></td><td>string</td><td>The ID which uniquely identifies a `Study` within the given database server</td></tr>
<tr><td><span style="font-weight:bold;">trialDbId</span></td><td>string</td><td>The ID which uniquely identifies a `Trial` within the given database server</td></tr>
</table>


 

+ Parameters
    + sampleDbId (Optional, ) ... The unique identifier for a `Sample`
    + sampleName (Optional, ) ... The human readable name of the `Sample`
    + sampleGroupDbId (Optional, ) ... The unique identifier for a group of related `Samples`
    + observationUnitDbId (Optional, ) ... The ID which uniquely identifies an `ObservationUnit`
    + plateDbId (Optional, ) ... The ID which uniquely identifies a `Plate` of `Samples`
    + plateName (Optional, ) ... The human readable name of a `Plate` of `Samples`
    + commonCropName (Optional, ) ... The BrAPI Common Crop Name is the simple, generalized, widely accepted name of the organism being researched. It is most often used in multi-crop systems where digital resources need to be divided at a high level. Things like 'Maize', 'Wheat', and 'Rice' are examples of common crop names.Use this parameter to only return results associated with the given crop. Use `GET /commoncropnames` to find the list of available crops on a server.
    + programDbId (Optional, ) ... Use this parameter to only return results associated with the given `Program` unique identifier. <br/>Use `GET /programs` to find the list of available `Programs` on a server.
    + trialDbId (Optional, ) ... Use this parameter to only return results associated with the given `Trial` unique identifier. <br/>Use `GET /trials` to find the list of available `Trials` on a server.
    + studyDbId (Optional, ) ... Use this parameter to only return results associated with the given `Study` unique identifier. <br/>Use `GET /studies` to find the list of available `Studies` on a server.
    + germplasmDbId (Optional, ) ... Use this parameter to only return results associated with the given `Germplasm` unique identifier. <br/>Use `GET /germplasm` to find the list of available `Germplasm` on a server.
    + externalReferenceID (Optional, ) ... **Deprecated in v2.1** Please use `externalReferenceId`. Github issue number #460 <br>An external reference ID. Could be a simple string or a URI. (use with `externalReferenceSource` parameter)
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
                "plateBarcode": "11223344",
                "plateDbId": "a106467f",
                "plateFormat": "PLATE_96",
                "plateName": "Plate_123_XYZ",
                "programDbId": "bd748e00",
                "sampleType": "TISSUE",
                "studyDbId": "64bd6bf9",
                "trialDbId": "d34c5349"
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




### Post - /plates [POST /brapi/v2/plates]

Submit new Plate entities to the server

**Request Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">plateName</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>A human readable name for a `Plate`</td></tr>
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">plateBarcode</span></td><td>string</td><td>A unique identifier physically attached to a `Plate`</td></tr>
<tr><td><span style="font-weight:bold;">plateFormat</span></td><td>string</td><td>Enum for plate formats, usually "PLATE_96" for a 96 well plate or "TUBES" for plateless format</td></tr>
<tr><td><span style="font-weight:bold;">programDbId</span></td><td>string</td><td>The ID which uniquely identifies a `Program` within the given database server</td></tr>
<tr><td><span style="font-weight:bold;">sampleType</span></td><td>string</td><td>The type of samples taken. ex. 'DNA', 'RNA', 'Tissue', etc</td></tr>
<tr><td><span style="font-weight:bold;">studyDbId</span></td><td>string</td><td>The ID which uniquely identifies a `Study` within the given database server</td></tr>
<tr><td><span style="font-weight:bold;">trialDbId</span></td><td>string</td><td>The ID which uniquely identifies a `Trial` within the given database server</td></tr>
</table>


**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">plateDbId</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>The ID which uniquely identifies a `Plate`</td></tr>
<tr><td><span style="font-weight:bold;">plateName</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>A human readable name for a `Plate`</td></tr>
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">plateBarcode</span></td><td>string</td><td>A unique identifier physically attached to a `Plate`</td></tr>
<tr><td><span style="font-weight:bold;">plateFormat</span></td><td>string</td><td>Enum for plate formats, usually "PLATE_96" for a 96 well plate or "TUBES" for plateless format</td></tr>
<tr><td><span style="font-weight:bold;">programDbId</span></td><td>string</td><td>The ID which uniquely identifies a `Program` within the given database server</td></tr>
<tr><td><span style="font-weight:bold;">sampleType</span></td><td>string</td><td>The type of samples taken. ex. 'DNA', 'RNA', 'Tissue', etc</td></tr>
<tr><td><span style="font-weight:bold;">studyDbId</span></td><td>string</td><td>The ID which uniquely identifies a `Study` within the given database server</td></tr>
<tr><td><span style="font-weight:bold;">trialDbId</span></td><td>string</td><td>The ID which uniquely identifies a `Trial` within the given database server</td></tr>
</table>


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
[
    {
        "additionalInfo": {},
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
        "plateBarcode": "11223344",
        "plateFormat": "PLATE_96",
        "plateName": "Plate_123_XYZ",
        "programDbId": "bd748e00",
        "sampleType": "TISSUE",
        "studyDbId": "64bd6bf9",
        "trialDbId": "d34c5349"
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
                "plateBarcode": "11223344",
                "plateDbId": "a106467f",
                "plateFormat": "PLATE_96",
                "plateName": "Plate_123_XYZ",
                "programDbId": "bd748e00",
                "sampleType": "TISSUE",
                "studyDbId": "64bd6bf9",
                "trialDbId": "d34c5349"
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




### Put - /plates [PUT /brapi/v2/plates/]

Update the details of existing Plates

**Request Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
</table>


**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">plateDbId</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>The ID which uniquely identifies a `Plate`</td></tr>
<tr><td><span style="font-weight:bold;">plateName</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>A human readable name for a `Plate`</td></tr>
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">plateBarcode</span></td><td>string</td><td>A unique identifier physically attached to a `Plate`</td></tr>
<tr><td><span style="font-weight:bold;">plateFormat</span></td><td>string</td><td>Enum for plate formats, usually "PLATE_96" for a 96 well plate or "TUBES" for plateless format</td></tr>
<tr><td><span style="font-weight:bold;">programDbId</span></td><td>string</td><td>The ID which uniquely identifies a `Program` within the given database server</td></tr>
<tr><td><span style="font-weight:bold;">sampleType</span></td><td>string</td><td>The type of samples taken. ex. 'DNA', 'RNA', 'Tissue', etc</td></tr>
<tr><td><span style="font-weight:bold;">studyDbId</span></td><td>string</td><td>The ID which uniquely identifies a `Study` within the given database server</td></tr>
<tr><td><span style="font-weight:bold;">trialDbId</span></td><td>string</td><td>The ID which uniquely identifies a `Trial` within the given database server</td></tr>
</table>


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "<plateDbId_1>": {
        "additionalInfo": {},
        "externalReferences": [],
        "plateBarcode": "3a027b59",
        "plateFormat": "PLATE_96",
        "plateName": "Plate_alpha_20191022",
        "programDbId": "bd748e00",
        "sampleType": "Tissue",
        "studyDbId": "64bd6bf9",
        "trialDbId": "d34c5349"
    },
    "<plateDbId_2>": {
        "additionalInfo": {},
        "externalReferences": [],
        "plateBarcode": "27b593a0",
        "plateFormat": "PLATE_96",
        "plateName": "Plate_alpha_20191022",
        "programDbId": "bd748e00",
        "sampleType": "Tissue",
        "studyDbId": "64bd6bf9",
        "trialDbId": "d34c5349"
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
                "plateBarcode": "11223344",
                "plateDbId": "a106467f",
                "plateFormat": "PLATE_96",
                "plateName": "Plate_123_XYZ",
                "programDbId": "bd748e00",
                "sampleType": "TISSUE",
                "studyDbId": "64bd6bf9",
                "trialDbId": "d34c5349"
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




### Get - /plates/{plateDbId} [GET /brapi/v2/plates/{plateDbId}]

Get the details of a specific `Plate`. Each `Plate` is a collection of `Samples` that are physically grouped together.



**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">plateDbId</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>The ID which uniquely identifies a `Plate`</td></tr>
<tr><td><span style="font-weight:bold;">plateName</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>A human readable name for a `Plate`</td></tr>
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">plateBarcode</span></td><td>string</td><td>A unique identifier physically attached to a `Plate`</td></tr>
<tr><td><span style="font-weight:bold;">plateFormat</span></td><td>string</td><td>Enum for plate formats, usually "PLATE_96" for a 96 well plate or "TUBES" for plateless format</td></tr>
<tr><td><span style="font-weight:bold;">programDbId</span></td><td>string</td><td>The ID which uniquely identifies a `Program` within the given database server</td></tr>
<tr><td><span style="font-weight:bold;">sampleType</span></td><td>string</td><td>The type of samples taken. ex. 'DNA', 'RNA', 'Tissue', etc</td></tr>
<tr><td><span style="font-weight:bold;">studyDbId</span></td><td>string</td><td>The ID which uniquely identifies a `Study` within the given database server</td></tr>
<tr><td><span style="font-weight:bold;">trialDbId</span></td><td>string</td><td>The ID which uniquely identifies a `Trial` within the given database server</td></tr>
</table>


 

+ Parameters
    + plateDbId (Required, ) ... The ID which uniquely identifies a `Plate`
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
        "plateBarcode": "11223344",
        "plateDbId": "a106467f",
        "plateFormat": "PLATE_96",
        "plateName": "Plate_123_XYZ",
        "programDbId": "bd748e00",
        "sampleType": "TISSUE",
        "studyDbId": "64bd6bf9",
        "trialDbId": "d34c5349"
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




### Post - /search/plates [POST /brapi/v2/search/plates]

Submit a search request for `Plates`<br/>
Search requests allow a client to send a complex query for data. However, the server may not respond with the search results immediately. 
If a server needs more time to process the request, it might respond with a `searchResultsDbId`. 
Use the corresponding `GET /search/plates/{searchResultsDbId}` to retrieve the results of the search. <br/> 
Review the <a target="_blank" href="https://wiki.brapi.org/index.php/Search_Services#POST_Search_Entity">Search Services documentation</a> for additional implementation details.

**Request Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">commonCropNames</span></td><td>array[string]</td><td>The BrAPI Common Crop Name is the simple, generalized, widely accepted name of the organism being researched. It is most often used in multi-crop systems where digital resources need to be divided at a high level. Things like 'Maize', 'Wheat', and 'Rice' are examples of common crop names.  Use this parameter to only return results associated with the given crops.   Use `GET /commoncropnames` to find the list of available crops on a server.</td></tr>
<tr><td><span style="font-weight:bold;">externalReferenceIDs</span></td><td>array[string]</td><td>**Deprecated in v2.1** Please use `externalReferenceIds`. Github issue number #460  <br>List of external reference IDs. Could be a simple strings or a URIs. (use with `externalReferenceSources` parameter)</td></tr>
<tr><td><span style="font-weight:bold;">externalReferenceIds</span></td><td>array[string]</td><td>List of external reference IDs. Could be a simple strings or a URIs. (use with `externalReferenceSources` parameter)</td></tr>
<tr><td><span style="font-weight:bold;">externalReferenceSources</span></td><td>array[string]</td><td>List of identifiers for the source system or database of an external reference (use with `externalReferenceIDs` parameter)</td></tr>
<tr><td><span style="font-weight:bold;">germplasmDbIds</span></td><td>array[string]</td><td>The ID which uniquely identifies a germplasm</td></tr>
<tr><td><span style="font-weight:bold;">germplasmNames</span></td><td>array[string]</td><td>List of human readable names to identify germplasm to search for</td></tr>
<tr><td><span style="font-weight:bold;">observationUnitDbIds</span></td><td>array[string]</td><td>The ID which uniquely identifies an observation unit</td></tr>
<tr><td><span style="font-weight:bold;">page</span></td><td>integer</td><td>Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.</td></tr>
<tr><td><span style="font-weight:bold;">pageSize</span></td><td>integer</td><td>The size of the pages to be returned. Default is `1000`.</td></tr>
<tr><td><span style="font-weight:bold;">plateBarcodes</span></td><td>array[string]</td><td>A unique identifier physically attached to the plate</td></tr>
<tr><td><span style="font-weight:bold;">plateDbIds</span></td><td>array[string]</td><td>The ID which uniquely identifies a plate of samples</td></tr>
<tr><td><span style="font-weight:bold;">plateNames</span></td><td>array[string]</td><td>The human readable name of a plate of samples</td></tr>
<tr><td><span style="font-weight:bold;">programDbIds</span></td><td>array[string]</td><td>A BrAPI Program represents the high level organization or group who is responsible for conducting trials and studies. Things like Breeding Programs and Funded Projects are considered BrAPI Programs.   Use this parameter to only return results associated with the given programs.   Use `GET /programs` to find the list of available programs on a server.</td></tr>
<tr><td><span style="font-weight:bold;">programNames</span></td><td>array[string]</td><td>Use this parameter to only return results associated with the given program names. Program names are not required to be unique.  Use `GET /programs` to find the list of available programs on a server.</td></tr>
<tr><td><span style="font-weight:bold;">sampleDbIds</span></td><td>array[string]</td><td>The ID which uniquely identifies a sample</td></tr>
<tr><td><span style="font-weight:bold;">sampleGroupDbIds</span></td><td>array[string]</td><td>The unique identifier for a group of related Samples</td></tr>
<tr><td><span style="font-weight:bold;">sampleNames</span></td><td>array[string]</td><td>The human readable name of the sample</td></tr>
<tr><td><span style="font-weight:bold;">studyDbIds</span></td><td>array[string]</td><td>List of study identifiers to search for</td></tr>
<tr><td><span style="font-weight:bold;">studyNames</span></td><td>array[string]</td><td>List of study names to filter search results</td></tr>
<tr><td><span style="font-weight:bold;">trialDbIds</span></td><td>array[string]</td><td>The ID which uniquely identifies a trial to search for</td></tr>
<tr><td><span style="font-weight:bold;">trialNames</span></td><td>array[string]</td><td>The human readable name of a trial to search for</td></tr>
</table>


**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">plateDbId</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>The ID which uniquely identifies a `Plate`</td></tr>
<tr><td><span style="font-weight:bold;">plateName</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>A human readable name for a `Plate`</td></tr>
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">plateBarcode</span></td><td>string</td><td>A unique identifier physically attached to a `Plate`</td></tr>
<tr><td><span style="font-weight:bold;">plateFormat</span></td><td>string</td><td>Enum for plate formats, usually "PLATE_96" for a 96 well plate or "TUBES" for plateless format</td></tr>
<tr><td><span style="font-weight:bold;">programDbId</span></td><td>string</td><td>The ID which uniquely identifies a `Program` within the given database server</td></tr>
<tr><td><span style="font-weight:bold;">sampleType</span></td><td>string</td><td>The type of samples taken. ex. 'DNA', 'RNA', 'Tissue', etc</td></tr>
<tr><td><span style="font-weight:bold;">studyDbId</span></td><td>string</td><td>The ID which uniquely identifies a `Study` within the given database server</td></tr>
<tr><td><span style="font-weight:bold;">trialDbId</span></td><td>string</td><td>The ID which uniquely identifies a `Trial` within the given database server</td></tr>
</table>


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "commonCropNames": [
        "Tomatillo",
        "Paw Paw"
    ],
    "externalReferenceIDs": [
        "doi:10.155454/12341234",
        "14a19841"
    ],
    "externalReferenceIds": [
        "doi:10.155454/12341234",
        "14a19841"
    ],
    "externalReferenceSources": [
        "DOI",
        "Field App Name"
    ],
    "germplasmDbIds": [
        "d745e1e2",
        "6dd28d74"
    ],
    "germplasmNames": [
        "A0000003",
        "A0000477"
    ],
    "observationUnitDbIds": [
        "3cd0ca36",
        "983f3b14"
    ],
    "page": 0,
    "pageSize": 1000,
    "plateBarcodes": [
        "11223344",
        "55667788"
    ],
    "plateDbIds": [
        "0cac98b8",
        "b96125fb"
    ],
    "plateNames": [
        "0cac98b8",
        "b96125fb"
    ],
    "programDbIds": [
        "8f5de35b",
        "0e2d4a13"
    ],
    "programNames": [
        "Better Breeding Program",
        "Best Breeding Program"
    ],
    "sampleDbIds": [
        "3bece2ca",
        "dd286cc6"
    ],
    "sampleGroupDbIds": [
        "45e1e2d7",
        "6cc6dd28"
    ],
    "sampleNames": [
        "SA_111",
        "SA_222"
    ],
    "studyDbIds": [
        "cf6c4bd4",
        "691e69d6"
    ],
    "studyNames": [
        "The First Bob Study 2017",
        "Wheat Yield Trial 246"
    ],
    "trialDbIds": [
        "d2593dc2",
        "9431a731"
    ],
    "trialNames": [
        "All Yield Trials 2016",
        "Disease Resistance Study Comparison Group"
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
                "plateBarcode": "11223344",
                "plateDbId": "a106467f",
                "plateFormat": "PLATE_96",
                "plateName": "Plate_123_XYZ",
                "programDbId": "bd748e00",
                "sampleType": "TISSUE",
                "studyDbId": "64bd6bf9",
                "trialDbId": "d34c5349"
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




### Get - /search/plates/{searchResultsDbId} [GET /brapi/v2/search/plates/{searchResultsDbId}{?page}{?pageSize}]

Get the results of a `Plates` search request <br/>
Clients should submit a search request using the corresponding `POST /search/plates` endpoint.
Search requests allow a client to send a complex query for data. However, the server may not respond with the search results immediately. 
If a server needs more time to process the request, it might respond with a `searchResultsDbId`. 
Use this endpoint to retrieve the results of the search. <br/> 
Review the <a target="_blank" href="https://wiki.brapi.org/index.php/Search_Services#POST_Search_Entity">Search Services documentation</a> for additional implementation details.



**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">plateDbId</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>The ID which uniquely identifies a `Plate`</td></tr>
<tr><td><span style="font-weight:bold;">plateName</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>A human readable name for a `Plate`</td></tr>
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">plateBarcode</span></td><td>string</td><td>A unique identifier physically attached to a `Plate`</td></tr>
<tr><td><span style="font-weight:bold;">plateFormat</span></td><td>string</td><td>Enum for plate formats, usually "PLATE_96" for a 96 well plate or "TUBES" for plateless format</td></tr>
<tr><td><span style="font-weight:bold;">programDbId</span></td><td>string</td><td>The ID which uniquely identifies a `Program` within the given database server</td></tr>
<tr><td><span style="font-weight:bold;">sampleType</span></td><td>string</td><td>The type of samples taken. ex. 'DNA', 'RNA', 'Tissue', etc</td></tr>
<tr><td><span style="font-weight:bold;">studyDbId</span></td><td>string</td><td>The ID which uniquely identifies a `Study` within the given database server</td></tr>
<tr><td><span style="font-weight:bold;">trialDbId</span></td><td>string</td><td>The ID which uniquely identifies a `Trial` within the given database server</td></tr>
</table>


 

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
                "plateBarcode": "11223344",
                "plateDbId": "a106467f",
                "plateFormat": "PLATE_96",
                "plateName": "Plate_123_XYZ",
                "programDbId": "bd748e00",
                "sampleType": "TISSUE",
                "studyDbId": "64bd6bf9",
                "trialDbId": "d34c5349"
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

+ Response 404 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - The requested object DbId is not found"
```

