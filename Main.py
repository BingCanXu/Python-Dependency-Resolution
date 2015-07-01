import os
import json
import getReq
import getSetup
import checkRequirements
import pkg_resources


'''This script will walk through the directory '/srv/pypi/web/packages/source' 
and find the dependencies from either the requires.txt, setup.py, or 
requirements.txt file. It will store the data into reqs, which is a dictionary
that has its key as the package name and the value a list of the dependencies.
prereqs has its key as the dependency and the value a list of packages that 
need this dependency. Then, using these two dictionary, it will store the information
into two json files. There is also a list called problematicPackages, which
will add the packages that have trouble opening the setup.py file.
The list weirdCases is to troubleshoot as potential errors in reading
the setup.py file'''

topdir= '/srv/pypi/web/packages/source/Z'
req_string = ''
problematicPackages = []
reqs = {}
prereqs = {}
counter = 0
weirdCases = []


for dirpath,dirnames, files in os.walk(topdir):
  for name in files:
    # Stop from looking within package for other setup.py
    if(os.path.join(dirpath,name).count("/") == 9):
      if name == 'setup.py':
        # The name of the package
        dirpathCpy = dirpath.lower()
        packageName = dirpathCpy[dirpathCpy.rfind('/')+1:len(dirpathCpy)]
        splicedstring = dirpathCpy[:dirpathCpy.rfind('/')]
        #The name of the directory that contain the package 
        packageDir = splicedstring[splicedstring.rfind('/')+1:len(splicedstring)]
        packageNamesub = dirpathCpy[dirpathCpy.rfind('/')+1:len(dirpathCpy)]
        # Normalize the name by replacing non-alphanumerics with '-'
        packageDir = pkg_resources.safe_name(packageDir)
        packageNamesub = pkg_resources.safe_name(packageNamesub)
        # Checks for potential errors because standard naming: Numpy/Numpy-1.2 
        # where Numpy = package directory and Numpy-1.2 is packageName
        if packageDir not in packageNamesub:
          weirdCases.append(os.path.join(dirpath,name))
          break
        counter = counter + 1
        # Should return '' if there is no requires.txt.
        req_string = getReq.get_from_require(os.path.join(dirpath,''))
        req_string = req_string.lower()
        if req_string:
          req_list = req_string.split()

        else: 
          try:
            dataFile = open(os.path.join(dirpath,name))
          except Exception:
            problematicPackages.append(packageName)
            continue
          # Should return the dependencies or (check requirements.txt) if can't find requires
          req_string = getSetup.get_from_setup(dataFile)
          req_string = req_string.lower()
          if req_string:
            # Check to see if it's a method or (check requirements.txt)
            if '(' in req_string:		
              # Make sure it's not numpy(<=1.2) before going to check requirements.txt
              if not (req_string[req_string.find('(')+1]=='<' or \
              req_string[req_string.find('(')+1]=='>' or \
              req_string[req_string.find('(')+1]=='='):
                req_string = checkRequirements.get_requirements(os.path.join(dirpath,''))
              req_string = req_string.lower()
              if req_string: 
                req_list = req_string.split()
              else:
                req_list = []
            else:
              req_list = req_string.split() 
          else:
            req_list = [] 
        # Package name is key and list of dependency is value
        dict_value = []
        if packageName in reqs:
          weirdCases.append(packageName)
        for u in req_list:
          dict_value.append(u)
        reqs[packageName] = dict_value

        # Dictionary with key as required package
        for u in req_list:
          # Check if key already exists else creates one
          if u in prereqs:
            if packageName not in prereqs[u]:
              prereqs[u].append(packageName)
          else:
            prereqs[u] = []
            prereqs[u].append(packageName)
        print counter
        print packageName
        print req_list


print counter

with open("weirdcases.txt",'w') as weird:
  for packName in weirdCases:
    weird.write(packName + '\n')

with open("probGetPak.txt",'w') as probPak:
  for packName in problematicPackages:
    probPak.write(packName + '\n')	

with open("reqs.txt",'w') as reqPak:
  for packList in reqs:
    reqPak.write(packList + ": ")
    for packName in reqs[packList]:
      reqPak.write(' - ' + packName)
    reqPak.write('\n')	
    reqPak.write('\n')	

with open("prereqs.txt",'w') as prePak:
  for packList in prereqs:
    prePak.write(packList + ": ")
    for packName in prereqs[packList]:
      prePak.write(' - ' + packName)
    prePak.write('\n')	
    prePak.write('\n')	

json.dump(reqs, open("reqjson.txt",'w'))
json.dump(prereqs, open("prereqjson.txt",'w'))								



