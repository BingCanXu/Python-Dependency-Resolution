import os

'''This function reads from the requires.txt file.
It eliminates all the spaces to have the same
result as setup.py. It does not read any comments
or any requirements from [dev] or [test].
It returns a string of requirements and returns
empty string if it does not exist'''


def get_from_require(topdir):
  req_string = ''
  for dirpath,dirnames, files in os.walk(topdir):
    for name in files:
      try:
        if name == 'requires.txt':
          req_file = file(os.path.join(dirpath,name))
          for line in req_file:
            # Replaces ' ' with '' for consistency with data from setup.py     
            line = line.replace(' ', '')
            if '#' in line:
              # Splice string to not read anything after #.
              line = line[0:line.find('#')]
            # Checks for cases for requirements of [test] or [dev]. 
            if '[' in line:
              break
            req_string = req_string + line 
      except Exception:
        continue  
  
return req_string





