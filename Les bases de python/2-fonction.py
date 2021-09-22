def fonction1() :
    # Récolter une premiere note
    note1 = int(input("Entrer la premier note"))
    # Récolter la deuxieme note
    note2 = int(input("Entrer la seconde note"))
    # Récolter la troisieme note
    note3 = int(input("Entrer la derniere note"))
    # Calculer la moyenne
    result = note1 + note2 + note3 / 3
    # Afficher le résultat
    print ("La moyenne de l'élève est de " + str(result))