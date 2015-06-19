import json
counter = 0
betterResult = 0
nobetterResult = 0
data = 0
txt = 0
weird = 0
stxt = 0
sdata = 0
with open("reqsetup.txt") as json_file:
    json_data = json.load(json_file)
    
with open('reqjson.txt') as j_file:
	jfile = json.load(j_file)

with open("reqtxt.txt") as json_txt_file:
	json_txt = json.load(json_txt_file)



for s in json_data:
	json_data[s].sort()
	json_txt[s].sort()
	jfile[s].sort()
	#if jfile[s] == json_txt[s]:
	#	stxt = stxt + 1
	#if jfile[s] == json_data[s]:
	#	sdata = sdata + 1
	if json_data[s] == [] and jfile[s] != []:
		betterResult = betterResult + 1
	elif json_data[s] != [] and jfile[s] == []:
		nobetterResult = nobetterResult + 1
	
	elif len(json_data[s]) > len(jfile[s]):
		data = data + 1
	elif len(jfile[s]) > len(json_data[s]):
		txt = txt + 1
		
	elif len(jfile[s]) == len(json_data[s]) and json_data[s]!= jfile[s]:
		weird = weird + 1
		print str(weird) + s
	#if json_data[s]== json_txt[s]:
		
	#	counter = counter +1
	
print len(jfile)
print len(json_data)
print len(json_data) == len(json_txt)
print 'counter = ' + str(counter)
print 'betterResult = ' + str(betterResult)
print 'nobetterResult = ' + str(nobetterResult)
print 'data = ' + str(data)
print 'txt = ' + str(txt)
print 'weird = ' + str(weird)

print stxt
print sdata
