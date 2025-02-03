class Produit : 
    def __init__(self, name, prixHT, TVA):
        self.name = name
        self.prixHT = prixHT
        self.TVA = TVA

    def CalculerPrixTTC(self) :  #her I have to return one chain, in order to call it with the instance
        return self.prixHT + self.TVA   #It is better to return the price before prixHT+TVA without changing prixHT, else, we change permanantly

    def afficher(self) :
        return f"Le nom du produit est : {self.name}\nLa taxe à payer est : {self.TVA}\nLe prix hors taxes est : {self.prixHT}"


    def modifier(self, new_nom, new_prix) :
        self.name = new_nom
        self.prixHT = new_prix

    def nom_produit(self) :
        return self.name 
    
    def prix_produit(self) :
        return self.prixHT
    
    def TVA_produit(self) :
        return self.TVA

print(f"\nLes information sur le produit 1")
produit1 = Produit('ordinateur', 700, 20)
print(produit1.afficher())
produit1.modifier('ordinateur_Hp',750)
print(f"n\Après modification : ")
print(produit1.afficher())
print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
print(f"\nLes information sur le produit 2")
produit2 = Produit('Téléplone', 200, 8)
print(produit2.afficher())
produit1.modifier('Samsung',300)
print(f"\nAprès modification : ")
print(produit2.afficher())
