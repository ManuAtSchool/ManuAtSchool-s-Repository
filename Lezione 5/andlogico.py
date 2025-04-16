# Chiedi all'utente il nome, la sua eta' e se possiede l'invito

nome = input("Come ti chiami? ")
eta = int(input("Quanti anni hai? "))
invito = input("Hai un invito? (si/no) ") == "si"

if eta >= 18 and invito:
    print("Ciao", nome, "puoi far parte della festa.")
elif eta < 18 and invito:
    print("Signor", nome, "non hai ancora compiuto 18 anni. Anche avendo l'invito, non puoi entrare alla festa.")
elif eta >= 18 and not invito:
    print("Signor", nome, ", anche essendo maggiorenne non puoi entrare visto che ti manca l'invito.")
else:
    print("Mi spiace", nome, ", non puoi entrare alla festa. Non hai 18 anni e non hai neanche un invito.") 