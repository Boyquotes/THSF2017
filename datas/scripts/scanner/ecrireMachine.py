import pickle

# creation d'un dictionnaire
ordis = {
'1':'A0:1B:29:B8:65:98',
'2':'54:64:D9:E7:A6:52'
}

# enregistrement du dictionnaire dans un fichier
Fichier = open('parcMachines.p','wb')
pickle.dump(ordis,Fichier)    # serialisation
Fichier.close()
