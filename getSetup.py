import os
import string_modify

''' This function reads from the setup.py file and checks if it contains
a dependency list with keys requires or install_requires. If it does have
these keywords, it will instruct the main to check requirements.txt, this
function calls on string_modify.py to modify the string so that it would
be same as from requires.txt'''

def get_from_setup(openedFile):
  req_strings = ""
  string_of_file = openedFile.read().replace(' ',"")

  if 'install_requires=[' in string_of_file:
    req = 'install_requires=['
  elif 'install_requires={' in string_of_file:
    req = 'install_requires={'
  elif 'requires=[' in string_of_file:
    req = 'requires=['
  elif 'requires={' in string_of_file:
    req = 'requires={'
  else:
    req_strings = "(check requirements.txt)"
    # Returns (check requirements.txt) so it would check requirements.txt 
    return req_strings


  numBracket = 0
  # Restart at the beginning of the file
  openedFile.seek(0)
  for line in openedFile:

    if '#' in line:      
      line = line[0:line.find('#')]

    no_space_line = line.replace(' ',"") 

    if req == 'requires=[' or req == 'install_requires=[':

      if req in no_space_line:
        req_strings = req_strings + no_space_line
        req_strings= req_strings[req_strings.find('[')+1:len(req_strings)+1]
        numBracket = req_strings.count('[') - req_strings.count(']') + 1

      elif ']' in req_strings and numBracket==0:
        break

      elif req_strings!= "":
        req_strings = req_strings + no_space_line
        numBracket = req_strings.count('[') - req_strings.count(']')

    elif req == 'requires={' or req =='install_requires={':

      if req in no_space_line:
        req_strings = req_strings + no_space_line
        req_strings= req_strings[req_strings.find('{')+1:len(req_strings)+1]
        numBracket = req_strings.count('{') - req_strings.count('}') + 1

      elif '}' in req_strings and numBracket==0:
        break

      elif req_strings!= "":
        req_strings = req_strings + no_space_line
        numBracket = req_strings.count('{') - req_strings.count('}')

  # Takes out the extra quotes or comma from the string
  req_strings = string_modify.setup_string_modifications(req_strings)

  return req_strings




