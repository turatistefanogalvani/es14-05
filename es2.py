import random

def gestisci_lavaggi():
    clienti = []
    while True:
        codice_cliente = int(input("Inserisci il codice del cliente (999999 per terminare): "))
        print("MENU PRINCIPALE: (1 per gestire i lavaggi) (2 per visualizzare clienti >5kg) (3 per convertire in dollari) (4 per modificare dati) (5 per analizzare giorni) (6 per premio sconto) (7 per uscire)")

        
        if codice_cliente == 999999:
            break
        
        kg_lavati = float(input("Inserisci i kg lavati: "))
        euro_pagati = float(input("Inserisci gli euro pagati: "))
        
        cliente = {
            'codice': codice_cliente,
            'kg': kg_lavati,
            'euro': euro_pagati
        }
        
        clienti.append(cliente)
    
    totale_kg = 0
    totale_pagato = 0
    
    for cliente in clienti:
        totale_kg += cliente['kg']
        totale_pagato += cliente['euro']
    
    media_kg = totale_kg / len(clienti) if len(clienti) > 0 else 0
    
    cliente_max_pagato = None
    max_pagato = 0
    
    for cliente in clienti:
        if cliente['euro'] > max_pagato:
            max_pagato = cliente['euro']
            cliente_max_pagato = cliente
    
    print(f"Totale kg lavati: {totale_kg}")
    print(f"Media kg lavati per cliente: {media_kg:.2f}")
    print(f"Totale pagato: {totale_pagato}")
    if cliente_max_pagato:
        print(f"Cliente che ha pagato di più: {cliente_max_pagato['codice']} con {cliente_max_pagato['euro']} euro")
    
    return clienti

def clienti_piu_5kg(clienti):
    risultato = []
    for cliente in clienti:
        if cliente['kg'] > 5:
            risultato.append(cliente['codice'])
    return risultato

def euro_a_dollari(euro):
    return euro / 0.89

def converti_in_dollari(clienti):
    for cliente in clienti:
        cliente['euro'] = euro_a_dollari(cliente['euro'])
    print("Tutti i pagamenti sono stati convertiti in dollari.")

def modifica(clienti, codice_cliente, nuovi_kg, nuovi_euro):
    cliente_trovato = False
    for cliente in clienti:
        if cliente['codice'] == codice_cliente:
            cliente['kg'] = nuovi_kg
            cliente['euro'] = nuovi_euro
            cliente_trovato = True
            break
    
    if cliente_trovato:
        print(f"Dati del cliente {codice_cliente} aggiornati.")
    else:
        print(f"Cliente con codice {codice_cliente} non trovato.")

def giorni_lavaggio(clienti_giorni):
    giorni_comuni = []
    for giorno in clienti_giorni[0]:
        presente_in_tutti = True
        for cliente_giorni in clienti_giorni[1:]:
            if giorno not in cliente_giorni:
                presente_in_tutti = False
                break
        if presente_in_tutti:
            giorni_comuni.append(giorno)
    
    tutti_giorni = list(range(1, 31))
    
    giorni_assenti = []
    for giorno in tutti_giorni:
        assente = True
        for cliente_giorni in clienti_giorni:
            if giorno in cliente_giorni:
                assente = False
                break
        if assente:
            giorni_assenti.append(giorno)
    
    giorni_almeno_uno = []
    for giorno in tutti_giorni:
        for cliente_giorni in clienti_giorni:
            if giorno in cliente_giorni and giorno not in giorni_almeno_uno:
                giorni_almeno_uno.append(giorno)
    
    giorni_comuni.sort()
    giorni_assenti.sort()
    giorni_almeno_uno.sort()
    
    print(f"Giorni in cui si sono presentati tutti e tre i clienti: {giorni_comuni}")
    print(f"Giorni in cui non si è presentato nessuno: {giorni_assenti}")
    print(f"Giorni in cui si è presentato almeno uno dei tre clienti: {giorni_almeno_uno}")

def controllo_premio():
    lista_premi = [random.randint(100000, 999999) for _ in range(100)]
    codice_cliente = int(input("Inserisci il tuo codice cliente (6 cifre): "))
    
    if codice_cliente in lista_premi:
        print("Hai vinto!")
    else:
        print("Non hai vinto!")

clienti = []
while True:
        scelta = input("Inserisci il numero dell'opzione: ")
        
        if scelta == '1':
            clienti = gestisci_lavaggi()
        elif scelta == '2':
            if not clienti:
                print("Non ci sono clienti da analizzare. Aggiungi prima dei clienti.")
            else:
                codici = clienti_piu_5kg(clienti)
                print("Clienti che hanno lavato più di 5 kg:", codici)
        elif scelta == '3':
            if not clienti:
                print("Non ci sono clienti da analizzare. Aggiungi prima dei clienti.")
            else:
                converti_in_dollari(clienti)
        elif scelta == '4':
            if not clienti:
                print("Non ci sono clienti da modificare. Aggiungi prima dei clienti.")
            else:
                codice_cliente = int(input("Inserisci il codice cliente da modificare: "))
                nuovi_kg = float(input("Inserisci i nuovi kg lavati: "))
                nuovi_euro = float(input("Inserisci i nuovi euro pagati: "))
                modifica(clienti, codice_cliente, nuovi_kg, nuovi_euro)
        elif scelta == '5':
            clienti_giorni = [
                [1, 5, 7, 10],
                [3, 5, 7, 9],
                [2, 5, 6, 9] 
            ]
            giorni_lavaggio(clienti_giorni)
        elif scelta == '6':
            controllo_premio()
        elif scelta == '7':
            print("Grazie per aver utilizzato il programma!")
            break
        else:
            print("Opzione non valida. Riprova.")