import time, os

from Klassen.KI import *
from Klassen.MinenZealer import *
from Klassen.Timer import *


class Menu():
    def __init__(self, master):
        self.master = master
        img = tk.PhotoImage(file=f"design/img/bg_2.png")
        # hintergrundbild #

        self.bg = tk.Label(master, image=img)
        self.bg.image = img
        self.bg.place(x=0,y=0)
        # setzt hintergrund #

        self.view = tk.LabelFrame(master, bg="#b4b4b4", width=800, height=500, relief="solid")
        self.view.place(relx=0.5, rely=0.5, anchor="center")
        # fläche des menü #
        
        self.menueBtn = [   
        # standart menü button #              
                            tk.Entry(self.view, bg="white", relief="solid", font=("Gill Sans Nova", 20), cursor="xterm"),
                            tk.Button(self.view, command=self.setSpielModus, bg="#cdcbcb", relief="solid", pady=12, padx=130, text="Neues Spiel", font=("Gill Sans Nova", 20)),
                            tk.Button(self.view, command=self.highScoore, bg="#cdcbcb", relief="solid", pady=12, padx=140, text="Highscore", font=("Gill Sans Nova", 20)),
                            tk.Button(self.view, command=lambda:os.system("start Anleitung.pdf"), bg="#cdcbcb", relief="solid", pady=12, padx=142, text="Anleitung", font=("Gill Sans Nova", 20))]

        for i in range(len(self.menueBtn)):
        # standart menue button werden gesetzt #
            self.menueBtn[i].place(relx=0.5, rely=0.2*(i+1), anchor="center")

        self.spielModi = [  
        # button bei spielmodi auswahl #
                            tk.Button(self.view, command=lambda:self.newGame(master=self.master, mode="einfach", row=8, column=8, numOfmine=10), bg="#cdcbcb", relief="solid", pady=12, padx=158, fg="#47ab42", text="Einfach", font=("Gill Sans Nova", 20)),
                            tk.Button(self.view, command=lambda:self.newGame(master=self.master, mode="mittel", row=16, column=16, numOfmine=40), bg="#cdcbcb", relief="solid", pady=12, padx=164, fg="#d0952c", text="Mittel", font=("Gill Sans Nova", 20)),
                            tk.Button(self.view, command=lambda:self.newGame(master=self.master, mode="schwer", row=30, column=16, numOfmine=99), bg="#cdcbcb", relief="solid", pady=12, padx=155, fg="#d44343", text="Schwer", font=("Gill Sans Nova", 20)),
                            tk.Button(self.view, command=self.customGame, bg="#cdcbcb", relief="solid", fg="#c72ed4", pady=12, padx=99, text="Benutzerdefiniert", font=("Gill Sans Nova", 20))]

        self.customFactors = [  
        # überschriften von breite, höhe und minen bei benutzerdefinierten eingabe #
                                tk.Label(self.view, text="Breite:\t", font=("Gill Sans Nova", 20), bg="#b4b4b4"),
                                tk.Label(self.view, text="Höhe:\t", font=("Gill Sans Nova", 20), bg="#b4b4b4"),
                                tk.Label(self.view, text="Minen:\t", font=("Gill Sans Nova", 20), bg="#b4b4b4")]

        self.customScales = [   
        # scales von breite, höhe und minen bei benutzerdefinierten eingabe #
                                tk.Scale(self.view, command=lambda i:self.updateScale(0), orient="horizontal", length=610, from_=2, to=30, relief="sunken", showvalue=0),
                                tk.Scale(self.view, command=lambda i:self.updateScale(1), orient="horizontal", length=610, from_=2, to=30, relief="sunken", showvalue=0),
                                tk.Scale(self.view, command=lambda i:self.updateScale(2), orient="horizontal", length=610, from_=1, to=800, relief="sunken", showvalue=0)]
    
        self.customDigits = [  tk.Label(self.view, text=f"{self.customScales[i].get()}", relief="solid", width=3, font=("arial", 15)) for i in range(3)]
        # zahlen von breite, höhe und minen bei benutzerdefinierten eingabe #

        self.start = tk.Button(self.view, text="Spiel starten", relief="solid", font=("arial", 15), command=self.startCustomGame)
        # spiel starten button #

        self.back = tk.Button(self.view, text="Zurück", relief="solid", font=("arial", 15))
        self.back.place(relx=0.2, rely=0.9)
        # zurück button #

        self.usrName = ""
        # nutzername #

        self.usrNameEntry = self.menueBtn[0]
        self.usrNameEntry.insert(0, "Nutzername")
        # eingabefeld für nutzernamen #

    def newGame(self, master, row, column, numOfmine, mode=None):
        self.destroyMenue()
        # clean menue #

        field = SpielFeld(master=master, bg=self.bg, menu=self.view, menuBtn=self.menueBtn, usrName=self.usrNameEntry.get(), mode=mode, column=column, row=row, numOfMine=numOfmine)
        # field init #

        field.drawField()
        # field zeichnen #
        
        field.timer.updateTimer(0, 0, 0)
        # start timer #

    def highScoore(self):
    # bildschrim interface bei highscore abfrage #

        itemList = []
        # die itemList besteht aus allen tkinter objekten, aus dem aktuellen screen sind #

        for i in self.menueBtn:
            i.place_forget()

        highscoores = pickle.load(open('highscoores.txt', 'rb'))
        # läd highscores aus txt datei #

        headline = tk.Label(self.view, text="Highscores", font=("Gill Sans Nova", 50), bg="#b4b4b4")
        headline.place(relx=0.5, rely=0.12, anchor="center")
        # setzt überschift #

        scrollBarY = tk.Scrollbar(self.view)
        scrollBarY.place(relx=0.83, rely=0.55, anchor="center", height=275)
        # setzt vertikale scrollbar #

        scrollBarX = tk.Scrollbar(self.view, orient="horizontal")
        scrollBarX.place(relx=0.48, rely=0.87, anchor="center", width=475)
        # setzt horizontale scrollbar #

        highList = tk.Listbox(self.view, yscrollcommand=scrollBarY.set, xscrollcommand=scrollBarX.set, font=("Gill Sans Nova", 15), height=10,  width=50, relief="solid")
        # liste mit allen rekorden in allen 4 modi #
        
        for mode in ["einfach", "mittel", "schwer", "benutzerdefiniert"]:
            highList.insert(tk.END, f"  {mode.upper()}:")
            for i in range(5):
            # top 5 zeiten #

                if (highscoores[mode][i]['time'] == "99:99:99"):
                # wenn kein neuer eintrag gefunden wurde #

                    highList.insert(tk.END, "    Noch kein Rekord")
                    continue

                else:
                    userTime = highscoores[mode][i]['time']
                
                highList.insert(tk.END, f"    {i+1}. Time: {userTime} | Grid: {highscoores[mode][i]['grid']} | {highscoores[mode][i]['name']}    ")
                # nimmt rekord mit in highList auf #

            highList.insert(tk.END, "")

        highList.place(relx=0.48, rely=0.55, anchor="center")

        scrollBarY.config(command=highList.yview )
        scrollBarX.config(command=highList.xview )
        # aktivier scrollbars #

        itemList += [scrollBarY]+[highList]+[headline]+[scrollBarX]
        self.back["command"] = lambda:Menu.backTo(itemList ,self.menueBtn)
        # aktiviert den zurück button #
        # currentList = sind alle objekte des highscore screen #
        # nextList = sind die menü button #  

    def updateScale(self, id):
    # bei auswahl der faktoren im benutzerdefinierten modus werden die scales aktualisiert #
        
        self.customDigits[id]["text"] = self.customScales[id].get()

    def destroyMenue(self):
    # blendet menü aus #
        self.view.place_forget()

        for i in self.menueBtn:
            i.place_forget()
        
        for i in self.spielModi:
            i.place_forget()
        
    def setSpielModus(self):
        self.usrName = self.usrNameEntry.get()
        # setzt nutzernamen #

        itemList = []
        # die itemList besteht aus allen tkinter objekten, aus dem aktuellen screen sind #
        
        for i in self.menueBtn:
        # blendet menü button aus #
            i.place_forget()

        for i in range(len(self.spielModi)):
        # blendet spielmodi button ein #
            self.spielModi[i].place(relx=0.5, rely=0.2*(i+1), anchor="center")
            itemList.append(self.spielModi[i])

        self.back["command"] = lambda:Menu.backTo(currentList=itemList ,nextList=self.menueBtn)
        # aktiviert den zurück button #
        # currentList = sind die aktuellen button #
        # nextList = sind die vorherigen menü button #

    def customGame(self):
        itemList = []
        # enthält später alle tkinter objekte aus diesem screen #

        for i in self.spielModi:
        # disable spielmodi #

            i.place_forget()

        for i in range(len(self.customFactors)):
        # place tkinter obj for the custom screen #

            self.customFactors[i].place(relx=0.2, rely=0.25*(i+0.5), anchor="e")
            self.customScales[i].place(relx=0.85, rely=0.25*(i+1), anchor="e")
            self.customDigits[i].place(relx=0.92, rely=0.25*(i+1), anchor="e")
            # blendet die 3 scales und beschriftungen ein für die benutzerdefinierte eingabe #

            itemList += [self.customFactors[i]]+[self.customScales[i]]+[self.customDigits[i]]

        self.start.place(relx=0.02, rely=0.9)
        # setzt den spiel starten button #

        itemList += [self.start]

        self.back["command"] = lambda:Menu.backTo(itemList ,self.spielModi)
        # aktiviert den zurück button #
        # currentList = sind die scale objekte und der start button #
        # nextList = sind die vorherigen spielmodi button #
    
    def startCustomGame(self):
        itemList = [self.start]+self.customDigits+self.customFactors+self.customScales
        # alle tkinter objekte aus diesem screen #

        for i in itemList:
        # blendet alles aus #
            i.place_forget()

        self.newGame(master=self.master, mode="benutzerdefiniert", row=self.customScales[0].get(), column=self.customScales[1].get(), numOfmine=self.customScales[2].get())
        # startet ein benutzerdefiniertes spiel #

    @staticmethod
    def backTo(currentList, nextList):
    # zurück button funktion #

        for i in currentList:
        # ausblenden #
            i.place_forget()

        for i in range(len(nextList)):
        # einblenden #
            nextList[i].place(relx=0.5, rely=0.2*(i+1), anchor="center")

    @staticmethod
    def popScreen(master, text="verloren", mode="win/lose", sec=1):
    # animiertes fenster wenn verloren/gewonnen #

        square = tk.Label(master, relief="solid", bg="white", padx=2, pady=1)
        square.place(relx = 0.5, rely = 0.5, anchor = "center")
        # erstellen und setzten des fensters #

        for i in range(20):
        # zoom #
            square["padx"] *= 1.25
            square["pady"] *= 1.25
            master.update()
            time.sleep(0.00000000025)

        square.config(text=text, font=(20))
        # setzt text z.B. "verloren" #

        master.update()

        time.sleep(sec)
        # lässt das fenster stehen, das der user es lesen kann #

        square.destroy()
        # zerstört das fenster wieder #

class SpielFeld():
    def __init__(self, master, usrName, bg, menu, menuBtn, mode, column=0, row = 0, numOfMine = 0):
        self.master = master
        self.bg = bg
        self.menu = menu
        self.menuBtn = menuBtn
        self.mode = mode
        self.column = column
        self.row = row
        self.numOfMine = numOfMine

        self.grid = tk.LabelFrame(self.master)
        self.grid.place(relx = 0.5, rely = 0.5, anchor = "center")
        # gitter in dem die minesweeper zellen platziert werden #

        self.newTry = tk.Button(master, command=self.restart, text="Neustarten", width=10, pady=2.5, relief="solid", font=("Gill Sans Nova", 15))
        self.newTry.place(relx = 0.98, rely = 0.97, anchor = "se")
        # neustarten button #

        self.back = tk.Button(master, command=self.exitGame, text="Beenden", width=10, pady=2.5, relief="solid", font=("Gill Sans Nova", 15))
        self.back.place(relx = 0.12, rely = 0.97, anchor = "se")
        # zurück button #

        self.ki = KI(master)
        self.timer = Timer(masterTimer=master, mode=mode, usrName=usrName, usrGrid=f"{row}x{column}")        
        self.minenZealer = MinenZealer(masterMinenZealer=master, numOfMine=numOfMine)
        
    def drawField(self):
    # zeichnet spielfeld #

        img = tk.PhotoImage(file=f"design/img/bg_3.png")
        self.bg.config(image=img)
        self.bg.image = img
        # setzt spielfeld hintergrund #

        plainImg = tk.PhotoImage(file="design/python-button/cell_gray.png")
        # standart bild für jede zelle #

        global cellAsList
        # cellAsList wird nur einmal initialisiert und dann bleibt sie immer gleich #
        # deshalb wird sie global gesetzt um unkompliziert zuzgreifen aus anderen klassen #

        cellAsList = [Zelle(grid=self.grid,
                            img=plainImg,
                            master=self.master,
                            num=i,
                            buildField=True,
                            numOfMine=self.numOfMine,
                            minenZealer=self.minenZealer,
                            mode=self.mode,
                            timer=self.timer,
                            probability=self.numOfMine/(self.row*self.column)) for i in range(self.column*self.row)]
        # erstellt liste mit allen zellen #

        self.ki.hint.config(command=lambda:KI.getHint(cellAsList))
        # übergibt der ki die liste mit zellen als pointer #

        for i in range(len(cellAsList)):
            cellAsList[i].getNeighbor(numCols=self.column, numRows=self.row) 
            # findet die nachbarn jeder zelle #

            cellAsList[i].view.grid(row=i//self.row, column=i%self.row)
            # plaziert zelle #

            cellAsList[i].image = plainImg
            # setzt bild der zelle #

            cellAsList[i].view.bind(sequence='<Button-1>', func=cellAsList[i].linksklick) 
            # linksklick event #

            cellAsList[i].view.bind(sequence='<Button-3>', func=cellAsList[i].rechtsklick) 
            # rechtsklick event #

            self.master.update()
            # aktualisiert damit zelle sichtbar wird #

        for i in cellAsList:
        # macht die zellen klickbar, wenn feld fertig aufgebaut ist #
            i.buildField = False

    def restart(self):
    # neustart des spiels #

        self.grid.destroy()
        # zerstört aktuelles grid #

        self.timer.resetTimer()
        # setzt timer zurück #

        self.minenZealer.resetZealer()
        # setzt minenzealer zurück #

        self.grid = tk.LabelFrame(self.master)
        self.grid.place(relx = 0.5, rely = 0.5, anchor = "center")
        # erstellt und setzt neues feld #

        self.drawField()
        # zeichnet neues feld #

        self.timer.startTimer()
        # start timer #

    def exitGame(self):
    # zurück aus dem spiel #

        img = tk.PhotoImage(file=f"design/img/bg_2.png")
        self.bg.config(image=img)
        self.bg.image = img
        # setzt menü hintergrund #

        self.menu.place(relx=0.5, rely=0.5, anchor="center")
        # setzt menü #

        itemList = [self.grid, self.timer.view, self.back, self.minenZealer.view, self.newTry, self.ki.hint]
        # enthält alle tkinter objekte aus diesem screen #

        Menu.backTo(currentList=itemList, nextList=self.menuBtn)
        # aktiviert den zurück button #
        # currentList = sind alle elemente aus einem laufendem spiel #
        # nextList = sind die menü button #
        
    
    @staticmethod
    def checkGame(master, numOfMine, timer, lose=False):
    # überprufung ob gewonnen oder verloren #
        if (lose):
        # verloren #
            Menu.popScreen(master, text="verloren")
            # animation #

            for i in cellAsList:
            # alle zellen sind nicht mehr klickbar #
                i.untoucht = False

        openCell, flaggedMine = 0, 0
        for cell in cellAsList:
            if (cell.untoucht == False):
            # offene zellen #
                openCell+=1

            elif (cell.flagged and cell.var=="mine"):
            # richtig markierte mine #
                flaggedMine += 1

        if ((openCell==len(cellAsList)-numOfMine) or flaggedMine==numOfMine):
        # gewonnen wenn: #
        #   a) nur noch minen als felde übrig sind #
        #   b) alle minen richtig markirt wurden  #

            timer.running = False
            timer.win = True
            # stoppt timer #

            for i in cellAsList:
            # alle zellen sind nicht mehr klickbar #
                i.untoucht = False

            Menu.popScreen(master, text="gewonnen")
            # animation #

class Zelle():
    def __init__(self, master, grid, img, numOfMine, minenZealer, timer, probability, buildField, mode=None, num=0, var=""):
        self.master = master
        # master des spielfeld #

        self.mode = mode
        # einfach, mittel, schwer, benutzerdefiniert #

        self.minenZealer = minenZealer
        self.timer = timer
        self.grid = grid
        # master der zellen, sie liegen im grid #

        self.neighbor = []
        # nachbar zellen (min 3 max 8) #
        
        self.mine, self.unkown, self.flagged, self.cell_gray = False, False, False, True
        # ob mine, flagged, fragezeichen oder unmarkiert #

        self.var = var
        # open, flag, mine #

        self.numOfMine = numOfMine
        # anzahl der minen #

        self.num = num
        # position im grid #

        self.view = tk.Label(master=grid, width=20, heigh=20, textvariable=num, image=img)
        self.buildField = buildField
        # boolean der angibt ob das spielfeld fertig aufgebaut ist #

        self.untoucht = True
        # wurde zelle geklickt #

        self.tmpProb = 0
        self.baseProb = probability
        self.probability = probability
        # warscheinlichkeits belegungen für die KI #

    def getNeighbor(self, numCols, numRows):
    # findet nachbarn einer zelle #
        cell = self.num
        #   jede zelle hat eine nummer, beginnend bei 0 bis max 900 bei 30x30 grid
        #   linke zelle -1, rechte zelle +1
        #   zelle drüber und drunter analog, hier wird +- (Anazahl der Rows) gerechnet um zeile zu überspringen

        #   ränder und ecken sind ausnahmen, welche im folgenden abgefangen wurden

        if (cell%numRows==0):
        #####   linker rand    #####

            if (cell==0):
            #####   ecke links oben    #####

                self.neighbor = [cell+1, (cell+numRows), (cell+numRows)+1]
                return

            elif (cell==(numRows*numCols)-numRows):
            #####   ecke links unten    #####

                self.neighbor = [cell+1, (cell-numRows), (cell-numRows)+1]
                return
            
            self.neighbor = [cell+1, (cell-numRows), (cell-numRows)+1, (cell+numRows), (cell+numRows)+1]
            
        elif ((cell-(numRows-1))%numRows==0):
        #####   rechter rand    #####

            if (cell==numRows-1):
            #####   ecke rechts oben    #####

                self.neighbor = [cell-1, (cell+numRows)-1, (cell+numRows)]
                return
            
            elif (cell==((numRows*numCols)-1)):
            #####   ecke rechts unten    #####

                self.neighbor = [cell-1, (cell-numRows)-1, (cell-numRows)]
                return
            
            self.neighbor = [cell-1, (cell-numRows)-1, (cell-numRows), (cell+numRows)-1, (cell+numRows)]

        elif (cell<=(numRows-1)):
        #####   oberer rand    #####

            self.neighbor = [cell-1, cell+1, (cell+numRows)-1, (cell+numRows), (cell+numRows)+1]
            return
            
        elif (cell>=((numRows*numCols)-numRows)):
        #####   unterer rand    #####

            self.neighbor = [cell-1, cell+1, (cell-numRows)-1, (cell-numRows), (cell-numRows)+1]
            return
        
        else:
        #####   keine ausnahme    ######

            self.neighbor = [cell-1, cell+1, (cell-numRows)-1, (cell-numRows), (cell-numRows)+1, (cell+numRows)-1, (cell+numRows), (cell+numRows)+1]
    
    def linksklick(self, event):
        self.view.config(bg="white")
        # zelle wird aufgedeckt #

        if (not self.flagged and not self.unkown and not self.buildField):
        # nur wenn ein unmarkiertes feld angeklickt wird #

            def setMine(firstCell):
            # setzt die minen nachdem der erste klick gemacht wurde #
            # firstCell = erste zelle ist ausnahme (kann keine mine sein) #

                for i in cellAsList:
                # alle auf plain #

                    i.var = "plain"
                    # sind alle leere felder vorerst #

                mineSet = 0
                # anzahl der minen die gesetzt wurden #

                while(mineSet<self.numOfMine):
                # minen zufällig verteilen #

                    totalCells = len(cellAsList)
                    # anzahl der zellen #

                    tmpCell = random.randint(0,(totalCells-1))
                    # zufällige zelle wird bestimmt #

                    if (cellAsList[tmpCell].var != "mine" and tmpCell!=firstCell):
                    # nur leere zellen und nicht die erste können minen werden #

                        cellAsList[tmpCell].var = "mine"
                        mineSet += 1

                        for cell in cellAsList[tmpCell].neighbor:
                        # alle nachbarn werden um 1 erhöht #

                            if (cellAsList[cell].var!="mine"):
                            # minen können nicht eine zahl zugewiesen bekommen #

                                if(cellAsList[cell].var in [i for i in "12345678"]):
                                # wenn .var bereits eine zahl ist #
                                # ist bereits eine mine in der nähe #

                                    cellAsList[cell].var  = str(int(cellAsList[cell].var)+1)
                                    # .var ist str #
                                    # wert der zelle wird um 1 erhöht da eine mine dazu kam #

                                else:
                                # keien mine bisher in der nähe #

                                    cellAsList[cell].var = "1"
                                    # einmalig wird .var auf 1 gesetzt #
                    
            def checkCell(cell=self.var, num=self.num):
            # was unter der zelle lag #

                def openPlain(neighbor):
                # rekursives öffnen bei klick einer leeren zelle #
                # geht alle nachbarn durch und öffnet sie ggf. #

                    for nCell in neighbor:
                    # geht alle nachbarn durch #

                        if (cellAsList[nCell].var=="plain"):
                        # nachbar ist auch plain, also muss er geöffnet werden #


                            if (cellAsList[nCell].flagged==True):
                            # falls markierte zellen geöffnet werden, #
                            # muss der minenzähler geupdated werden #

                                cellAsList[nCell].flagged = False
                                self.minenZealer.updateZealer(opperation=0)
                                # opperation 0 zieht eine mine ab #

                            cellAsList[nCell].untoucht = False
                            # zelle wurde geöffnet und somit berührt #

                            img = tk.PhotoImage(file="design/python-button/plain_gray.png")
                            cellAsList[nCell].var = "open"
                            cellAsList[nCell].view["image"]=img
                            cellAsList[nCell].image = img
                            # updaten des design der zell zu offen #

                            openPlain(cellAsList[nCell].neighbor)
                            # rekursiver aufruf #

                        elif (cellAsList[nCell].var in [i for i in "12345678"]):
                        # nachbarzelle ist eine zahl #

                            if (cellAsList[nCell].flagged==True):
                            # falls markierte zellen geöffnet werden, #
                            # muss der minenzähler geupdated werden #

                                cellAsList[nCell].flagged = False
                                self.minenZealer.updateZealer(opperation=0)
                                # opperation 0 zieht eine mine ab #

                            cellAsList[nCell].untoucht = False
                            # zelle wurde geöffnet und somit berührt #
                            
                            img = tk.PhotoImage(file=f"design/python-button/{cellAsList[nCell].var}_gray.png")
                            cellAsList[nCell].view["image"]=img
                            cellAsList[nCell].image = img
                             # updaten des design der zell zu entsprechender zahl #
                             # kein rekursiver auruf mehr für die nachbarn dieser zahl #

                        

                if (cell != "open" and self.untoucht):
                # nur ungeöffnete felder #

                    if (cell == ""):
                    # erste zelle hat noch kein .var#
                    
                        setMine(firstCell=self.num)
                        # setzt alle minen #

                        if (cellAsList[num].var=="plain"):
                        # wenn erste zelle leer ist #

                            openPlain(cellAsList[num].neighbor)
                            # öffnet rekursiv alle nacharzellen #
                            # die auch leer sind #
                        
                        else:
                        # wenn erste zelle eine zahl ist #

                            img = tk.PhotoImage(file=f"design/python-button/{cellAsList[num].var}_gray.png")
                            self.view["image"] = img
                            self.view.image = img
                            # design update #

                    elif (cell == "plain"): 
                    # leeres feld aber nicht erste zelle #

                        img = tk.PhotoImage(file=f"design/python-button/plain_gray.png")
                        self.view["image"] = img
                        self.view.image = img
                        # design update #

                        openPlain(self.neighbor)
                        # öffnet rekursiv alle nacharzellen #
                        # die auch leer sind # 
                    
                    elif (cell == "mine"):
                    # mine wurde geöffnet #
                    # spiel somit verloren #

                        self.timer.running = False
                        # stoppt timer #

                        for i in cellAsList:
                        # alle zellen werden aufgedeckt #
                        
                            i.view.config(bg="white")
                            
                            if i.var == "open" or i is self: continue
                            # offene zellen und geöffnete minen werden übersprungen #

                            else:
                                img = tk.PhotoImage(file=f"design/python-button/{i.var}_gray.png")
                                i.view["image"] = img
                                i.view.image = img
                                # design update #

                                i.untoucht = False
                                # zelle wurde geöffnet und somit berührt #
                                

                        img = tk.PhotoImage(file="design/python-button/red_mine.png")
                        self.view["image"] = img
                        self.view.image = img
                        # geöffnete mine rot einfärben #

                        SpielFeld.checkGame(master=self.master, numOfMine=self.numOfMine, timer=self.timer, lose=True)
                        # spiel beenden #

                    else:
                    # zahl wurde geöffnet #

                        img = tk.PhotoImage(file = f"design/python-button/{cell}_gray.png")
                        self.view["image"] = img
                        self.view.image = img
                        # design update #
                
                self.untoucht = False
                # zelle wurde geöffnet und somit berührt #

            
            checkCell()
            # zelle checken #

            KI.updateBaseProb(numOfMine=self.numOfMine, cellAsList=cellAsList)
            KI.updateTmpProb(cellAsList=cellAsList)
            # mit jedem öffnen einer zelle bekommt die KI informationen #
            # sie updated dann warscheinlichkeiten um die zellen einzuschätzen #


        SpielFeld.checkGame(master=self.master, numOfMine=self.numOfMine, timer=self.timer)
        # checkt ob das spiel gewonnen wurde #
    
    def rechtsklick(self, event):
        #print(f"base: {self.baseProb}\ntmp: {self.tmpProb}\nprob: {self.probability}")
        if (self.untoucht and not self.buildField):
            if (self.flagged):
            # flagge wurde geklickt #
                self.flagged = False
                self.unkown = True
                img = tk.PhotoImage(file="design/python-button/unknown_gray.png")
                event.widget.config(image = img)
                event.widget.image = img
                self.minenZealer.updateZealer(opperation=0)

            elif (self.unkown):
            # fragezeichen wurde geklickt #
                self.unkown = False
                self.cell_gray = True
                img = tk.PhotoImage(file="design/python-button/cell_gray.png")
                event.widget.config(image=img)
                event.widget.image = img

            elif (self.cell_gray):
            # leere zelle wurde geklickt #
                self.cell_gray = False
                self.flagged = True
                img = tk.PhotoImage(file="design/python-button/flag_gray.png")
                event.widget.config(image=img)
                event.widget.image = img
                self.minenZealer.updateZealer(opperation=1)

        SpielFeld.checkGame(master=self.master, numOfMine=self.numOfMine, timer=self.timer)
        # checkt ob gewonnen #
