import pandas as pd
import datetime

crr_date = datetime.datetime.now()

#read_file = pd.DataFrame(pd.read_excel("PMLA sheet.xlsx"))
#print(df.head())

d = crr_date.strftime("%d")
m = crr_date.strftime("%m")
Y = crr_date.strftime("%Y")
y = crr_date.strftime("%y")


#print(fdate)

# read_file.to_csv ("PMLA.csv", 
#                   index = None,
#                   header=True)
df = pd.DataFrame(pd.read_csv("PMLA.csv"))

#print(df.head())

file_names = df['InputFile Name'].to_list()

for i in range(len(file_names)):
    file_names[i] = file_names[i].replace('dd', d)
    file_names[i] = file_names[i].replace('mm', m)
    file_names[i] = file_names[i].replace('yyyy', Y)
    file_names[i] = file_names[i].replace('yy', y)
    file_names[i] = file_names[i].replace('<', '')
    file_names[i] = file_names[i].replace('>', '')
    #print(file_names[i])

df['InputFile Name'] = file_names
print(df.head())