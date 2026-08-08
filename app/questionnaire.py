import tkinter as tk
from tkinter import ttk


class QuestionnaireApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Fit My Style - Questionnaire")
        self.root.minsize(420, 360)

        self.color_var = tk.StringVar(value="")
        self.casual_var = tk.BooleanVar(value=False)
        self.formal_var = tk.BooleanVar(value=False)
        self.sporty_var = tk.BooleanVar(value=False)

        self.create_widgets()

    def create_widgets(self):
        self.questionnaire_frame = ttk.Frame(self.root, padding=20)
        self.questionnaire_frame.grid(row=0, column=0, sticky="nsew")

        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)
        self.questionnaire_frame.columnconfigure(0, weight=1)

        ttk.Label(
            self.questionnaire_frame,
            text="Trouvons ton style",
            font=("TkDefaultFont", 16, "bold"),
        ).grid(row=0, column=0, sticky="w", pady=(0, 20))

        color_frame = ttk.LabelFrame(
            self.questionnaire_frame,
            text="Couleur préférée",
            padding=10,
        )
        color_frame.grid(row=1, column=0, sticky="ew", pady=(0, 15))
        color_frame.columnconfigure(0, weight=1)

        ttk.Radiobutton(
            color_frame,
            text="Bleu",
            value="Bleu",
            variable=self.color_var,
        ).grid(row=0, column=0, sticky="w")
        ttk.Radiobutton(
            color_frame,
            text="Noir",
            value="Noir",
            variable=self.color_var,
        ).grid(row=1, column=0, sticky="w")
        ttk.Radiobutton(
            color_frame,
            text="Blanc",
            value="Blanc",
            variable=self.color_var,
        ).grid(row=2, column=0, sticky="w")

        styles_frame = ttk.LabelFrame(
            self.questionnaire_frame,
            text="Styles qui t'intéressent",
            padding=10,
        )
        styles_frame.grid(row=2, column=0, sticky="ew", pady=(0, 15))
        styles_frame.columnconfigure(0, weight=1)

        ttk.Checkbutton(
            styles_frame,
            text="Casual",
            variable=self.casual_var,
        ).grid(row=0, column=0, sticky="w")
        ttk.Checkbutton(
            styles_frame,
            text="Chic",
            variable=self.formal_var,
        ).grid(row=1, column=0, sticky="w")
        ttk.Checkbutton(
            styles_frame,
            text="Sportif",
            variable=self.sporty_var,
        ).grid(row=2, column=0, sticky="w")

        self.error_label = ttk.Label(
            self.questionnaire_frame,
            text="",
            foreground="red",
        )
        self.error_label.grid(row=3, column=0, sticky="w", pady=(0, 10))

        self.submit_button = ttk.Button(
            self.questionnaire_frame,
            text="Voir mon profil",
            command=self.show_profile,
        )
        self.submit_button.grid(row=4, column=0, sticky="ew")

    def show_profile(self):
        if not self.color_var.get():
            self.error_label.config(text="Choisis une couleur avant de continuer.")
            return

        styles = self.get_selected_styles()
        styles_text = ", ".join(styles) if styles else "Aucun style sélectionné"

        for widget in self.questionnaire_frame.winfo_children():
            widget.destroy()

        self.questionnaire_frame.columnconfigure(0, weight=1)
        ttk.Label(
            self.questionnaire_frame,
            text="Ton profil",
            font=("TkDefaultFont", 16, "bold"),
        ).grid(row=0, column=0, sticky="w", pady=(0, 20))
        ttk.Label(
            self.questionnaire_frame,
            text=f"Couleur préférée : {self.color_var.get()}",
        ).grid(row=1, column=0, sticky="w", pady=5)
        ttk.Label(
            self.questionnaire_frame,
            text=f"Styles : {styles_text}",
        ).grid(row=2, column=0, sticky="w", pady=5)
        ttk.Button(
            self.questionnaire_frame,
            text="Recommencer",
            command=self.reset_questionnaire,
        ).grid(row=3, column=0, sticky="ew", pady=(20, 0))

    def get_selected_styles(self):
        styles = []

        if self.casual_var.get():
            styles.append("Casual")
        if self.formal_var.get():
            styles.append("Chic")
        if self.sporty_var.get():
            styles.append("Sportif")

        return styles

    def reset_questionnaire(self):
        self.color_var.set("")
        self.casual_var.set(False)
        self.formal_var.set(False)
        self.sporty_var.set(False)

        self.questionnaire_frame.destroy()
        self.create_widgets()


if __name__ == "__main__":
    root = tk.Tk()
    questionnaire_app = QuestionnaireApp(root)
    root.mainloop()
