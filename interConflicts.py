import json
import version_set
import find_unresolvable

#Return a list of dependencies

with open('updatedDependency.txt') as j_dependency:
  jdepend=json.load(j_dependency)


def get_req(listy,akey,dependency_list):

  for packageName in jdepend[akey]:
    
    if packageName not in dependency_list:
      dependency_list.append(packageName)
      dependName = packageName[:packageName.rfind('(')]
      ver_set = version_set.find_latest(packageName)
      dependency_copy = []
      for x in dependency_list:
        dependency_copy.append(x)
      for ver_num in ver_set:
        try:
          dependency_list = get_req(listy,dependName +'-'+str(ver_num),dependency_list)
        except KeyError:
          continue
        if len(listy) > 30000:
          listy.append(3)
          return dependency_list
        listy.append(1)
        if find_unresolvable.find_conflict(dependency_list):
      
          break
        if ver_num == ver_set[len(ver_set)-1]:
        
          listy.append(0)
        dependency_list = dependency_copy

  
  return dependency_list

