import pandas as pd
import os
from config import data_folder

raw_data_file = os.path.join(data_folder, 'raw_data.csv')

def list_stations():
    df = pd.read_csv(raw_data_file)
    return [c for (c, g) in df.groupby(['STCDT'])]

def extract_station_data(id: int):
    raw_data = pd.read_csv(raw_data_file)
    print(raw_data.dtypes)
    return raw_data[raw_data['STCDT'] == id]

def generate_date_files():
    stations = list_stations()
    for s in stations:
        df = extract_station_data(s)
        csv_file = os.path.join(data_folder, '%d.csv' % s)
        df.to_csv(csv_file, index = False)



if (__name__ == '__main__'):
    generate_date_files()