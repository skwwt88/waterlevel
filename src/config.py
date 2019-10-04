import os

src_folder = os.path.dirname(os.path.abspath(__file__))
data_folder = os.path.abspath(src_folder + "/../data")
model_folder = os.path.abspath(src_folder + "/../models")
river_data = os.path.join(data_folder, "river.json")
rain_data = os.path.join(data_folder, "rain.json")
all_data = os.path.join(data_folder, "all_data-1004-1")
reduced_data = os.path.join(data_folder, "reduced_data-1004-1")

if __name__ == "__main__":
    print(src_folder)
    print(data_folder)
    print(model_folder)