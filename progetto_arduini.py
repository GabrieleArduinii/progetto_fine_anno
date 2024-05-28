import random
import time  

def crea_mazzo():
    semi = ["Denari", "Coppe", "Bastoni", "Spade"]
    valori = ["Asso", "2", "3", "4", "5", "6", "7", "Fante", "Cavallo", "Re"]
    mazzo =  for seme in semi for valore in valori
    random.shuffle(mazzo)  
    return mazzo

def distribuisci_carte(mazzo):
    return mazzo[:26], mazzo[26:]  

def stampa_stato_gioco(giocatore1, giocatore2):
    print("\n--- Stato del gioco ---")
    print("Giocatore 1:", len(giocatore1), "carte")
    print("Giocatore 2:", len(giocatore2), "carte")

def gioca_turno(mano_giocatore, mazzo_giocatore, mazzo_avversario):

    carta_giocata = mano_giocatore.pop(0)  
    mazzo_giocatore.append(carta_giocata)  

    if mazzo_avversario and mazzo_avversario[-1][0] == carta_giocata[0]:  
        mazzo_giocatore += mazzo_avversario  
        mazzo_avversario = []
        print("Rubamazzo")
     

def rubamazzo(giocatore1, giocatore2):
   
    turno = 1  
    while giocatore1 and giocatore2:
        print(f"\n--- Turno {turno} ---")
        stampa_stato_gioco(giocatore1, giocatore2) 

        input("Premi Invio per giocare il turno del Giocatore 1")
        gioca_turno(giocatore1, giocatore1, giocatore2)

        input("Premi Invio per giocare il turno del Giocatore 2")
        gioca_turno(giocatore2, giocatore2, giocatore1)

        turno += 1

def determina_vincitore(giocatore1, giocatore2):

    if len(giocatore1) > len(giocatore2):
        return "Giocatore 1"
    elif len(giocatore1) < len(giocatore2):
        return "Giocatore 2"
    else:
        return "Pareggio"

mazzo = crea_mazzo()
giocatore1, giocatore2 = distribuisci_carte(mazzo)

rubamazzo(giocatore1, giocatore2)
vincitore = determina_vincitore(giocatore1, giocatore2)
print(f"Il vincitore è: {vincitore}")
