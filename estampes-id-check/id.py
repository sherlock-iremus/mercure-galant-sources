from pprint import pprint

with open('id-bd.txt', 'r') as file:
    inbd = file.readlines()
    inbd = [l.replace('\n', '') for l in inbd]

with open('id-fi.txt', 'r') as file:
    infi = file.readlines()
    infi = [l.replace('\n', '') for l in infi]

only_in_bd = []
only_in_filenames = []

for x in inbd:
    if x not in infi:
        only_in_bd.append(x)

with open('only_in_bd.txt', 'w') as file:
    file.write(('\n').join(only_in_bd))

for x in infi:
    if x not in inbd:
        only_in_filenames.append(x)

with open('only_in_filenames.txt', 'w') as file:
    file.write(('\n').join(only_in_filenames))
