import json
import compromise
import findsimilar
import latest_version_match
import getDist
import sys

#Finds all the distance among unresolvable conflicts

dictlol = {}

with open('unresolvableConflict') as unresolv:
  unresc = json.load(unresolv)

with open('updatedDependency.txt') as upDep:
 dependenc = json.load(upDep) 
counter = 0
distance = {}  
for x in unresc:
  print x

  distances = getDist.getLOL(x,1) 

  print distances
  counter = counter + 1
  #print counter 
  dicty = {}
  finalres = ''
  for zz in unresc[x]:
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
  for pp1 in newdict:
    for p1 in newdict[pp1]:
      for p2 in newdict[pp1]:

        finalres = findsimilar.simar(p1,p2)
        if finalres == '':
          val1 = distances[p1]
          val2 = distances[p2]
          for meh in val1:
            for meh2 in val2:
              difference = meh-meh2
              if difference >= 0:
                print difference
                if difference not in dictlol: 
                  dictlol[difference] = 1
                else:
                  dictlol[difference] = dictlol[difference] + 1
          
        
        

       
print dictlol

json.dump(dictlol, open("dictlol",'w'))
