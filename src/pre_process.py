from config import river_data, rain_data, all_data, reduced_data
from utils import str2time, sample2key, to_key
from contracts import sample, telemetry
from datetime import time, datetime
import json

def import_data():
    result = {}
    input_file = open(river_data)
    json_array = json.load(input_file)

    count = 0
    for i in json_array:
        station = i['STCD']
        tm = str2time(i['TM'])
        z = float(i['Z'])
        
        if tm < datetime(2017, 1, 1):
            continue

        item = sample(station, tm, z, 0)
        result[sample2key(item)] = item

        count += 1
        if count % 1000 == 0:
            print(count)

    input_file = open(rain_data)
    json_array = json.load(input_file)
    miss_items = 0
    count = 0
    for i in json_array:
        station = i['STCD']
        tm = str2time(i['TM'])
        drp = i["DRP"]
        
        if tm < datetime(2017, 1, 1):
            continue

        if to_key(station, tm) in result:
            item = result[to_key(station, tm)]
            item.drp = drp
        else:
            miss_items += 1
            item = sample(station, tm, 0, drp)
            item.invalid = True
            result[sample2key(item)] = item
        
        count += 1
        if count % 1000 == 0:
            print("{0}:{1}".format(miss_items, count))
    
    return result

def store_all_data(items = None):
    import pickle 
    if items == None:
        items = import_data() 
    with open(all_data, 'wb') as handle:
        pickle.dump(items, handle, protocol=pickle.HIGHEST_PROTOCOL)

def load_all_data():
    import pickle

    with open(all_data, 'rb') as handle:
        data = pickle.load(handle)
        return data

def reduce_rain(split):
    items = [i for i in load_all_data().values()]
    record = {}
    
    count = 0
    for item in items:
        catagory = split[0]
        for i in range(0, len(split)):
            if item.tm.time() > split[i]:
                catagory = split[i]
            else:
                break

        key_datetime = datetime.combine(item.tm.date(), catagory)
        if key_datetime not in record:
            record[key_datetime] = []

        record[key_datetime].append(item)
        count += 1
        if count % 1000 == 0:
            print(count)

    result = {}
    count = 0
    for tm, samples in record.items():
        stations = {s.station for s in samples}
        result[tm] = []
        for station in stations:
            s_records = [s for s in samples if s.station == station]
            z_valid_samples = [s.z for s in s_records if s.invalid == False]
            if len(z_valid_samples) == 0:
                z_valid_samples = [0]

            min_z = min(z_valid_samples)
            max_z = max(z_valid_samples)
            avg_z = sum(z_valid_samples) / len(z_valid_samples)
            drp = sum([s.drp for s in s_records])
            invalid = len(s_records) != len(z_valid_samples)
            t = telemetry(station, avg_z=avg_z, max_z=max_z, min_z=min_z, drp=drp)
            t.invalid = invalid
            result[tm].append(t)
        
        count += 1
        if count % 1000 == 0:
            print(count)

    print(len(result))

    import pickle 
    with open(reduced_data, 'wb') as handle:
        pickle.dump(result, handle, protocol=pickle.HIGHEST_PROTOCOL)    

if (__name__ == "__main__"):
    # store_all_data()
        
    reduce_rain([time(i) for i in range(0, 24)])