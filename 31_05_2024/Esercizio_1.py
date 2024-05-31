lista_dati_film = []
with open("film.txt", "r") as f:
    for l in f:
        elementi_riga = l.strip().split("!")
        dizionario_dati = {
            "nome_film": elementi_riga[0],
            "autore_film": elementi_riga[1],
            "anno_uscita": int(elementi_riga[2])
        }
        lista_dati_film.append(dizionario_dati)
"""for i in range(len(lista_dati_film)):
    print(lista_dati_film[i])"""
# METODO 2
dizionario_dati_film = {}
with open("film.txt", "r") as f:
    for l in f:
        elementi_riga = l.strip().split("!")
        # ASSUMO CHE NON SI RIPETANO I NOMI DEI FILM
        # METODO 1
        """
        chiave = elementi_riga[0] # NOME DEL FILM
        autore = elementi_riga[1]
        anno = int(elementi_riga[2])
        dizionario_dati = {
            "autore_film": autore,
            "anno_uscita": anno
        }
        dizionario_dati_film[chiave] = dizionario_dati
        """
        # METODO 2
        dizionario_dati_film[elementi_riga[0]] = {
            "autore_film": elementi_riga[1],
            "anno_uscita": int(elementi_riga[2])
        }
for k,i in dizionario_dati_film.items():
    print(k)
    for kk, ii in i.items():
        print("\t" + kk + ": " + str(ii))


# DOMANDA 1
print("---------------------------------")
for k,i in dizionario_dati_film.items():
    print(k,i)
print("------------------------------------")
print("DOMANDA 1:")
dizionario_ordinato = dict(sorted(dizionario_dati_film.items(), key=lambda item: item[1]["autore_film"]))
for k, i in dizionario_ordinato.items():
    print("Nome Film: " + k + "; Nome Autore: " + i["autore_film"] + "; Anno Uscita: " + str(i["anno_uscita"]))

# DOMANDA 2
print("------------------------------------")
print("DOMANDA 2:")
dizionario_ordinato = dict(sorted(dizionario_dati_film.items(), key=lambda item: item[1]["anno_uscita"]))
chiavi_dizionario_ordinato = list(dizionario_ordinato.keys())
ultima_chiave = chiavi_dizionario_ordinato[-1]
print("Nome Film: " + ultima_chiave + ", Nome Autore: " + dizionario_ordinato[ultima_chiave]["autore_film"] + ", Anno Uscita: " + str(dizionario_ordinato[ultima_chiave]["anno_uscita"]))
# elementi_dizionario_ordinato = list(dizionario_ordinato.values())
# print(elementi_dizionario_ordinato)

# DOMANDA 3
print("------------------------------------")
print("DOMANDA 3:")
# lunghezza_massima = -100000000000000000000000000000000000000
# METODO 1
chiavi_dizionario = list(dizionario_dati_film.keys())
lunghezza_massima = len(chiavi_dizionario[0])
chiave_massima = chiavi_dizionario[0]
for k, i in dizionario_dati_film.items():
    if len(k) > lunghezza_massima:
        lunghezza_massima = len(k)
        chiave_massima = k
print("Nome Film: " + chiave_massima + ", Nome Autore: " + dizionario_dati_film[chiave_massima]["autore_film"] + ", Anno Uscita: " + str(dizionario_dati_film[chiave_massima]["anno_uscita"]))
# METODO 2
dizionario_ordinato = dict(sorted(dizionario_dati_film.items(), key=lambda item: len(item[0])))
chiavi_dizionario_ordinato = list(dizionario_ordinato.keys())
ultima_chiave = chiavi_dizionario_ordinato[-1]
print("Nome Film: " + ultima_chiave + ", Nome Autore: " + dizionario_ordinato[ultima_chiave]["autore_film"] + ", Anno Uscita: " + str(dizionario_ordinato[ultima_chiave]["anno_uscita"]))

# DOMANDA 4
print("------------------------------------")
print("DOMANDA 4:")
somma_date = 0
cont = 0
for k, i in dizionario_dati_film.items():
    somma_date += i["anno_uscita"]
    cont += 1
print("La media delle date di uscita dei film è: " + str(int(round(somma_date/cont, 0))))
