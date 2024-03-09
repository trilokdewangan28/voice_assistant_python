import pyttsx3  # to construct speak engine

# file1 = open('msg.txt','r+')

tdata = ''


class Spk:
    def say(Text='empty value'):
        # obj = Gui_start()
        # gui = obj.startTask()
        global tdata
        tdata = Text
        # file1.write(Text)
        # gui.MainMsg_tb.setText(text)
        engine = pyttsx3.init('sapi5')
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[2].id)
        engine.setProperty('rate', 180)
        print("   ")
        print(f"A.I. :{Text}\n")
        engine.say(text=Text)    #responsible for text to speech
        engine.runAndWait()
        print("   ")
        # return tdata
# Spk.say()
# print('this is '+tdata)
