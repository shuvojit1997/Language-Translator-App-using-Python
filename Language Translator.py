from tkinter import *
from tkinter import ttk
from textblob import TextBlob
import googletrans

# this will create a interface window
root = Tk()

root.geometry('600x500')
root.configure(bg="#F9F9F9")
root.resizable(0, 0)  # to set app interface size as default
root.title("Language Translator")

langDict = googletrans.LANGUAGES
langValue = list(langDict.values())
langKey = langDict.keys()

# print(langValue)
# print(langKey)
# to add Background Image
# background_image = PhotoImage(file="C:/Users/Shuvojit/Downloads/Pictures/languages.png")  # ?
# image_background = Label(root, image=background_image)
# image_background.place(x=0, y=0)

# to check current input language
default_Language = "English"

# Welcome Message
welcome_msg = Label(root, text="Welcome to Language Translator !!", font=("bold", 20), bg="white", fg="#F67752")
welcome_msg.place(x=20, y=0)

# Input Message
input_label = Label(root, text="Enter Your Sentence :", bg="white", font=("italic", 14))
input_label.place(x=20, y=51)

# Input Textbox
input_box = Text(root, font=("regular", 10), height=7, width=78)
input_box.place(x=25, y=80)

# output Message
output_label = Label(root, text="Translated Sentence :", bg="white", font=("italic", 14))
output_label.place(x=20, y=241)

# Output TextBox
output_box = Text(root, font=("regular", 10), height=7, width=78)
output_box.place(x=25, y=270)

# Current Input Language
input_language = ttk.Combobox(root, values=langValue, state="readonly")
input_language.current(21)
input_language.place(x=220, y=55)

# Current Output Language
output_language = ttk.Combobox(root, values=langValue, state="readonly")
output_language.current(8)
output_language.place(x=220, y=245)


# This function is for translate conversation
def translate():
    try:
        error_label.configure(text='')
        output_box.delete(0.0, END)  # this will clear previous result

        # this will convert string into translatable Textblob format
        input_conversation = TextBlob(input_box.get(0.0, END))
        from_language = input_conversation.detect_language()

        output_lang=output_language.get()

        for to_language, value in langDict.items():
            if output_lang == value:
                output_conversation = input_conversation.translate(from_lang=from_language, to=to_language)
                output_box.insert(END, output_conversation)


    except:
        output_box.delete(0.0, END)
        error_label.configure(text="Try Again....\nInput a Valid Word or\nCheck Your Internet Connection")


# Language Translate Button
search_image = PhotoImage(file="C:/Users/Shuvojit/Downloads/Pictures/search.png")
search_button = Button(root, command=lambda: translate(), text="Translate", font=("italic", 12))
search_button.place(x=250, y=200)


# Changing Language Function
def changeLanguage():
    input_lan = input_language.get()
    input_lan_index = langValue.index(input_lan)

    output_lan = output_language.get()
    output_lan_index = langValue.index(output_lan)

    input_language.current(output_lan_index)
    output_language.current(input_lan_index)


# Language Change Button
change_language_button = Button(root, command=lambda: changeLanguage(), text="Alternate Language", font=("regular", 8))
change_language_button.place(x=25, y=205)


# Text Box Clearing Function
def inputClearScreen():
    input_box.delete(0.0, END)
    error_label.configure(text='')


def outputClearScreen():
    output_box.delete(0.0, END)
    error_label.configure(text='')


# error message
error_label = Label(text="", bg='white', fg='red')
error_label.place(x=180, y=400)

# Text Clear Button
inputClearButton = Button(root, command=inputClearScreen, text="Clear Text", font=("regular", 8), fg="red")
inputClearButton.place(x=520, y=200)

# Text Clear Button
outputClearButton = Button(root, command=outputClearScreen, text="Clear Text", font=("regular", 8), fg="red")
outputClearButton.place(x=520, y=390)


# exit function
def exitApp():
    root.destroy()


# exit Button
exit_button = Button(root, text="Exit", command=exitApp, bg="#FF3630")
exit_button.place(x=560, y=10)

# description
'''desc_label=Label(root, text="This App Can Translate English to Bengali\n"
                            "and English to Bengali as Well ................", bg="white", font=("regular",10))
desc_label.place(x=20, y=250)'''

# credit
credit_label = Label(root, text="Created by Shuvojit Biswas")
credit_label.place(x=453, y=480)

root.mainloop()  # helps to hold application interface
