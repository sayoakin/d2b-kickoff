import json

import pandas as pd


def json_csv(path):
    try:
        with open(path, 'r') as j_file:
            json_file = json.load(j_file)
        df = pd.DataFrame()
        df['Name'] = json_file["name"]
        df['Age'] = json_file["age"]
        df.to_csv("data/json_csv.csv")
        print(df)

    except Exception as e:
        print(e)
        print("File type is not json")
        print("input json file of 1 degree")


f_path = "C:/Users/user/Desktop/DATA2BOT/First_Pro/data-c/data/user.json"
a = json_csv(f_path)
