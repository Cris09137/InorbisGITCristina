import flet as ft
import time as time

def main(page: ft.Page):
   t1=ft.Text(value="Cristina Prieto Coll", color="grey",size=17,italic=True)
   t2=ft.Text(value="Francesc", color="blue", size=13)
   t3=ft.Text(value="Oriol", color="red", size=13)
   t4=ft.Text(value="Rayan", color="#5DC1B9", size=13)
   page.add(t1,t2,t3,t4)

   contador=ft.Text()
   contador.color="#B8CCEA"
   contador.size=15
   contador100=ft.Text()
   contador100.color="#F5DF4D"
   contador100.size=14
   contadorb=ft.Text()
   contadorb.color="#E2583E"
   contadorb.size=16
   page.add(contador,contador100,contadorb)
   for i in range(11):
      contador.value=f"Contador: {i}"
      page.update()
      time.sleep(1)
   for i in range(8):
      contador100.value=f"Contador: {i}"
      page.update()
      time.sleep(1)
   i=100
   while(i!=0):
      contadorb.value=f"Contador: {i}"
      page.update()
      time.sleep(1)
      i=i-1
     


ft.app(target=main)

