# SMP-Mapper

(Slight misnomer - should be PathBank mapper now)

Given a whole bunch of stuff from [PathBank](https://pathbank.org), map significantly differentially abundant metabolites onto `.svg` pathways.

* Simple svgs are the file of choice. At the time of this writing, these aren't available from the website, contact PathBank for these.
* Use the pathway enrichment analysis module from `metaboanalyst.ca` to find differentially enriched pathways.
* Use a differential abundance analysis methodology of your choice (e.g. multiple t-tests) to find significantly differentially abundant metabolites between case and control, and plot these on the `svg`s of differentially enriched pathways. 

### PathBank Files

in `/db`. Not actually in this repo; get them [here](https://pathbank.org/downloads)

* `pathbank_all_pathways_nodesc.csv` - headers: `SMPDB ID` (which is Pathbank ID, e.g. `SMP0000055`), `PW ID` (e.g. `PW000005`), `Name` (pathway name), `Subject`. A very verbose `Description` column removed.
* `pathbank_all_metabolites.csv` - lots of columns. Contains a whole lot of organisms; can't tell if each organism has a unique `SMPDB ID`/`PathBank ID`. Used to retrieve the `Metabolite ID` (e.g. `PW_C000414`)
* At some point, the results from `MetaboAnalyst.ca` will have to be used to
