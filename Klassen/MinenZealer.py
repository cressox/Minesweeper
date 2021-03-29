import tkinter as tk

class MinenZealer():
    def __init__(self, masterMinenZealer, numOfMine):
        self.master = masterMinenZealer
        self.numOfMine = numOfMine
        self.minen = self.numOfMine
        self.view = tk.Label(masterMinenZealer, width=10, height=2, relief="solid", text=f"Minen: {numOfMine}", font=("Gill Sans Nova", 15))
        self.view.place(relx = 0.98, rely = 0.1, anchor = "se")
    
    def updateZealer(self, opperation=0):
        if (opperation):
        # eine mine weniger aufzudecken #

            self.minen -= 1
            self.view["text"] = f"Minen: {self.minen}"
        
        else:
        # eine mine mehr aufzudecken #

            self.minen += 1
            self.view["text"] = f"Minen: {self.minen}"

    def resetZealer(self):
    # minenzähler wird zurückgesetzt #
    
        self.view.destroy()
        self.view = tk.Label(self.master, width=10, height=2, relief="solid", text=f"Minen: {self.numOfMine}", font=("Gill Sans Nova", 15))
        self.view.place(relx = 0.98, rely = 0.1, anchor = "se")
        self.minen = self.numOfMine
