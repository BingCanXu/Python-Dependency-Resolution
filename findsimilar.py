import compromise

#Return a list of version numbers that work for both parameter dependencies
def simar(p1,p2):
  bigList = []
  bigList.append(compromise.compromise(p1))
  bigList.append(compromise.compromise(p2))
  result = set(bigList[0])
  for s in bigList[1:]:
      result.intersection_update(s)
  xres = str(result)
  finalres = xres[xres.find('[')+1:xres.find(']')].replace(' ','')
  return finalres
