import os

'''
This function goes through the top directory and checks for any requirements.txt file.
Once it finds one, it checks if the file is redirecting to another file. If it does
redirect, the content will be ignored and the function moves on to next
requirements.txt file. Once it finds the correct file, it will add the content 
of requirements.txt before [dev] or [test] and return it. This function
will return an empty string if requirements.txt is not found'''



def get_requirements(topdir): 
  req_string = ''
  for dirpath,dirnames, files in os.walk(topdir):
    for name in files:
      if(os.path.join(dirpath,name).count("/") == 9):
        try:
          if name == 'requirements.txt':
            reqments_file = open(os.path.join(dirpath,name))
          # Checks for cases where there are multiple requirements.txt file and it redirects to another folder
          # Since reqments_file.read() already read the file any more reading would generate '' because it's already eof
          if not 'requirements.txt' in reqments_file.read().replace(' ',""):
            # Re-opens the file so we can read it
            reqments_file.close()
            reqments_file = open(os.path.join(dirpath,name))
          for aline in reqments_file:
            if '#' in aline:
              # Splice string to not read anything after #.
              aline = aline[0:aline.find('#')]
            # Checks for cases for requirements of [test] or [dev]. 
            if '[' in aline:
              break
            req_string = req_string + aline
        except Exception:
          continue

  return req_string 			
