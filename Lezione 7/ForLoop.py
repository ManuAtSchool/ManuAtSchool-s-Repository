#liste
#0 based, la conta parte da 0
miaLista= ["mela","pera","banana","fichi"]
for frutto in miaLista:
    print(frutto)
    #Fornisco la mia lista dei mie voti, tute le volte che incontro un voto insufficente stampo un avviso
    voti = [100, 50, 25, 85, 20]
    for voto in voti:
         if voto <= 50: 
            print("voto:", voto, "attenzione sei sotto soglia di sufficenza")
else: 
    print("voto:", voto)