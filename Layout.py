import flet as ft

nom1=ft.Text("Cristina")
nom1.color="#B8CCEA"
nom1.size=20
nom2=ft.Text(value="Oriol",color="red",size=20)
nom3=ft.Text(value="Rayan",color="blue",size=20)
nom4=ft.Text(value="Francesc",color="green",size=20)
nom5=ft.Text(value="Eduardo",color="yellow",size=20)
nom6=ft.Text(value="Jan",color="orange",size=20)

label1=ft.TextField(label="Nombre")

def main(page: ft.Page):
    page.add(
     ft.Row(controls=[
        nom1,
        nom2,
        nom3,
         
    ]),
    ft.Row(controls=[
         nom4,
         nom5,
         nom6,
         
    ]),
     ft.Row(controls=[
        label1
         
    ]),     
    )
    
    pass
ft.app(target=main)