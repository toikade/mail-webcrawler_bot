import os
import pandas as pd

file_path = "../h1bdatacsv"
#file_list = os.listdir(file_path)
file_list = ['message_data_columns.csv', 'message_data_columns1.csv']

df = pd.DataFrame()
for file in file_list:
    #data = pd.read_csv(f"../h1bdatacsv/{file}")
    data = pd.read_csv(file)
    df = pd.concat([df, data], axis=0)
#df.to_csv('merged_files.csv', index=False)
df.to_csv('final_h1b_email_data.csv', index=False)

