def inversemot(mot):
	resultat =''
	u=len(mot)
	for k in range(0,u):
		resultat = resultat + mot[u-k-1]
	return resultat

phrase ='Bonjour ami : viens me voir à la maison'

zorgphrase=''

L=phrase.lower().split(' ')
print L

for k in range(len(L)):
	L[k]=inversemot(L[k])
	zorgphrase= zorgphrase+L[k]+' '


zorgphrase=zorgphrase[0:len(zorgphrase)-1]
print L ; print zorgphrase