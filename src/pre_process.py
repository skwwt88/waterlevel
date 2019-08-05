import pandas as pd
import os
from config import data_folder

raw_data_file = os.path.join(data_folder, 'raw_data.csv')
raw_data = pd.read_csv(raw_data_file)

print(raw_data)