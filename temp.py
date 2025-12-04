# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""
import random
import time
import matplotlib.pyplot as plt



tab = [1,3,5,2,-3,9,7,8,0,-1,6]





def tri_rapide(tab):
    taille = len(tab)
    droite = []
    gauche = []
    if taille <= 1:
        return tab
    else:
        for i in tab[0:(taille-1)]:
            if i >= tab[taille-1]:
                droite.append(i)
            else:
                gauche.append(i)
        return tri_rapide(gauche) + [tab[taille-1]] + tri_rapide(droite)
        #print(droite)
        #print(gauche)
            
tab = [9, -3, 5, 2, 6, 8, -6, 1, 3]

# tri_rapide(tab)
# print(tri_rapide(tab))       
    
    
# tab = [1, 7, 4, 1, 10, 9, -2]
# tri_rapide(tab1)
# print(tab)


#...................................................................................#

SEUIL = 15




def tri_par_insertion(tab):
    taille = len(tab)
    for i in range(1,taille):
        j = i
        #print(tab)
        while(tab[j-1] > tab[j] and j > 0):
            tmp = 0
            tmp = tab[j]
            tab[j] = tab[j-1]
            tab[j-1] = tmp
            j -= 1
            #print(tab)
    return tab


# Test simple
# tab = [3, 8, 5, 4, 1, 9 ,-2]
# print(tri_par_insertion(tab))


# Test avec 1 000 element         
#tab = [random.randint(-5000, 5000) for _ in range(1001)]       
#print(tri_par_insertion(tab))     

def tri_rapide_hybride(tab):
    taille = len(tab)
    if taille <= SEUIL:
        return tri_par_insertion(tab)
        #print(tab)
    droite = []
    gauche = []
    
    for i in tab[0:(taille-1)]:
        if i < tab[taille-1]:
            gauche.append(i)
            #print(gauche)
        else:
            droite.append(i)
            #print(droite)

            
            
    return tri_rapide_hybride(gauche) + [tab[taille-1]] + tri_rapide_hybride(droite)
    

# Test simple        
#tab = [24, 97, 40, 67, 88, 85, 15, 66, 53, 44, 26, 48, 16, 52, 45, 23, 90, 18, 49, 80]
#print(tri_rapide_hybride(tab))       
        
        
# Test avec 50 000 element         
#tab = [random.randint(-5000, 5000) for _ in range(50000)]       
#print(tri_rapide_hybride(tab))     
        

#...................................................................................#


def  tri_par_enombrement(tab):
    if len(tab) == 0:
        return []
    
    Min = min(tab)
    Max = max(tab)
    tmp =[]
    taille = Max - Min + 1
    
    #constrire le tableau
    for i in range(taille):
        tmp.append(0)
    
    # comp
    for i in tab:     #i = 1 , i = 7 
        tmp[i - Min] += 1
    #print(tmp)

    tab = []
    for i in range(len(tmp)):
        while tmp[i] > 0:
            tab.append(i + Min)
            tmp[i] -= 1
    #print(tab)
    return tab
        
        
                
    
#Test simple
#tab = [7, 4, 1, 10, 9, 5, 3, 8]
        
       

# Test avec 50 000 element 
#tab = [random.randint(-5000, 5000) for _ in range(50000)]       
#print(tri_par_enombrement(tab)) 


# 
#  
# ============================================================
# QUESTION 4 — VERSION MINIMALE
# ============================================================


# def test(func, tab):
#     start = time.time()
#     func(tab.copy())
#     end = time.time()
#     return round(end - start, 4)

# print("\n=== QUESTION 4 : COMPARAISON DES 3 ALGORITHMES ===")
# print("Taille : 50 000 éléments")
# print("Plage : [-5000, 5000]")
# print()

# tab = [random.randint(-5000, 5000) for _ in range(50000)]

# # Tester les 3 algorithmes
# t_rapide = test(tri_rapide, tab)
# t_hybride = test(tri_rapide_hybride, tab)
# t_counting = test(tri_par_enombrement, tab)

# # Afficher les résultats
# print(f"Tri rapide           : {t_rapide} sec")
# print(f"Tri rapide hybride   : {t_hybride} sec")
# print(f"Tri par dénombrement : {t_counting} sec")

# # Graphique simple
# plt.figure(figsize=(10, 6))
# plt.bar(["Tri rapide", "Tri hybride", "Tri dénombrement"], 
#         [t_rapide, t_hybride, t_counting],
#         color=['#E74C3C', '#3498DB', '#2ECC71'])

# plt.title("Comparaison des temps d'exécution\n50 000 éléments", fontsize=14, fontweight='bold')
# plt.ylabel("Temps (secondes)", fontweight='bold')
# plt.grid(axis='y', alpha=0.3)

# # Ajouter les valeurs sur les barres
# for i, v in enumerate([t_rapide, t_hybride, t_counting]):
#     plt.text(i, v + 0.002, f'{v}s', ha='center', fontweight='bold')

# plt.tight_layout()
# plt.savefig('graphique_question4.png', dpi=150)
# print("\n✓ Graphique sauvegardé : graphique_question4.png")
# plt.show()


       
    

