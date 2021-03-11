from tkinter import *
from textblob import TextBlob

# this will create a interface window
root = Tk()

root.geometry('600x400')
root.resizable(0, 0)  # to set app interface size as default
root.title("Language Translator")

# to add Background Image
background_image = PhotoImage(file="C:/Users/Shuvojit/Downloads/Pictures/languages.png")  #?
image_background = Label(root, image=background_image)
image_background.place(x=0, y=0)

# to check current input language
default_Language = "English"

# Welcome Message
welcome_msg = Label(root, text="Welcome to Language Translator !!", font=("bold", 20), bg="white", fg="#F67752")
welcome_msg.place(x=20, y=0)

# Input Message
input_label = Label(root, text="Enter Your Sentence :", bg="white", font=("italic", 14))
input_label.place(x=20, y=50)

# Input Textbox
input_box = Text(root, font=("regular", 10), height=7, width=30)
input_box.place(x=25, y=80)

# output Message
output_label = Label(root, text="Translated Sentence :", bg="white", font=("italic", 14))
output_label.place(x=300, y=50)

# Output TextBox
output_box = Text(root, font=("regular", 10), height=7, width=30)
output_box.place(x=300, y=80)

# Current Input Language
input_language = Label(root, text="English", bg="white")
input_language.place(x=110, y=200)

# Current Output Language
output_language = Label(root, text="Bengali", bg="white")
output_language.place(x=390, y=200)


# This function is for translate conversation
def translate():
    try:
        error_label.configure(text='')
        output_box.delete(0.0, END)  # this will clear previous result
        # this will convert string into translatable Textblob format
        input_conversation = TextBlob(input_box.get(0.0, END))

        if default_Language == "English":  # Language Translate English to Bengali
            output_conversation = input_conversation.translate(from_lang='en', to='bn')
        else:  # Language Translate Bengali to English
            output_conversation = input_conversation.translate(from_lang='bn', to='en')

        output_box.insert(END, output_conversation)

    except:
        output_box.delete(0.0, END)
        error_label.configure(text="Try Again....\nInput a Valid Word or\nCheck Your Internet Connection")


# Language Translate Button
search_image = PhotoImage(file="C:/Users/Shuvojit/Downloads/Pictures/search.png")
search_button = Button(root, command=lambda: translate(), image=search_image, width=25, height=25)
search_button.place(x=257, y=79)


# Changing Language Function
def changeLanguage():
    global default_Language
    if default_Language == "English":
        input_language.configure(text="Bengali")
        output_language.configure(text="English")
        default_Language = "Bengali"
    else:
        input_language.configure(text="English")
        output_language.configure(text="Bengali")
        default_Language = "English"


# Language Change Button
change_language_button = Button(root, command=lambda: changeLanguage(), text="Change", font=("regular", 8))
change_language_button.place(x=248, y=125)


# Text Box Clearing Function
def clearScreen():
    input_box.delete(0.0, END)
    output_box.delete(0.0, END)
    error_label.configure(text='')


# error message
error_label = Label(text="", bg='white', fg='red')
error_label.place(x=180, y=200)

# Text Clear Button
clearButton = Button(root, command=clearScreen, text="Clear", font=("regular", 8), fg="red")
clearButton.place(x=254, y=160)


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
credit_label.place(x=453, y=380)

root.mainloop()  # helps to hold application interface
