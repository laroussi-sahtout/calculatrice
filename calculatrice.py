def calculatrice(chiffre, operator, chiffre2, historique):
    try:
        chiffre = float(chiffre)
        chiffre2 = float(chiffre2)

        if operator == "/":
            resultat = chiffre / chiffre2 if chiffre2 != 0 else "La division par 0 est impossible"
        elif operator == "x":
            resultat = chiffre * chiffre2
        elif operator == "+":
            resultat = chiffre + chiffre2
        elif operator == "-":
            resultat = chiffre - chiffre2
        else:
            raise ValueError("Opérateur non valide")

        calcul = f"{chiffre} {operator} {chiffre2} = {resultat}"
        historique.append(calcul)
        return resultat

    except ValueError as e:
        return f"Erreur : {e}"

historique = []

chiffre = input("Entrer un chiffre : ")
chiffre2 = input("Entrer un second chiffre : ")
operator = input("Entrer votre opération : ")

resultat = calculatrice(chiffre, operator, chiffre2, historique)

print(resultat)

print("\nHistorique des calculs :")
for calcul in historique:
    print(calcul)
