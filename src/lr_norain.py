from sklearn.linear_model import LinearRegression
from config import reduced_data
from datetime import datetime, timedelta

def load_raw_data():
    import pickle

    with open(reduced_data, 'rb') as handle:
        data = pickle.load(handle)
        return data

stations = ['63301600', '63307200', '63310600', '63309600', '63301150', '63310400', '63307800', '63309200']
def generate_samples_single_station(startTime, endTime, station):
    raw_data = load_raw_data()
    
    def get_z(entries, s):

        for e in entries:
            if e.station == s:
                return e.avg_z
        
        return 0

    x = []
    y = []
    for record in [[tm, v] for tm, v in raw_data.items() if tm < endTime and tm > startTime]:
        feature = []
        invalid = False
        for i in range(0, 48):
            delta = timedelta(hours=i)
            tm = record[0] - delta

            if tm not in raw_data:
                invalid = True
                break

            telemteries = sorted(raw_data[tm], key=lambda t: t.station)

            tmp_x = {s:0 for s in stations}
            for t in telemteries:
                tmp_x[t.station] = t.drp
            
            feature.extend([tmp_x[s] for s in stations])
        
        if invalid:
            continue

        x.append(feature)
        tmp_y = get_z(record[1], station) - get_z(raw_data[record[0] - timedelta(hours=25)], station)
        y.append(tmp_y)

    return x, y

if __name__ == "__main__":
    X_train, y_train = generate_samples_single_station(datetime(2019, 1, 1), datetime(2019, 9, 2), '63301150')
    X_test, y_test = generate_samples_single_station(datetime(2018, 9, 2), datetime(2018, 9, 3), '63301150')

    model = LinearRegression()
    model.fit(X_train, y_train)

    y_predicted = model.predict(X_test)

    for i in range(len(X_test)):
        print("{0}:{1}".format(y_predicted[i], y_test[i]))