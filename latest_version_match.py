from distlib.version import NormalizedVersion,NormalizedMatcher,_suggest_normalized_version
import json

#Return the latest version that match


with open('updatedVersion.txt') as j_ver:
  jver=json.load(j_ver)
  
def find_latest(dependency):
 # print dependency
  acceptable_versions = []
  packageName = dependency[:dependency.rfind('(')]
  m = NormalizedMatcher(dependency)
  if not jver[packageName]:
    return ''
  for ver_num in jver[packageName]:
    norm_ver=NormalizedVersion(ver_num)
    if (m.match(norm_ver)):
      acceptable_versions.append(norm_ver)     
  latest_vers = NormalizedVersion('0.0.0')
  for vers in acceptable_versions:
    if vers >= latest_vers:
      latest_vers = vers
  
  return packageName + '-' + str(latest_vers)
    
