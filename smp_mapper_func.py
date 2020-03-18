import numpy as np
import pandas as pd


def sanitize_pathway_names(pw_name):
    """Makes Pathbank pathway names match. 
    Removes some special characters from PathBank pathway names, 
    and capitalizes all first letters. 

    PARAMS
    ------
    pw_name: str; pathway name.

    RETURNS
    -------
    new_pw_name: str; sanitized pathway name.
    """
    chars_to_remove_ls = ["'", '"', ","]

    new_pw_name = pw_name.title()
    for char in chars_to_remove_ls:
        new_pw_name = new_pw_name.replace(char, "")

    return new_pw_name


def get_ids(metabs_ls):
    """GETs a dataframe of all sorts of IDs from the ma.ca API.
    
    PARAMS
    ------
    metabs_ls: list of str; list of metabs as common compound names
    
    RETURNS
    -------
    d_nm_map: dataframe; dataframe of a bunch of IDs, e.g. KEGG, HMDB, InCHI...
    """
    url = "http://api.xialab.ca/mapcompounds"
    cpd_ls_str = ";".join(metabs_ls)
    payload_prefix = '{\n\t\"queryList\": \"'
    payload_suffix = '\",\n\t\"inputType\": \"name\"\n}'
    payload = payload_prefix + cpd_ls_str + payload_suffix
    headers = {'Content-Type': "application/json",
               'cache-control': "no-cache",}

    r = requests.request("POST", url, data=payload, headers=headers)
    # Convert string to dict
    resp_dict = json.loads(r.text)
    contents = []
    my_colnames = list(resp_dict[0].keys())
    for row_dict in resp_dict:
        new_row = []
        for k in my_colnames:
            new_row.append(row_dict[k])
        contents.append(new_row)

    d_nm_map = pd.DataFrame(data=contents, columns=my_colnames)
    
    return d_nm_map


def make_ref_tables(pw_id_ref_fn, pathbank_prot_ref_fn, pathbank_metab_ref_fn):
    """Join raw pathbank tables, directly downloaded from the pathbank website, by PathBank ID.
    
    PARAMS
    ------
    pw_id_ref_fn: str; fn to pathbank_all_pathways.csv
    pathbank_prot_ref_fn: str; 
    pathbank_metab_ref_fn: str; 
    
    RETURNS
    -------
    d_prot_ref_tbl: pandas df
    d_metab_ref_tbl: metabs df
    """
    # Read reference pw table data
    d_pw_ids = pd.read_csv(pw_id_ref_fn)
    d_prot_ref_tbl = pd.read_csv(pathbank_prot_ref_fn)
    d_metab_ref_tbl = pd.read_csv(pathbank_metab_ref_fn)

    colnames_ls = list(d_pw_ids.columns)
    colnames_ls[0] = "PathBank ID"
    d_pw_ids.columns = colnames_ls

    # Outer join. There will be some SMPDB IDs associated with Subject==Metabolic,
    # which results in NaNs. leave those. 
    d_prot_ref_tbl = pd.merge(d_prot_ref_tbl, d_pw_ids, on="PathBank ID", how="outer")
    d_metab_ref_tbl = pd.merge(d_metab_ref_tbl, d_pw_ids, on="PathBank ID", how="outer")
    
    return d_prot_ref_tbl, d_metab_ref_tbl


def make_metab_ref_table(pw_id_ref_fn, pathbank_metab_ref_fn):
    """Join raw pathbank tables, directly downloaded from the pathbank website, by PathBank ID.
    
    PARAMS
    ------
    pw_id_ref_fn: str; fn to pathbank_all_pathways.csv
    pathbank_prot_ref_fn: str; 
    pathbank_metab_ref_fn: str; 
    
    RETURNS
    -------
    d_prot_ref_tbl: pandas df
    d_metab_ref_tbl: metabs df
    """
    # Read reference pw table data
    d_pw_ids = pd.read_csv(pw_id_ref_fn)
    d_metab_ref_tbl = pd.read_csv(pathbank_metab_ref_fn)

    colnames_ls = list(d_pw_ids.columns)
    colnames_ls[0] = "PathBank ID"
    d_pw_ids.columns = colnames_ls

    # Outer join. There will be some SMPDB IDs associated with Subject==Metabolic,
    # which results in NaNs. leave those. 
    d_metab_ref_tbl = pd.merge(d_metab_ref_tbl, d_pw_ids, on="PathBank ID", how="outer")
    
    return d_metab_ref_tbl
