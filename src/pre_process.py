import pandas as pd
from random import randint
import os
from config import data_folder

raw_data_file = os.path.join(data_folder, 'raw_data.csv')
lookback_hour = 48

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

def generate_samples_single_station(id, count):
    csv_file = os.path.join(data_folder, '%d.csv' % id)
    df = pd.read_csv(csv_file)

    length = len(df)
    result_x = []
    result_y = []
    while count > 0:
        index = randint(0, length - lookback_hour - 24)
        x = []
        y = df.iloc[index]['Z']

        valid = True
        for i in range(lookback_hour):
            entry = df.iloc[index + i + 25]
            if entry['R'] > 0.001 or not (entry['Z'] > 0.001):
                valid = False
                break
            
            x.append(entry['Z'])
        
        for i in range(24):
            entry = df.iloc[index + i + 1]

            if entry['R'] > 0.001:
                valid = False
                break

        if valid:
           result_x.append(x)
           result_y.append(y)
           count -= 1
         
    return result_x, result_y


if (__name__ == '__main__'):
    print(generate_samples_single_station(69794, 10))