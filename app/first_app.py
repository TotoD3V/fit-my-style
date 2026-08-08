import tkinter as tk

class FitMyStyleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Fit My Style")
        self.create_widgets()

    def create_widgets(self):
        # Create a label
        self.label = tk.Label(self.root, text="Welcome to Fit My Style!")
        self.label.pack(pady=10)

        # Create a button
        self.button = tk.Button(self.root, text="Get Started", command=self.get_started)
        self.button.pack(pady=10)

    def get_started(self):
        # Placeholder for the action when the button is clicked
        self.label.config(text="Let's find your style!")

root = tk.Tk()
fit_my_style_app = FitMyStyleApp(root)
root.mainloop()