BrAPI-Genotyping Concept Dictionary
==============

Allele Matrix
-----

The Allele Matrix object is used to describe a matrix of genotyping results. This 2d 
array of data reduces the overall size of the response for larger datasets, when 
compared to the Calls endpoints. This makes genotype data retrieval faster and easier.


CallSet
-----

A CallSet represents a Sample that was used during some sequencing event. In most 
cases, the CallSet will have a 1-to-1 relationship with a given Sample. However, in 
some cases, a single Sample may be used in multiple different sequencing events or 
experiments. The CallSet gives an identifier to the relationship between a Sample and 
a genotype sequencing event. In a VCF file, CallSets are the columns are the data 
matrix.


Call
--------

From the GA4GH Variants specification: A Call encodes the genotype of an individual 
with respect to a variant, as determined by some analysis of experimental data.


Genome Maps
------

Notes on the GenomeMaps objects:

- type: [Genetic | Physical]
- unit: [cM | Mb]
- linkageGroup: may be scaffold (i.e. linkageGroupCount may consist of chromosomes or scaffolds or a combination of the two)
- For genetic maps, map naming convention should tell whether it is a consensus or mapping population (name of population) map for genetic maps
- For physical maps, map naming convention should tell whether it is a reference genome (name of line) or pan-genome


Plates
------

API methods for tracking/managing Plates which contain Samples and related meta-data. 
A Plate is usually a plastic tray full of Samples, or a collection of test tubes 
grouped together.


Reference Sets
------

From GA4GH Variants schema documentation

A reference genome is a genome assembly that other genomes are compared to and 
described with respect to. For example, sequencing reads are mapped to and described 
with respect to a reference genome in the API, and genetic variations are described 
as edits to reference scaffolds/contigs. In the API a reference genome is described 
by a ReferenceSet. In turn a ReferenceSet is composed of a set of Reference objects, 
each which represents a scaffold or contig in the assembly. Reference sequences are 
expected to have unique names within a ReferenceSet


References
------

From GA4GH Variants schema documentation

A reference genome is a genome assembly that other genomes are compared to and 
described with respect to. For example, sequencing reads are mapped to and described 
with respect to a reference genome in the API, and genetic variations are described 
as edits to reference scaffolds/contigs. In the API a reference genome is described 
by a ReferenceSet. In turn a ReferenceSet is composed of a set of Reference objects, 
each which represents a scaffold or contig in the assembly. Reference sequences are 
expected to have unique names within a ReferenceSet


Samples
-----

API methods for tracking/managing plant samples and related meta-data. A BrAPI 
Sample is the set of identifiers and metadata associated with a physical piece of 
biological material collected from the field for external analysis. A Sample can take 
many forms (leaf clipping, seed, DNA, etc) and might be used for a variety of 
analysis procedures (spectra, genotyping, etc).


VariantSets
-----



Variants
-----

A Variant describes a site of interest in a genetic sequence. It is usually described in terms of being compared to a Reference.

A Variant may also describe a more traditional marker, which can be positioned on a GenomeMap.


Vendor Samples
-----

This interface is specific to facilities that performs an external analysis, such as genotyping facilities. The interface should be implemented by that facility's server. The breeding database is the client of this interface.

Note that to use these calls, you likely have to use the authentication call prior to connecting (see Authentication best practices).


