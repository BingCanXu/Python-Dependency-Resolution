import os
import zipfile

topdir= '/srv/pypi/web/packages/source'
exten = '.zip'

problematicPackages = []

for dirpath,dirnames, files in os.walk(topdir):
	for name in files:
		if(os.path.join(dirpath,name).count("/") < 9):
			if name.lower().endswith(exten):
				print(os.path.join(dirpath,name))
			 	os.chdir(os.path.join(dirpath,""))
				try:
					zf = zipfile.ZipFile(name)
					zf.extractall()
					zf.close()
				except Exception:
					print dirpath
					problematicPackages.append(name)
					continue
			

print problematicPackages

with open("probZip.txt",'w') as f:
	for s in problematicPackages:
		f.write(s + '\n')

