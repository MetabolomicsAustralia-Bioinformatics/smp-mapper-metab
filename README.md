### PathBank Files

in `/db`. Not actually in this repo; get them [here](https://pathbank.org/downloads)

* `pathbank_all_pathways_nodesc.csv` - headers: `SMPDB ID` (which is Pathbank ID, e.g. `SMP0000055`), `PW ID` (e.g. `PW000005`), `Name` (pathway name), `Subject`. A very verbose `Description` column removed.
* `pathbank_all_metabolites.csv` - lots of columns. Contains a whole lot of organisms; can't tell if each organism has a unique `SMPDB ID`/`PathBank ID`. Used to retrieve the `Metabolite ID` (e.g. `PW_C000414`)
