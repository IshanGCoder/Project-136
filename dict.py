import pandas as pd
df = pd.read_csv("star_with_gravity.csv")
df.head()
df.drop(['Unnamed: 0'], axis = 1, inplace = True)
name = df["Star_name"].to_list()
mass = df["Mass"].to_list()
distance = df["Distance"].to_list()
radius = df["Radius"].to_list()
gravity = df["Gravity"].to_list()
finalstarlist = []
tempdict = {}
for i in range(0,len(name)):
    tempdict["name"] = name[i]
    tempdict["mass"] = mass[i]
    tempdict["distance"] = distance[i]
    tempdict["radius"] = radius[i]
    tempdict["gravity"] = gravity[i]
    finalstarlist.append(tempdict)
    tempdict = {}
print(finalstarlist)