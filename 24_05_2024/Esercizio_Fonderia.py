with open("InputFile_PagamentiDipendenti.txt", "r") as f:
    for l in f:
        # LETTURA TOGLIENDO LE RIGHE VUOTE - INTERPRETAZIONE 1
        if l.strip() != "":
            print(l.strip())
print("-----------------------------")
print("Domanda a + b:\n")
# SE NON STAMPO LA PRIMA RIGA
prima_riga = True
with open("InputFile_PagamentiDipendenti.txt", "r") as f:
    for l in f:
        if prima_riga:
            prima_riga = False
        else:
            # LETTURA TOGLIENDO LE RIGHE VUOTE E I TAB TRA LE PAROLE - INTERPRETAZIONE 2
            if l.strip() != "":
                lista_elementi_riga = l.strip().split("\t") # il risultato della funzione split è sempre una lista
                for i in range(len(lista_elementi_riga)):
                    if lista_elementi_riga[i] != "" and lista_elementi_riga[i] != " ":
                        lista_elementi_riga[i].replace(" ", "")
                        if i == len(lista_elementi_riga) - 1:
                            print(lista_elementi_riga[i], end="")
                        else:
                            print(lista_elementi_riga[i], end=",")
                print()
print("-----------------------------")
print("Domanda c:\n")
list_of_lists = []
# SE NON STAMPO LA PRIMA RIGA
prima_riga = True
with open("InputFile_PagamentiDipendenti.txt", "r") as f:
    for l in f:
        if prima_riga:
            prima_riga = False
        else:
            # LETTURA TOGLIENDO LE RIGHE VUOTE E I TAB TRA LE PAROLE - INTERPRETAZIONE 2
            if l.strip() != "":
                lista_riga_intermedia = []
                lista_elementi_riga = l.strip().split("\t") # il risultato della funzione split è sempre una lista
                for i in range(len(lista_elementi_riga)):
                    if lista_elementi_riga[i] != "" and lista_elementi_riga[i] != " ":
                        lista_elementi_riga[i].replace(" ", "")
                        lista_riga_intermedia.append(lista_elementi_riga[i])
                list_of_lists.append(lista_riga_intermedia)
for riga in list_of_lists:
    print(riga)
print("-----------------------------")
print("Domanda d METODO 1:\n")
list_of_lists = []
# SE NON STAMPO LA PRIMA RIGA
prima_riga = True
with open("InputFile_PagamentiDipendenti.txt", "r") as f:
    for l in f:
        if prima_riga:
            prima_riga = False
        else:
            # LETTURA TOGLIENDO LE RIGHE VUOTE E I TAB TRA LE PAROLE - INTERPRETAZIONE 2
            if l.strip() != "":
                lista_riga_intermedia = []
                lista_elementi_riga = l.strip().split("\t") # il risultato della funzione split è sempre una lista
                for i in range(len(lista_elementi_riga)):
                    if lista_elementi_riga[i] != "" and lista_elementi_riga[i] != " ":
                        lista_elementi_riga[i].replace(" ", "")
                        try:
                            lista_riga_intermedia.append(int(lista_elementi_riga[i]))
                        except:
                            lista_riga_intermedia.append(lista_elementi_riga[i])
                list_of_lists.append(lista_riga_intermedia)
print()
tot = 0
for riga in list_of_lists:
    if riga[2] == "FONDERIA":
        tot_persona = riga[3] + riga[4] + riga[5] + riga[6]
        tot += tot_persona
        print(riga[0] + " " + riga[1] + ": " + str(tot_persona))
print("\nTOTALE FONDERIA: " + str(tot))
print()
tot = 0
for i in range(len(list_of_lists)):
    if list_of_lists[i][2] == "FONDERIA":
        tot_persona = list_of_lists[i][3] + list_of_lists[i][4] + list_of_lists[i][5] + list_of_lists[i][6]
        tot += tot_persona
        print(list_of_lists[i][0] + " " + list_of_lists[i][1] + ": " + str(tot_persona))
print("\nTOTALE FONDERIA: " + str(tot))
print("-----------------------------")
print("Domanda d METODO 2:\n")
list_of_lists = []
# SE NON STAMPO LA PRIMA RIGA
prima_riga = True
with open("InputFile_PagamentiDipendenti.txt", "r") as f:
    for l in f:
        if prima_riga:
            prima_riga = False
        else:
            # LETTURA TOGLIENDO LE RIGHE VUOTE E I TAB TRA LE PAROLE - INTERPRETAZIONE 2
            if l.strip() != "":
                lista_riga_intermedia = []
                lista_elementi_riga = l.strip().split("\t") # il risultato della funzione split è sempre una lista
                for i in range(len(lista_elementi_riga)):
                    if lista_elementi_riga[i] != "" and lista_elementi_riga[i] != " ":
                        lista_elementi_riga[i].replace(" ", "")
                        lista_riga_intermedia.append(lista_elementi_riga[i])
                list_of_lists.append(lista_riga_intermedia)
print()
tot = 0
for riga in list_of_lists:
    if riga[2] == "FONDERIA":
        tot_persona = int(riga[3]) + int(riga[4]) + int(riga[5]) + int(riga[6])
        tot += tot_persona
        print(riga[0] + " " + riga[1] + ": " + str(tot_persona))
print("\nTOTALE FONDERIA: " + str(tot))
print()
tot = 0
for i in range(len(list_of_lists)):
    if list_of_lists[i][2] == "FONDERIA":
        tot_persona = int(list_of_lists[i][3]) + int(list_of_lists[i][4]) + int(list_of_lists[i][5]) + int(list_of_lists[i][6])
        tot += tot_persona
        print(list_of_lists[i][0] + " " + list_of_lists[i][1] + ": " + str(tot_persona))
print("\nTOTALE FONDERIA: " + str(tot))
