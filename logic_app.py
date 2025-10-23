import customtkinter as ctk

# Ventana mínima de prueba
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("500x400")
app.title("Test customtkinter")

label = ctk.CTkLabel(app, text="Si ves esto, customtkinter funciona")
label.pack(pady=12)

button = ctk.CTkButton(app, text="Cerrar", command=app.destroy)
button.pack(pady=6)


if __name__ == '__main__':
    app.mainloop()
