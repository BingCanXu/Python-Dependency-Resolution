def setup_string_modifications(oneString): 
  aStrings = oneString
  # Some packages has requirements like [Django,] or {Django,}
  if ',]' in aStrings:
    aStrings = aStrings.replace(',]', ']')
	
  if ']' in aStrings:
    aStrings= aStrings[0:aStrings.find(']')]

  if ',}' in aStrings:
    aStrings = aStrings.replace(',}', '}')
	
  if '}' in aStrings:
    aStrings= aStrings[0:aStrings.find('}')]
  
  
  # Checks for cases where the string only contains \r or \n and replaces ,\n with a space
  aStrings = aStrings.replace(',\n',' ')
  aStrings = aStrings.replace(',\r\n',' ')
  if(len(aStrings) < 3):
    aStrings = aStrings.replace('\n',"")

  aStrings = aStrings.replace('\r',"")
 
  # Replaces the extra quotes and comma from install_requires or requires
  newString = aStrings.replace("','", ' ')
  newStringw = newString.replace('","', ' ')
  newStringr = newStringw.replace("\',\"", ' ')
  newStringt = newStringr.replace("\",\'", ' ')
  newStringv = newStringt.replace('"','')
  finString = newStringv.replace("'","")
  
  return finString			


						
					
