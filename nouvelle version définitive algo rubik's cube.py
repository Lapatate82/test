# Le cube est défini par 54 variables représentant chancune une petite facette du cube et ayant pour valeur le nom de la couleur de cette facette.

# les variables sont nommées en fonction de deux choses: la face où elles sont avec une lettre pour chaque face et leur position dans la face avec
# un numéro pour chaque position.

# Les lettres sont: U pour la face supérieure, F pour la face avant, R pour la face droite, B pour la face arrière, L pour la face gauche et D pour
# la face inférieure.

# Les numéros sont repartis de cette manière:   1       2       3

#                                               4       5       6

#                                               7       8       9


# Pour les faces F, R, B, et L, on fait des mouvements y pour obtenir cette répartition des numéros. (Voir notation internationnale des mouvements du
# rubik's cube: https://www.francocube.com/notation) Pour la face U on fait un mouvement x' et pour la face D un mouvement x.

# Exemple: F7 est le coin bas gauche de la face avant.



# Quelques concepts pour mieux comprendre le rubik's cube: -Les facettes avec un 5 sont les centres. Ils restent toujours immobiles les uns par
#                                                            rapport aux autres et définissent donc la couleur que devra prendre leur face.

#                                                           -Les facettes avec des chiffres pairs forment les arêtes en s'associant par groupes de
#                                                            deux facettes de face adjacentes qui resteront immmobiles l'une par rapport à l'autre.

#                                                           -Les autres facettes forment les coins en s'associant par groupe de trois facettes de faces
#                                                            adjacentes qui resteront immobiles les unes par rapport aux autres.

#                                                           -Résoudre le cube revient donc à  placer correctement les coins et les arêtes par rapport
#                                                            aux centres.




# Définition des mouvements de base du cube avec avec dans la notation un I pour remplacer le ' quand le mouvement est inversé.
# Notations internationales: (https://www.francocube.com/notation)




def R(U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9):
    U3B = U6
    U3 = F6
    F3 = D6
    D3 = B7
    B7 = U3B
    U6B = U9
    U6 = F6
    F6 = D6
    D6 = B4
    B4 = U6B
    U9B = U9
    U9 = F9
    F9 = D9
    D9 = B1
    B1 = U9B
    R1B = R1
    R1 = R7
    R7 = R9
    R9 = R3
    R3 = R1B
    R2B = R2
    R2 = R4
    R4 = R8
    R8 = R6
    R6 = R2B
    return(U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9)


def RI(U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9):
    U3B = U3
    U3 = B7
    B7 = D3
    D3 = F3
    F3 = U3B
    U6B = U6
    U6 = B4
    B4 = D6
    D6 = F6
    F6 = U6B
    U9B = U9
    U9 = B1
    B1 = D9
    D9 = F9
    F9 = U9B
    R1B = R1
    R1 = R3
    R3 = R9
    R9 = R7
    R7 = R1B
    R2B = R2
    R2 = R6
    R6 = R8
    R8 = R4
    R4 = R2B
    return(U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9)


def L(U1,U4,U7,F1,F4,F7,D1,D4,D7,B3,B6,B9,L1,L2,L3,L4,L6,L7,L8,L9):
    U1B = U1
    U1 = B9
    B9 = D1
    D1 = F1
    F1 = U1B
    U4B = U4
    U4 = B6
    B6 = D4
    D4 = F4
    F4 = U4B
    U7B = U7
    U7 = B3
    B3 = D7
    D7 = F7
    F7 = U7B
    L1B = L1
    L1 = L7
    L7 = L9
    L9 = L3
    L3 = L1B
    L2B = L2
    L2 = L4
    L4 = L8
    L8 = L6
    L6 = L2B
    return(U1,U4,U7,F1,F4,F7,D1,D4,D7,B3,B6,B9,L1,L2,L3,L4,L6,L7,L8,L9)


def LI(U1,U4,U7,F1,F4,F7,D1,D4,D7,B3,B6,B9,L1,L2,L3,L4,L6,L7,L8,L9):
    U1B = U1
    U1 = F1
    F1 = D1
    D1 = B9
    B9 = U1B
    U4B = U4
    U4 = F4
    F4 = D4
    D4 = B6
    B6 = U4B
    U7B = U7
    U7 = F7
    F7 = D7
    D7 = B3
    B3 = U7B
    L1B = L1
    L1 = L3
    L3 = L9
    L9 = L7
    L7 = L1B
    L2B = L2
    L2 = L6
    L6 = L8
    L8 = L4
    L4 = L2B
    return(U1,U4,U7,F1,F4,F7,D1,D4,D7,B3,B6,B9,L1,L2,L3,L4,L6,L7,L8,L9)


def U(F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result):
    F1B = F1
    F1 = R1
    R1 = B1
    B1 = L1
    L1 = F1B
    F2B = F2
    F2 = R2
    R2 = B2
    B2 = L2
    L2 = F2B
    F3B = F3
    F3 = R3
    R3 = B3
    B3 = L3
    L3 = F3B
    U1B = U1
    U1 = U7
    U7 = U9
    U9 = U3
    U3 = U1B
    U2B = U2
    U2 = U4
    U4 = U8
    U8 = U6
    U6 = U2B
    memory,memorysens,result = enregistrement("U"," ",memory,memorysens,result)
    return(F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result)


def UI(F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result):
    F1B = F1
    F1 = L1
    L1 = B1
    B1 = R1
    R1 = F1B
    F2B = F2
    F2 = L2
    L2 = B2
    B2 = R2
    R2 = F2B
    F3B = F3
    F3 = L3
    L3 = B3
    B3 = R3
    R3 = F3B
    U1B = U1
    U1 = U3
    U3 = U9
    U9 = U7
    U7 = U1B
    U2B = U2
    U2 = U6
    U6 = U8
    U8 = U4
    U4 = U2B
    memory,memorysens,result = enregistrement("U","' ",memory,memorysens,result)
    return(F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result)


def D(F7,F8,F9,R7,R8,R9,B7,B8,B9,L7,L8,L9,D1,D2,D3,D4,D6,D7,D8,D9,memory,memorysens,result):
    F7B = F7
    F7 = L7
    L7 = B7
    B7 = R7
    R7 = F7B
    F8B = F8
    F8 = L8
    L8 = B8
    B8 = R8
    R8 = F8B
    F9B = F9
    F9 = L9
    L9 = B9
    B9 = R9
    R9 = F9B
    D1B = D1
    D1 = D7
    D7 = D9
    D9 = D3
    D3 = D1B
    D2B = D2
    D2 = D4
    D4 = D8
    D8 = D6
    D6 = D2B
    memory,memorysens,result = enregistrement("D"," ",memory,memorysens,result)
    return(F7,F8,F9,R7,R8,R9,B7,B8,B9,L7,L8,L9,D1,D2,D3,D4,D6,D7,D8,D9,memory,memorysens,result)


def DI(F7,F8,F9,R7,R8,R9,B7,B8,B9,L7,L8,L9,D1,D2,D3,D4,D6,D7,D8,D9,memory,memorysens,result):
    F7B = F7
    F7 = R7
    R7 = B7
    B7 = L7
    L7 = F7B
    F8B = F8
    F8 = R8
    R8 = B8
    B8 = L8
    L8 = F8B
    F9B = F9
    F9 = R9
    R9 = B9
    B9 = L9
    L9 = F9B
    D1B = D1
    D1 = D3
    D3 = D9
    D9 = D7
    D7 = D1B
    D2B = D2
    D2 = D6
    D6 = D8
    D8 = D4
    D4 = D2B
    memory,memorysens,result = enregistrement("D","' ",memory,memorysens,result)
    return(F7,F8,F9,R7,R8,R9,B7,B8,B9,L7,L8,L9,D1,D2,D3,D4,D6,D7,D8,D9,memory,memorysens,result)


def F(U7,U8,U9,R1,R4,R7,L3,L6,L9,D1,D2,D3,F1,F2,F3,F4,F6,F7,F8,F9):
    U7B = U7
    U7 = L9
    L9 = D3
    D3 = R1
    R1 = U7B
    U8B = U8
    U8 = L6
    L6 = D2
    D2 = R4
    R4 = U8B
    U9B = U9
    U9 = L3
    L3 = D1
    D1 = R7
    R7 = U9B
    F1B = F1
    F1 = F7
    F7 = F9
    F9 = F3
    F3 = F1B
    F2B = F2
    F2 = F4
    F4 = F8
    F8 = F6
    F6 = F2B
    return(U7,U8,U9,R1,R4,R7,L3,L6,L9,D1,D2,D3,F1,F2,F3,F4,F6,F7,F8,F9)


def FI(U7,U8,U9,R1,R4,R7,L3,L6,L9,D1,D2,D3,F1,F2,F3,F4,F6,F7,F8,F9):
    U7B = U7
    U7 = R1
    R1 = D3
    D3 = L9
    L9 = U7B
    U8B = U8
    U8 = R4
    R4 = D2
    D2 = L6
    L6 = U8B
    U9B = U9
    U9 = R7
    R7 = D1
    D1 = L3
    L3 = U9B
    F1B = F1
    F1 = F3
    F3 = F9
    F9 = F7
    F7 = F1B
    F2B = F2
    F2 = F6
    F6 = F8
    F8 = F4
    F4 = F2B
    return(U7,U8,U9,R1,R4,R7,L3,L6,L9,D1,D2,D3,F1,F2,F3,F4,F6,F7,F8,F9)


def B(U1,U2,U3,R3,R6,R9,L1,L4,L7,D7,D8,D9,B1,B2,B3,B4,B6,B7,B8,B9):
    U1B = U1
    U1 = R3
    R3 = D9
    D9 = L7
    L7 = U1B
    U2B = U2
    U2 = R6
    R6 = D8
    D8 = L4
    L4 = U2B
    U3B = U3
    U3 = R9
    R9 = D7
    D7 = L1
    L1 = U3B
    B1B = B1
    B1 = B7
    B7 = B9
    B9 = B3
    B3 = B1B
    B2B = B2
    B2 = B4
    B4 = B8
    B8 = B6
    B6 = B2B
    return(U1,U2,U3,R3,R6,R9,L1,L4,L7,D7,D8,D9,B1,B2,B3,B4,B6,B7,B8,B9)


def BI(U1,U2,U3,R3,R6,R9,L1,L4,L7,D7,D8,D9,B1,B2,B3,B4,B6,B7,B8,B9):
    U1B = U1
    U1 = L7
    L7 = D9
    D9 = R3
    R3 = U1B
    U2B = U2
    U2 = L4
    L4 = D8
    D8 = R6
    R6 = U2B
    U3B = U3
    U3 = L1
    L1 = D7
    D7 = R9
    R9 = U3B
    B1B = B1
    B1 = B3
    B3 = B9
    B9 = B7
    B7 = B1B
    B2B = B2
    B2 = B6
    B6 = B8
    B8 = B4
    B4 = B2B
    return(U1,U2,U3,R3,R6,R9,L1,L4,L7,D7,D8,D9,B1,B2,B3,B4,B6,B7,B8,B9)


def y(U1,U2,U3,U4,U5,U6,U7,U8,U9,F1,F2,F3,F4,F5,F6,F7,F8,F9,R1,R2,R3,R4,R5,R6,R7,R8,R9,B1,B2,B3,B4,B5,B6,B7,B8,B9,L1,L2,L3,L4,L5,L6,L7,L8,L9,D1,D2,D3,D4,D5,D6,D7,D8,D9,P):
    U1B = U1
    U1 = U3
    U3 = U9
    U9 = U7
    U7 = U1B
    U2B = U2
    U2 = U6
    U6 = U8
    U8 = U4
    U4 = U2B
    F1B = F1
    F1 = L1
    L1 = B1
    B1 = R1
    R1 = F1B
    F2B = F2
    F2 = L2
    L2 = B2
    B2 = R2
    R2 = F2B
    F3B = F3
    F3 = L3
    L3 = B3
    B3 = R3
    R3 = F3B
    F4B = F4
    F4 = L4
    L4 = B4
    B4 = R4
    R4 = F4B
    F5B = F5
    F5 = L5
    L5 = B5
    B5 = R5
    R5 = F5B
    F6B = F6
    F6 = L6
    L6 = B6
    B6 = R6
    R6 = F6B
    F7B = F7
    F7 = L7
    L7 = B7
    B7 = R7
    R7 = F7B
    F8B = F8
    F8 = L8
    L8 = B8
    B8 = R8
    R8 = F8B
    F9B = F9
    F9 = L9
    L9 = B9
    B9 = R9
    R9 = F9B
    D1B = D1
    D1 = D7
    D7 = D9
    D9 = D3
    D3 = D1B
    D2B = D2
    D2 = D4
    D4 = D8
    D8 = D6
    D6 = D2B
    if P == 1:
        P = 2
    elif P == 2:
        P = 3
    elif P == 3:
        P = 4
    elif P == 4:
        P = 1
    return(U1,U2,U3,U4,U5,U6,U7,U8,U9,F1,F2,F3,F4,F5,F6,F7,F8,F9,R1,R2,R3,R4,R5,R6,R7,R8,R9,B1,B2,B3,B4,B5,B6,B7,B8,B9,L1,L2,L3,L4,L5,L6,L7,L8,L9,D1,D2,D3,D4,D5,D6,D7,D8,D9,P)


def enregistrement(move,movesens,memory,memorysens,result):
    if move != memory:
        result = result + memory + memorysens
        memory = move
        memorysens = movesens
    else:
        if ((memorysens == " ") & (movesens == "' ")) | (memorysens == "' ") & (movesens == " "):
            memory = ""
            memorysens = ""
        elif ((memorysens == " ") & (movesens == " ")) | (memorysens == "' ") & (movesens == "' "):
            memorysens = "2 "
        elif (memorysens == "2 ") & (movesens == "' "):
            memorysens = " "
        elif (memorysens == "2 ") & (movesens == " "):
            memorysens = "' "
    return(memory,memorysens,result)


def RB(U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,P,memory,memorysens,result):
    U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9 = R(U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9)
    if P == 1:
        memory,memorysens,result = enregistrement("R"," ",memory,memorysens,result)
    if P == 2:
        memory,memorysens,result = enregistrement("F"," ",memory,memorysens,result)
    if P == 3:
        memory,memorysens,result = enregistrement("L"," ",memory,memorysens,result)
    if P == 4:
        memory,memorysens,result = enregistrement("B"," ",memory,memorysens,result)
    return(U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,memory,memorysens,result)


def LB(U1,U4,U7,F1,F4,F7,D1,D4,D7,B3,B6,B9,L1,L2,L3,L4,L6,L7,L8,L9,P,memory,memorysens,result):
    U1,U4,U7,F1,F4,F7,D1,D4,D7,B3,B6,B9,L1,L2,L3,L4,L6,L7,L8,L9 = L(U1,U4,U7,F1,F4,F7,D1,D4,D7,B3,B6,B9,L1,L2,L3,L4,L6,L7,L8,L9)
    if P == 1:
        memory,memorysens,result = enregistrement("L"," ",memory,memorysens,result)
    if P == 2:
        memory,memorysens,result = enregistrement("B"," ",memory,memorysens,result)
    if P == 3:
        memory,memorysens,result = enregistrement("R"," ",memory,memorysens,result)
    if P == 4:
        memory,memorysens,result = enregistrement("F"," ",memory,memorysens,result)
    return(U1,U4,U7,F1,F4,F7,D1,D4,D7,B3,B6,B9,L1,L2,L3,L4,L6,L7,L8,L9,memory,memorysens,result)


def FB(U7,U8,U9,R1,R4,R7,L3,L6,L9,D1,D2,D3,F1,F2,F3,F4,F6,F7,F8,F9,P,memory,memorysens,result):
    U7,U8,U9,R1,R4,R7,L3,L6,L9,D1,D2,D3,F1,F2,F3,F4,F6,F7,F8,F9 = F(U7,U8,U9,R1,R4,R7,L3,L6,L9,D1,D2,D3,F1,F2,F3,F4,F6,F7,F8,F9)
    if P == 1:
        memory,memorysens,result = enregistrement("F"," ",memory,memorysens,result)
    if P == 2:
        memory,memorysens,result = enregistrement("L"," ",memory,memorysens,result)
    if P == 3:
        memory,memorysens,result = enregistrement("B"," ",memory,memorysens,result)
    if P == 4:
        memory,memorysens,result = enregistrement("R"," ",memory,memorysens,result)
    return(U7,U8,U9,R1,R4,R7,L3,L6,L9,D1,D2,D3,F1,F2,F3,F4,F6,F7,F8,F9,memory,memorysens,result)


def BB(U1,U2,U3,R3,R6,R9,L1,L4,L7,D7,D8,D9,B1,B2,B3,B4,B6,B7,B8,B9,P,memory,memorysens,result):
    U1,U2,U3,R3,R6,R9,L1,L4,L7,D7,D8,D9,B1,B2,B3,B4,B6,B7,B8,B9 = B(U1,U2,U3,R3,R6,R9,L1,L4,L7,D7,D8,D9,B1,B2,B3,B4,B6,B7,B8,B9)
    if P == 1:
        memory,memorysens,result = enregistrement("B"," ",memory,memorysens,result)
    if P == 2:
        memory,memorysens,result = enregistrement("R"," ",memory,memorysens,result)
    if P == 3:
        memory,memorysens,result = enregistrement("F"," ",memory,memorysens,result)
    if P == 4:
        memory,memorysens,result = enregistrement("L"," ",memory,memorysens,result)
    return(U1,U2,U3,R3,R6,R9,L1,L4,L7,D7,D8,D9,B1,B2,B3,B4,B6,B7,B8,B9,memory,memorysens,result)


def RIB(U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,P,memory,memorysens,result):
    U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9 = RI(U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9)
    if P == 1:
        memory,memorysens,result = enregistrement("R","' ",memory,memorysens,result)
    if P == 2:
        memory,memorysens,result = enregistrement("F","' ",memory,memorysens,result)
    if P == 3:
        memory,memorysens,result = enregistrement("L","' ",memory,memorysens,result)
    if P == 4:
        memory,memorysens,result = enregistrement("B","' ",memory,memorysens,result)
    return(U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,memory,memorysens,result)


def LIB(U1,U4,U7,F1,F4,F7,D1,D4,D7,B3,B6,B9,L1,L2,L3,L4,L6,L7,L8,L9,P,memory,memorysens,result):
    U1,U4,U7,F1,F4,F7,D1,D4,D7,B3,B6,B9,L1,L2,L3,L4,L6,L7,L8,L9 = LI(U1,U4,U7,F1,F4,F7,D1,D4,D7,B3,B6,B9,L1,L2,L3,L4,L6,L7,L8,L9)
    if P == 1:
        memory,memorysens,result = enregistrement("L","' ",memory,memorysens,result)
    if P == 2:
        memory,memorysens,result = enregistrement("B","' ",memory,memorysens,result)
    if P == 3:
        memory,memorysens,result = enregistrement("R","' ",memory,memorysens,result)
    if P == 4:
        memory,memorysens,result = enregistrement("F","' ",memory,memorysens,result)
    return(U1,U4,U7,F1,F4,F7,D1,D4,D7,B3,B6,B9,L1,L2,L3,L4,L6,L7,L8,L9,memory,memorysens,result)


def FIB(U7,U8,U9,R1,R4,R7,L3,L6,L9,D1,D2,D3,F1,F2,F3,F4,F6,F7,F8,F9,P,memory,memorysens,result):
    U7,U8,U9,R1,R4,R7,L3,L6,L9,D1,D2,D3,F1,F2,F3,F4,F6,F7,F8,F9 = FI(U7,U8,U9,R1,R4,R7,L3,L6,L9,D1,D2,D3,F1,F2,F3,F4,F6,F7,F8,F9)
    if P == 1:
        memory,memorysens,result = enregistrement("F","' ",memory,memorysens,result)
    if P == 2:
        memory,memorysens,result = enregistrement("L","' ",memory,memorysens,result)
    if P == 3:
        memory,memorysens,result = enregistrement("B","' ",memory,memorysens,result)
    if P == 4:
        memory,memorysens,result = enregistrement("R","' ",memory,memorysens,result)
    return(U7,U8,U9,R1,R4,R7,L3,L6,L9,D1,D2,D3,F1,F2,F3,F4,F6,F7,F8,F9,memory,memorysens,result)


def BIB(U1,U2,U3,R3,R6,R9,L1,L4,L7,D7,D8,D9,B1,B2,B3,B4,B6,B7,B8,B9,P,memory,memorysens,result):
    U1,U2,U3,R3,R6,R9,L1,L4,L7,D7,D8,D9,B1,B2,B3,B4,B6,B7,B8,B9 = BI(U1,U2,U3,R3,R6,R9,L1,L4,L7,D7,D8,D9,B1,B2,B3,B4,B6,B7,B8,B9)
    if P == 1:
        memory,memorysens,result = enregistrement("B","' ",memory,memorysens,result)
    if P == 2:
        memory,memorysens,result = enregistrement("R","' ",memory,memorysens,result)
    if P == 3:
        memory,memorysens,result = enregistrement("F","' ",memory,memorysens,result)
    if P == 4:
        memory,memorysens,result = enregistrement("L","' ",memory,memorysens,result)
    return(U1,U2,U3,R3,R6,R9,L1,L4,L7,D7,D8,D9,B1,B2,B3,B4,B6,B7,B8,B9,memory,memorysens,result)


# Fonction principale qui renvoit les mouvements à faire pour résoudre le cube grâce à la variable result.

def cube(U1,U2,U3,U4,U5,U6,U7,U8,U9,F1,F2,F3,F4,F5,F6,F7,F8,F9,R1,R2,R3,R4,R5,R6,R7,R8,R9,B1,B2,B3,B4,B5,B6,B7,B8,B9,L1,L2,L3,L4,L5,L6,L7,L8,L9,D1,D2,D3,D4,D5,D6,D7,D8,D9):
    result = " "
    memory = ""
    memorysens = ""
    P = 1
    
    # On considère à des fins de clarté que le centre sur la face du bas est le centre blanc et que la face blanche une fois le cube résolu sera donc en bas
    # Première étape: La croix blanche (Résoudre les arêtes de la face inférieure en les plaçant au bon endroit.)
    
    # Première étape intermédiaire non indispensable pour optimiser le nombre de mouvements de la solution: si une arrête est déjà sur la bonne face elle est amenée à son bon emplacement
    if D2 == D5:    # Recherche d'une arrête blanche déjà bien placée sur la bonne face en D2
        while F8 != F5:     # L'arrête trouvée est déplacée jusqu'à sa bonne place
            U1,U2,U3,U4,U5,U6,U7,U8,U9,F1,F2,F3,F4,F5,F6,F7,F8,F9,R1,R2,R3,R4,R5,R6,R7,R8,R9,B1,B2,B3,B4,B5,B6,B7,B8,B9,L1,L2,L3,L4,L5,L6,L7,L8,L9,D1,D2,D3,D4,D5,D6,D7,D8,D9,P = y(U1,U2,U3,U4,U5,U6,U7,U8,U9,F1,F2,F3,F4,F5,F6,F7,F8,F9,R1,R2,R3,R4,R5,R6,R7,R8,R9,B1,B2,B3,B4,B5,B6,B7,B8,B9,L1,L2,L3,L4,L5,L6,L7,L8,L9,D1,D2,D3,D4,D5,D6,D7,D8,D9,P)
            F7,F8,F9,R7,R8,R9,B7,B8,B9,L7,L8,L9,D1,D2,D3,D4,D6,D7,D8,D9,memory,memorysens,result = DI(F7,F8,F9,R7,R8,R9,B7,B8,B9,L7,L8,L9,D1,D2,D3,D4,D6,D7,D8,D9,memory,memorysens,result)
        U1,U2,U3,U4,U5,U6,U7,U8,U9,F1,F2,F3,F4,F5,F6,F7,F8,F9,R1,R2,R3,R4,R5,R6,R7,R8,R9,B1,B2,B3,B4,B5,B6,B7,B8,B9,L1,L2,L3,L4,L5,L6,L7,L8,L9,D1,D2,D3,D4,D5,D6,D7,D8,D9,P = y(U1,U2,U3,U4,U5,U6,U7,U8,U9,F1,F2,F3,F4,F5,F6,F7,F8,F9,R1,R2,R3,R4,R5,R6,R7,R8,R9,B1,B2,B3,B4,B5,B6,B7,B8,B9,L1,L2,L3,L4,L5,L6,L7,L8,L9,D1,D2,D3,D4,D5,D6,D7,D8,D9,P)
    # Même chose pour les trois autres positions potentielles
    # Utilisation du elif car en replaçant bien une deuxième arrête on déplaçerait la première arrête que l'on avait déjà bien mise. On ne peut donc placer bien qu'une seule arrête via cette méthode.
    elif D4 == D5:
        U1,U2,U3,U4,U5,U6,U7,U8,U9,F1,F2,F3,F4,F5,F6,F7,F8,F9,R1,R2,R3,R4,R5,R6,R7,R8,R9,B1,B2,B3,B4,B5,B6,B7,B8,B9,L1,L2,L3,L4,L5,L6,L7,L8,L9,D1,D2,D3,D4,D5,D6,D7,D8,D9,P = y(U1,U2,U3,U4,U5,U6,U7,U8,U9,F1,F2,F3,F4,F5,F6,F7,F8,F9,R1,R2,R3,R4,R5,R6,R7,R8,R9,B1,B2,B3,B4,B5,B6,B7,B8,B9,L1,L2,L3,L4,L5,L6,L7,L8,L9,D1,D2,D3,D4,D5,D6,D7,D8,D9,P)
        while F8 != F5:
            U1,U2,U3,U4,U5,U6,U7,U8,U9,F1,F2,F3,F4,F5,F6,F7,F8,F9,R1,R2,R3,R4,R5,R6,R7,R8,R9,B1,B2,B3,B4,B5,B6,B7,B8,B9,L1,L2,L3,L4,L5,L6,L7,L8,L9,D1,D2,D3,D4,D5,D6,D7,D8,D9,P = y(U1,U2,U3,U4,U5,U6,U7,U8,U9,F1,F2,F3,F4,F5,F6,F7,F8,F9,R1,R2,R3,R4,R5,R6,R7,R8,R9,B1,B2,B3,B4,B5,B6,B7,B8,B9,L1,L2,L3,L4,L5,L6,L7,L8,L9,D1,D2,D3,D4,D5,D6,D7,D8,D9,P)
            F7,F8,F9,R7,R8,R9,B7,B8,B9,L7,L8,L9,D1,D2,D3,D4,D6,D7,D8,D9,memory,memorysens,result = DI(F7,F8,F9,R7,R8,R9,B7,B8,B9,L7,L8,L9,D1,D2,D3,D4,D6,D7,D8,D9,memory,memorysens,result)
        U1,U2,U3,U4,U5,U6,U7,U8,U9,F1,F2,F3,F4,F5,F6,F7,F8,F9,R1,R2,R3,R4,R5,R6,R7,R8,R9,B1,B2,B3,B4,B5,B6,B7,B8,B9,L1,L2,L3,L4,L5,L6,L7,L8,L9,D1,D2,D3,D4,D5,D6,D7,D8,D9,P = y(U1,U2,U3,U4,U5,U6,U7,U8,U9,F1,F2,F3,F4,F5,F6,F7,F8,F9,R1,R2,R3,R4,R5,R6,R7,R8,R9,B1,B2,B3,B4,B5,B6,B7,B8,B9,L1,L2,L3,L4,L5,L6,L7,L8,L9,D1,D2,D3,D4,D5,D6,D7,D8,D9,P)
    elif D8 == D5:
        U1,U2,U3,U4,U5,U6,U7,U8,U9,F1,F2,F3,F4,F5,F6,F7,F8,F9,R1,R2,R3,R4,R5,R6,R7,R8,R9,B1,B2,B3,B4,B5,B6,B7,B8,B9,L1,L2,L3,L4,L5,L6,L7,L8,L9,D1,D2,D3,D4,D5,D6,D7,D8,D9,P = y(U1,U2,U3,U4,U5,U6,U7,U8,U9,F1,F2,F3,F4,F5,F6,F7,F8,F9,R1,R2,R3,R4,R5,R6,R7,R8,R9,B1,B2,B3,B4,B5,B6,B7,B8,B9,L1,L2,L3,L4,L5,L6,L7,L8,L9,D1,D2,D3,D4,D5,D6,D7,D8,D9,P)
        U1,U2,U3,U4,U5,U6,U7,U8,U9,F1,F2,F3,F4,F5,F6,F7,F8,F9,R1,R2,R3,R4,R5,R6,R7,R8,R9,B1,B2,B3,B4,B5,B6,B7,B8,B9,L1,L2,L3,L4,L5,L6,L7,L8,L9,D1,D2,D3,D4,D5,D6,D7,D8,D9,P = y(U1,U2,U3,U4,U5,U6,U7,U8,U9,F1,F2,F3,F4,F5,F6,F7,F8,F9,R1,R2,R3,R4,R5,R6,R7,R8,R9,B1,B2,B3,B4,B5,B6,B7,B8,B9,L1,L2,L3,L4,L5,L6,L7,L8,L9,D1,D2,D3,D4,D5,D6,D7,D8,D9,P)
        while F8 != F5:
            U1,U2,U3,U4,U5,U6,U7,U8,U9,F1,F2,F3,F4,F5,F6,F7,F8,F9,R1,R2,R3,R4,R5,R6,R7,R8,R9,B1,B2,B3,B4,B5,B6,B7,B8,B9,L1,L2,L3,L4,L5,L6,L7,L8,L9,D1,D2,D3,D4,D5,D6,D7,D8,D9,P = y(U1,U2,U3,U4,U5,U6,U7,U8,U9,F1,F2,F3,F4,F5,F6,F7,F8,F9,R1,R2,R3,R4,R5,R6,R7,R8,R9,B1,B2,B3,B4,B5,B6,B7,B8,B9,L1,L2,L3,L4,L5,L6,L7,L8,L9,D1,D2,D3,D4,D5,D6,D7,D8,D9,P)
            F7,F8,F9,R7,R8,R9,B7,B8,B9,L7,L8,L9,D1,D2,D3,D4,D6,D7,D8,D9,memory,memorysens,result = DI(F7,F8,F9,R7,R8,R9,B7,B8,B9,L7,L8,L9,D1,D2,D3,D4,D6,D7,D8,D9,memory,memorysens,result)
        U1,U2,U3,U4,U5,U6,U7,U8,U9,F1,F2,F3,F4,F5,F6,F7,F8,F9,R1,R2,R3,R4,R5,R6,R7,R8,R9,B1,B2,B3,B4,B5,B6,B7,B8,B9,L1,L2,L3,L4,L5,L6,L7,L8,L9,D1,D2,D3,D4,D5,D6,D7,D8,D9,P = y(U1,U2,U3,U4,U5,U6,U7,U8,U9,F1,F2,F3,F4,F5,F6,F7,F8,F9,R1,R2,R3,R4,R5,R6,R7,R8,R9,B1,B2,B3,B4,B5,B6,B7,B8,B9,L1,L2,L3,L4,L5,L6,L7,L8,L9,D1,D2,D3,D4,D5,D6,D7,D8,D9,P)
    elif D6 == D5:
        U1,U2,U3,U4,U5,U6,U7,U8,U9,F1,F2,F3,F4,F5,F6,F7,F8,F9,R1,R2,R3,R4,R5,R6,R7,R8,R9,B1,B2,B3,B4,B5,B6,B7,B8,B9,L1,L2,L3,L4,L5,L6,L7,L8,L9,D1,D2,D3,D4,D5,D6,D7,D8,D9,P = y(U1,U2,U3,U4,U5,U6,U7,U8,U9,F1,F2,F3,F4,F5,F6,F7,F8,F9,R1,R2,R3,R4,R5,R6,R7,R8,R9,B1,B2,B3,B4,B5,B6,B7,B8,B9,L1,L2,L3,L4,L5,L6,L7,L8,L9,D1,D2,D3,D4,D5,D6,D7,D8,D9,P)
        U1,U2,U3,U4,U5,U6,U7,U8,U9,F1,F2,F3,F4,F5,F6,F7,F8,F9,R1,R2,R3,R4,R5,R6,R7,R8,R9,B1,B2,B3,B4,B5,B6,B7,B8,B9,L1,L2,L3,L4,L5,L6,L7,L8,L9,D1,D2,D3,D4,D5,D6,D7,D8,D9,P = y(U1,U2,U3,U4,U5,U6,U7,U8,U9,F1,F2,F3,F4,F5,F6,F7,F8,F9,R1,R2,R3,R4,R5,R6,R7,R8,R9,B1,B2,B3,B4,B5,B6,B7,B8,B9,L1,L2,L3,L4,L5,L6,L7,L8,L9,D1,D2,D3,D4,D5,D6,D7,D8,D9,P)
        U1,U2,U3,U4,U5,U6,U7,U8,U9,F1,F2,F3,F4,F5,F6,F7,F8,F9,R1,R2,R3,R4,R5,R6,R7,R8,R9,B1,B2,B3,B4,B5,B6,B7,B8,B9,L1,L2,L3,L4,L5,L6,L7,L8,L9,D1,D2,D3,D4,D5,D6,D7,D8,D9,P = y(U1,U2,U3,U4,U5,U6,U7,U8,U9,F1,F2,F3,F4,F5,F6,F7,F8,F9,R1,R2,R3,R4,R5,R6,R7,R8,R9,B1,B2,B3,B4,B5,B6,B7,B8,B9,L1,L2,L3,L4,L5,L6,L7,L8,L9,D1,D2,D3,D4,D5,D6,D7,D8,D9,P)
        while F8 != F5:
            U1,U2,U3,U4,U5,U6,U7,U8,U9,F1,F2,F3,F4,F5,F6,F7,F8,F9,R1,R2,R3,R4,R5,R6,R7,R8,R9,B1,B2,B3,B4,B5,B6,B7,B8,B9,L1,L2,L3,L4,L5,L6,L7,L8,L9,D1,D2,D3,D4,D5,D6,D7,D8,D9,P = y(U1,U2,U3,U4,U5,U6,U7,U8,U9,F1,F2,F3,F4,F5,F6,F7,F8,F9,R1,R2,R3,R4,R5,R6,R7,R8,R9,B1,B2,B3,B4,B5,B6,B7,B8,B9,L1,L2,L3,L4,L5,L6,L7,L8,L9,D1,D2,D3,D4,D5,D6,D7,D8,D9,P)
            F7,F8,F9,R7,R8,R9,B7,B8,B9,L7,L8,L9,D1,D2,D3,D4,D6,D7,D8,D9,memory,memorysens,result = DI(F7,F8,F9,R7,R8,R9,B7,B8,B9,L7,L8,L9,D1,D2,D3,D4,D6,D7,D8,D9,memory,memorysens,result)
        U1,U2,U3,U4,U5,U6,U7,U8,U9,F1,F2,F3,F4,F5,F6,F7,F8,F9,R1,R2,R3,R4,R5,R6,R7,R8,R9,B1,B2,B3,B4,B5,B6,B7,B8,B9,L1,L2,L3,L4,L5,L6,L7,L8,L9,D1,D2,D3,D4,D5,D6,D7,D8,D9,P = y(U1,U2,U3,U4,U5,U6,U7,U8,U9,F1,F2,F3,F4,F5,F6,F7,F8,F9,R1,R2,R3,R4,R5,R6,R7,R8,R9,B1,B2,B3,B4,B5,B6,B7,B8,B9,L1,L2,L3,L4,L5,L6,L7,L8,L9,D1,D2,D3,D4,D5,D6,D7,D8,D9,P)

    # Etape de la croix blanche en elle même. La boucle while assure que l'étape soit bien réalisée. 
    # Chaque emplacement potentiel d'une arrête blanche est testé puis l'arrête détécté est mise à sa bonne place. 
    # Pour limiter le nombre de cas potentiels à prendre en compte, seule une partie du cube est testée et si aucune arrête blanche n'y est trouvée, l'algorithme fait tourner le cube pour tester une autre partie.
    # On est ainsi assuré que toutes les arrêtes blanches soient détectées et placées au bon endroit.

    while (D2 != D5) | (D4 != D5) | (D6 != D5) | (D8 != D5) | (F8 != F5) | (R8 != R5) | (B8 != B5) | (L8 != L5):
        if U8 == D5:
            while F2 != F5:     # L'arrête est amenée au-dessus de son emplacement.
                U1,U2,U3,U4,U5,U6,U7,U8,U9,F1,F2,F3,F4,F5,F6,F7,F8,F9,R1,R2,R3,R4,R5,R6,R7,R8,R9,B1,B2,B3,B4,B5,B6,B7,B8,B9,L1,L2,L3,L4,L5,L6,L7,L8,L9,D1,D2,D3,D4,D5,D6,D7,D8,D9,P = y(U1,U2,U3,U4,U5,U6,U7,U8,U9,F1,F2,F3,F4,F5,F6,F7,F8,F9,R1,R2,R3,R4,R5,R6,R7,R8,R9,B1,B2,B3,B4,B5,B6,B7,B8,B9,L1,L2,L3,L4,L5,L6,L7,L8,L9,D1,D2,D3,D4,D5,D6,D7,D8,D9,P)
                F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result = U(F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result)
            # L'arrête est descendue.
            U7,U8,U9,R1,R4,R7,L3,L6,L9,D1,D2,D3,F1,F2,F3,F4,F6,F7,F8,F9,memory,memorysens,result = FB(U7,U8,U9,R1,R4,R7,L3,L6,L9,D1,D2,D3,F1,F2,F3,F4,F6,F7,F8,F9,P,memory,memorysens,result)
            U7,U8,U9,R1,R4,R7,L3,L6,L9,D1,D2,D3,F1,F2,F3,F4,F6,F7,F8,F9,memory,memorysens,result = FB(U7,U8,U9,R1,R4,R7,L3,L6,L9,D1,D2,D3,F1,F2,F3,F4,F6,F7,F8,F9,P,memory,memorysens,result)
        elif (D2 == D5) & (F8 != F5):
            # L'arrête est montée sur la face du haut.
            U7,U8,U9,R1,R4,R7,L3,L6,L9,D1,D2,D3,F1,F2,F3,F4,F6,F7,F8,F9,memory,memorysens,result = FB(U7,U8,U9,R1,R4,R7,L3,L6,L9,D1,D2,D3,F1,F2,F3,F4,F6,F7,F8,F9,P,memory,memorysens,result)
            U7,U8,U9,R1,R4,R7,L3,L6,L9,D1,D2,D3,F1,F2,F3,F4,F6,F7,F8,F9,memory,memorysens,result = FB(U7,U8,U9,R1,R4,R7,L3,L6,L9,D1,D2,D3,F1,F2,F3,F4,F6,F7,F8,F9,P,memory,memorysens,result)
            while F2 != F5:     # L'arrête est amenée au-dessus de son emplacement.
                U1,U2,U3,U4,U5,U6,U7,U8,U9,F1,F2,F3,F4,F5,F6,F7,F8,F9,R1,R2,R3,R4,R5,R6,R7,R8,R9,B1,B2,B3,B4,B5,B6,B7,B8,B9,L1,L2,L3,L4,L5,L6,L7,L8,L9,D1,D2,D3,D4,D5,D6,D7,D8,D9,P = y(U1,U2,U3,U4,U5,U6,U7,U8,U9,F1,F2,F3,F4,F5,F6,F7,F8,F9,R1,R2,R3,R4,R5,R6,R7,R8,R9,B1,B2,B3,B4,B5,B6,B7,B8,B9,L1,L2,L3,L4,L5,L6,L7,L8,L9,D1,D2,D3,D4,D5,D6,D7,D8,D9,P)
                F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result = U(F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result)
            # L'arrête est descendue.
            U7,U8,U9,R1,R4,R7,L3,L6,L9,D1,D2,D3,F1,F2,F3,F4,F6,F7,F8,F9,memory,memorysens,result = FB(U7,U8,U9,R1,R4,R7,L3,L6,L9,D1,D2,D3,F1,F2,F3,F4,F6,F7,F8,F9,P,memory,memorysens,result)
            U7,U8,U9,R1,R4,R7,L3,L6,L9,D1,D2,D3,F1,F2,F3,F4,F6,F7,F8,F9,memory,memorysens,result = FB(U7,U8,U9,R1,R4,R7,L3,L6,L9,D1,D2,D3,F1,F2,F3,F4,F6,F7,F8,F9,P,memory,memorysens,result)
        elif F6 == D5:
            place = R4      # Mémorisation de la couleur de l'arrête.
            while place != R5:      # Recherche du centre de la couleur de l'arrête et donc de son emplacement.
                U1,U2,U3,U4,U5,U6,U7,U8,U9,F1,F2,F3,F4,F5,F6,F7,F8,F9,R1,R2,R3,R4,R5,R6,R7,R8,R9,B1,B2,B3,B4,B5,B6,B7,B8,B9,L1,L2,L3,L4,L5,L6,L7,L8,L9,D1,D2,D3,D4,D5,D6,D7,D8,D9,P = y(U1,U2,U3,U4,U5,U6,U7,U8,U9,F1,F2,F3,F4,F5,F6,F7,F8,F9,R1,R2,R3,R4,R5,R6,R7,R8,R9,B1,B2,B3,B4,B5,B6,B7,B8,B9,L1,L2,L3,L4,L5,L6,L7,L8,L9,D1,D2,D3,D4,D5,D6,D7,D8,D9,P)
            while (place != R4) | (D5 != F6):   # L'arrête est amenée au-dessus de son emplacement. Cela désaligne temporairement les centres F,R,B et L avec les arrêtes blanches déjà bien placées.
                U1,U2,U3,U4,U5,U6,U7,U8,U9,F1,F2,F3,F4,F5,F6,F7,F8,F9,R1,R2,R3,R4,R5,R6,R7,R8,R9,B1,B2,B3,B4,B5,B6,B7,B8,B9,L1,L2,L3,L4,L5,L6,L7,L8,L9,D1,D2,D3,D4,D5,D6,D7,D8,D9,P = y(U1,U2,U3,U4,U5,U6,U7,U8,U9,F1,F2,F3,F4,F5,F6,F7,F8,F9,R1,R2,R3,R4,R5,R6,R7,R8,R9,B1,B2,B3,B4,B5,B6,B7,B8,B9,L1,L2,L3,L4,L5,L6,L7,L8,L9,D1,D2,D3,D4,D5,D6,D7,D8,D9,P)
                F7,F8,F9,R7,R8,R9,B7,B8,B9,L7,L8,L9,D1,D2,D3,D4,D6,D7,D8,D9,memory,memorysens,result = DI(F7,F8,F9,R7,R8,R9,B7,B8,B9,L7,L8,L9,D1,D2,D3,D4,D6,D7,D8,D9,memory,memorysens,result)
            # L'arrête est descendue.
            U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,memory,memorysens,result = RIB(U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,P,memory,memorysens,result)
            while R8 != R5:     # Les arrêtes sont réalignées avec les centres. 
                U1,U2,U3,U4,U5,U6,U7,U8,U9,F1,F2,F3,F4,F5,F6,F7,F8,F9,R1,R2,R3,R4,R5,R6,R7,R8,R9,B1,B2,B3,B4,B5,B6,B7,B8,B9,L1,L2,L3,L4,L5,L6,L7,L8,L9,D1,D2,D3,D4,D5,D6,D7,D8,D9,P = y(U1,U2,U3,U4,U5,U6,U7,U8,U9,F1,F2,F3,F4,F5,F6,F7,F8,F9,R1,R2,R3,R4,R5,R6,R7,R8,R9,B1,B2,B3,B4,B5,B6,B7,B8,B9,L1,L2,L3,L4,L5,L6,L7,L8,L9,D1,D2,D3,D4,D5,D6,D7,D8,D9,P)
                F7,F8,F9,R7,R8,R9,B7,B8,B9,L7,L8,L9,D1,D2,D3,D4,D6,D7,D8,D9,memory,memorysens,result = DI(F7,F8,F9,R7,R8,R9,B7,B8,B9,L7,L8,L9,D1,D2,D3,D4,D6,D7,D8,D9,memory,memorysens,result)
        elif F4 == D5:
            place = L6  # Mémorisation de la couleur de l'arrête.
            while place != L5:  # Recherche du centre de la couleur de l'arrête et donc de son emplacement.
                U1,U2,U3,U4,U5,U6,U7,U8,U9,F1,F2,F3,F4,F5,F6,F7,F8,F9,R1,R2,R3,R4,R5,R6,R7,R8,R9,B1,B2,B3,B4,B5,B6,B7,B8,B9,L1,L2,L3,L4,L5,L6,L7,L8,L9,D1,D2,D3,D4,D5,D6,D7,D8,D9,P = y(U1,U2,U3,U4,U5,U6,U7,U8,U9,F1,F2,F3,F4,F5,F6,F7,F8,F9,R1,R2,R3,R4,R5,R6,R7,R8,R9,B1,B2,B3,B4,B5,B6,B7,B8,B9,L1,L2,L3,L4,L5,L6,L7,L8,L9,D1,D2,D3,D4,D5,D6,D7,D8,D9,P)
            while (place != L6) | (D5 != F4):   # L'arrête est amenée au-dessus de son emplacement. Cela désaligne temporairement les centres F,R,B et L avec les arrêtes blanches déjà bien placées.
                U1,U2,U3,U4,U5,U6,U7,U8,U9,F1,F2,F3,F4,F5,F6,F7,F8,F9,R1,R2,R3,R4,R5,R6,R7,R8,R9,B1,B2,B3,B4,B5,B6,B7,B8,B9,L1,L2,L3,L4,L5,L6,L7,L8,L9,D1,D2,D3,D4,D5,D6,D7,D8,D9,P = y(U1,U2,U3,U4,U5,U6,U7,U8,U9,F1,F2,F3,F4,F5,F6,F7,F8,F9,R1,R2,R3,R4,R5,R6,R7,R8,R9,B1,B2,B3,B4,B5,B6,B7,B8,B9,L1,L2,L3,L4,L5,L6,L7,L8,L9,D1,D2,D3,D4,D5,D6,D7,D8,D9,P)
                F7,F8,F9,R7,R8,R9,B7,B8,B9,L7,L8,L9,D1,D2,D3,D4,D6,D7,D8,D9,memory,memorysens,result = DI(F7,F8,F9,R7,R8,R9,B7,B8,B9,L7,L8,L9,D1,D2,D3,D4,D6,D7,D8,D9,memory,memorysens,result)
            # L'arrête est descendue.
            U1,U4,U7,F1,F4,F7,D1,D4,D7,B3,B6,B9,L1,L2,L3,L4,L6,L7,L8,L9,memory,memorysens,result = LB(U1,U4,U7,F1,F4,F7,D1,D4,D7,B3,B6,B9,L1,L2,L3,L4,L6,L7,L8,L9,P,memory,memorysens,result)
            while L8 != L5:     # Les arrêtes sont réalignées avec les centres.
                U1,U2,U3,U4,U5,U6,U7,U8,U9,F1,F2,F3,F4,F5,F6,F7,F8,F9,R1,R2,R3,R4,R5,R6,R7,R8,R9,B1,B2,B3,B4,B5,B6,B7,B8,B9,L1,L2,L3,L4,L5,L6,L7,L8,L9,D1,D2,D3,D4,D5,D6,D7,D8,D9,P = y(U1,U2,U3,U4,U5,U6,U7,U8,U9,F1,F2,F3,F4,F5,F6,F7,F8,F9,R1,R2,R3,R4,R5,R6,R7,R8,R9,B1,B2,B3,B4,B5,B6,B7,B8,B9,L1,L2,L3,L4,L5,L6,L7,L8,L9,D1,D2,D3,D4,D5,D6,D7,D8,D9,P)
                F7,F8,F9,R7,R8,R9,B7,B8,B9,L7,L8,L9,D1,D2,D3,D4,D6,D7,D8,D9,memory,memorysens,result = DI(F7,F8,F9,R7,R8,R9,B7,B8,B9,L7,L8,L9,D1,D2,D3,D4,D6,D7,D8,D9,memory,memorysens,result)
        elif F2 == D5:
            while (U8 != R5) & (U8 != L5):  # L'arrête est amenée à côté de son emplacement.
                U1,U2,U3,U4,U5,U6,U7,U8,U9,F1,F2,F3,F4,F5,F6,F7,F8,F9,R1,R2,R3,R4,R5,R6,R7,R8,R9,B1,B2,B3,B4,B5,B6,B7,B8,B9,L1,L2,L3,L4,L5,L6,L7,L8,L9,D1,D2,D3,D4,D5,D6,D7,D8,D9,P = y(U1,U2,U3,U4,U5,U6,U7,U8,U9,F1,F2,F3,F4,F5,F6,F7,F8,F9,R1,R2,R3,R4,R5,R6,R7,R8,R9,B1,B2,B3,B4,B5,B6,B7,B8,B9,L1,L2,L3,L4,L5,L6,L7,L8,L9,D1,D2,D3,D4,D5,D6,D7,D8,D9,P)
                F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result = U(F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result)
            if U8 == R5:
                if (D2 == D5) & (F8 == F5):     # L'arrête est mise à sa place.
                    U7,U8,U9,R1,R4,R7,L3,L6,L9,D1,D2,D3,F1,F2,F3,F4,F6,F7,F8,F9,memory,memorysens,result = FB(U7,U8,U9,R1,R4,R7,L3,L6,L9,D1,D2,D3,F1,F2,F3,F4,F6,F7,F8,F9,P,memory,memorysens,result)
                    U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,memory,memorysens,result = RIB(U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,P,memory,memorysens,result)
                    U7,U8,U9,R1,R4,R7,L3,L6,L9,D1,D2,D3,F1,F2,F3,F4,F6,F7,F8,F9,memory,memorysens,result = FIB(U7,U8,U9,R1,R4,R7,L3,L6,L9,D1,D2,D3,F1,F2,F3,F4,F6,F7,F8,F9,P,memory,memorysens,result)
                else:   # L'arrête est mise à sa place mais un mouvement est economisé car l'arrête déplacée n'est pas à remettre.
                    U7,U8,U9,R1,R4,R7,L3,L6,L9,D1,D2,D3,F1,F2,F3,F4,F6,F7,F8,F9,memory,memorysens,result = FB(U7,U8,U9,R1,R4,R7,L3,L6,L9,D1,D2,D3,F1,F2,F3,F4,F6,F7,F8,F9,P,memory,memorysens,result)
                    U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,memory,memorysens,result = RIB(U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,P,memory,memorysens,result)
            else:
                if (D2 == D5) & (F8 == F5):     # L'arrête est mise à sa place.
                    U7,U8,U9,R1,R4,R7,L3,L6,L9,D1,D2,D3,F1,F2,F3,F4,F6,F7,F8,F9,memory,memorysens,result = FIB(U7,U8,U9,R1,R4,R7,L3,L6,L9,D1,D2,D3,F1,F2,F3,F4,F6,F7,F8,F9,P,memory,memorysens,result)
                    U1,U4,U7,F1,F4,F7,D1,D4,D7,B3,B6,B9,L1,L2,L3,L4,L6,L7,L8,L9,memory,memorysens,result = LB(U1,U4,U7,F1,F4,F7,D1,D4,D7,B3,B6,B9,L1,L2,L3,L4,L6,L7,L8,L9,P,memory,memorysens,result)
                    U7,U8,U9,R1,R4,R7,L3,L6,L9,D1,D2,D3,F1,F2,F3,F4,F6,F7,F8,F9,memory,memorysens,result = FB(U7,U8,U9,R1,R4,R7,L3,L6,L9,D1,D2,D3,F1,F2,F3,F4,F6,F7,F8,F9,P,memory,memorysens,result)
                else:   # L'arrête est mise à sa place mais un mouvement est economisé car l'arrête déplacée n'est pas à remettre.
                    U7,U8,U9,R1,R4,R7,L3,L6,L9,D1,D2,D3,F1,F2,F3,F4,F6,F7,F8,F9,memory,memorysens,result = FIB(U7,U8,U9,R1,R4,R7,L3,L6,L9,D1,D2,D3,F1,F2,F3,F4,F6,F7,F8,F9,P,memory,memorysens,result)
                    U1,U4,U7,F1,F4,F7,D1,D4,D7,B3,B6,B9,L1,L2,L3,L4,L6,L7,L8,L9,memory,memorysens,result = LB(U1,U4,U7,F1,F4,F7,D1,D4,D7,B3,B6,B9,L1,L2,L3,L4,L6,L7,L8,L9,P,memory,memorysens,result)
        elif F8 == D5:
            # L'arrête est placée en position F6.
            U7,U8,U9,R1,R4,R7,L3,L6,L9,D1,D2,D3,F1,F2,F3,F4,F6,F7,F8,F9,memory,memorysens,result = FIB(U7,U8,U9,R1,R4,R7,L3,L6,L9,D1,D2,D3,F1,F2,F3,F4,F6,F7,F8,F9,P,memory,memorysens,result)
            place = R4      # Mémorisation de la couleur de l'arrête.
            while place != R5:      # Recherche du centre de la couleur de l'arrête et donc de son emplacement.
                U1,U2,U3,U4,U5,U6,U7,U8,U9,F1,F2,F3,F4,F5,F6,F7,F8,F9,R1,R2,R3,R4,R5,R6,R7,R8,R9,B1,B2,B3,B4,B5,B6,B7,B8,B9,L1,L2,L3,L4,L5,L6,L7,L8,L9,D1,D2,D3,D4,D5,D6,D7,D8,D9,P = y(U1,U2,U3,U4,U5,U6,U7,U8,U9,F1,F2,F3,F4,F5,F6,F7,F8,F9,R1,R2,R3,R4,R5,R6,R7,R8,R9,B1,B2,B3,B4,B5,B6,B7,B8,B9,L1,L2,L3,L4,L5,L6,L7,L8,L9,D1,D2,D3,D4,D5,D6,D7,D8,D9,P)
            while (place != R4) | (D5 != F6):   # L'arrête est amenée au-dessus de son emplacement. Cela désaligne temporairement les centres F,R,B et L avec les arrêtes blanches déjà bien placées.
                U1,U2,U3,U4,U5,U6,U7,U8,U9,F1,F2,F3,F4,F5,F6,F7,F8,F9,R1,R2,R3,R4,R5,R6,R7,R8,R9,B1,B2,B3,B4,B5,B6,B7,B8,B9,L1,L2,L3,L4,L5,L6,L7,L8,L9,D1,D2,D3,D4,D5,D6,D7,D8,D9,P = y(U1,U2,U3,U4,U5,U6,U7,U8,U9,F1,F2,F3,F4,F5,F6,F7,F8,F9,R1,R2,R3,R4,R5,R6,R7,R8,R9,B1,B2,B3,B4,B5,B6,B7,B8,B9,L1,L2,L3,L4,L5,L6,L7,L8,L9,D1,D2,D3,D4,D5,D6,D7,D8,D9,P)
                F7,F8,F9,R7,R8,R9,B7,B8,B9,L7,L8,L9,D1,D2,D3,D4,D6,D7,D8,D9,memory,memorysens,result = DI(F7,F8,F9,R7,R8,R9,B7,B8,B9,L7,L8,L9,D1,D2,D3,D4,D6,D7,D8,D9,memory,memorysens,result)
            # L'arrête est descendue.
            U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,memory,memorysens,result = RIB(U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,P,memory,memorysens,result)
            while R8 != R5:     # Les arrêtes sont réalignées avec les centres. 
                U1,U2,U3,U4,U5,U6,U7,U8,U9,F1,F2,F3,F4,F5,F6,F7,F8,F9,R1,R2,R3,R4,R5,R6,R7,R8,R9,B1,B2,B3,B4,B5,B6,B7,B8,B9,L1,L2,L3,L4,L5,L6,L7,L8,L9,D1,D2,D3,D4,D5,D6,D7,D8,D9,P = y(U1,U2,U3,U4,U5,U6,U7,U8,U9,F1,F2,F3,F4,F5,F6,F7,F8,F9,R1,R2,R3,R4,R5,R6,R7,R8,R9,B1,B2,B3,B4,B5,B6,B7,B8,B9,L1,L2,L3,L4,L5,L6,L7,L8,L9,D1,D2,D3,D4,D5,D6,D7,D8,D9,P)
                F7,F8,F9,R7,R8,R9,B7,B8,B9,L7,L8,L9,D1,D2,D3,D4,D6,D7,D8,D9,memory,memorysens,result = DI(F7,F8,F9,R7,R8,R9,B7,B8,B9,L7,L8,L9,D1,D2,D3,D4,D6,D7,D8,D9,memory,memorysens,result)
        # Aucune arrête blanche n'est trouvable sur cette partie du cube, le cube est donc tourné.
        U1,U2,U3,U4,U5,U6,U7,U8,U9,F1,F2,F3,F4,F5,F6,F7,F8,F9,R1,R2,R3,R4,R5,R6,R7,R8,R9,B1,B2,B3,B4,B5,B6,B7,B8,B9,L1,L2,L3,L4,L5,L6,L7,L8,L9,D1,D2,D3,D4,D5,D6,D7,D8,D9,P = y(U1,U2,U3,U4,U5,U6,U7,U8,U9,F1,F2,F3,F4,F5,F6,F7,F8,F9,R1,R2,R3,R4,R5,R6,R7,R8,R9,B1,B2,B3,B4,B5,B6,B7,B8,B9,L1,L2,L3,L4,L5,L6,L7,L8,L9,D1,D2,D3,D4,D5,D6,D7,D8,D9,P)


    while (D1 != D5) | (D3 != D5) | (D7 != D5) | (D9 != D5) | (F9 != F5) | (R9 != R5) | (B9 != B5) | (L9 != L5):
        while(U9 == D5) | (R1 == D5) | (F3 == D5) | (F9 == D5) | (R7 == D5) | ((D3 == D5) & (F9 != F5)):
            if U9 == D5:
                while F3 != R5:
                    U1,U2,U3,U4,U5,U6,U7,U8,U9,F1,F2,F3,F4,F5,F6,F7,F8,F9,R1,R2,R3,R4,R5,R6,R7,R8,R9,B1,B2,B3,B4,B5,B6,B7,B8,B9,L1,L2,L3,L4,L5,L6,L7,L8,L9,D1,D2,D3,D4,D5,D6,D7,D8,D9,P = y(U1,U2,U3,U4,U5,U6,U7,U8,U9,F1,F2,F3,F4,F5,F6,F7,F8,F9,R1,R2,R3,R4,R5,R6,R7,R8,R9,B1,B2,B3,B4,B5,B6,B7,B8,B9,L1,L2,L3,L4,L5,L6,L7,L8,L9,D1,D2,D3,D4,D5,D6,D7,D8,D9,P)
                    F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result = U(F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result)
                U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,memory,memorysens,result = RB(U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,P,memory,memorysens,result)
                F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result = U(F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result)
                F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result = U(F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result)
                U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,memory,memorysens,result = RIB(U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,P,memory,memorysens,result)
                F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result = UI(F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result)
                U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,memory,memorysens,result = RB(U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,P,memory,memorysens,result)
                F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result = U(F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result)
                U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,memory,memorysens,result = RIB(U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,P,memory,memorysens,result)
            if R1 == D5:
                while U9 != R5:
                    U1,U2,U3,U4,U5,U6,U7,U8,U9,F1,F2,F3,F4,F5,F6,F7,F8,F9,R1,R2,R3,R4,R5,R6,R7,R8,R9,B1,B2,B3,B4,B5,B6,B7,B8,B9,L1,L2,L3,L4,L5,L6,L7,L8,L9,D1,D2,D3,D4,D5,D6,D7,D8,D9,P = y(U1,U2,U3,U4,U5,U6,U7,U8,U9,F1,F2,F3,F4,F5,F6,F7,F8,F9,R1,R2,R3,R4,R5,R6,R7,R8,R9,B1,B2,B3,B4,B5,B6,B7,B8,B9,L1,L2,L3,L4,L5,L6,L7,L8,L9,D1,D2,D3,D4,D5,D6,D7,D8,D9,P)
                    F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result = U(F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result)
                U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,memory,memorysens,result = RB(U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,P,memory,memorysens,result)
                F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result = U(F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result)
                U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,memory,memorysens,result = RIB(U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,P,memory,memorysens,result)
            if F3 == D5:
                while R1 != B5:
                    U1,U2,U3,U4,U5,U6,U7,U8,U9,F1,F2,F3,F4,F5,F6,F7,F8,F9,R1,R2,R3,R4,R5,R6,R7,R8,R9,B1,B2,B3,B4,B5,B6,B7,B8,B9,L1,L2,L3,L4,L5,L6,L7,L8,L9,D1,D2,D3,D4,D5,D6,D7,D8,D9,P = y(U1,U2,U3,U4,U5,U6,U7,U8,U9,F1,F2,F3,F4,F5,F6,F7,F8,F9,R1,R2,R3,R4,R5,R6,R7,R8,R9,B1,B2,B3,B4,B5,B6,B7,B8,B9,L1,L2,L3,L4,L5,L6,L7,L8,L9,D1,D2,D3,D4,D5,D6,D7,D8,D9,P)
                    F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result = U(F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result)
                U1,U2,U3,R3,R6,R9,L1,L4,L7,D7,D8,D9,B1,B2,B3,B4,B6,B7,B8,B9,memory,memorysens,result = BB(U1,U2,U3,R3,R6,R9,L1,L4,L7,D7,D8,D9,B1,B2,B3,B4,B6,B7,B8,B9,P,memory,memorysens,result)
                F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result = UI(F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result)
                U1,U2,U3,R3,R6,R9,L1,L4,L7,D7,D8,D9,B1,B2,B3,B4,B6,B7,B8,B9,memory,memorysens,result = BIB(U1,U2,U3,R3,R6,R9,L1,L4,L7,D7,D8,D9,B1,B2,B3,B4,B6,B7,B8,B9,P,memory,memorysens,result)
            if F9 == D5:
                U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,memory,memorysens,result = RB(U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,P,memory,memorysens,result)
                F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result = UI(F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result)
                U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,memory,memorysens,result = RIB(U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,P,memory,memorysens,result)
                while R1 != B5:
                    U1,U2,U3,U4,U5,U6,U7,U8,U9,F1,F2,F3,F4,F5,F6,F7,F8,F9,R1,R2,R3,R4,R5,R6,R7,R8,R9,B1,B2,B3,B4,B5,B6,B7,B8,B9,L1,L2,L3,L4,L5,L6,L7,L8,L9,D1,D2,D3,D4,D5,D6,D7,D8,D9,P = y(U1,U2,U3,U4,U5,U6,U7,U8,U9,F1,F2,F3,F4,F5,F6,F7,F8,F9,R1,R2,R3,R4,R5,R6,R7,R8,R9,B1,B2,B3,B4,B5,B6,B7,B8,B9,L1,L2,L3,L4,L5,L6,L7,L8,L9,D1,D2,D3,D4,D5,D6,D7,D8,D9,P)
                    F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result = U(F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result)
                U1,U2,U3,R3,R6,R9,L1,L4,L7,D7,D8,D9,B1,B2,B3,B4,B6,B7,B8,B9,memory,memorysens,result = BB(U1,U2,U3,R3,R6,R9,L1,L4,L7,D7,D8,D9,B1,B2,B3,B4,B6,B7,B8,B9,P,memory,memorysens,result)
                F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result = UI(F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result)
                U1,U2,U3,R3,R6,R9,L1,L4,L7,D7,D8,D9,B1,B2,B3,B4,B6,B7,B8,B9,memory,memorysens,result = BIB(U1,U2,U3,R3,R6,R9,L1,L4,L7,D7,D8,D9,B1,B2,B3,B4,B6,B7,B8,B9,P,memory,memorysens,result)
            if R7 == D5:
                U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,memory,memorysens,result = RB(U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,P,memory,memorysens,result)
                F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result = U(F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result)
                U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,memory,memorysens,result = RIB(U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,P,memory,memorysens,result)
                U1,U2,U3,U4,U5,U6,U7,U8,U9,F1,F2,F3,F4,F5,F6,F7,F8,F9,R1,R2,R3,R4,R5,R6,R7,R8,R9,B1,B2,B3,B4,B5,B6,B7,B8,B9,L1,L2,L3,L4,L5,L6,L7,L8,L9,D1,D2,D3,D4,D5,D6,D7,D8,D9,P = y(U1,U2,U3,U4,U5,U6,U7,U8,U9,F1,F2,F3,F4,F5,F6,F7,F8,F9,R1,R2,R3,R4,R5,R6,R7,R8,R9,B1,B2,B3,B4,B5,B6,B7,B8,B9,L1,L2,L3,L4,L5,L6,L7,L8,L9,D1,D2,D3,D4,D5,D6,D7,D8,D9,P)
                while U9 != R5:
                    U1,U2,U3,U4,U5,U6,U7,U8,U9,F1,F2,F3,F4,F5,F6,F7,F8,F9,R1,R2,R3,R4,R5,R6,R7,R8,R9,B1,B2,B3,B4,B5,B6,B7,B8,B9,L1,L2,L3,L4,L5,L6,L7,L8,L9,D1,D2,D3,D4,D5,D6,D7,D8,D9,P = y(U1,U2,U3,U4,U5,U6,U7,U8,U9,F1,F2,F3,F4,F5,F6,F7,F8,F9,R1,R2,R3,R4,R5,R6,R7,R8,R9,B1,B2,B3,B4,B5,B6,B7,B8,B9,L1,L2,L3,L4,L5,L6,L7,L8,L9,D1,D2,D3,D4,D5,D6,D7,D8,D9,P)
                    F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result = U(F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result)
                U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,memory,memorysens,result = RB(U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,P,memory,memorysens,result)
                F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result = U(F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result)
                U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,memory,memorysens,result = RIB(U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,P,memory,memorysens,result)
            if D3 == D5:
                if F9 != F5:
                    U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,memory,memorysens,result = RB(U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,P,memory,memorysens,result)
                    F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result = U(F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result)
                    U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,memory,memorysens,result = RIB(U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,P,memory,memorysens,result)
                    while U7 != F5:
                        U1,U2,U3,U4,U5,U6,U7,U8,U9,F1,F2,F3,F4,F5,F6,F7,F8,F9,R1,R2,R3,R4,R5,R6,R7,R8,R9,B1,B2,B3,B4,B5,B6,B7,B8,B9,L1,L2,L3,L4,L5,L6,L7,L8,L9,D1,D2,D3,D4,D5,D6,D7,D8,D9,P = y(U1,U2,U3,U4,U5,U6,U7,U8,U9,F1,F2,F3,F4,F5,F6,F7,F8,F9,R1,R2,R3,R4,R5,R6,R7,R8,R9,B1,B2,B3,B4,B5,B6,B7,B8,B9,L1,L2,L3,L4,L5,L6,L7,L8,L9,D1,D2,D3,D4,D5,D6,D7,D8,D9,P)
                        F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result = U(F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result)
                    U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,memory,memorysens,result = RB(U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,P,memory,memorysens,result)
                    F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result = UI(F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result)
                    U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,memory,memorysens,result = RIB(U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,P,memory,memorysens,result)
        U1,U2,U3,U4,U5,U6,U7,U8,U9,F1,F2,F3,F4,F5,F6,F7,F8,F9,R1,R2,R3,R4,R5,R6,R7,R8,R9,B1,B2,B3,B4,B5,B6,B7,B8,B9,L1,L2,L3,L4,L5,L6,L7,L8,L9,D1,D2,D3,D4,D5,D6,D7,D8,D9,P = y(U1,U2,U3,U4,U5,U6,U7,U8,U9,F1,F2,F3,F4,F5,F6,F7,F8,F9,R1,R2,R3,R4,R5,R6,R7,R8,R9,B1,B2,B3,B4,B5,B6,B7,B8,B9,L1,L2,L3,L4,L5,L6,L7,L8,L9,D1,D2,D3,D4,D5,D6,D7,D8,D9,P)


    while (F4 != F5) | (F6 != F5) | (R4 != R5) | (R6 != R5) | (B4 != B5) | (B6 != B5) | (L4 != L5) | (L6 != L5):
        
        while ((U8 != U5) & (F2 != U5)) | ((U6 != U5) & (R2 != U5)) | ((U2 != U5) & (B2 != U5)) | ((U4 != U5) & (L2 != U5)):
            if (U8 != U5) & (F2 != U5):
                while F2 != F5:
                    U1,U2,U3,U4,U5,U6,U7,U8,U9,F1,F2,F3,F4,F5,F6,F7,F8,F9,R1,R2,R3,R4,R5,R6,R7,R8,R9,B1,B2,B3,B4,B5,B6,B7,B8,B9,L1,L2,L3,L4,L5,L6,L7,L8,L9,D1,D2,D3,D4,D5,D6,D7,D8,D9,P = y(U1,U2,U3,U4,U5,U6,U7,U8,U9,F1,F2,F3,F4,F5,F6,F7,F8,F9,R1,R2,R3,R4,R5,R6,R7,R8,R9,B1,B2,B3,B4,B5,B6,B7,B8,B9,L1,L2,L3,L4,L5,L6,L7,L8,L9,D1,D2,D3,D4,D5,D6,D7,D8,D9,P)
                    F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result = U(F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result)
                if U8 == R5:
                    F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result = U(F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result)
                    U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,memory,memorysens,result = RB(U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,P,memory,memorysens,result)
                    F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result = UI(F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result)
                    U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,memory,memorysens,result = RIB(U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,P,memory,memorysens,result)
                    F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result = UI(F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result)
                    U7,U8,U9,R1,R4,R7,L3,L6,L9,D1,D2,D3,F1,F2,F3,F4,F6,F7,F8,F9,memory,memorysens,result = FIB(U7,U8,U9,R1,R4,R7,L3,L6,L9,D1,D2,D3,F1,F2,F3,F4,F6,F7,F8,F9,P,memory,memorysens,result)
                    F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result = U(F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result)
                    U7,U8,U9,R1,R4,R7,L3,L6,L9,D1,D2,D3,F1,F2,F3,F4,F6,F7,F8,F9,memory,memorysens,result = FB(U7,U8,U9,R1,R4,R7,L3,L6,L9,D1,D2,D3,F1,F2,F3,F4,F6,F7,F8,F9,P,memory,memorysens,result)
                elif U8 == L5:
                    F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result = UI(F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result)
                    U1,U4,U7,F1,F4,F7,D1,D4,D7,B3,B6,B9,L1,L2,L3,L4,L6,L7,L8,L9,memory,memorysens,result = LIB(U1,U4,U7,F1,F4,F7,D1,D4,D7,B3,B6,B9,L1,L2,L3,L4,L6,L7,L8,L9,P,memory,memorysens,result)
                    F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result = U(F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result)
                    U1,U4,U7,F1,F4,F7,D1,D4,D7,B3,B6,B9,L1,L2,L3,L4,L6,L7,L8,L9,memory,memorysens,result = LB(U1,U4,U7,F1,F4,F7,D1,D4,D7,B3,B6,B9,L1,L2,L3,L4,L6,L7,L8,L9,P,memory,memorysens,result)
                    F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result = U(F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result)
                    U7,U8,U9,R1,R4,R7,L3,L6,L9,D1,D2,D3,F1,F2,F3,F4,F6,F7,F8,F9,memory,memorysens,result = FB(U7,U8,U9,R1,R4,R7,L3,L6,L9,D1,D2,D3,F1,F2,F3,F4,F6,F7,F8,F9,P,memory,memorysens,result)
                    F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result = UI(F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result)
                    U7,U8,U9,R1,R4,R7,L3,L6,L9,D1,D2,D3,F1,F2,F3,F4,F6,F7,F8,F9,memory,memorysens,result = FIB(U7,U8,U9,R1,R4,R7,L3,L6,L9,D1,D2,D3,F1,F2,F3,F4,F6,F7,F8,F9,P,memory,memorysens,result)
            U1,U2,U3,U4,U5,U6,U7,U8,U9,F1,F2,F3,F4,F5,F6,F7,F8,F9,R1,R2,R3,R4,R5,R6,R7,R8,R9,B1,B2,B3,B4,B5,B6,B7,B8,B9,L1,L2,L3,L4,L5,L6,L7,L8,L9,D1,D2,D3,D4,D5,D6,D7,D8,D9,P = y(U1,U2,U3,U4,U5,U6,U7,U8,U9,F1,F2,F3,F4,F5,F6,F7,F8,F9,R1,R2,R3,R4,R5,R6,R7,R8,R9,B1,B2,B3,B4,B5,B6,B7,B8,B9,L1,L2,L3,L4,L5,L6,L7,L8,L9,D1,D2,D3,D4,D5,D6,D7,D8,D9,P)
        if (F4 != F5) | (F6 != F5) | (R4 != R5) | (R6 != R5) | (B4 != B5) | (B6 != B5) | (L4 != L5) | (L6 != L5):
            while ((F6 == F5) & (R4 == R5)) | (F6 == U5) | (R4 == U5):
                U1,U2,U3,U4,U5,U6,U7,U8,U9,F1,F2,F3,F4,F5,F6,F7,F8,F9,R1,R2,R3,R4,R5,R6,R7,R8,R9,B1,B2,B3,B4,B5,B6,B7,B8,B9,L1,L2,L3,L4,L5,L6,L7,L8,L9,D1,D2,D3,D4,D5,D6,D7,D8,D9,P = y(U1,U2,U3,U4,U5,U6,U7,U8,U9,F1,F2,F3,F4,F5,F6,F7,F8,F9,R1,R2,R3,R4,R5,R6,R7,R8,R9,B1,B2,B3,B4,B5,B6,B7,B8,B9,L1,L2,L3,L4,L5,L6,L7,L8,L9,D1,D2,D3,D4,D5,D6,D7,D8,D9,P)
            U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,memory,memorysens,result = RB(U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,P,memory,memorysens,result)
            F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result = UI(F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result)
            U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,memory,memorysens,result = RIB(U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,P,memory,memorysens,result)
            F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result = UI(F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result)
            U7,U8,U9,R1,R4,R7,L3,L6,L9,D1,D2,D3,F1,F2,F3,F4,F6,F7,F8,F9,memory,memorysens,result = FIB(U7,U8,U9,R1,R4,R7,L3,L6,L9,D1,D2,D3,F1,F2,F3,F4,F6,F7,F8,F9,P,memory,memorysens,result)
            F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result = U(F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result)
            U7,U8,U9,R1,R4,R7,L3,L6,L9,D1,D2,D3,F1,F2,F3,F4,F6,F7,F8,F9,memory,memorysens,result = FB(U7,U8,U9,R1,R4,R7,L3,L6,L9,D1,D2,D3,F1,F2,F3,F4,F6,F7,F8,F9,P,memory,memorysens,result)


    while (U2 != U5) | (U4 != U5) | (U6 != U5) | (U8 != U5):
        if (U4 == U5) & (U6 == U5):
            U7,U8,U9,R1,R4,R7,L3,L6,L9,D1,D2,D3,F1,F2,F3,F4,F6,F7,F8,F9,memory,memorysens,result = FB(U7,U8,U9,R1,R4,R7,L3,L6,L9,D1,D2,D3,F1,F2,F3,F4,F6,F7,F8,F9,P,memory,memorysens,result)
            U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,memory,memorysens,result = RB(U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,P,memory,memorysens,result)
            F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result = U(F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result)
            U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,memory,memorysens,result = RIB(U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,P,memory,memorysens,result)
            F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result = UI(F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result)
            U7,U8,U9,R1,R4,R7,L3,L6,L9,D1,D2,D3,F1,F2,F3,F4,F6,F7,F8,F9,memory,memorysens,result = FIB(U7,U8,U9,R1,R4,R7,L3,L6,L9,D1,D2,D3,F1,F2,F3,F4,F6,F7,F8,F9,P,memory,memorysens,result)
        elif (U2 == U5) & (U4 == U5):
            U7,U8,U9,R1,R4,R7,L3,L6,L9,D1,D2,D3,F1,F2,F3,F4,F6,F7,F8,F9,memory,memorysens,result = FB(U7,U8,U9,R1,R4,R7,L3,L6,L9,D1,D2,D3,F1,F2,F3,F4,F6,F7,F8,F9,P,memory,memorysens,result)
            F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result = U(F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result)
            U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,memory,memorysens,result = RB(U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,P,memory,memorysens,result)
            F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result = UI(F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result)
            U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,memory,memorysens,result = RIB(U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,P,memory,memorysens,result)
            U7,U8,U9,R1,R4,R7,L3,L6,L9,D1,D2,D3,F1,F2,F3,F4,F6,F7,F8,F9,memory,memorysens,result = FIB(U7,U8,U9,R1,R4,R7,L3,L6,L9,D1,D2,D3,F1,F2,F3,F4,F6,F7,F8,F9,P,memory,memorysens,result)
        elif (U2 != U5) & (U4 != U5) & (U6 != U5) & (U8 != U5):
            U7,U8,U9,R1,R4,R7,L3,L6,L9,D1,D2,D3,F1,F2,F3,F4,F6,F7,F8,F9,memory,memorysens,result = FB(U7,U8,U9,R1,R4,R7,L3,L6,L9,D1,D2,D3,F1,F2,F3,F4,F6,F7,F8,F9,P,memory,memorysens,result)
            U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,memory,memorysens,result = RB(U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,P,memory,memorysens,result)
            F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result = U(F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result)
            U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,memory,memorysens,result = RIB(U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,P,memory,memorysens,result)
            F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result = UI(F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result)
            U7,U8,U9,R1,R4,R7,L3,L6,L9,D1,D2,D3,F1,F2,F3,F4,F6,F7,F8,F9,memory,memorysens,result = FIB(U7,U8,U9,R1,R4,R7,L3,L6,L9,D1,D2,D3,F1,F2,F3,F4,F6,F7,F8,F9,P,memory,memorysens,result)
            U1,U2,U3,U4,U5,U6,U7,U8,U9,F1,F2,F3,F4,F5,F6,F7,F8,F9,R1,R2,R3,R4,R5,R6,R7,R8,R9,B1,B2,B3,B4,B5,B6,B7,B8,B9,L1,L2,L3,L4,L5,L6,L7,L8,L9,D1,D2,D3,D4,D5,D6,D7,D8,D9,P = y(U1,U2,U3,U4,U5,U6,U7,U8,U9,F1,F2,F3,F4,F5,F6,F7,F8,F9,R1,R2,R3,R4,R5,R6,R7,R8,R9,B1,B2,B3,B4,B5,B6,B7,B8,B9,L1,L2,L3,L4,L5,L6,L7,L8,L9,D1,D2,D3,D4,D5,D6,D7,D8,D9,P)
            U1,U2,U3,U4,U5,U6,U7,U8,U9,F1,F2,F3,F4,F5,F6,F7,F8,F9,R1,R2,R3,R4,R5,R6,R7,R8,R9,B1,B2,B3,B4,B5,B6,B7,B8,B9,L1,L2,L3,L4,L5,L6,L7,L8,L9,D1,D2,D3,D4,D5,D6,D7,D8,D9,P = y(U1,U2,U3,U4,U5,U6,U7,U8,U9,F1,F2,F3,F4,F5,F6,F7,F8,F9,R1,R2,R3,R4,R5,R6,R7,R8,R9,B1,B2,B3,B4,B5,B6,B7,B8,B9,L1,L2,L3,L4,L5,L6,L7,L8,L9,D1,D2,D3,D4,D5,D6,D7,D8,D9,P)
            U7,U8,U9,R1,R4,R7,L3,L6,L9,D1,D2,D3,F1,F2,F3,F4,F6,F7,F8,F9,memory,memorysens,result = FB(U7,U8,U9,R1,R4,R7,L3,L6,L9,D1,D2,D3,F1,F2,F3,F4,F6,F7,F8,F9,P,memory,memorysens,result)
            F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result = U(F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result)
            U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,memory,memorysens,result = RB(U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,P,memory,memorysens,result)
            F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result = UI(F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result)
            U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,memory,memorysens,result = RIB(U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,P,memory,memorysens,result)
            U7,U8,U9,R1,R4,R7,L3,L6,L9,D1,D2,D3,F1,F2,F3,F4,F6,F7,F8,F9,memory,memorysens,result = FIB(U7,U8,U9,R1,R4,R7,L3,L6,L9,D1,D2,D3,F1,F2,F3,F4,F6,F7,F8,F9,P,memory,memorysens,result)
        else:
            U1,U2,U3,U4,U5,U6,U7,U8,U9,F1,F2,F3,F4,F5,F6,F7,F8,F9,R1,R2,R3,R4,R5,R6,R7,R8,R9,B1,B2,B3,B4,B5,B6,B7,B8,B9,L1,L2,L3,L4,L5,L6,L7,L8,L9,D1,D2,D3,D4,D5,D6,D7,D8,D9,P = y(U1,U2,U3,U4,U5,U6,U7,U8,U9,F1,F2,F3,F4,F5,F6,F7,F8,F9,R1,R2,R3,R4,R5,R6,R7,R8,R9,B1,B2,B3,B4,B5,B6,B7,B8,B9,L1,L2,L3,L4,L5,L6,L7,L8,L9,D1,D2,D3,D4,D5,D6,D7,D8,D9,P)


    while (U1 != U5) | (U3 != U5) | (U7 != U5) | (U9 != U5):
        if (F3 == U5) & (R3 == U5) & (B3 == U5) & (U7 == U5):
            U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,memory,memorysens,result = RB(U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,P,memory,memorysens,result)
            F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result = U(F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result)
            U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,memory,memorysens,result = RIB(U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,P,memory,memorysens,result)
            F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result = U(F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result)
            U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,memory,memorysens,result = RB(U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,P,memory,memorysens,result)
            F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result = U(F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result)
            F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result = U(F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result)
            U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,memory,memorysens,result = RIB(U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,P,memory,memorysens,result)
        elif (R1 == U5) & (F1 == U5) & (L1 == U5) & (U3 == U5):
            U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,memory,memorysens,result = RB(U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,P,memory,memorysens,result)
            F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result = U(F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result)
            F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result = U(F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result)
            U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,memory,memorysens,result = RIB(U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,P,memory,memorysens,result)
            F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result = UI(F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result)
            U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,memory,memorysens,result = RB(U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,P,memory,memorysens,result)
            F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result = UI(F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result)
            U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,memory,memorysens,result = RIB(U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,P,memory,memorysens,result)
        elif (F1 == U5) & (F3 == U5) & (B1 == U5) & (B3 == U5):
            U7,U8,U9,R1,R4,R7,L3,L6,L9,D1,D2,D3,F1,F2,F3,F4,F6,F7,F8,F9,memory,memorysens,result = FB(U7,U8,U9,R1,R4,R7,L3,L6,L9,D1,D2,D3,F1,F2,F3,F4,F6,F7,F8,F9,P,memory,memorysens,result)
            U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,memory,memorysens,result = RB(U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,P,memory,memorysens,result)
            F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result = U(F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result)
            U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,memory,memorysens,result = RIB(U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,P,memory,memorysens,result)
            F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result = UI(F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result)
            U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,memory,memorysens,result = RB(U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,P,memory,memorysens,result)
            F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result = U(F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result)
            U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,memory,memorysens,result = RIB(U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,P,memory,memorysens,result)
            F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result = UI(F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result)
            U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,memory,memorysens,result = RB(U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,P,memory,memorysens,result)
            F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result = U(F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result)
            U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,memory,memorysens,result = RIB(U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,P,memory,memorysens,result)
            F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result = UI(F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result)
            U7,U8,U9,R1,R4,R7,L3,L6,L9,D1,D2,D3,F1,F2,F3,F4,F6,F7,F8,F9,memory,memorysens,result = FIB(U7,U8,U9,R1,R4,R7,L3,L6,L9,D1,D2,D3,F1,F2,F3,F4,F6,F7,F8,F9,P,memory,memorysens,result)
        elif (F3 == U5) & (L3 == U5) & (L1 == U5) & (B1 == U5):
            U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,memory,memorysens,result = RB(U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,P,memory,memorysens,result)
            F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result = U(F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result)
            F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result = U(F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result)
            U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,memory,memorysens,result = RB(U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,P,memory,memorysens,result)
            U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,memory,memorysens,result = RB(U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,P,memory,memorysens,result)
            F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result = UI(F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result)
            U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,memory,memorysens,result = RB(U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,P,memory,memorysens,result)
            U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,memory,memorysens,result = RB(U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,P,memory,memorysens,result)
            F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result = UI(F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result)
            U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,memory,memorysens,result = RB(U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,P,memory,memorysens,result)
            U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,memory,memorysens,result = RB(U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,P,memory,memorysens,result)
            F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result = U(F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result)
            F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result = U(F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result)
            U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,memory,memorysens,result = RB(U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,P,memory,memorysens,result)
        elif (L3 == U5) & (R1 == U5) & (U1 == U5) & (U3 == U5):
            U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,memory,memorysens,result = RB(U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,P,memory,memorysens,result)
            U1,U2,U3,R3,R6,R9,L1,L4,L7,D7,D8,D9,B1,B2,B3,B4,B6,B7,B8,B9,memory,memorysens,result = BB(U1,U2,U3,R3,R6,R9,L1,L4,L7,D7,D8,D9,B1,B2,B3,B4,B6,B7,B8,B9,P,memory,memorysens,result)
            U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,memory,memorysens,result = RIB(U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,P,memory,memorysens,result)
            U7,U8,U9,R1,R4,R7,L3,L6,L9,D1,D2,D3,F1,F2,F3,F4,F6,F7,F8,F9,memory,memorysens,result = FB(U7,U8,U9,R1,R4,R7,L3,L6,L9,D1,D2,D3,F1,F2,F3,F4,F6,F7,F8,F9,P,memory,memorysens,result)
            U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,memory,memorysens,result = RB(U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,P,memory,memorysens,result)
            U1,U2,U3,R3,R6,R9,L1,L4,L7,D7,D8,D9,B1,B2,B3,B4,B6,B7,B8,B9,memory,memorysens,result = BIB(U1,U2,U3,R3,R6,R9,L1,L4,L7,D7,D8,D9,B1,B2,B3,B4,B6,B7,B8,B9,P,memory,memorysens,result)
            U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,memory,memorysens,result = RIB(U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,P,memory,memorysens,result)
            U7,U8,U9,R1,R4,R7,L3,L6,L9,D1,D2,D3,F1,F2,F3,F4,F6,F7,F8,F9,memory,memorysens,result = FIB(U7,U8,U9,R1,R4,R7,L3,L6,L9,D1,D2,D3,F1,F2,F3,F4,F6,F7,F8,F9,P,memory,memorysens,result)
        elif (R1 == U5) & (B3 == U5) & (U3 == U5) & (U7 == U5):
            U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,memory,memorysens,result = RB(U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,P,memory,memorysens,result)
            U1,U2,U3,R3,R6,R9,L1,L4,L7,D7,D8,D9,B1,B2,B3,B4,B6,B7,B8,B9,memory,memorysens,result = BIB(U1,U2,U3,R3,R6,R9,L1,L4,L7,D7,D8,D9,B1,B2,B3,B4,B6,B7,B8,B9,P,memory,memorysens,result)
            U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,memory,memorysens,result = RIB(U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,P,memory,memorysens,result)
            U7,U8,U9,R1,R4,R7,L3,L6,L9,D1,D2,D3,F1,F2,F3,F4,F6,F7,F8,F9,memory,memorysens,result = FB(U7,U8,U9,R1,R4,R7,L3,L6,L9,D1,D2,D3,F1,F2,F3,F4,F6,F7,F8,F9,P,memory,memorysens,result)
            U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,memory,memorysens,result = RB(U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,P,memory,memorysens,result)
            U1,U2,U3,R3,R6,R9,L1,L4,L7,D7,D8,D9,B1,B2,B3,B4,B6,B7,B8,B9,memory,memorysens,result = BB(U1,U2,U3,R3,R6,R9,L1,L4,L7,D7,D8,D9,B1,B2,B3,B4,B6,B7,B8,B9,P,memory,memorysens,result)
            U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,memory,memorysens,result = RIB(U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,P,memory,memorysens,result)
            U7,U8,U9,R1,R4,R7,L3,L6,L9,D1,D2,D3,F1,F2,F3,F4,F6,F7,F8,F9,memory,memorysens,result = FIB(U7,U8,U9,R1,R4,R7,L3,L6,L9,D1,D2,D3,F1,F2,F3,F4,F6,F7,F8,F9,P,memory,memorysens,result)
        elif (F1 == U5) & (F3 == U5) & (U1 == U5) & (U3 == U5):
            U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,memory,memorysens,result = RB(U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,P,memory,memorysens,result)
            U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,memory,memorysens,result = RB(U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,P,memory,memorysens,result)
            F7,F8,F9,R7,R8,R9,B7,B8,B9,L7,L8,L9,D1,D2,D3,D4,D6,D7,D8,D9,memory,memorysens,result = D(F7,F8,F9,R7,R8,R9,B7,B8,B9,L7,L8,L9,D1,D2,D3,D4,D6,D7,D8,D9,memory,memorysens,result)
            U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,memory,memorysens,result = RIB(U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,P,memory,memorysens,result)
            F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result = U(F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result)
            F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result = U(F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result)
            U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,memory,memorysens,result = RB(U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,P,memory,memorysens,result)
            F7,F8,F9,R7,R8,R9,B7,B8,B9,L7,L8,L9,D1,D2,D3,D4,D6,D7,D8,D9,memory,memorysens,result = DI(F7,F8,F9,R7,R8,R9,B7,B8,B9,L7,L8,L9,D1,D2,D3,D4,D6,D7,D8,D9,memory,memorysens,result)
            U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,memory,memorysens,result = RIB(U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,P,memory,memorysens,result)
            F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result = U(F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result)
            F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result = U(F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result)
            U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,memory,memorysens,result = RIB(U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,P,memory,memorysens,result)
        else:
            U1,U2,U3,U4,U5,U6,U7,U8,U9,F1,F2,F3,F4,F5,F6,F7,F8,F9,R1,R2,R3,R4,R5,R6,R7,R8,R9,B1,B2,B3,B4,B5,B6,B7,B8,B9,L1,L2,L3,L4,L5,L6,L7,L8,L9,D1,D2,D3,D4,D5,D6,D7,D8,D9,P = y(U1,U2,U3,U4,U5,U6,U7,U8,U9,F1,F2,F3,F4,F5,F6,F7,F8,F9,R1,R2,R3,R4,R5,R6,R7,R8,R9,B1,B2,B3,B4,B5,B6,B7,B8,B9,L1,L2,L3,L4,L5,L6,L7,L8,L9,D1,D2,D3,D4,D5,D6,D7,D8,D9,P)


    while (F2 != F5) | (R2 != R5) | (B2 != B5) | (L2 != L5):
        for i in range(4):
            if (B2 == B5) & (R2 == L5) & (F2 == R5) & (L2 == F5):
                U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,memory,memorysens,result = RB(U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,P,memory,memorysens,result)
                F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result = UI(F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result)
                U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,memory,memorysens,result = RB(U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,P,memory,memorysens,result)
                F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result = U(F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result)
                U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,memory,memorysens,result = RB(U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,P,memory,memorysens,result)
                F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result = U(F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result)
                U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,memory,memorysens,result = RB(U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,P,memory,memorysens,result)
                F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result = UI(F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result)
                U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,memory,memorysens,result = RIB(U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,P,memory,memorysens,result)
                F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result = UI(F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result)
                U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,memory,memorysens,result = RB(U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,P,memory,memorysens,result)
                U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,memory,memorysens,result = RB(U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,P,memory,memorysens,result)
            elif (B2 == B5) & (R2 == F5) & (F2 == L5) & (L2 == R5):
                U1,U4,U7,F1,F4,F7,D1,D4,D7,B3,B6,B9,L1,L2,L3,L4,L6,L7,L8,L9,memory,memorysens,result = LIB(U1,U4,U7,F1,F4,F7,D1,D4,D7,B3,B6,B9,L1,L2,L3,L4,L6,L7,L8,L9,P,memory,memorysens,result)
                F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result = U(F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result)
                U1,U4,U7,F1,F4,F7,D1,D4,D7,B3,B6,B9,L1,L2,L3,L4,L6,L7,L8,L9,memory,memorysens,result = LIB(U1,U4,U7,F1,F4,F7,D1,D4,D7,B3,B6,B9,L1,L2,L3,L4,L6,L7,L8,L9,P,memory,memorysens,result)
                F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result = UI(F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result)
                U1,U4,U7,F1,F4,F7,D1,D4,D7,B3,B6,B9,L1,L2,L3,L4,L6,L7,L8,L9,memory,memorysens,result = LIB(U1,U4,U7,F1,F4,F7,D1,D4,D7,B3,B6,B9,L1,L2,L3,L4,L6,L7,L8,L9,P,memory,memorysens,result)
                F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result = UI(F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result)
                U1,U4,U7,F1,F4,F7,D1,D4,D7,B3,B6,B9,L1,L2,L3,L4,L6,L7,L8,L9,memory,memorysens,result = LIB(U1,U4,U7,F1,F4,F7,D1,D4,D7,B3,B6,B9,L1,L2,L3,L4,L6,L7,L8,L9,P,memory,memorysens,result)
                F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result = U(F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result)
                U1,U4,U7,F1,F4,F7,D1,D4,D7,B3,B6,B9,L1,L2,L3,L4,L6,L7,L8,L9,memory,memorysens,result = LB(U1,U4,U7,F1,F4,F7,D1,D4,D7,B3,B6,B9,L1,L2,L3,L4,L6,L7,L8,L9,P,memory,memorysens,result)
                F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result = U(F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result)
                U1,U4,U7,F1,F4,F7,D1,D4,D7,B3,B6,B9,L1,L2,L3,L4,L6,L7,L8,L9,memory,memorysens,result = LB(U1,U4,U7,F1,F4,F7,D1,D4,D7,B3,B6,B9,L1,L2,L3,L4,L6,L7,L8,L9,P,memory,memorysens,result)
                U1,U4,U7,F1,F4,F7,D1,D4,D7,B3,B6,B9,L1,L2,L3,L4,L6,L7,L8,L9,memory,memorysens,result = LB(U1,U4,U7,F1,F4,F7,D1,D4,D7,B3,B6,B9,L1,L2,L3,L4,L6,L7,L8,L9,P,memory,memorysens,result)
            elif (F2 == B5) & (B2 == F5) & (R2 == L5) & (L2 == R5):
                U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,memory,memorysens,result = RB(U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,P,memory,memorysens,result)
                U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,memory,memorysens,result = RB(U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,P,memory,memorysens,result)
                U1,U4,U7,F1,F4,F7,D1,D4,D7,B3,B6,B9,L1,L2,L3,L4,L6,L7,L8,L9,memory,memorysens,result = LB(U1,U4,U7,F1,F4,F7,D1,D4,D7,B3,B6,B9,L1,L2,L3,L4,L6,L7,L8,L9,P,memory,memorysens,result)
                U1,U4,U7,F1,F4,F7,D1,D4,D7,B3,B6,B9,L1,L2,L3,L4,L6,L7,L8,L9,memory,memorysens,result = LB(U1,U4,U7,F1,F4,F7,D1,D4,D7,B3,B6,B9,L1,L2,L3,L4,L6,L7,L8,L9,P,memory,memorysens,result)
                F7,F8,F9,R7,R8,R9,B7,B8,B9,L7,L8,L9,D1,D2,D3,D4,D6,D7,D8,D9,memory,memorysens,result = D(F7,F8,F9,R7,R8,R9,B7,B8,B9,L7,L8,L9,D1,D2,D3,D4,D6,D7,D8,D9,memory,memorysens,result)
                U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,memory,memorysens,result = RB(U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,P,memory,memorysens,result)
                U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,memory,memorysens,result = RB(U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,P,memory,memorysens,result)
                U1,U4,U7,F1,F4,F7,D1,D4,D7,B3,B6,B9,L1,L2,L3,L4,L6,L7,L8,L9,memory,memorysens,result = LB(U1,U4,U7,F1,F4,F7,D1,D4,D7,B3,B6,B9,L1,L2,L3,L4,L6,L7,L8,L9,P,memory,memorysens,result)
                U1,U4,U7,F1,F4,F7,D1,D4,D7,B3,B6,B9,L1,L2,L3,L4,L6,L7,L8,L9,memory,memorysens,result = LB(U1,U4,U7,F1,F4,F7,D1,D4,D7,B3,B6,B9,L1,L2,L3,L4,L6,L7,L8,L9,P,memory,memorysens,result)
                F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result = U(F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result)
                F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result = U(F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result)
                U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,memory,memorysens,result = RB(U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,P,memory,memorysens,result)
                U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,memory,memorysens,result = RB(U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,P,memory,memorysens,result)
                U1,U4,U7,F1,F4,F7,D1,D4,D7,B3,B6,B9,L1,L2,L3,L4,L6,L7,L8,L9,memory,memorysens,result = LB(U1,U4,U7,F1,F4,F7,D1,D4,D7,B3,B6,B9,L1,L2,L3,L4,L6,L7,L8,L9,P,memory,memorysens,result)
                U1,U4,U7,F1,F4,F7,D1,D4,D7,B3,B6,B9,L1,L2,L3,L4,L6,L7,L8,L9,memory,memorysens,result = LB(U1,U4,U7,F1,F4,F7,D1,D4,D7,B3,B6,B9,L1,L2,L3,L4,L6,L7,L8,L9,P,memory,memorysens,result)
                F7,F8,F9,R7,R8,R9,B7,B8,B9,L7,L8,L9,D1,D2,D3,D4,D6,D7,D8,D9,memory,memorysens,result = D(F7,F8,F9,R7,R8,R9,B7,B8,B9,L7,L8,L9,D1,D2,D3,D4,D6,D7,D8,D9,memory,memorysens,result)
                U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,memory,memorysens,result = RB(U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,P,memory,memorysens,result)
                U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,memory,memorysens,result = RB(U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,P,memory,memorysens,result)
                U1,U4,U7,F1,F4,F7,D1,D4,D7,B3,B6,B9,L1,L2,L3,L4,L6,L7,L8,L9,memory,memorysens,result = LB(U1,U4,U7,F1,F4,F7,D1,D4,D7,B3,B6,B9,L1,L2,L3,L4,L6,L7,L8,L9,P,memory,memorysens,result)
                U1,U4,U7,F1,F4,F7,D1,D4,D7,B3,B6,B9,L1,L2,L3,L4,L6,L7,L8,L9,memory,memorysens,result = LB(U1,U4,U7,F1,F4,F7,D1,D4,D7,B3,B6,B9,L1,L2,L3,L4,L6,L7,L8,L9,P,memory,memorysens,result)
            elif (F2 == F5) & (B2 == B5) & (R2 == L5) & (L2 == R5):
                U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,memory,memorysens,result = RIB(U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,P,memory,memorysens,result)
                F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result = UI(F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result)
                U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,memory,memorysens,result = RB(U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,P,memory,memorysens,result)
                F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result = UI(F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result)
                U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,memory,memorysens,result = RB(U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,P,memory,memorysens,result)
                F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result = U(F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result)
                U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,memory,memorysens,result = RB(U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,P,memory,memorysens,result)
                F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result = UI(F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result)
                U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,memory,memorysens,result = RIB(U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,P,memory,memorysens,result)
                F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result = U(F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result)
                U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,memory,memorysens,result = RB(U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,P,memory,memorysens,result)
                F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result = U(F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result)
                U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,memory,memorysens,result = RB(U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,P,memory,memorysens,result)
                U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,memory,memorysens,result = RB(U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,P,memory,memorysens,result)
                F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result = UI(F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result)
                U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,memory,memorysens,result = RIB(U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,P,memory,memorysens,result)
                F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result = U(F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result)
            else:
                U1,U2,U3,U4,U5,U6,U7,U8,U9,F1,F2,F3,F4,F5,F6,F7,F8,F9,R1,R2,R3,R4,R5,R6,R7,R8,R9,B1,B2,B3,B4,B5,B6,B7,B8,B9,L1,L2,L3,L4,L5,L6,L7,L8,L9,D1,D2,D3,D4,D5,D6,D7,D8,D9,P = y(U1,U2,U3,U4,U5,U6,U7,U8,U9,F1,F2,F3,F4,F5,F6,F7,F8,F9,R1,R2,R3,R4,R5,R6,R7,R8,R9,B1,B2,B3,B4,B5,B6,B7,B8,B9,L1,L2,L3,L4,L5,L6,L7,L8,L9,D1,D2,D3,D4,D5,D6,D7,D8,D9,P)
        if (F2 != F5) | (R2 != R5) | (B2 != B5) | (L2 != L5):
            F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result = U(F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result)



    while (F1 != F5) | (R1 != R5) | (B1 != B5) | (L1 != L5):
        for i in range (4):
            if (F1 == F5) & (R1 == L5):
                U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,memory,memorysens,result = RIB(U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,P,memory,memorysens,result)
                U7,U8,U9,R1,R4,R7,L3,L6,L9,D1,D2,D3,F1,F2,F3,F4,F6,F7,F8,F9,memory,memorysens,result = FB(U7,U8,U9,R1,R4,R7,L3,L6,L9,D1,D2,D3,F1,F2,F3,F4,F6,F7,F8,F9,P,memory,memorysens,result)
                U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,memory,memorysens,result = RIB(U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,P,memory,memorysens,result)
                U1,U2,U3,R3,R6,R9,L1,L4,L7,D7,D8,D9,B1,B2,B3,B4,B6,B7,B8,B9,memory,memorysens,result = BB(U1,U2,U3,R3,R6,R9,L1,L4,L7,D7,D8,D9,B1,B2,B3,B4,B6,B7,B8,B9,P,memory,memorysens,result)
                U1,U2,U3,R3,R6,R9,L1,L4,L7,D7,D8,D9,B1,B2,B3,B4,B6,B7,B8,B9,memory,memorysens,result = BB(U1,U2,U3,R3,R6,R9,L1,L4,L7,D7,D8,D9,B1,B2,B3,B4,B6,B7,B8,B9,P,memory,memorysens,result)
                U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,memory,memorysens,result = RB(U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,P,memory,memorysens,result)
                U7,U8,U9,R1,R4,R7,L3,L6,L9,D1,D2,D3,F1,F2,F3,F4,F6,F7,F8,F9,memory,memorysens,result = FIB(U7,U8,U9,R1,R4,R7,L3,L6,L9,D1,D2,D3,F1,F2,F3,F4,F6,F7,F8,F9,P,memory,memorysens,result)
                U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,memory,memorysens,result = RIB(U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,P,memory,memorysens,result)
                U1,U2,U3,R3,R6,R9,L1,L4,L7,D7,D8,D9,B1,B2,B3,B4,B6,B7,B8,B9,memory,memorysens,result = BB(U1,U2,U3,R3,R6,R9,L1,L4,L7,D7,D8,D9,B1,B2,B3,B4,B6,B7,B8,B9,P,memory,memorysens,result)
                U1,U2,U3,R3,R6,R9,L1,L4,L7,D7,D8,D9,B1,B2,B3,B4,B6,B7,B8,B9,memory,memorysens,result = BB(U1,U2,U3,R3,R6,R9,L1,L4,L7,D7,D8,D9,B1,B2,B3,B4,B6,B7,B8,B9,P,memory,memorysens,result)
                U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,memory,memorysens,result = RB(U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,P,memory,memorysens,result)
                U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,memory,memorysens,result = RB(U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,P,memory,memorysens,result)
            elif (F1 == F5) & (R1 == B5):
                U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,memory,memorysens,result = RB(U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,P,memory,memorysens,result)
                U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,memory,memorysens,result = RB(U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,P,memory,memorysens,result)
                U1,U2,U3,R3,R6,R9,L1,L4,L7,D7,D8,D9,B1,B2,B3,B4,B6,B7,B8,B9,memory,memorysens,result = BB(U1,U2,U3,R3,R6,R9,L1,L4,L7,D7,D8,D9,B1,B2,B3,B4,B6,B7,B8,B9,P,memory,memorysens,result)
                U1,U2,U3,R3,R6,R9,L1,L4,L7,D7,D8,D9,B1,B2,B3,B4,B6,B7,B8,B9,memory,memorysens,result = BB(U1,U2,U3,R3,R6,R9,L1,L4,L7,D7,D8,D9,B1,B2,B3,B4,B6,B7,B8,B9,P,memory,memorysens,result)
                U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,memory,memorysens,result = RB(U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,P,memory,memorysens,result)
                U7,U8,U9,R1,R4,R7,L3,L6,L9,D1,D2,D3,F1,F2,F3,F4,F6,F7,F8,F9,memory,memorysens,result = FB(U7,U8,U9,R1,R4,R7,L3,L6,L9,D1,D2,D3,F1,F2,F3,F4,F6,F7,F8,F9,P,memory,memorysens,result)
                U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,memory,memorysens,result = RIB(U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,P,memory,memorysens,result)
                U1,U2,U3,R3,R6,R9,L1,L4,L7,D7,D8,D9,B1,B2,B3,B4,B6,B7,B8,B9,memory,memorysens,result = BB(U1,U2,U3,R3,R6,R9,L1,L4,L7,D7,D8,D9,B1,B2,B3,B4,B6,B7,B8,B9,P,memory,memorysens,result)
                U1,U2,U3,R3,R6,R9,L1,L4,L7,D7,D8,D9,B1,B2,B3,B4,B6,B7,B8,B9,memory,memorysens,result = BB(U1,U2,U3,R3,R6,R9,L1,L4,L7,D7,D8,D9,B1,B2,B3,B4,B6,B7,B8,B9,P,memory,memorysens,result)
                U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,memory,memorysens,result = RB(U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,P,memory,memorysens,result)
                U7,U8,U9,R1,R4,R7,L3,L6,L9,D1,D2,D3,F1,F2,F3,F4,F6,F7,F8,F9,memory,memorysens,result = FIB(U7,U8,U9,R1,R4,R7,L3,L6,L9,D1,D2,D3,F1,F2,F3,F4,F6,F7,F8,F9,P,memory,memorysens,result)
                U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,memory,memorysens,result = RB(U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,P,memory,memorysens,result)
            elif (F1 == L5) & (R1 == B5):
                U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,memory,memorysens,result = RB(U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,P,memory,memorysens,result)
                U1,U2,U3,R3,R6,R9,L1,L4,L7,D7,D8,D9,B1,B2,B3,B4,B6,B7,B8,B9,memory,memorysens,result = BIB(U1,U2,U3,R3,R6,R9,L1,L4,L7,D7,D8,D9,B1,B2,B3,B4,B6,B7,B8,B9,P,memory,memorysens,result)
                U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,memory,memorysens,result = RIB(U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,P,memory,memorysens,result)
                U7,U8,U9,R1,R4,R7,L3,L6,L9,D1,D2,D3,F1,F2,F3,F4,F6,F7,F8,F9,memory,memorysens,result = FB(U7,U8,U9,R1,R4,R7,L3,L6,L9,D1,D2,D3,F1,F2,F3,F4,F6,F7,F8,F9,P,memory,memorysens,result)
                U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,memory,memorysens,result = RB(U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,P,memory,memorysens,result)
                U1,U2,U3,R3,R6,R9,L1,L4,L7,D7,D8,D9,B1,B2,B3,B4,B6,B7,B8,B9,memory,memorysens,result = BB(U1,U2,U3,R3,R6,R9,L1,L4,L7,D7,D8,D9,B1,B2,B3,B4,B6,B7,B8,B9,P,memory,memorysens,result)
                U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,memory,memorysens,result = RIB(U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,P,memory,memorysens,result)
                U7,U8,U9,R1,R4,R7,L3,L6,L9,D1,D2,D3,F1,F2,F3,F4,F6,F7,F8,F9,memory,memorysens,result = FIB(U7,U8,U9,R1,R4,R7,L3,L6,L9,D1,D2,D3,F1,F2,F3,F4,F6,F7,F8,F9,P,memory,memorysens,result)
                U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,memory,memorysens,result = RB(U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,P,memory,memorysens,result)
                U1,U2,U3,R3,R6,R9,L1,L4,L7,D7,D8,D9,B1,B2,B3,B4,B6,B7,B8,B9,memory,memorysens,result = BB(U1,U2,U3,R3,R6,R9,L1,L4,L7,D7,D8,D9,B1,B2,B3,B4,B6,B7,B8,B9,P,memory,memorysens,result)
                U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,memory,memorysens,result = RIB(U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,P,memory,memorysens,result)
                U7,U8,U9,R1,R4,R7,L3,L6,L9,D1,D2,D3,F1,F2,F3,F4,F6,F7,F8,F9,memory,memorysens,result = FB(U7,U8,U9,R1,R4,R7,L3,L6,L9,D1,D2,D3,F1,F2,F3,F4,F6,F7,F8,F9,P,memory,memorysens,result)
                U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,memory,memorysens,result = RB(U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,P,memory,memorysens,result)
                U1,U2,U3,R3,R6,R9,L1,L4,L7,D7,D8,D9,B1,B2,B3,B4,B6,B7,B8,B9,memory,memorysens,result = BIB(U1,U2,U3,R3,R6,R9,L1,L4,L7,D7,D8,D9,B1,B2,B3,B4,B6,B7,B8,B9,P,memory,memorysens,result)
                U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,memory,memorysens,result = RIB(U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,P,memory,memorysens,result)
                U7,U8,U9,R1,R4,R7,L3,L6,L9,D1,D2,D3,F1,F2,F3,F4,F6,F7,F8,F9,memory,memorysens,result = FIB(U7,U8,U9,R1,R4,R7,L3,L6,L9,D1,D2,D3,F1,F2,F3,F4,F6,F7,F8,F9,P,memory,memorysens,result)
            elif (F1 == B5) & (R1 == L5):
                F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result = U(F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result)
                F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result = U(F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result)
                U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,memory,memorysens,result = RB(U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,P,memory,memorysens,result)
                U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,memory,memorysens,result = RB(U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,P,memory,memorysens,result)
                U1,U4,U7,F1,F4,F7,D1,D4,D7,B3,B6,B9,L1,L2,L3,L4,L6,L7,L8,L9,memory,memorysens,result = LB(U1,U4,U7,F1,F4,F7,D1,D4,D7,B3,B6,B9,L1,L2,L3,L4,L6,L7,L8,L9,P,memory,memorysens,result)
                U1,U4,U7,F1,F4,F7,D1,D4,D7,B3,B6,B9,L1,L2,L3,L4,L6,L7,L8,L9,memory,memorysens,result = LB(U1,U4,U7,F1,F4,F7,D1,D4,D7,B3,B6,B9,L1,L2,L3,L4,L6,L7,L8,L9,P,memory,memorysens,result)
                F7,F8,F9,R7,R8,R9,B7,B8,B9,L7,L8,L9,D1,D2,D3,D4,D6,D7,D8,D9,memory,memorysens,result = D(F7,F8,F9,R7,R8,R9,B7,B8,B9,L7,L8,L9,D1,D2,D3,D4,D6,D7,D8,D9,memory,memorysens,result)
                U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,memory,memorysens,result = RB(U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,P,memory,memorysens,result)
                U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,memory,memorysens,result = RB(U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,P,memory,memorysens,result)
                U1,U4,U7,F1,F4,F7,D1,D4,D7,B3,B6,B9,L1,L2,L3,L4,L6,L7,L8,L9,memory,memorysens,result = LB(U1,U4,U7,F1,F4,F7,D1,D4,D7,B3,B6,B9,L1,L2,L3,L4,L6,L7,L8,L9,P,memory,memorysens,result)
                U1,U4,U7,F1,F4,F7,D1,D4,D7,B3,B6,B9,L1,L2,L3,L4,L6,L7,L8,L9,memory,memorysens,result = LB(U1,U4,U7,F1,F4,F7,D1,D4,D7,B3,B6,B9,L1,L2,L3,L4,L6,L7,L8,L9,P,memory,memorysens,result)
                F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result = U(F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result)
                F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result = U(F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result)
                U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,memory,memorysens,result = RB(U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,P,memory,memorysens,result)
                U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,memory,memorysens,result = RB(U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,P,memory,memorysens,result)
                U1,U4,U7,F1,F4,F7,D1,D4,D7,B3,B6,B9,L1,L2,L3,L4,L6,L7,L8,L9,memory,memorysens,result = LB(U1,U4,U7,F1,F4,F7,D1,D4,D7,B3,B6,B9,L1,L2,L3,L4,L6,L7,L8,L9,P,memory,memorysens,result)
                U1,U4,U7,F1,F4,F7,D1,D4,D7,B3,B6,B9,L1,L2,L3,L4,L6,L7,L8,L9,memory,memorysens,result = LB(U1,U4,U7,F1,F4,F7,D1,D4,D7,B3,B6,B9,L1,L2,L3,L4,L6,L7,L8,L9,P,memory,memorysens,result)
                F7,F8,F9,R7,R8,R9,B7,B8,B9,L7,L8,L9,D1,D2,D3,D4,D6,D7,D8,D9,memory,memorysens,result = D(F7,F8,F9,R7,R8,R9,B7,B8,B9,L7,L8,L9,D1,D2,D3,D4,D6,D7,D8,D9,memory,memorysens,result)
                U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,memory,memorysens,result = RB(U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,P,memory,memorysens,result)
                U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,memory,memorysens,result = RB(U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,P,memory,memorysens,result)
                U1,U4,U7,F1,F4,F7,D1,D4,D7,B3,B6,B9,L1,L2,L3,L4,L6,L7,L8,L9,memory,memorysens,result = LB(U1,U4,U7,F1,F4,F7,D1,D4,D7,B3,B6,B9,L1,L2,L3,L4,L6,L7,L8,L9,P,memory,memorysens,result)
                U1,U4,U7,F1,F4,F7,D1,D4,D7,B3,B6,B9,L1,L2,L3,L4,L6,L7,L8,L9,memory,memorysens,result = LB(U1,U4,U7,F1,F4,F7,D1,D4,D7,B3,B6,B9,L1,L2,L3,L4,L6,L7,L8,L9,P,memory,memorysens,result)
            else:
                U1,U2,U3,U4,U5,U6,U7,U8,U9,F1,F2,F3,F4,F5,F6,F7,F8,F9,R1,R2,R3,R4,R5,R6,R7,R8,R9,B1,B2,B3,B4,B5,B6,B7,B8,B9,L1,L2,L3,L4,L5,L6,L7,L8,L9,D1,D2,D3,D4,D5,D6,D7,D8,D9,P = y(U1,U2,U3,U4,U5,U6,U7,U8,U9,F1,F2,F3,F4,F5,F6,F7,F8,F9,R1,R2,R3,R4,R5,R6,R7,R8,R9,B1,B2,B3,B4,B5,B6,B7,B8,B9,L1,L2,L3,L4,L5,L6,L7,L8,L9,D1,D2,D3,D4,D5,D6,D7,D8,D9,P)

    memory,memorysens,result = enregistrement("","",memory,memorysens,result)


    print(U1,U2,U3,U4,U5,U6,U7,U8,U9,F1,F2,F3,F4,F5,F6,F7,F8,F9,R1,R2,R3,R4,R5,R6,R7,R8,R9,B1,B2,B3,B4,B5,B6,B7,B8,B9,L1,L2,L3,L4,L5,L6,L7,L8,L9,D1,D2,D3,D4,D5,D6,D7,D8,D9)
    print(len(result))
    return(result)



def exemple(U1,U2,U3,U4,U5,U6,U7,U8,U9,F1,F2,F3,F4,F5,F6,F7,F8,F9,R1,R2,R3,R4,R5,R6,R7,R8,R9,B1,B2,B3,B4,B5,B6,B7,B8,B9,L1,L2,L3,L4,L5,L6,L7,L8,L9,D1,D2,D3,D4,D5,D6,D7,D8,D9):
    P = 3
    result = ""
    memory = ""
    memorysens = ""
    U1,U2,U3,U4,U5,U6,U7,U8,U9,F1,F2,F3,F4,F5,F6,F7,F8,F9,R1,R2,R3,R4,R5,R6,R7,R8,R9,B1,B2,B3,B4,B5,B6,B7,B8,B9,L1,L2,L3,L4,L5,L6,L7,L8,L9,D1,D2,D3,D4,D5,D6,D7,D8,D9,P = y(U1,U2,U3,U4,U5,U6,U7,U8,U9,F1,F2,F3,F4,F5,F6,F7,F8,F9,R1,R2,R3,R4,R5,R6,R7,R8,R9,B1,B2,B3,B4,B5,B6,B7,B8,B9,L1,L2,L3,L4,L5,L6,L7,L8,L9,D1,D2,D3,D4,D5,D6,D7,D8,D9,P)

    U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,memory,memorysens,result = RB(U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,P,memory,memorysens,result)
    F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result = U(F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result)
    F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result = U(F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result)
    F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result = U(F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result)
    F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result = U(F1,F2,F3,R1,R2,R3,B1,B2,B3,L1,L2,L3,U1,U2,U3,U4,U6,U7,U8,U9,memory,memorysens,result)


    U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,memory,memorysens,result = RB(U3,U6,U9,F3,F6,F9,D3,D6,D9,B1,B4,B7,R1,R2,R3,R4,R6,R7,R8,R9,P,memory,memorysens,result)

    memory,memorysens,result = enregistrement("","",memory,memorysens,result)

    print(U1,U2,U3,U4,U5,U6,U7,U8,U9,F1,F2,F3,F4,F5,F6,F7,F8,F9,R1,R2,R3,R4,R5,R6,R7,R8,R9,B1,B2,B3,B4,B5,B6,B7,B8,B9,L1,L2,L3,L4,L5,L6,L7,L8,L9,D1,D2,D3,D4,D5,D6,D7,D8,D9)
    return(result)
