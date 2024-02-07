# Author: ggns7
# For everbody, I hope it'll save you some time
# This version, for ignore unresolved chars

import os

if __name__ == "__main__":
	files = {
		0		: 'item_names.txt',
		1		: 'item_proto.txt',
		2		: 'mob_names.txt',
		3		: 'mob_proto.txt'
	}

	for key, value in files.items():
		print(key, ": {}".format(value))

	getInput = int(input('Choose file by index: '))
	selectedFile = getInput

	try:
		with open(files[selectedFile], 'rb') as file:
			readFile = []
			for line in file.readlines():
				text = line.decode('euc_kr', errors='ignore')
				readFile.append(text)
			fileContent = {}

			def sort_data(fileIndex=None):
				vnums = [line.split()[0].replace('\n', '') for line in readFile]
				if fileIndex == 0 or fileIndex == 2:
					values = [" ".join(line.split('\t')[1:]).replace('\n', '') for line in readFile]
				elif fileIndex == 3:
					values = ["\t".join(line.split('\t')[1:]).replace('\n', '') for line in readFile]
				elif fileIndex == 1:
					values = ["\t".join(line.split('\t')[1:]).replace('\n', '') for line in readFile]
				tempVnumColumns = vnums[0] + '\t' + values[0] + '\n'

				del vnums[0]  # delete column name
				del values[0]  # delete column name

				for i in range(len(readFile)-1): # because we deleted column lines
					fileContent[vnums[i]] = values[i]

				with open('new_item_proto.txt', 'wb') as outputFile:
					for i in readFile:
						outputFile.write(i.encode('euc_kr'))

				specials = []
				toIntVnums = []
				result = []
				if fileIndex == 1:
					for i in vnums:
						try:
							toIntVnums.append(int(i))
						except ValueError:
							specials.append(i)
							toIntVnums.append(int(i.split('~')[0]))
				else:
					toIntVnums = [int(vnum) for vnum in vnums]


				sortedItemVnums = sorted(toIntVnums)
				s = [i.split('~')[0] for i in specials]
				for index in range(len(sortedItemVnums)):
					if str(sortedItemVnums[index]) in s:
						sortedItemVnums[index] = specials[s.index(str(sortedItemVnums[index]))]
						text = str(sortedItemVnums[index]) + '\t' + fileContent[sortedItemVnums[index]] + '\n'
						result.append(text)
					else:
						text = str(sortedItemVnums[index]) + '\t' + fileContent[str(sortedItemVnums[index])] + '\n'
						if text not in result:
							print(text)
							result.append(text)

				# Write sorted data to new file
				with open('new_' + files[selectedFile], 'wb') as outputFile:
					for i in range(len(result)):
						if i == 0:
							outputFile.write(tempVnumColumns.encode('euc_kr'))
							outputFile.write(result[i].encode('euc_kr'))
						else:
							outputFile.write(result[i].encode('euc_kr'))

					input("Succesfully completed.")


			if getInput == 0 or getInput == 2:
				sort_data(fileIndex=getInput)
			elif getInput == 1:
				sort_data(fileIndex=1)
			elif getInput == 3:
				sort_data(fileIndex=3)

	except FileNotFoundError:
		print(files[selectedFile], "is not founded in current directory", '\ncurrent directory: ', os.getcwd())
		input()