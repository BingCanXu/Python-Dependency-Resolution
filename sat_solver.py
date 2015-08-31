import json

with open('updatedDependency.txt') as jp:
  jd = json.load(jp)
  
#Test scenarios to break sat-solver
  
newdict = {}
counter = 0
for x in jd:
  counter = counter + 1
  print counter
  if x != "fabgis-0.3.0":
    newdict[x] = jd[x]
  else:
    newdict[x] = ["fabric(==1.6.0)", "fabtools(>=0.19.0)"]
    
json.dump(newdict, open("updatedDependencyTest.txt",'w'))
