nom = "Banane"
prix = 10
stock = 10

#We display product information
print ("Produit:",nom,"\nPrix:",prix,"€","\nStock",stock)

#Add stock
stock = stock + 10

#enter quantity produit want to buy
demande = int(input("Saisir la quantité de produits que vous souhaitez acheter "))
#Cannot buy more product than stock
if demande > stock:
    print("Il n'y a pas assez de produit demandé en stock:",stock)
    demande = int(input("Resaisir la quantité de produits acheter "))

#update stock
stock -= demande
print ("Stock:",stock)

#inflation
prix = prix*1.10
print ("Le prix d’un produit a subi l’inflation et a augmenté de 10%.\nSon prix est maintenant de:",prix,"€")