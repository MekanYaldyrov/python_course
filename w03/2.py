def write_array(arr, file):
	arr = map(lambda x : x+'\n',arr)
	file.writelines(arr)

arr = ["never", "gonna", "give", "you up"]

with open("2.txt", "w") as F:
	write_array(arr, F)

with open("2.txt", "r") as F:
	for line in F:
		print(line)
