import pandas as pd
import xmltodict
import json
import ast

def formatting(file):
    df = pd.read_csv(file)

    for i in range(0,len(df)):
        obser_dict = df.iloc[i]['Observation']
        data = ast.literal_eval(obser_dict)
        for key in data:
            if(key == '@type'): continue
            if key == "DateTime":
                if key not in df.columns: df[key] = None
                df.at[i,key] = data[key]
                if(df[key].dtype != 'datetime64[ns]') : df[key] = pd.to_datetime(df[key])

            else:
                sub_dic = dict(data[key])
                #format column name
                columns_format = f'{key}({list(sub_dic.values())[0]})'

                #create column
                if columns_format not in df.columns: df[columns_format] = None

                #set column value
                try:
                    df[columns_format] = list(sub_dic.values())[1]
                except: df[columns_format] = None
    return df


if __name__ == "__main__":
    df = formatting("raw.csv")
