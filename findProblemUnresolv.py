import json
import interConflicts2
import sys
import find_unresolvable

WeirdPackages = []
dependency_chain = {}
counter = 0
with open('updatedDependency.txt') as j_dependency:
  jdepend=json.load(j_dependency)
  
with open('pwc.txt') as polo:
  pwc=json.load(polo)



counter = 0
num = 0
for x in pwc:
  if x == "fabgis-0.3.0":
    num = num + 1
    print "num: " + str(num)
    print x
    dependency_list = []
    
    listy = []
    solutions = (interConflicts2.get_req(listy,x,dependency_list))
    print listy
 
  



json.dump(WeirdPackages, open("failed_packages",'w'))
