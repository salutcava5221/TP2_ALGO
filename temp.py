# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

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

tri_rapide(tab)
print(tri_rapide(tab))       
    
    
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


def tri_rapide(tab):
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

            
            
    return tri_rapide(gauche) + [tab[taille-1]] + tri_rapide(droite)
    

        
tab = [24, 97, 40, 67, 88, 85, 15, 66, 53, 44, 26, 48, 16, 52, 45, 23, 90, 18, 49, 80]
tri_rapide(tab)
print(tri_rapide(tab))        
        
        
        
        
        
        
# tab = [3, 8, 5, 4, 1, 9 ,-2]
# print(tri_par_insertion(tab))


#tri_hybride(tab,0,len(tab)-1)
#...................................................................................#


def  tri_par_enombrement(tab):
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
    print(tmp)

    tab = []
    for i in range(len(tmp)):
        while tmp[i] > 0:
            tab.append(i + Min)
            tmp[i] -= 1
    print(tab)
        
        
                
    
    
        
                        
            
# tab = [1, 7, 4, 1, 10, 9, -2, 5, 3, 8, 0]
# tri_par_enombrement(tab)  

#...................................................................................#

      
import matplotlib.pyplot as plt

# Your recorded timings
labels = ["QuickSort", "Hybrid QuickSort", "Counting Sort"]

# Test Set 1 (random large values)
test1 = [0.2415, 0.2297, 0]  # counting sort not used → set to 0

# Test Set 2 (counting sort compatible)
test2 = [0.2278, 0.2285, 0.0327]

x = range(len(labels))

plt.figure(figsize=(10, 6))

# Bars for Test 1
plt.bar([i - 0.15 for i in x], test1, width=0.3,
        label="Test Set 1 (random large values)")

# Bars for Test 2
plt.bar([i + 0.15 for i in x], test2, width=0.3,
        label="Test Set 2 (counting-sort-compatible)")

plt.xticks(x, labels)
plt.ylabel("Time (seconds)")
plt.title("Comparison of Sorting Algorithms")
plt.legend()
plt.tight_layout()
plt.show()


       
    

