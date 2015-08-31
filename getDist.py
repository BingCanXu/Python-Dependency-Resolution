import json
import latest_version_match

with open('updatedDependency.txt') as upDep:
 dependenc = json.load(upDep) 

dicty = {}
child_parent = {}
packageList = []

#This functions finds how far apart the conflicts are and creates the packList dictionary
def getDist(depende,top,counter):
 # print counter
  for x in dependenc[top]:
    
    if x not in packageList or depende not in child_parent[x]:
      if x not in child_parent:
        child_parent[x] = []
        child_parent[x].append(depende)
      else:
        child_parent[x].append(depende)
      if counter not in dicty:
        dicty[counter] = []
      dicty[counter].append(x)
      packageList.append(x)
      latest_dependency = latest_version_match.find_latest(x)
      getDist(x,latest_dependency,counter+1)
    #print counter
    #print x
  


# This returns the dependencies along with their number code, which will help determine the shortest distance between the two
def getRelationship(depende,top,counter):
  print top
  child_parent.clear()
  dicty.clear()
  del packageList[:]
  getDist(depende,top,counter)
  child_parent2 = {}
  for p in child_parent:
    for p2 in child_parent[p]:
      if p2 not in child_parent2:
        child_parent2[p2] = []
        child_parent2[p2].append(p)
      else:
        child_parent2[p2].append(p)
  hoff_codes = {}
  hoff_codes[top] = []
  hoff_codes[top].append('0')
  dictList = child_parent2.keys()
  #print child_parent2

  while dictList:
    for listhing in dictList:
      if listhing in hoff_codes:
        num = 0
        for innerthing in child_parent2[listhing]:
     #    print num
          num = num + 1
          if innerthing not in hoff_codes:
            hoff_codes[innerthing] = []
            for confused in hoff_codes[listhing]:
              hoff_codes[innerthing].append(confused + '.'+str(num))
          else:
            for confused in hoff_codes[listhing]:
              hoff_codes[innerthing].append(confused + '.'+str(num))
        dictList.remove(listhing)  
  return hoff_codes  
      
    
    
      

    
  
  
  
  
'''
print top
print dependenc[top]
if dependency in dependenc[top]:
  return dist
if dependenc[top] == []:
  dist = 0
  return dist
for x in dependenc[top]:
    latest_dependency = latest_version_match.find_latest(x)
    dist = dist + getDist(dependency, latest_dependency) 
return dist


'''
'''
"fabgis-0.3.0": ["fabric(==1.6.0)", "paramiko(>=1.10.0)", "pycrypto(>=2.1,!=2.4)", "ecdsa(>=0.11)", "fabtools(>=0.13.0)", "fabric(>=1.7.0)", "paramiko(>=1.10,<1.13)", "ecdsa()"]
'''
