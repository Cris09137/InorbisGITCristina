import flet as ft


def main(page: ft.Page):
    def button_clicked(e):
        page.clean()
        name=input_name.value
        age=int(input_age.value)
        if age >=  18:
            text_age=ft.Text(value=f"You have {age} congratulations, you can enter.",color="green")
        else:
            text_age=ft.Text(value=f"You have {age}, You can't enter here. Go back to your house",color="red")     
        text_name=ft.Text(value=f"Hello {name} 👋",color="#b48395",size=50)
        page.add(
            ft.Row(
            controls=[text_name],
            alignment="center",
            ),
            ft.Row(
            controls=[text_age],
            alignment="center",
            ),
        )



    Title=ft.Text(value="Qüestionari",color="#b48395",size=50)
    input_name=ft.TextField(label="Name",border_color="#b48395",color="#8BB8E8")
    input_age=ft.TextField(label="Age",border_color="#b48395",color="#8BB8E8")
    input_street=ft.TextField(label="Street",border_color="#b48395",color="#8BB8E8")
    input_mail=ft.TextField(label="E-mail",border_color="#b48395",color="#8BB8E8")
    input_telephone=ft.TextField(label="Telephone",border_color="#b48395",color="#8BB8E8")
    send_button=ft.ElevatedButton(text="Submit",on_click=button_clicked,bgcolor="#b48395",color="black")
    page.add(    
        ft.Row(
            controls=[Title],
            alignment="center",
        ),
         ft.Row(
            controls=[input_name,],
            alignment="center",
        ),
         ft.Row(
            controls=[input_age,],
            alignment="center",
         ),
         ft.Row(
            controls=[input_street],
            alignment="center",
        ),
         ft.Row(
            controls=[input_mail],
            alignment="center",
        ),
         ft.Row(
            controls=[input_telephone],
            alignment="center",
        ),
         ft.Row(
            controls=[send_button],
            alignment="center",
        )
    )
    pass

ft.app(target=main)