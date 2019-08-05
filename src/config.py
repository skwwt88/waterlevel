import os

src_folder = os.path.dirname(os.path.abspath(__file__))
data_folder = os.path.abspath(src_folder + "/../data")
model_folder = os.path.abspath(src_folder + "/../models")

if __name__ == "__main__":
    print(src_folder)
    print(data_folder)
    print(model_folder)