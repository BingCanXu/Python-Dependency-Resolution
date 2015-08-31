import json
import compromise
import latest_version


dictlol = {}

with open('newpwoc.txt') as unresolv:
  resc = json.load(unresolv)


counter = 0
pipnogood = []

for x in resc:
 


  dicty = {}
  finalres = ''
  for zz in resc[x]:
    v = zz[:zz.find('(')]
    if v not in dicty:
      dicty[v] = []
      dicty[v].append(zz)
    else:
      dicty[v].append(zz)
  newdict = {}
  for zzz in dicty:
    if len(dicty[zzz]) > 1:
      newdict[zzz] = dicty[zzz]
  for x in newdict:
    set1 = latest_version.find_latest(newdict[x][0])
    bigList = []
    for olo in newdict[x]:
      bigList.append(compromise.compromise(olo))
    result = set(bigList[0])
    for s in bigList[1:]:
        result.intersection_update(s)
    xres = str(result)
    finalres = xres[xres.find('[')+1:xres.find(']')].replace(' ','')
    
    if set1 not in finalres:
      print counter
      counter = counter + 1
      pipnogood.append(x)
      break
json.dump(pipnogood, open('pipnogood','w'))
          
       
