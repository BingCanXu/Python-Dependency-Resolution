import os
import tarfile

topdir= '/srv/pypi/web/packages/source/g/gaeframework'

exten = '.tar.gz'

problematicPackages = []

for dirpath,dirnames, files in os.walk(topdir):
	for name in files:
		if(os.path.join(dirpath,name).count("/") < 9):
			if name.lower().endswith(exten):
				print(os.path.join(dirpath,name))
			 	os.chdir(os.path.join(dirpath,""))
				try:
					tar = tarfile.open(name)
					tar.extractall()
					tar.close()
				except Exception:
					print dirpath
					problematicPackages.append(name)
					continue
				
print problematicPackages

with open("probGZip.txt",'w') as f:
	for s in problematicPackages:
		f.write(s + '\n')
		
