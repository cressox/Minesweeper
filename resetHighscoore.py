import pickle
def reset():
# setzt alle highscores zurück #
    
    highscoores = {
                    "einfach":[{"time": "99:99:99", "name":"", "grid":"8x8"},
                                {"time": "99:99:99", "name":"", "grid":"8x8"},
                                {"time": "99:99:99", "name":"", "grid":"8x8"},
                                {"time": "99:99:99", "name":"", "grid":"8x8"},
                                {"time": "99:99:99", "name":"", "grid":"8x8"},],
                    
                    "mittel":[{"time": "99:99:99", "name":"", "grid":"16x16"},
                                {"time": "99:99:99", "name":"", "grid":"16x16"},
                                {"time": "99:99:99", "name":"", "grid":"16x16"},
                                {"time": "99:99:99", "name":"", "grid":"16x16"},
                                {"time": "99:99:99", "name":"", "grid":"16x16"},],
                    
                    "schwer":[{"time": "99:99:99", "name":"", "grid":"30x16"},
                                {"time": "99:99:99", "name":"", "grid":"30x16"},
                                {"time": "99:99:99", "name":"", "grid":"30x16"},
                                {"time": "99:99:99", "name":"", "grid":"30x16"},
                                {"time": "99:99:99", "name":"", "grid":"30x16"},],
                    
                    "benutzerdefiniert":[{"time": "99:99:99", "name":"", "grid":""},
                                {"time": "99:99:99", "name":"", "grid":""},
                                {"time": "99:99:99", "name":"", "grid":""},
                                {"time": "99:99:99", "name":"", "grid":""},
                                {"time": "99:99:99", "name":"", "grid":""}]
                    }

    pickle.dump(highscoores, open('highscoores.txt', 'wb'))

def fiktiv():
# setzt einen fiktiven highscore #

    highscoores = {
                    "einfach":[{"time": "00:00:23", "name":"Herr Barth", "grid":"8x8"},
                                {"time": "00:00:41", "name":"Annika", "grid":"8x8"},
                                {"time": "00:00:53", "name":"Dustin", "grid":"8x8"},
                                {"time": "00:01:12", "name":"Gustav", "grid":"8x8"},
                                {"time": "00:01:10", "name":"Phillip", "grid":"8x8"},],
                    
                    "mittel":[{"time": "00:01:47", "name":"Herr Barth", "grid":"16x16"},
                                {"time": "00:02:01", "name":"Lasse", "grid":"16x16"},
                                {"time": "00:02:42", "name":"Moritz", "grid":"16x16"},
                                {"time": "00:02:45", "name":"Peter", "grid":"16x16"},
                                {"time": "00:03:13", "name":"Emily", "grid":"16x16"},],
                    
                    "schwer":[{"time": "00:05:57", "name":"Herr Barth", "grid":"30x16"},
                                {"time": "00:06:13", "name":"Garry", "grid":"30x16"},
                                {"time": "00:06:23", "name":"Christian", "grid":"30x16"},
                                {"time": "00:08:53", "name":"Manu", "grid":"30x16"},
                                {"time": "00:09:32", "name":"Ammen", "grid":"30x16"},],
                    
                    "benutzerdefiniert":[{"time": "00:07:00", "name":"Herr Barth", "grid":"30x30"},
                                {"time": "00:07:15", "name":"Tom", "grid":"30x30"},
                                {"time": "00:11:14", "name":"Kay", "grid":"19x25"},
                                {"time": "00:13:32", "name":"Gina", "grid":"29x21"},
                                {"time": "00:25:12", "name":"Sheela", "grid":"12x30"}]
                    }

    pickle.dump(highscoores, open('highscoores.txt', 'wb'))

#reset()
fiktiv()
