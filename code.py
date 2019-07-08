# --------------
import yaml

# Read the data of the format .yaml type
with open(path, 'r') as f:
    loadFile = yaml.load(f)

# Find data type of the file
print(type(loadFile))

# In which city, and at which venue the match was played and where was it played ?

print("City", loadFile['info']['city'])
print("Venue", loadFile['info']['venue'])
# Which are all the teams that played in the tournament ? How many teams participated in total?
print("Teams", loadFile['info']['teams'])
print("Total Teams", len(loadFile['info']['teams']))
# Which team won the toss and what was the decision of toss winner ?
print("Toss won By: ", loadFile['info']['toss']['winner'])
print("Decesion : ", loadFile['info']['toss']['decision'])

# Find the first bowler and first batsman who played the first ball of the first inning

#print((loadFile['innings'][0]['1st innings']['deliveries'][0][0.1]['bowler']))
print("First Bowler :", loadFile['innings'][0]['1st innings']['deliveries'][0][0.1]['bowler'])
print("First Batsman :", loadFile['innings'][0]['1st innings']['deliveries'][0][0.1]['batsman'])

# How many deliveries were delivered in first inning ?
print("No of Deliveries :", len(loadFile['innings'][0]['1st innings']['deliveries']))

# How many deliveries were delivered in second inning ?
print("No of Deliveries :", len(loadFile['innings'][1]['2nd innings']['deliveries']))

# Which team won and how ?
print("Team : ", loadFile['info']['outcome']['winner'])
print("Won by", loadFile['info']['outcome']['by']['runs'])



