Pagination
==========

The pagination object is applicable only when the result payload
contains a data field. It describes the pagination of the records
contained in the data array, as a way to identify which subset of data
is being returned.

If the ``data`` array is not present in the results, pagination should be
ignored. All of the following responses are acceptable, and should be
ignored equally.


::

  pagination key omitted from the metadata
  "pagination": null
  "pagination": {}
  "pagination": {"totalCount" : 0, "pageSize" : 0, "totalPages" : 0, "currentPage" : 0}


Most endpoints in BrAPI use page index numbers to determine how to get
the next page of data. Page numbers start at zero, so the first page
will be page 0 (zero). When appropriate, a request will have two
parameters for paging: page and pageSize. If these query parameters are
omitted from the request, the defaults will be page=0 and pageSize=1000.
page allows the client to request a specific page number. Page numbers
start at zero, so the first page will be ?page=0. pageSize allows the
client to control the maximum number of records that will be returned
per page. A typical paged response will have four fields: currentPage,
pageSize, totalCount and totalPages. currentPage is the number for the
current returned page. In most cases, this will be a confirmation of the
requested page parameter. If page is not populated in the request, then
currentPage should have the default value zero, indicating the first
page of data was retrieved by default. pageSize indicates the number
of records in the current response page. totalCount indicates the total
number of records available in the unpaged super set. totalPages
indicates the total number of pages available and can be calculated
with the formula totalCount / requested pageSize.

Note: A small subset of BrAPI endpoints use a nextPageToken instead of
an page number. These endpoints are related to Genotyping and the
alternative paging scheme is better suited to handle larger data sets.
These endpoints are clearly marked as different from the norm and the
paging mechanism is described in more detail in the endpoint
descriptions.
