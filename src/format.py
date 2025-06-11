import xmltodict, ast
import pandas as pd


def extract_text(val):
    try:
        parsed = ast.literal_eval(val)
        return parsed['#text']
    except:
        return None
    
def parse_observation(obser_str):
    data = ast.literal_eval(obser_str)
    row_dict = {}

    for key in data:
        if key == "@type": continue
        elif key == "DateTime":
            row_dict[key] = data[key]
        else:
            sub_dic = data[key]
            # format column name
            unit = sub_dic.get('@Unit') or sub_dic.get("@unit")
            text = sub_dic.get("#text")
            col_name = f'{key}({unit})'
            row_dict[col_name] = text
    
    return row_dict

def convert_dtypes(df: pd.DataFrame) -> pd.DataFrame:
    for col in df.columns:
        if 'Name' in col or col == 'Province':
            df[col] = df[col].astype(str)
        elif col == 'DateTime':
            df[col] = pd.to_datetime(df[col], errors='coerce')
        else:
            df[col] = pd.to_numeric(df[col], errors='coerce')
    return df

def formatting(file: str):
    df = pd.read_csv(file)

    parsed_rows = df['Observation'].apply(parse_observation)
    parsed_df = pd.DataFrame(parsed_rows.tolist())
    df = pd.concat([df.drop(['Observation'], axis =1 ), parsed_df], axis = 1)

    l = ['Latitude', 'Longitude']
    for key in l: df[key] = df[key].apply(extract_text)

    df = convert_dtypes(df)
    df.to_parquet("data/format.parquet")

    return df

if __name__ == "__main__":
    formatting("data/raw.csv")
    print("formatting successful...")
