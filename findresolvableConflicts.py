import json
import compromise
import findsimilar

#Separate the conflicts into resolvable and unresolvable

with open('packWconflicts') as jexample:
  je = json.load(jexample)

resolvableConflict = {}
unresolvableConflict = {}
unresolvable = 0
resolvable = 0
counter = 0
for x in je:
  counter = counter + 1
  #print counter 
  dicty = {}
  finalres = ''
  for zz in je[x]:
    v = zz[:zz.find('(')]
    if v not in dicty:
      dicty[v] = []
      dicty[v].append(zz)
    else:
      dicty[v].append(zz)
  for zz in dicty:
    if len(dicty[zz]) > 1:
      
      bigList = []
      for vpo in dicty[zz]:
        bigList.append(compromise.compromise(vpo))
      result = set(bigList[0])
      for s in bigList[1:]:
          result.intersection_update(s)
      xres = str(result)
      finalres = xres[xres.find('[')+1:xres.find(']')].replace(' ','')
      #print bigList
      #print finalres
      if finalres == '':
        unresolvable = unresolvable + 1
        unresolvableConflict[x] = je[x]
        break
  if finalres != '':    
    resolvable = resolvable + 1
    resolvableConflict[x] = je[x]
        
print "unresolvable = " + str(unresolvable)
print "resolvable = " + str(resolvable)      
    
json.dump(unresolvableConflict, open("unresolvableConflict",'w'))
json.dump(resolvableConflict, open("resolvableConflict",'w'))
