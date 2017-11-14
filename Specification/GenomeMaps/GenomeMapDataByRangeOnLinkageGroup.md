## Genome Map Data by range on linkageGroup [/brapi/v1/maps/{mapDbId}/positions/{linkageGroupDbId}?min={min}&max={max}&pageSize={pageSize}&page={page}]

### Get map data by range on linkageGroup [GET]

markers ordered by linkageGroup and position

+ Parameters
   + mapDbId (required, string, `6`) ... unique id of the map
   + linkageGroupDbId (required, string)
   + min (optional) ... minimum position on linkage group
   + max (optional) ... maximumn position on linkage group
   + pageSize (optional, integer, `1000`) ... The size of the pages to be returned. Default is `1000`.
   + page (optional, integer, `0`) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.


+ Response 200 (application/json)

        {
            "metadata" : {
                "pagination" : {             
                    "pageSize": 1000, 
                    "currentPage": 0, 
                    "totalCount": 2, 
                    "totalPages": 1 
                },
                "status" : [],
                "datafiles": []
            }    
            "result": { 
                "data" : [
                    {
                        "markerDbId": "1",
                        "markerName": "marker1",
                        "location": "1000"
                    }, {
                        "markerDbId": "2",
                        "markerName": "marker2",
                        "location": "1001"
                    }
                ]
            }
        }

       
