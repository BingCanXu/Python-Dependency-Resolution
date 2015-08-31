from distlib.version import NormalizedVersion,NormalizedMatcher,_suggest_normalized_version
import json



with open('updatedVersion.txt') as j_ver:
  jver=json.load(j_ver)
  
# This function returns all the acceptable versions for the dependency
def compromise(dependency):
  acceptable_versions = []
  packageName = dependency[:dependency.rfind('(')]
  m = NormalizedMatcher(dependency)
  if not jver[packageName]:
    print "lol gg"
  for ver_num in jver[packageName]:
    norm_ver=NormalizedVersion(ver_num)
    if (m.match(norm_ver)):
      acceptable_versions.append(str(norm_ver))     
  
  return acceptable_versions
    
