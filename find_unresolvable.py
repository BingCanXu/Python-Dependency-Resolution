import json
import compromise



def find_conflict(listy):
  dicty={}
  for zz in listy:
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
        return False
        
  return True
