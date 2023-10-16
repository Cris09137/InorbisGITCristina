



#Suspès, Aprovat, Bé, Notable, Excel·lent
def Notes(nota):
    if nota<=4:
        nota="Suspès"
    elif (nota>=5) and (nota<6):
        nota="Aprovat"
    elif (nota>=6) and (nota<7):
        nota="Bé"
    elif (nota>=7) and (nota<=9):
        nota="Notable"
    elif nota==10:
        nota="Excel·lent"
     
    return nota



def Corrector():
    array_resultats=[]
    array_notes=[2,3,4,10,8,5,1,7,6]
    array_correcio=["Suspès","Suspès","Suspès","Excel·lent","Notable","Aprovat","Suspès","Notable","Bé"]

    for i in range(0,len(array_notes)):
        resultat=Notes(array_notes[i])
        array_resultats.append(resultat)
    
    if(array_resultats==array_correcio):
        print("TEST OK")
    else:
        print("TEST NOT OK")


Corrector()