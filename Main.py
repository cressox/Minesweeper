from Klassen.Interface import *

def centerScreen():
    window_height, window_width = 800, 1200
    screen_width, screen_height = root.winfo_screenwidth(), root.winfo_screenheight()
    x_cordinate, y_cordinate= int((screen_width/2) - (window_width/2)), int((screen_height/2) - (window_height/2))
    root.geometry(f"{window_width}x{window_height}+{x_cordinate}+{y_cordinate-15}")

def setupRoot():
    root.title("Minesweeper")

    root.iconbitmap(default="design/img/logo.ico")
    # setzt individuelles logo #

    root.resizable(False, False)
    # fenster kann nicht max/minnimiert werder #

    centerScreen()
    # zentriert die anwendung auf dem bildschirm des users #

if __name__ == "__main__":
    root = tk.Tk()
    
    setupRoot()

    newGame = Menu(root)
    
    root.mainloop()