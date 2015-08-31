from depsolver import PackageInfo, Pool, Repository, Request, Requirement, Solver
import sat-solver
listy = []

#This assumes that a git clone of ethoughts/depsolver is copied and this is placed within that folder
#test the sat-solver

stuff = sat-solver.get_data()
counter = 0
for x in stuff:
  if x!= "BingResearch":
    s1 = "x" + str(counter)
    counter = counter + 1
    vars()[s1] = PackageInfo.from_string('"' + x + '; depends (' + stuff[x] + ')"')
    listy.append(s1)
    
for x in stuff["BingResearch"]:
  s1 = "x" + str(counter) 
  vars()[s1] = PackageInfo.from_string('"' + x + '"')
  listy.append(s1)

print listy

repo = Repository([a_1_0_0, b_1_0_0, c_1_0_0, d_1_1_0, d_0_9_0])
installed_repo = Repository()
pool = Pool([repo, installed_repo])

# despolver resolves each dependency 'globally', and does not install
# D-1.1.0 as pip currently does
request = Request(pool)
request.install(Requirement.from_string("A"))
for operation in Solver(pool, installed_repo).solve(request):
    print operation
