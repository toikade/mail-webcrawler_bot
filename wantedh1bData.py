import pandas as pd 

df = pd.read_csv('h1bdata.csv')

#message_data_columns = df[["CASE_STATUS", "VISA_CLASS", "JOB_TITLE", "SOC_TITLE", "EMPLOYER_NAME", "EMPLOYER_STATE", "EMPLOYER_POC_FIRST_NAME", "EMPLOYER_POC_LAST_NAME", "EMPLOYER_POC_EMAIL", "EMPLOYER_STATE"]].dropna().drop_duplicates(subset='EMPLOYER_POC_EMAIL', keep="first")
message_data_columns = df[["CASE_STATUS", "JOB_TITLE", "EMPLOYER_NAME", "WORKSITE_STATE", "EMPLOYER_POC_FIRST_NAME", "EMPLOYER_POC_LAST_NAME", "EMPLOYER_POC_EMAIL"]].dropna().assign(VISA_CLASS='H-1B', SOC_TITLE=df['JOB_TITLE'], EMPLOYER_STATE=df['WORKSITE_STATE']).drop_duplicates(subset='EMPLOYER_POC_EMAIL', keep="first")

message_data_columns.to_csv("message_data_columns1.csv", index=0)

