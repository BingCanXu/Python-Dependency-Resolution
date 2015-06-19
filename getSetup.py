import os
import string_modify


def get_from_setup(openedFile,packageName):
  req_strings = ""

  #checks to see if install_requires exist
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
    return req_strings
  print req
  numBracket = 0
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




  req_strings = string_modify.setup_string_modifications(req_strings)
  
  return req_strings
							

			
					
