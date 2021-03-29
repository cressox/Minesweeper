import tkinter as tk
import pickle

class Timer():
    def __init__(self, masterTimer, mode, usrGrid, usrName="unkown"):
        self.usrGrid = usrGrid
        # 8x8 oder 16x16 oder 30x30 usw.

        self.master = masterTimer
        # tkinter master #

        self.endTime = "00:00:00"
        self.running = True
        # timer läuft #

        self.mode = mode
        # einfach, mittel schwer, benutzerdefiniert #

        self.win = False
        self.usrName = usrName

        self.view = tk.Label(masterTimer, width=10, height=2, relief="solid", text="00:00:00", font=("Gill Sans Nova", 15))
        self.view.place(relx = 0.12, rely = 0.1, anchor = "se")
        # tkinter objekt im screen sichtbar #
    
    def updateTimer(self, sec=0, minute=0, hour=0, reset=False):
        if (reset):
        # nach einer sekunde beginnt der timer sich rekusiv zu erhöhen #

            self.view.after(1000, lambda:self.updateTimer(sec, minute, hour))

        elif (self.running and self.view!=None):
        # solange das spiel läuft #

            sec += 1
            if (sec==60):
            # kann maximal 59 sein #

                sec = 0
                minute += 1

                if (minute==60):
                # kann maximal 59 sein #

                    minute = 0
                    hour += 1

            newTime = f"{'0'*(len(str(hour))%2)}{hour}:{'0'*(len(str(minute))%2)}{minute}:{'0'*(len(str(sec))%2)}{sec}"
            # folgender format: XX:XX:XX wird erzeugt #
            # setzt nullen in abhängigkeit der länge der einzelnen zeiten #
            # z.B. entsteht aus 0:22:9 nun 00:22:09 #

            self.view.config(text=newTime)
            # setzt die zeit als text im label #

            self.view.after(1000, lambda:self.updateTimer(sec, minute, hour))
            # wiederholt nach 1 sekunde #

        elif (self.view!=None):
        # wenn das spiel stoppt #

            self.endTime = f"{'0'*(len(str(hour))%2)}{hour}:{'0'*(len(str(minute))%2)}{minute}:{'0'*(len(str(sec))%2)}{sec}"
            # folgender format: XX:XX:XX wird erzeugt #
            # setzt nullen in abhängigkeit der länge der einzelnen zeiten #
            # z.B. entsteht aus 0:22:9 nun 00:22:09 #

            if (self.win):
                self.updateHighscoore()
                # setzt ggf. neuen highscore #
        else:
        # wenn der timer nicht existiert #

            return
    
    def resetTimer(self):
    # setzt timer zurück #

        self.view.destroy()
        self.endTime = "00:00:00"
        self.view = tk.Label(self.master, width=10, height=2, relief="solid", text="00:00:00", font=("Gill Sans Nova", 15))
        self.view.place(relx = 0.12, rely = 0.1, anchor = "se")
        

    def startTimer(self):
    # startet timer #

        self.running = True
        self.updateTimer(0, 0, 0, reset=True)

    def updateHighscoore(self):
    # setzt ggf. neuen highscore #

        highscoores = pickle.load(open('highscoores.txt', 'rb'))
        # liest akutelle highscores ein im dictonary format #

        if (self.mode):
            oldHighscoore = self.endTime
            for i in highscoores[self.mode]:
            # geht alle zeiten im .mode durch #

                if i["time"] > self.endTime:
                # higscoore wurde gebrochen #

                    oldHighscoore = i["time"]
                    # welche zeit gebrochen wurde #

                    index = highscoores[self.mode].index(i)
                    # an welcher stelle gebrochen wurde #

                    break

            if (oldHighscoore!=self.endTime):
            # nur wenn neuer highscoore gesetzt wurde #

                for i in range(1+index, 5):
                # verschiebt alle zeiten nach neuem highscoore um eins nach unten #

                    highscoores[self.mode][5+index-i]["time"] = highscoores[self.mode][4+index-i]["time"]
                    highscoores[self.mode][5+index-i]["name"] = highscoores[self.mode][4+index-i]["name"]
                    highscoores[self.mode][5+index-i]["grid"] = highscoores[self.mode][4+index-i]["grid"]
                
                highscoores[self.mode][index]["time"] = self.endTime
                highscoores[self.mode][index]["name"] = self.usrName
                highscoores[self.mode][index]["grid"] = self.usrGrid
                # setzt neuen highscoore #

        pickle.dump(highscoores, open('highscoores.txt', 'wb'))
        # spiechert aktualisierte highscores #
