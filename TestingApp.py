#Testing App

import json
import pandas as pd
from flask import Flask, render_template

file_name = "lesson10_jsonfile"

file = open(file_name,'w')

open_file = open(file_name,'r')

opened_file = json.load(open_file)

print(f"There are {len(opened_file['name'])} records.")

new_df = pd.DataFrame(opened_file)

ny_df = new_df[new_df['city'] == 'New York']

print(f"There is {len(ny_df)} occurance(s) with companies based in New York")

ny_json = ny_df.to_json(orient = 'records')

ny_json = json.loads(ny_json)

app = Flask("New_York")

@app.route('/')
def new_york():
    return ny_json

