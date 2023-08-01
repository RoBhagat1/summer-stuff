#importing modules
from tkinter import *
import googletrans
from googletrans import Translator
# initializing window
Screen = Tk()
Screen.title("Language Translator")
translator = Translator()
InputLanguageChoice = StringVar()
TranslateLanguageChoice = StringVar()

LanguageChoices = {'Choose One', 'Hindi','English','French','German','Spanish','Korean'}
InputLanguageChoice.set('Choose One')
TranslateLanguageChoice.set('Choose One')

def Translate():
    translated = translator.translate(TextVar.get(), dest = TranslateLanguageChoice.get())
    OutputVar.set(translated.text)


#choice for input language
InputLanguageChoiceMenu = OptionMenu(Screen,InputLanguageChoice,*LanguageChoices)
Label(Screen,text="Choose a Language").grid(row=0,column=1)
InputLanguageChoiceMenu.grid(row=1,column=1)

#choice in which the language is to be translated
NewLanguageChoiceMenu = OptionMenu(Screen,TranslateLanguageChoice,*LanguageChoices)
Label(Screen,text="Translated Language").grid(row=0,column=2)
NewLanguageChoiceMenu.grid(row=1,column=2)

Label(Screen,text="Enter Text").grid(row=2,column =0)
TextVar = StringVar()
TextBox = Entry(Screen,textvariable=TextVar).grid(row=2,column = 1)

Label(Screen,text="Output Text").grid(row=2,column =2)
OutputVar = StringVar()
TextBox = Entry(Screen,textvariable=OutputVar).grid(row=2,column = 3)

#Button for calling function
B = Button(Screen,text="Translate",command=Translate, relief = GROOVE).grid(row=3,column=1,columnspan = 3)

mainloop()
