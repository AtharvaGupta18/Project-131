import csv
import pandas as pd

df = pd.read_csv('final_data.csv')
del df['Unnamed: 0']
print(df.head())

radius = df['Radius'].to_list()
mass = df['Mass'].to_list()

mass_final = []
radius_final = []
g1 = []
gravity = []

for m in mass:
    m = float(m)*6.957e+8
    print(m)
    mass_final.append(m)
    g1.append(float(m*6.674e-11))

for r in radius:
    r = float(r)*(1.989e+30)
    print(r)
    radius_final.append(r)

for index, i in enumerate(g1):
    gravity.append(float(g1[index]/(radius_final[index] * radius_final[index]))) 

df['Mass'] = mass_final
df['Radius'] = radius_final
df['Gravity'] = gravity

df.to_csv('p131file.csv')