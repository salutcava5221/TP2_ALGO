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
            
tab = [9, -3, 5, 2, 6, 8, -6, 1, 3]

tri_rapide(tab)
print(tri_rapide(tab))       
    
    
# tab = [1, 7, 4, 1, 10, 9, -2]
# tri_rapide(tab, 0, len(tab) - 1)
# print(tab)


#...................................................................................#

SEUIL = 15




def tri_par_insertion(tab):
    taille = len(tab)
    for i in range(1,taille):
        j = i
        while(tab[j-1] > tab[j] and j > 0):
            tmp = 0
            tmp = tab[j]
            tab[j] = tab[j-1]
            tab[j-1] = tmp
            j -= 1
    return tab


def tri_rapide(tab):
    taille = len(tab)
    droite = []
    gauche = []
    for i in tab[0:(taille-1)]:
        if i >= tab[taille-1]:
            droite.append(i)
        else:
            gauche.append(i)
    if taille >= SEUIL:
        return tri_rapide(gauche) + [tab[taille-1]] + tri_par_insertion(droite)
    else:
        return tri_par_insertion(gauche) + [tab[taille-1]] + tri_par_insertion(droite)

        
tab = [24, 97, 40, 67, 88, 85, 15, 66, 53, 44, 26, 48, 16, 52, 45, 23, 90, 18, 49, 80]
tri_rapide(tab)
print(tri_rapide(tab))        
        
        
        
        
        
        
# tab = [3, 8, 5, 4, 1, 9 ,-2]
# print(tri_par_insertion(tab))


#tri_hybride(tab,0,len(tab)-1)
#...................................................................................#


def count_sort(tab):
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
# count_sort(tab)  

#...................................................................................#

      

       
    

