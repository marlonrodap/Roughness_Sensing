import os
from scipy.io import wavfile

in_paths = ["./../opus/stereo/","./../raw/stereo/"]
out_paths = [["./../opus/piezo/","./../opus/air/"],["./../raw/piezo/","./../raw/air/"]]

for sublist in out_paths:
	for folder in sublist:
		try:
			os.mkdir(folder,mode = 0o777)
		except FileExistsError:
			pass

for p in range(len(in_paths)):
	files = os.listdir(in_paths[p])
	files.sort()
	for file in files:

		print("Splitting '"+in_paths[p]+file+"'...",end='')

		rate, data = wavfile.read(in_paths[p]+file)
		assert data.shape[1] == len(out_paths[p]) , "Number of channels of '"+file+"' ("+str(data.shape[1])+") doesn't match the specified number of out_paths ("+str(len(out_paths[p]))+")"
		for c in range(data.shape[1]):
			wavfile.write(out_paths[p][c]+file,rate,data[:,c])

		print("done!")