codice_corretto = 123456
tentativi = 0
peso_totale = 0

while True:
    x = int(input("Inserisci il codice: "))
    
    if len(str(x)) != 6:
        print("Inserire un numero con 6 cifre")
    elif x == codice_corretto:
        peso_totale = 0
        unita_misura = input("Scegli l'unità di misura (kg/lb): ").lower()
        
        while peso_totale <= 9:
            y = int(input(f"Inserisci un peso in {'libbre' if unita_misura == 'lb' else 'grammi'} (0 per uscire) e (per pagare scrivere 1): "))
            
            if y == 0:
                print(f"Peso totale dei capi di abbigliamento: {peso_totale} kg")
                print("Termina il programma")
                break
                
            elif y == 1:
                temp = int(input("Inserisci una gradazione tra 40, 60 o 90: "))
                
                if peso_totale < 5 and temp == 40:
                    costo = peso_totale * 0.50
                    print(f"Il costo totale è {costo} euro")
                elif peso_totale < 5 and temp == 60:
                    costo = peso_totale * 0.75
                    print(f"Il costo totale è {costo} euro")
                elif peso_totale < 5 and temp == 90:
                    costo = peso_totale * 1
                    print(f"Il costo totale è {costo} euro")
                elif peso_totale >= 5 and temp == 40:
                    costo = peso_totale * 0.75
                    print(f"Il costo totale è {costo} euro")
                elif peso_totale >= 5 and temp == 60:
                    costo = peso_totale * 1
                    print(f"Il costo totale è {costo} euro")
                elif peso_totale >= 5 and temp == 90:
                    costo = peso_totale * 1.50
                    print(f"Il costo totale è {costo} euro")
                
                banconota = int(input("Inserisci una banconota tra 5, 10, 20 o 50: "))
                resto = banconota - costo
                print(f"Il resto è di {resto} euro")
                break
            else:
                if unita_misura == 'lb':
                    peso = y * 0.45359237
                    if y > 20 or (peso_totale + peso) > 9:
                        print("Il peso è troppo grande")
                        print(f"Peso totale dei capi di abbigliamento: {peso_totale} kg")
                        break
                else:
                    peso = y / 1000
                    if y > 9000 or (peso_totale + peso) > 9:
                        print("Il peso è troppo grande")
                        print(f"Peso totale dei capi di abbigliamento: {peso_totale} kg")
                        break
                peso_totale += peso
                print(f"Peso accettato: {peso} kg")
                print(f"Peso totale dei capi di abbigliamento: {peso_totale} kg")
    else:
        tentativi += 1
        print("Il codice è sbagliato")
        if tentativi == 3:
            print("Hai esaurito i tentativi.")
            break