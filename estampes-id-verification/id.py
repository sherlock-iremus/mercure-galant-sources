from pprint import pprint

with open('id_dans_feuille.txt', 'r') as file:
    inbd = file.readlines()
    inbd = [l.replace('\n', '') for l in inbd]

with open('id_dans_noms_de_fichiers.txt', 'r') as file:
    infi = file.readlines()
    infi = [l.replace('\n', '') for l in infi]

with open('id_articles_transcrits.txt', 'r') as file:
    id_articles_transcrits = file.readlines()
    id_articles_transcrits = [l.replace('\n', '') for l in id_articles_transcrits]

only_in_bd = []
only_in_filenames = []

for x in inbd:
    if x not in infi:
        only_in_bd.append(x)

with open('id_seulement_dans_feuille.txt', 'w') as file:
    file.write(('\n').join(only_in_bd))

for x in infi:
    if x not in inbd:
        only_in_filenames.append(x)

with open('id_seulement_dans_noms_de_fichiers.txt', 'w') as file:
    file.write(('\n').join(only_in_filenames))
