

from array import array


def ImparellParell(num): #imparell=false #parell=true
    if num :
        return True
    else:
        return False  
    return 





def Corrector():
    array_numeros=[22,33,44,50,100,55,74,73,2]
    array_resultat=[True,False,True,True,True,False,True,False,True]
    array_resultat_alumne=[]
    for numero in array_numeros:
        array_resultat_alumne.append(ImparellParell(numero))
    
    if(array_resultat==array_resultat_alumne):
        print("TEST OK")
    else:
        print("TEST NOT OK")

        
        

Corrector()