from datetime import datetime
from contracts import sample

# 2016-01-01T01:55:00
def str2time(input: str):
    return datetime.strptime(input,'%Y-%m-%dT%H:%M:%S')

def time2str(input: datetime):
    return input.strftime('%Y-%m-%dT%H:%M:%S')

def to_key(station: str, time:datetime):
    return "{0}-{1}".format(station, time)

def sample2key(item: sample):
    return to_key(item.station, item.tm)

if (__name__ == '__main__'):
    print(time2str(str2time("2016-01-01T01:55:00")))

    item = sample("test", str2time("2016-01-01T01:55:00"), 1.0, 2.0)
    print(sample2key(item))
