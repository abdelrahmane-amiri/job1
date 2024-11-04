#Input for Montant and taux
montantIn = float(input("Saisir le montant initial de l'investissement: "))
taux = float(input("Saisir le taux de rendement annuel: "))

#calculate profit and print
print ("Le gaint annuel est de: ",montantIn*taux)

#New profit
montantIn += 5000
taux += 0.02
print ("Le nouveau gaint annuel est de: ",montantIn*taux)

#Final montant and profits
montantIn *= 0.9
taux -= 0.01
print("Le montant final de l'investissement est: ",montantIn)
print("Le gain final est: ",montantIn*taux)