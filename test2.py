import pandas as pd

df = pd.read_csv("PMLA.csv")

file_names = df['InputFile Name'].to_list()
src_path = df['0Margin Path'].to_list()
dest_path = df['PMLA (Server) Path'].to_list()


for i in range(len(file_names)):
    file_names[i] = file_names[i].replace('<', '')
    file_names[i] = file_names[i].replace('>', '')

for i in range(len(src_path)):
    src_path[i] = src_path[i].replace('JAN2022', 'month')
    src_path[i] = src_path[i].replace('02012022', 'date')

df['InputFile Name'] = file_names
df['0Margin Path'] = src_path

print(df.head())