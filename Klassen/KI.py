import tkinter as tk
import random

"""
Die KI muss in manchen fällen raten, da es 50/50 oder nicht 100% Sitouationen gibt.
Dann wählt sie das feld mit der ihr bekannt niedrigsten Warscheinlichkeit und färbt es 
gelb ein. Somit ist Gelb das Zeichen, dass die KI nicht 100% sicher ist.
"""

class KI():
    def __init__(self, master):
        self.hint = tk.Button(master, text="Hinweis", width=10, pady=2.5, relief="solid", font=("Gill Sans Nova", 15))
        self.hint.place(relx = 0.98, rely = 0.2, anchor = "se")
        # hinweis button #
    
    @staticmethod
    def getHint(cellAsList):
    # gibt user einen visuellen hinweis #

        trys = []

        minProb = 100
        # hoher vergleichswert für warscheinlichkeiten #
        # wird als oberste grenze verwendet #

        bg = cellAsList[0].view["bg"]
        # alle zellen sollten den selben bg haben, damit ein hinweis gegeben werden kann #
        # somit sind nicht mehrere hinweise gleichzeitig möglich (bzw. spamen) #

        tmpCell = None
        # später zelle die verändert wird #
        
        for i in cellAsList:
        # geht alle zellen durch #

            if i.view["bg"]!=bg:
            # alle sollen den selben bg haben, außer berührte zellen #

                if i.untoucht:
                # eine unberührte zelle hat einen anderen bg #
                #  also gibt es bereits einen hinweis #

                    return

                else:
                # eine berührte zelle hat einen anderen bg #

                    i.view["bg"]=bg
                    # ihr bg wird wieder normal #
                    # ein neuer hinweis wird danach gegeben #

            if i.probability != 1 and i.untoucht:
            # nur unberührte zellen werden betrachtet #
            # zellen mit prob = 1 werden auch übersprungen, #
            # da sie definitiv minen sind #

                if (i.tmpProb+i.baseProb) < minProb:
                # minimale warscheinlichkeit wird aktualisiert #
                # wenn gesamtwarscheinlichkeit der aktuellen zelle #
                # geringer ist #

                    minProb = (i.tmpProb+i.baseProb)
                    tmpCell = i

        OpenCells = False
        # ob es offenen zellen gibt #

        for i in cellAsList:
        # zählt offenen zellen und checkt ob #
        # es mehr als eine zelle mit der minProb gibt #

            if (i.tmpProb+i.baseProb)==minProb and i.untoucht and i.probability != 1:
                trys.append(i)
            
            elif not i.untoucht:
                OpenCells = True
        
        tmpCell = trys[random.randint(0, len(trys)-1)]
        # eine zufällige zelle aller zellen die die #
        # minimale warscheinlichkeit haben #

        if minProb and OpenCells:
        # wenn minProb != 0, dann gibt es keine zelle #
        # die sicher keine mine ist, und es muss min eine zelle #
        # offen sein, denn sonst ist es immer sicher keien mine #

            tmpCell.view.config(bg="yellow")
            # weil die zelle nicht sicher ist, wird sie #
            # gelb eingefärbt, statt grün #
    
        else:
        # minProb == 0, deswegen gibt es eine sichere zelle #

            tmpCell.view.config(bg="green")
            # zelle wird grün eingefärbt weil sie sicher ist #

    @staticmethod
    def updateBaseProb(numOfMine, cellAsList):
    # base warscheinlichkeit #
    # einfach nach laplace anzahl der minen #
    # durch anzahl der übrigen zellen #

        cellsLeft = 0
        # anzahl der übrigen zellen #

        for cell in cellAsList:
        # geht alle zellen durch #

            if cell.untoucht:
            # zelle ist ungeöffnet, also übrig #

                cellsLeft += 1

        for cell in cellAsList:
        # geht alle zellen durch #

            if cell.probability == 0:
            # wenn eine zelle definitiv keine mine ist #

                continue

            if cell.untoucht or not cell.probability == 1 and cellsLeft:
            # warscheinlichkeit wird aktualisiert #
            
                cell.probability += (numOfMine/cellsLeft)-cell.baseProb
                # gesamtwarscheinlichkeit #

                cell.baseProb = numOfMine/cellsLeft
                # laplace #

            if not cell.untoucht:
            # wenn zelle offen ist wird ihre #
            # warscheinlichkeit auf 0 gesetzt #

                cell.baseProb = 0
                cell.tmpProb = 0
                cell.probability = 0

    @staticmethod
    def updateTmpProb(cellAsList):
    # temporäre warscheinlichkeit #

        for zelle in cellAsList:
        # tmp warscheinlichkeit auf 0 setzten #
        # als reset und dann wird sie neu errechnet #

            zelle.tmpProb = 0

        for zelle in cellAsList:
        # geht alle zellen durch #

            neigLeft = 0
            # anzahl der übrigen geschlossenen nachbarn einer zelle #

            if zelle.var in [i for i in "123456789"] and not zelle.untoucht:
            # zelle ist zahl und nicht offen #

                number = int(zelle.var)
                # nummer der zelle #

                for i in zelle.neighbor:
                # geht nachbarn der zelle durch #

                    if cellAsList[i].untoucht:
                    # nachbar ist ungeöffnet #

                        neigLeft += 1

                if neigLeft == number:
                # anzahl der nachbarn ist anzahl der #
                # minen die in den nachbarn liegen #
                # also alles minen #

                    for i in zelle.neighbor:
                    # geht nachbarn durch #

                        if cellAsList[i].untoucht:
                        # nur die ungeöffneten nachbarn werden aktualisiert #
                            
                            cellAsList[i].tmpProb = 0.5
                            cellAsList[i].probability = 0.5
                            cellAsList[i].probability = 1
                            # gesamtwarscheinlichkeit auf 1 #
                
                else:
                # anzahl der nachbarn ist nicht anzahl der #
                # minen die in den nachbarn liegen #
                # also nicht alles minen #

                    for i in zelle.neighbor:
                    # geht nachbarn durch #

                        if cellAsList[i].untoucht:
                        # nur die ungeöffneten nachbarn werden aktualisiert #

                            cellAsList[i].tmpProb += number/neigLeft
                            # gesamtwarscheinlichkeit bekommt laplace warscheinlichkeit dazu #
                            # anzahl der möglichen minen durch anzahl der verbleibenden minen #

        for cell in cellAsList:
        # geht alle zellen durch #
        # hier wird überprüft ob es zellen gibt wo die anzahl der bekannten minen in den #
        # nachbarn gleich ist mit der zahl der zelle deren nachbarn betrachtet werden, #
        # denn dann sind alle anderen zellen in den nachbarn keine minen #

            tmpMinen = []
            # liste von minen #

            for i in cell.neighbor:
            # geht nachbarn der zelle durch #

                    if cellAsList[i].probability == 1 and not cell.untoucht: 
                    # nachbar ist eine mine und markiert #

                        tmpMinen.append(i)

            if str(len(tmpMinen)) == cell.var:
            # alle minen in den nachbarn sind bekannt #

                for i in cell.neighbor:
                # geht alle nachbarn erneut durch #

                    if i in tmpMinen:
                    # zelle ist eine mine #

                        cellAsList[i].tmpProb = 0.5
                        cellAsList[i].probability = 0.5
                        cellAsList[i].probability = 1
                        # gesamtwarscheinlichkeit #
                    
                    if i not in tmpMinen and cellAsList[i].untoucht:
                    # zelle kann keine mine sein #

                        cellAsList[i].probability = 0
                        cellAsList[i].baseProb = 0
                        cellAsList[i].tmpProb = 0
                        # alle warscheinlichkeiten auf 0 #
