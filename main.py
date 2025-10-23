import customtkinter as ctk

def main_window():
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")

    app = ctk.CTk()
    app.geometry("500x400")
    app.title("Test customtkinter")

    # Usar solo grid() — no mezclar pack() y grid()
    label = ctk.CTkLabel(app, text="Bienvenido", font=("Times New Roman", 20))
    label.grid(row=0, column=10, columnspan=2, pady=(12, 8), padx=12)

    button = ctk.CTkButton(app, text="Cerrar", command=app.destroy)
    button.grid(row=1, column=10, padx=12, pady=8, sticky='w')

    app.mainloop()


if __name__ == '__main__':
    main_window()
