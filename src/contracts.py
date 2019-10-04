from datetime import time, date, datetime

class sample:
    def __init__(self, station: str, tm: datetime, z: float, drp: float):
        self.station = station
        self.tm = tm
        self.z = z
        self.drp = drp
        self.invalid = False

    def generate_key(self, split):
        catagory = split[0]
        
        for i in range(0, len(split)):
            if self.tm.time() > split[i]:
                catagory = split[i]
            else:
                break

        return "{0}-{1}".format(self.station, datetime.combine(self.tm.date(), catagory))
    

class telemetry:
    def __init__(self, station: str, avg_z = None, max_z = None, min_z = None, drp = None):
        self.avg_z = avg_z
        self.max_z = max_z
        self.min_z = min_z
        self.drp = drp
        self.station = station
        self.invalid = False   

if (__name__ == '__main__'):
    test = sample("a", datetime(2019, 9, 30, 5, 2, 1), 1.0, 1.0)
    print(test.generate_key([time(2), time(4), time(8)]))
    print(test.tm)

        
