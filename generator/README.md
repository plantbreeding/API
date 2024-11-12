
# BrAPI Schema Generator

Generates the OpenAPI Specification, GraphQL Schema and OWL Model from the JSON Schema.
The files are generated in the Specification/Generated directory.

### How to use

To generate all use the following
    ```
    ./gradlew generateAll
    ```
For individual tasks try

* *generateGraphQL* to generate the GraphQL Schema from the JSON Schema
* *generateOpenAPI* to generate the OpenAPI Specification from the JSON Schema
* *generateOWL* to generate the OWL Model from the JSON Schema
* *validate* to validate the JSON Schema without generating any file 

The files are generated in the Specification/Generated directory.

to change the version of BrAPI used in the file name edit the *brapiVersion* in
[Settings](settings.gradle).

### Configuration

To configure the generator see https://github.com/plantbreeding/brapi-schema-tools


