import os

def get_requirements(topdir): 
  req_string = ''
  for dirpath,dirnames, files in os.walk(topdir):
      for name in files:
	
	try:
		if name == 'requirements.txt':
		 reqments_file = file(os.path.join(dirpath,name))
                 #Checks for cases where there are multiple requirements.txt file and it redirects to another folder
		 # Since reqfile.read() already read the file any more reading would generate '' because it's already eof
                 if not 'requirements.txt' in reqfile.read().replace(' ',""):
	           # Re-opens the file so we can read it
                   reqments_file.close()
		   reqfile = file(os.path.join(dirpath,name))
	         for aline in reqfile:
		   if '#' in aline:
	             # Splice string to not read anything after #.
		     aline = aline[0:aline.find('#')]
		     # Checks for cases for requirements of [test] or [dev]. 
		   if '[' in aline:
		      break
		   strings = strings + aline
					
	except Exception:
	  continue

  return req_string 			
