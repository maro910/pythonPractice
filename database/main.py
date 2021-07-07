import csv
import os
import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine 

data = pd.read_csv("cities.csv")

engine = create_engine('mysql://root:codio@localhost/location')
data.to_sql('information', con=engine, if_exists='replace', index=False)

os.system("mysqldump -u root -pcodio location > visual.sql")
print(data)