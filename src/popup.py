import datetime
import tkinter as tk
from object import DataCollector
import os
import socket

def pop_up():
    root = tk.Tk()
    root.withdraw()

    options = ["Sunet", "Localizare", "Date Apelant", "CEVA"]

    top = tk.Toplevel(root)
    top.title("New problem")
    top.geometry("300x350")
    top.attributes("-topmost", 1)

    top.configure(bg="lightgray")

    label = tk.Label(
        top,
        text="Vă rugăm să scrieți mici detalii despre problemă.",
        bg="lightgray")
    label.pack(pady=10)

    dropdown_label = tk.Label(
        top,
        text="Alegeți opțiunea:",
        bg="lightgray",
        width=20
    )
    dropdown_label.pack(pady=5)

    selected_option = tk.StringVar()
    selected_option.set(options[0])
    dropdown = tk.OptionMenu(top, selected_option, *options)
    dropdown.pack(pady=10)

    comment_label = tk.Label(
        top,
        text="Adăugați comentariu:",
        bg="lightgray",
        width=20
    )
    comment_label.pack(pady=5)

    input_text = tk.Text(top, height=5, width=25, wrap=tk.WORD)
    input_text.pack(pady=10)

    result = tk.StringVar()

    def on_ok():
        current_time = datetime.datetime.now()
        my_object = DataCollector(
            user_name=os.getlogin(),
            computer_name=socket.gethostname(),
            index_selected=selected_option.get(),
            comment=input_text.get("1.0", tk.END).strip(),
            date_time=current_time
        )

        result.set(str(my_object))
        top.destroy()

    def on_close():
        top.destroy()

    def create_button(text, command):
        button = tk.Button(
            top,
            text=text,
            command=command,
            width=7,
            height=1,
            relief="flat",
            bg="gray",
            fg="white",
            font=("Arial", 10),
            bd=0,
            highlightthickness=0
        )
        return button

    ok_button = create_button("OK", on_ok)
    close_button = create_button("Close", on_close)

    button_frame = tk.Frame(
        top,
        bg="lightgray",
    )
    button_frame.pack(pady=15)

    ok_button.pack(side=tk.LEFT, padx=55,)
    close_button.pack(side=tk.LEFT, padx=10)

    root.update()
    top.wait_window()

    return result.get()

