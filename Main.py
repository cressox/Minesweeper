from Klassen.Interface import *

def centerScreen(height=800, width=1200):
# zentriert die gui im screen des users #

    screen_width, screen_height = root.winfo_screenwidth(), root.winfo_screenheight()
    x_cordinate, y_cordinate= int((screen_width/2) - (width/2)), int((screen_height/2) - (height/2))
    root.geometry(f"{width}x{height}+{x_cordinate}+{y_cordinate-15}")

def setupRoot():
    root.title("Minesweeper")

    centerScreen()
    # zentriert die anwendung auf dem bildschirm des users #

    root.iconbitmap(default="design/img/logo.ico")
    # setzt individuelles logo #

    root.resizable(False, False)
    # fenster kann nicht max/minnimiert werder #

if __name__ == "__main__":
    try:
        root = tk.Tk()
        
        setupRoot()

        newGame = Menu(root)
        
        root.mainloop()

    except FileNotFoundError and tk._tkinter.TclError:
        error = tk.Label(root, text="Fehler, einige Datein können\nnicht gefunden werden, bitte laden\nSie das Projekt erneut herunter.",
                            font=("Gill Sans Nova", 50))

        error.place(relx=0.5, rely=0.5, anchor="center")

        link = tk.Button(root, command=lambda:os.system("start https://github.com/cressox/Minesweeper"),
                            text="https://github.com/cressox/Minesweeper", font=("Gill Sans Nova", 20),
                            bg="darkblue", fg="white", relief="raised", border=5)

        link.place(relx=0.5, rely=0.75, anchor="center")

        root.mainloop()
