
# Group Scales

API to manage the details of observation variable Scales. An observation variable is composed by the unique combination of one Trait, one Method and one Scale. A Scale describes the units and acceptable values for a Variable. For example, an Observation Variable might be defined with a Trait of "plant height", a Scale of "meters", and a Method of "tape measure". This Variable would be distinct from a Variable with the Scale "inches" or "pixels". 






### Get - /scales [GET /brapi/v2/scales{?scaleDbId}{?observationVariableDbId}{?ontologyDbId}{?commonCropName}{?programDbId}{?externalReferenceID}{?externalReferenceId}{?externalReferenceSource}{?page}{?pageSize}]

Returns a list of Scales available on a server.

An Observation Variable has 3 critical parts; A Trait being observed, a Method for making the observation, and a Scale on which the observation can be measured and compared with other observations.



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|additionalInfo|object|Additional arbitrary info|
|dataType|string|<p>Class of the scale, entries can be</p> <p>"Code" -  This scale class is exceptionally used to express complex traits. Code is a nominal scale that combines the expressions of the different traits composing the complex trait. For example a severity trait might be expressed by a 2 digit and 2 character code. The first 2 digits are the percentage of the plant covered by a fungus and the 2 characters refer to the delay in development, e.g. "75VD" means "75 %" of the plant is infected and the plant is very delayed.</p> <p>"Date" - The date class is for events expressed in a time format, See ISO 8601</p> <p>"Duration" - The Duration class is for time elapsed between two events expressed in a time format, e.g. days, hours, months</p> <p>"Nominal" - Categorical scale that can take one of a limited and fixed number of categories. There is no intrinsic ordering to the categories</p> <p>"Numerical" - Numerical scales express the trait with real numbers. The numerical scale defines the unit e.g. centimeter, ton per hectare, branches</p> <p>"Ordinal" - Ordinal scales are scales composed of ordered categories</p> <p>"Text" - A free text is used to express the trait.</p>|
|decimalPlaces|integer|For numerical, number of decimal places to be reported|
|externalReferences|array[object]|An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.|
|referenceID|string|**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.|
|referenceId|string|The external reference ID. Could be a simple string or a URI.|
|referenceSource|string|An identifier for the source system or database of this reference|
|ontologyReference|object|MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).|
|documentationLinks|array[object]|links to various ontology documentation|
|URL|string (uri)||
|type|string||
|ontologyDbId|string|Ontology database unique identifier|
|ontologyName|string|Ontology name|
|version|string|Ontology version (no specific format)|
|scaleDbId|string|Unique identifier of the scale. If left blank, the upload system will automatically generate a scale ID.|
|scaleName|string|Name of the scale <br/>MIAPPE V1.1 (DM-92) Scale Name of the scale associated with the variable|
|scalePUI|string|The Permanent Unique Identifier of a Scale, usually in the form of a URI|
|units|string|This field can be used to describe the units used for this scale. This should be the abbreviated  form of the units, intended to be displayed with every value using this scale. Usually this only  applies when `dataType` is Numeric, but could also be included for other dataTypes when applicable.|
|validValues|object||
|categories|array[object]|List of possible values with optional labels|
|label|string|A text label for a category|
|value|string|The actual value for a category|
|max|integer|**Deprecated in v2.1** Please use `maximumValue`. Github issue number #450   Maximum value for numerical scales. Typically used for data capture control and QC.|
|maximumValue|string|Maximum value for numerical, date, and time scales. Typically used for data capture control and QC.|
|min|integer|**Deprecated in v2.1** Please use `minimumValue`. Github issue number #450  <br/>Minimum value for numerical scales. Typically used for data capture control and QC.|
|minimumValue|string|Minimum value for numerical, date, and time scales. Typically used for data capture control and QC.|


 

+ Parameters
    + scaleDbId (Optional, ) ... The unique identifier for a scale
    + observationVariableDbId (Optional, ) ... The unique identifier for an observation variable
    + ontologyDbId (Optional, ) ... The unique identifier for an ontology definition. Use this parameter to filter results based on a specific ontology Use `GET /ontologies` to find the list of available ontologies on a server.
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
                "dataType": "Numerical",
                "decimalPlaces": 2,
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
                "ontologyReference": {
                    "documentationLinks": [
                        {
                            "URL": "http://purl.obolibrary.org/obo/ro.owl",
                            "type": "OBO"
                        }
                    ],
                    "ontologyDbId": "6b071868",
                    "ontologyName": "The Crop Ontology",
                    "version": "7.2.3"
                },
                "scaleDbId": "af730171",
                "scaleName": "Meters",
                "scalePUI": "http://my-traits.com/trait/CO_123:0000112",
                "units": "m",
                "validValues": {
                    "categories": [
                        {
                            "label": "low",
                            "value": "0"
                        },
                        {
                            "label": "medium",
                            "value": "5"
                        },
                        {
                            "label": "high",
                            "value": "10"
                        }
                    ],
                    "max": 9999,
                    "maximumValue": "9999",
                    "min": 2,
                    "minimumValue": "2"
                }
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




### Post - /scales [POST /brapi/v2/scales]

Create new scale objects in the database

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|additionalInfo|object|Additional arbitrary info|
|dataType|string|<p>Class of the scale, entries can be</p> <p>"Code" -  This scale class is exceptionally used to express complex traits. Code is a nominal scale that combines the expressions of the different traits composing the complex trait. For example a severity trait might be expressed by a 2 digit and 2 character code. The first 2 digits are the percentage of the plant covered by a fungus and the 2 characters refer to the delay in development, e.g. "75VD" means "75 %" of the plant is infected and the plant is very delayed.</p> <p>"Date" - The date class is for events expressed in a time format, See ISO 8601</p> <p>"Duration" - The Duration class is for time elapsed between two events expressed in a time format, e.g. days, hours, months</p> <p>"Nominal" - Categorical scale that can take one of a limited and fixed number of categories. There is no intrinsic ordering to the categories</p> <p>"Numerical" - Numerical scales express the trait with real numbers. The numerical scale defines the unit e.g. centimeter, ton per hectare, branches</p> <p>"Ordinal" - Ordinal scales are scales composed of ordered categories</p> <p>"Text" - A free text is used to express the trait.</p>|
|decimalPlaces|integer|For numerical, number of decimal places to be reported|
|externalReferences|array[object]|An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.|
|referenceID|string|**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.|
|referenceId|string|The external reference ID. Could be a simple string or a URI.|
|referenceSource|string|An identifier for the source system or database of this reference|
|ontologyReference|object|MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).|
|documentationLinks|array[object]|links to various ontology documentation|
|URL|string (uri)||
|type|string||
|ontologyDbId|string|Ontology database unique identifier|
|ontologyName|string|Ontology name|
|version|string|Ontology version (no specific format)|
|scaleName|string|Name of the scale <br/>MIAPPE V1.1 (DM-92) Scale Name of the scale associated with the variable|
|scalePUI|string|The Permanent Unique Identifier of a Scale, usually in the form of a URI|
|units|string|This field can be used to describe the units used for this scale. This should be the abbreviated  form of the units, intended to be displayed with every value using this scale. Usually this only  applies when `dataType` is Numeric, but could also be included for other dataTypes when applicable.|
|validValues|object||
|categories|array[object]|List of possible values with optional labels|
|label|string|A text label for a category|
|value|string|The actual value for a category|
|max|integer|**Deprecated in v2.1** Please use `maximumValue`. Github issue number #450   Maximum value for numerical scales. Typically used for data capture control and QC.|
|maximumValue|string|Maximum value for numerical, date, and time scales. Typically used for data capture control and QC.|
|min|integer|**Deprecated in v2.1** Please use `minimumValue`. Github issue number #450  <br/>Minimum value for numerical scales. Typically used for data capture control and QC.|
|minimumValue|string|Minimum value for numerical, date, and time scales. Typically used for data capture control and QC.|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|additionalInfo|object|Additional arbitrary info|
|dataType|string|<p>Class of the scale, entries can be</p> <p>"Code" -  This scale class is exceptionally used to express complex traits. Code is a nominal scale that combines the expressions of the different traits composing the complex trait. For example a severity trait might be expressed by a 2 digit and 2 character code. The first 2 digits are the percentage of the plant covered by a fungus and the 2 characters refer to the delay in development, e.g. "75VD" means "75 %" of the plant is infected and the plant is very delayed.</p> <p>"Date" - The date class is for events expressed in a time format, See ISO 8601</p> <p>"Duration" - The Duration class is for time elapsed between two events expressed in a time format, e.g. days, hours, months</p> <p>"Nominal" - Categorical scale that can take one of a limited and fixed number of categories. There is no intrinsic ordering to the categories</p> <p>"Numerical" - Numerical scales express the trait with real numbers. The numerical scale defines the unit e.g. centimeter, ton per hectare, branches</p> <p>"Ordinal" - Ordinal scales are scales composed of ordered categories</p> <p>"Text" - A free text is used to express the trait.</p>|
|decimalPlaces|integer|For numerical, number of decimal places to be reported|
|externalReferences|array[object]|An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.|
|referenceID|string|**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.|
|referenceId|string|The external reference ID. Could be a simple string or a URI.|
|referenceSource|string|An identifier for the source system or database of this reference|
|ontologyReference|object|MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).|
|documentationLinks|array[object]|links to various ontology documentation|
|URL|string (uri)||
|type|string||
|ontologyDbId|string|Ontology database unique identifier|
|ontologyName|string|Ontology name|
|version|string|Ontology version (no specific format)|
|scaleDbId|string|Unique identifier of the scale. If left blank, the upload system will automatically generate a scale ID.|
|scaleName|string|Name of the scale <br/>MIAPPE V1.1 (DM-92) Scale Name of the scale associated with the variable|
|scalePUI|string|The Permanent Unique Identifier of a Scale, usually in the form of a URI|
|units|string|This field can be used to describe the units used for this scale. This should be the abbreviated  form of the units, intended to be displayed with every value using this scale. Usually this only  applies when `dataType` is Numeric, but could also be included for other dataTypes when applicable.|
|validValues|object||
|categories|array[object]|List of possible values with optional labels|
|label|string|A text label for a category|
|value|string|The actual value for a category|
|max|integer|**Deprecated in v2.1** Please use `maximumValue`. Github issue number #450   Maximum value for numerical scales. Typically used for data capture control and QC.|
|maximumValue|string|Maximum value for numerical, date, and time scales. Typically used for data capture control and QC.|
|min|integer|**Deprecated in v2.1** Please use `minimumValue`. Github issue number #450  <br/>Minimum value for numerical scales. Typically used for data capture control and QC.|
|minimumValue|string|Minimum value for numerical, date, and time scales. Typically used for data capture control and QC.|


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
[
    {
        "additionalInfo": {},
        "dataType": "Numerical",
        "decimalPlaces": 2,
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
        "ontologyReference": {
            "documentationLinks": [
                {
                    "URL": "http://purl.obolibrary.org/obo/ro.owl",
                    "type": "OBO"
                }
            ],
            "ontologyDbId": "6b071868",
            "ontologyName": "The Crop Ontology",
            "version": "7.2.3"
        },
        "scaleName": "Meters",
        "scalePUI": "http://my-traits.com/trait/CO_123:0000112",
        "units": "m",
        "validValues": {
            "categories": [
                {
                    "label": "low",
                    "value": "0"
                },
                {
                    "label": "medium",
                    "value": "5"
                },
                {
                    "label": "high",
                    "value": "10"
                }
            ],
            "max": 9999,
            "maximumValue": "9999",
            "min": 2,
            "minimumValue": "2"
        }
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
                "dataType": "Numerical",
                "decimalPlaces": 2,
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
                "ontologyReference": {
                    "documentationLinks": [
                        {
                            "URL": "http://purl.obolibrary.org/obo/ro.owl",
                            "type": "OBO"
                        }
                    ],
                    "ontologyDbId": "6b071868",
                    "ontologyName": "The Crop Ontology",
                    "version": "7.2.3"
                },
                "scaleDbId": "af730171",
                "scaleName": "Meters",
                "scalePUI": "http://my-traits.com/trait/CO_123:0000112",
                "units": "m",
                "validValues": {
                    "categories": [
                        {
                            "label": "low",
                            "value": "0"
                        },
                        {
                            "label": "medium",
                            "value": "5"
                        },
                        {
                            "label": "high",
                            "value": "10"
                        }
                    ],
                    "max": 9999,
                    "maximumValue": "9999",
                    "min": 2,
                    "minimumValue": "2"
                }
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




### Get - /scales/{scaleDbId} [GET /brapi/v2/scales/{scaleDbId}]

Retrieve details about a specific scale

An Observation Variable has 3 critical parts: A Trait being observed, a Method for making the observation, and a Scale on which the observation can be measured and compared with other observations.



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|additionalInfo|object|Additional arbitrary info|
|dataType|string|<p>Class of the scale, entries can be</p> <p>"Code" -  This scale class is exceptionally used to express complex traits. Code is a nominal scale that combines the expressions of the different traits composing the complex trait. For example a severity trait might be expressed by a 2 digit and 2 character code. The first 2 digits are the percentage of the plant covered by a fungus and the 2 characters refer to the delay in development, e.g. "75VD" means "75 %" of the plant is infected and the plant is very delayed.</p> <p>"Date" - The date class is for events expressed in a time format, See ISO 8601</p> <p>"Duration" - The Duration class is for time elapsed between two events expressed in a time format, e.g. days, hours, months</p> <p>"Nominal" - Categorical scale that can take one of a limited and fixed number of categories. There is no intrinsic ordering to the categories</p> <p>"Numerical" - Numerical scales express the trait with real numbers. The numerical scale defines the unit e.g. centimeter, ton per hectare, branches</p> <p>"Ordinal" - Ordinal scales are scales composed of ordered categories</p> <p>"Text" - A free text is used to express the trait.</p>|
|decimalPlaces|integer|For numerical, number of decimal places to be reported|
|externalReferences|array[object]|An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.|
|referenceID|string|**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.|
|referenceId|string|The external reference ID. Could be a simple string or a URI.|
|referenceSource|string|An identifier for the source system or database of this reference|
|ontologyReference|object|MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).|
|documentationLinks|array[object]|links to various ontology documentation|
|URL|string (uri)||
|type|string||
|ontologyDbId|string|Ontology database unique identifier|
|ontologyName|string|Ontology name|
|version|string|Ontology version (no specific format)|
|scaleDbId|string|Unique identifier of the scale. If left blank, the upload system will automatically generate a scale ID.|
|scaleName|string|Name of the scale <br/>MIAPPE V1.1 (DM-92) Scale Name of the scale associated with the variable|
|scalePUI|string|The Permanent Unique Identifier of a Scale, usually in the form of a URI|
|units|string|This field can be used to describe the units used for this scale. This should be the abbreviated  form of the units, intended to be displayed with every value using this scale. Usually this only  applies when `dataType` is Numeric, but could also be included for other dataTypes when applicable.|
|validValues|object||
|categories|array[object]|List of possible values with optional labels|
|label|string|A text label for a category|
|value|string|The actual value for a category|
|max|integer|**Deprecated in v2.1** Please use `maximumValue`. Github issue number #450   Maximum value for numerical scales. Typically used for data capture control and QC.|
|maximumValue|string|Maximum value for numerical, date, and time scales. Typically used for data capture control and QC.|
|min|integer|**Deprecated in v2.1** Please use `minimumValue`. Github issue number #450  <br/>Minimum value for numerical scales. Typically used for data capture control and QC.|
|minimumValue|string|Minimum value for numerical, date, and time scales. Typically used for data capture control and QC.|


 

+ Parameters
    + scaleDbId (Required, ) ... Id of the scale to retrieve details of.
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
        "dataType": "Numerical",
        "decimalPlaces": 2,
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
        "ontologyReference": {
            "documentationLinks": [
                {
                    "URL": "http://purl.obolibrary.org/obo/ro.owl",
                    "type": "OBO"
                }
            ],
            "ontologyDbId": "6b071868",
            "ontologyName": "The Crop Ontology",
            "version": "7.2.3"
        },
        "scaleDbId": "af730171",
        "scaleName": "Meters",
        "scalePUI": "http://my-traits.com/trait/CO_123:0000112",
        "units": "m",
        "validValues": {
            "categories": [
                {
                    "label": "low",
                    "value": "0"
                },
                {
                    "label": "medium",
                    "value": "5"
                },
                {
                    "label": "high",
                    "value": "10"
                }
            ],
            "max": 9999,
            "maximumValue": "9999",
            "min": 2,
            "minimumValue": "2"
        }
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




### Put - /scales/{scaleDbId} [PUT /brapi/v2/scales/{scaleDbId}/]

Update the details of an existing scale

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|additionalInfo|object|Additional arbitrary info|
|dataType|string|<p>Class of the scale, entries can be</p> <p>"Code" -  This scale class is exceptionally used to express complex traits. Code is a nominal scale that combines the expressions of the different traits composing the complex trait. For example a severity trait might be expressed by a 2 digit and 2 character code. The first 2 digits are the percentage of the plant covered by a fungus and the 2 characters refer to the delay in development, e.g. "75VD" means "75 %" of the plant is infected and the plant is very delayed.</p> <p>"Date" - The date class is for events expressed in a time format, See ISO 8601</p> <p>"Duration" - The Duration class is for time elapsed between two events expressed in a time format, e.g. days, hours, months</p> <p>"Nominal" - Categorical scale that can take one of a limited and fixed number of categories. There is no intrinsic ordering to the categories</p> <p>"Numerical" - Numerical scales express the trait with real numbers. The numerical scale defines the unit e.g. centimeter, ton per hectare, branches</p> <p>"Ordinal" - Ordinal scales are scales composed of ordered categories</p> <p>"Text" - A free text is used to express the trait.</p>|
|decimalPlaces|integer|For numerical, number of decimal places to be reported|
|externalReferences|array[object]|An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.|
|referenceID|string|**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.|
|referenceId|string|The external reference ID. Could be a simple string or a URI.|
|referenceSource|string|An identifier for the source system or database of this reference|
|ontologyReference|object|MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).|
|documentationLinks|array[object]|links to various ontology documentation|
|URL|string (uri)||
|type|string||
|ontologyDbId|string|Ontology database unique identifier|
|ontologyName|string|Ontology name|
|version|string|Ontology version (no specific format)|
|scaleName|string|Name of the scale <br/>MIAPPE V1.1 (DM-92) Scale Name of the scale associated with the variable|
|scalePUI|string|The Permanent Unique Identifier of a Scale, usually in the form of a URI|
|units|string|This field can be used to describe the units used for this scale. This should be the abbreviated  form of the units, intended to be displayed with every value using this scale. Usually this only  applies when `dataType` is Numeric, but could also be included for other dataTypes when applicable.|
|validValues|object||
|categories|array[object]|List of possible values with optional labels|
|label|string|A text label for a category|
|value|string|The actual value for a category|
|max|integer|**Deprecated in v2.1** Please use `maximumValue`. Github issue number #450   Maximum value for numerical scales. Typically used for data capture control and QC.|
|maximumValue|string|Maximum value for numerical, date, and time scales. Typically used for data capture control and QC.|
|min|integer|**Deprecated in v2.1** Please use `minimumValue`. Github issue number #450  <br/>Minimum value for numerical scales. Typically used for data capture control and QC.|
|minimumValue|string|Minimum value for numerical, date, and time scales. Typically used for data capture control and QC.|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|additionalInfo|object|Additional arbitrary info|
|dataType|string|<p>Class of the scale, entries can be</p> <p>"Code" -  This scale class is exceptionally used to express complex traits. Code is a nominal scale that combines the expressions of the different traits composing the complex trait. For example a severity trait might be expressed by a 2 digit and 2 character code. The first 2 digits are the percentage of the plant covered by a fungus and the 2 characters refer to the delay in development, e.g. "75VD" means "75 %" of the plant is infected and the plant is very delayed.</p> <p>"Date" - The date class is for events expressed in a time format, See ISO 8601</p> <p>"Duration" - The Duration class is for time elapsed between two events expressed in a time format, e.g. days, hours, months</p> <p>"Nominal" - Categorical scale that can take one of a limited and fixed number of categories. There is no intrinsic ordering to the categories</p> <p>"Numerical" - Numerical scales express the trait with real numbers. The numerical scale defines the unit e.g. centimeter, ton per hectare, branches</p> <p>"Ordinal" - Ordinal scales are scales composed of ordered categories</p> <p>"Text" - A free text is used to express the trait.</p>|
|decimalPlaces|integer|For numerical, number of decimal places to be reported|
|externalReferences|array[object]|An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.|
|referenceID|string|**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.|
|referenceId|string|The external reference ID. Could be a simple string or a URI.|
|referenceSource|string|An identifier for the source system or database of this reference|
|ontologyReference|object|MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).|
|documentationLinks|array[object]|links to various ontology documentation|
|URL|string (uri)||
|type|string||
|ontologyDbId|string|Ontology database unique identifier|
|ontologyName|string|Ontology name|
|version|string|Ontology version (no specific format)|
|scaleDbId|string|Unique identifier of the scale. If left blank, the upload system will automatically generate a scale ID.|
|scaleName|string|Name of the scale <br/>MIAPPE V1.1 (DM-92) Scale Name of the scale associated with the variable|
|scalePUI|string|The Permanent Unique Identifier of a Scale, usually in the form of a URI|
|units|string|This field can be used to describe the units used for this scale. This should be the abbreviated  form of the units, intended to be displayed with every value using this scale. Usually this only  applies when `dataType` is Numeric, but could also be included for other dataTypes when applicable.|
|validValues|object||
|categories|array[object]|List of possible values with optional labels|
|label|string|A text label for a category|
|value|string|The actual value for a category|
|max|integer|**Deprecated in v2.1** Please use `maximumValue`. Github issue number #450   Maximum value for numerical scales. Typically used for data capture control and QC.|
|maximumValue|string|Maximum value for numerical, date, and time scales. Typically used for data capture control and QC.|
|min|integer|**Deprecated in v2.1** Please use `minimumValue`. Github issue number #450  <br/>Minimum value for numerical scales. Typically used for data capture control and QC.|
|minimumValue|string|Minimum value for numerical, date, and time scales. Typically used for data capture control and QC.|


 

+ Parameters
    + scaleDbId (Required, ) ... Id of the scale to retrieve details of.
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "additionalInfo": {},
    "dataType": "Numerical",
    "decimalPlaces": 2,
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
    "ontologyReference": {
        "documentationLinks": [
            {
                "URL": "http://purl.obolibrary.org/obo/ro.owl",
                "type": "OBO"
            }
        ],
        "ontologyDbId": "6b071868",
        "ontologyName": "The Crop Ontology",
        "version": "7.2.3"
    },
    "scaleName": "Meters",
    "scalePUI": "http://my-traits.com/trait/CO_123:0000112",
    "units": "m",
    "validValues": {
        "categories": [
            {
                "label": "low",
                "value": "0"
            },
            {
                "label": "medium",
                "value": "5"
            },
            {
                "label": "high",
                "value": "10"
            }
        ],
        "max": 9999,
        "maximumValue": "9999",
        "min": 2,
        "minimumValue": "2"
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
        "additionalInfo": {},
        "dataType": "Numerical",
        "decimalPlaces": 2,
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
        "ontologyReference": {
            "documentationLinks": [
                {
                    "URL": "http://purl.obolibrary.org/obo/ro.owl",
                    "type": "OBO"
                }
            ],
            "ontologyDbId": "6b071868",
            "ontologyName": "The Crop Ontology",
            "version": "7.2.3"
        },
        "scaleDbId": "af730171",
        "scaleName": "Meters",
        "scalePUI": "http://my-traits.com/trait/CO_123:0000112",
        "units": "m",
        "validValues": {
            "categories": [
                {
                    "label": "low",
                    "value": "0"
                },
                {
                    "label": "medium",
                    "value": "5"
                },
                {
                    "label": "high",
                    "value": "10"
                }
            ],
            "max": 9999,
            "maximumValue": "9999",
            "min": 2,
            "minimumValue": "2"
        }
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

