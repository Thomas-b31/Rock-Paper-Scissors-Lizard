#=====================================================================================================================#
#                                                   SCRIPT MODELE                                                    #
#=====================================================================================================================#

###   IMPORT DES PACKAGES   ###

import random
from collections import Counter
from matplotlib import colors
import matplotlib.pyplot as plt
from math import sqrt

#=====================================================================================================================#
#                  NE PAS OUBLIER : UNCOMMENT UN DES DEUX PLOTS POUR VISUALISER (LIGNES 122 ET 124)                   #
#=====================================================================================================================#


###   VARIABLES GENERALES   ###

# couleurs
cmap = colors.ListedColormap(['white','#7bf9ff','#fff97b','#ff9659'])
# Nombre de lézards B,J,O
B=20
J=20
O=20
SOM=B+J+O
# taille de la matrice
taille_coté=round(sqrt(B+J+O))
# valeurs initiales pour les fréquences (avant les rencontres)    
Fréquence_bleus=B/SOM
Freq_bleus=[B/SOM]
Freq_jaunes=[J/SOM]
Freq_oranges=[O/SOM]

#=====================================================================================================================#


###   FONCTION D'INITIALISATION   ###

def initialisation():
    
    ### CREATION DE LA MATRICE ###
    matrice=[[0 for x in range(0,taille_coté)]for y in range(0,taille_coté)]
    input_lézards(matrice)
    # Plot damier initial :
    plt.imshow(matrice,cmap=cmap)
    plt.axis('off')
    plt.show()
    
    # Rend le nombre de 0,1 et 2 dans la matrice (counter)
    Résumé_matrice = sum(map(Counter, matrice), Counter())
    print(Résumé_matrice)
    print("il y a :",B,"bleus,",J,"jaunes et",O,"oranges.")
    
    # Fréquence initiale des bleus
    Fréquence_bleus=B/SOM
        
    ###   RENCONTRES   ###
    Boucle_rencontres(taille_coté,matrice,Fréquence_bleus)

#=====================================================================================================================#


###   FONCTION QUI PLACE LES LEZARDS DANS LE DAMIER   ###

def input_lézards(matrice):
    for i in range(0,B):
        x=random.randint(0,taille_coté-1)
        y=random.randint(0,taille_coté-1)
        place=matrice[x][y]
        while place!=0:
            x=random.randint(0,taille_coté-1)
            y=random.randint(0,taille_coté-1)
            place=matrice[x][y]
        matrice[x][y]=1
    for i in range(0,J):
        x=random.randint(0,taille_coté-1)
        y=random.randint(0,taille_coté-1)
        place=matrice[x][y]
        while place!=0:
            x=random.randint(0,taille_coté-1)
            y=random.randint(0,taille_coté-1)
            place=matrice[x][y]
        matrice[x][y]=2
    for i in range(0,O):
        x=random.randint(0,taille_coté-1)
        y=random.randint(0,taille_coté-1)
        place=matrice[x][y]
        while place!=0:
            x=random.randint(0,taille_coté-1)
            y=random.randint(0,taille_coté-1)
            place=matrice[x][y]
        matrice[x][y]=3

#=====================================================================================================================#

        
###   FONCTION QUI INITIALISE LES LEZARDS QUI VONT SE RENCONTRER   ###        
    
def Boucle_rencontres(taille_coté,matrice,Fréquence_bleus):    
    # boucle rencontres
    while (Fréquence_bleus)!=1 and (Fréquence_bleus)!=0:      
        # Valeurs pour déterminer le numéro de colone et de ligne des valeurs 1 et 2
        a=random.randint(0,taille_coté-1)
        b=random.randint(0,taille_coté-1)
        c=random.randint(0,taille_coté-1)
        d=random.randint(0,taille_coté-1)
        
        ###   CHOIX ALEATOIRE DES DEUX LEZARDS   ###
        Lézard1=matrice[a][b]
        Lézard2=matrice[c][d]
        if Lézard1==Lézard2:
            c=random.randint(0,taille_coté-1)
            d=random.randint(0,taille_coté-1)
            Lézard2=matrice[c][d]
        
        ###   INTERACTION ENTRE LES DEUX LEZARDS   ###
        interaction(Lézard1,Lézard2,matrice,a,b,c,d)
        
        ###   CALCUL DES FREQUENCES DE CHAQUE LEZARD   ###
        Fréquence_bleus=Calcul_fréquences(matrice)
        
        ### PLOT FREQUENCES ###
        Plot_fréquences()
        ### PLOT DAMIER ###
        #Plot_damier(matrice)
 
#=====================================================================================================================#
     
   
###   FONCTION QUI SIMULE LE COMBAT ENTRE LES DEUX LEZARDS   ###
 
def interaction(Lézard1,Lézard2,matrice,a,b,c,d):
    if Lézard1==1:
        if Lézard2==1 : # Bleu contre Bleu
            matrice[a][b]=1
        elif Lézard2==2 : # Bleu contre Jaune
            matrice[c][d]=1
        elif Lézard2==3: # Bleu contre Orange
            matrice[a][b]=3
    elif Lézard1==2: 
        if Lézard2==2 : # Jaune contre Jaune
            matrice[a][b]=2
        elif Lézard2==1 : # Jaune contre Bleu
            matrice[a][b]=1
        elif Lézard2==3: # Jaune contre Orange
            matrice[c][d]=2
    elif Lézard1==3: 
        if Lézard2==3 : # Orange contre Orange
            matrice[a][b]=3
        elif Lézard2==2 : # Orange contre Jaune
            matrice[a][b]=2
        elif Lézard2==1: # Orange contre Bleu
            matrice[c][d]=3

#=====================================================================================================================#


###   FONCTION QUI CALCULE LA FREQUENCE DE CHAQUE COULEUR   ###
                        
def Calcul_fréquences(matrice):
    Résumé_matrice = sum(map(Counter, matrice), Counter())
    Fréquence_bleus=(Résumé_matrice[1]/SOM)
    Freq_bleus.append(Résumé_matrice[1]/SOM)
    Freq_jaunes.append(Résumé_matrice[2]/SOM)
    Freq_oranges.append(Résumé_matrice[3]/SOM)   
    B=Résumé_matrice[1]
    J=Résumé_matrice[2]
    O=Résumé_matrice[3]
    print("il y a :",B,"bleus,",J,"jaunes et",O,"oranges.")
    return Fréquence_bleus

#=====================================================================================================================#


###   FONCTION QUI PLOT LA MATRICE   ###
   
def Plot_damier(matrice):     
    plt.imshow(matrice,cmap=cmap)
    plt.axis('off')
    plt.show()  
 
#=====================================================================================================================#


###   FONCTION QUI PLOT LES FREQUENCES DE CHAQUE COULEUR   ###
       
def Plot_fréquences():
    plt.plot(Freq_bleus,label="Lézards bleus",c="#7bf9ff")
    plt.plot(Freq_jaunes,label="Lézards jaunes",c="#fff97b")
    plt.plot(Freq_oranges,label="Lézards oranges",c="#ff9659")
    plt.legend()
    plt.show()

#=====================================================================================================================#


###   PERMET DE LANCER AUTOMATIQUEMENT LE PROGRAMME   ###
               
if __name__=='__main__':
    initialisation()
