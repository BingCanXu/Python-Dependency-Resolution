import json
import compromise
import findsimilar
import latest_version_match
import getDist

#Finds the shortest path


dictlol = {}

with open('unresolvableConflict') as unresolv:
  unresc = json.load(unresolv)

with open('updatedDependency.txt') as upDep:
 dependenc = json.load(upDep) 
counter = 0
distance = {}  
for x in unresc:
  print x
  distances = getDist.getLOL(x,x,1) 

  child_parent = getDist.getRelationship(x,x,1)
  print 3
  #print distances
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
    list_no_rep = []
    for p1 in newdict[pp1]:
      
      for p2 in newdict[pp1]:
        finalres = findsimilar.simar(p1,p2)
        if finalres == '':
          list1 = []
          list2 = []
          val1 = child_parent[p1]
          val2 = child_parent[p2]
         
          for bleh in val1:
            for blah in val2:
              
             # print blah 
             # print bleh
              indexb = 0
              while blah.find('.',indexb) != -1 \
                    and bleh.find('.',indexb) != -1 \
                    and bleh[:bleh.find('.',indexb)] == blah[:blah.find('.',indexb)]:
                indexb  = bleh.find('.',indexb) + 1
             # print indexb
              s1 = blah[indexb-1:]
              s2 = bleh[indexb-1:]
              print list_no_rep
              if s1 and s2 not in list_no_rep:
                print s1
                print s2
                shortestlen = s1.count('.') + s2.count('.')
                print shortestlen
                if x not in dictlol:
                  dictlol[x] = []
                dictlol[x].append(shortestlen) 
              list_no_rep.append(s1)
              list_no_rep.append(s2)
  print dictlol
        
        


json.dump(dictlol, open("dictlol",'w'))
