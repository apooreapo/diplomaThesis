import sys
from extract_features import Extraction
import glob
import pandas as pd
import gc

file_titles = "./extracted_features/short_updated/*.csv"
files = glob.glob(file_titles)
file_titles_no_cad = "./extracted_features/short_updated/short_updated_extracted_1*.csv"
files_no_cad = glob.glob(file_titles_no_cad)
file_titles_cad = "./extracted_features/short_updated/short_updated_extracted_s*.csv"
files_cad = glob.glob(file_titles_cad)
print(f"Total number of files: {len(files)}")
print(f"Total number of CAD files: {len(files_cad)}")
print(f"Total number of NO CAD files: {len(files_no_cad)}")

dataframes_cad = []
for file in files_cad:
    # print("Hello")
    # print(file)
    new_dataframe = pd.read_csv(file)
    df_len = len(new_dataframe)
    fl_name = file.split(sep="_")
    txt_help = [fl_name[5]] * df_len
    new_dataframe["FileName"] = txt_help
    dataframes_cad.append(new_dataframe)
res_cad = pd.concat(dataframes_cad, ignore_index=True)
output = "./extracted_features/short_updated/" + "s_updated_cad.csv"
res_cad.to_csv(path_or_buf=output)

dataframes_no_cad = []
for file in files_no_cad:
    new_dataframe = pd.read_csv(file)
    df_len = len(new_dataframe)
    fl_name = file.split(sep="_")
    txt_help = [fl_name[5]] * df_len
    new_dataframe["FileName"] = txt_help
    dataframes_no_cad.append(new_dataframe)
res_no_cad = pd.concat(dataframes_no_cad, ignore_index=True)
output = "./extracted_features/short_updated/" + "s_updated_no_cad.csv"
res_no_cad.to_csv(path_or_buf=output)

dataframes = []
for file in files:
    fl_name = file.split(sep="_")
    # print("HI")
    # print(fl_name)
    if len(fl_name) > 4:
        new_dataframe = pd.read_csv(file)
        df_len = len(new_dataframe)

        # print(fl_name)
        txt_help = [fl_name[:]] * df_len
        new_dataframe["FileName"] = txt_help
        dataframes.append(new_dataframe)
res = pd.concat(dataframes, ignore_index=True)
output = "./extracted_features/short_updated/" + "s_updated_full.csv"
res.to_csv(path_or_buf=output)
