import os 

path = "./../raw/stereo/"
files = os.listdir(path)
files.sort()

counter = 0
for file in files:
	if file.find(".wav") > 0:
		if counter > 0:
			print(', ',end="")
			if counter % 7 == 0:
				print()
		print('"'+file+'"',end="")
		counter += 1
print()
		