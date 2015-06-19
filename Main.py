import os
import json
import getReq
import getSetup
import checkRequirements


topdir= '/srv/pypi/web/packages/source'
req_string = ''
problematicPackages = []
reqs = {}
prereqs = {}
counter = 0


for dirpath,dirnames, files in os.walk(topdir):
  for name in files:
    # Stop from looking within package for other setup.py
    if(os.path.join(dirpath,name).count("/") < 10):	
	    if name == 'setup.py':
	      counter = counter + 1
	      packageName = dirpath[dirpath.rfind('/')+1:len(dirpath)]
	      # Should return none if there is no requires.txt.
	      req_string = getReq.get_from_require(os.path.join(dirpath,''))
	      if req_string:
		req_list = req_string.split()
	     
	      else: 
		try:
		  dataFile = file(os.path.join(dirpath,name))
		except Exception:
		  problematicPackages.append(packageName)
		  continue
		req_string = getSetup.get_from_setup(dataFile,packageName)
	
		if req_string:
		  if '(' in req_string:		
		  # Make sure it's not numpy(<=1.2) before going to check requirements.txt
		    if not (req_string[req_string.find('(')+1]=='<' or \
		    req_string[req_string.find('(')+1]=='>' or \
		    req_string[req_string.find('(')+1]=='='):
		      req_string = checkRequirements.get_requirements(os.path.join(dirpath,''))

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
										


