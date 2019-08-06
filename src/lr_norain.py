from sklearn.linear_model import LinearRegression
from pre_process import generate_samples_single_station

id = 69794
train_set_size = 300
test_set_size = 20

X_train, y_train = generate_samples_single_station(id, train_set_size)
X_test, y_test = generate_samples_single_station(id, test_set_size)


model = LinearRegression()
model.fit(X_train, y_train)

y_predicted = model.predict(X_test)

for i in range(test_set_size):
    print(X_test[i])
    print(y_predicted[i])
    print(y_test[i])