from tkinter import *

from tkinter.tix import *
from tkinter import messagebox
import json
import pyttsx3  # text to audio
import speech_recognition as sr
# module allow users to compare sets of data ,help to get  classes matches
from difflib import get_close_matches


engine = pyttsx3.init()


def wordaudio():
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(enterwordentry.get())
    engine.runAndWait()

def rate_1():

    wordaudio(120)


def rate_2():

    wordaudio(200)


def rate_3():

    wordaudio(270)

def meaningaudio(rate=0):
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', rate)
    engine.say(textarea.get(1.0, END))  # 1.0 means from 1st word to end
    engine.runAndWait()


def rate1():

    meaningaudio(120)


def rate2():

    meaningaudio(200)


def rate3():

    meaningaudio(270)


def iexit():
    res = messagebox.askyesno('Confirm', 'Do you want to exit?')

    if res == True:
        root.destroy()

    else:
        pass


def clear():

    enterwordentry.delete(0, END)
    textarea.delete(1.0, END)


def search():
    # to store the content of data.json in data variBLE
    data = json.load(open('data.json'))
    i=0
    word = enterwordentry.get()  # method =get of class lable

    # to convert enterd word into lower case as in data all are in lowercase
    word = word.lower()

    if word in data:  # to check req word present is data or not
        meaning = data[word]  # in list format

        textarea.delete(1.0, END)  # to delete if prev present anything
        for item in meaning:
            # .insert method to display on screen
            textarea.insert(END, u'\u2022' + item + '\n\n')
    # get_close_matches(word,opssibiliyeis(list)(optional),n=3,cutoff=0.6(optional))
    elif len(get_close_matches(word, data.keys())) > 0:

        # best match is at 1st postion in list so [0] used
        close_match = get_close_matches(word, data.keys())[0]

        res = messagebox.askyesno(
            'Confirm', 'Did you mean ' + close_match + ' instead?')  # askyesno methode to ask / {close_match} can be used

        if res == True:

            meaning = data[close_match]
            # to remove prev spelling (from where,to where)
            textarea.delete(1.0, END)
            textarea.config(state=NORMAL)
            for item in meaning:

                # u'\u2022' = for  bollet symbol
                textarea.insert(END, u'\u2022' + item + '\n\n')

            textarea.config(state=DISABLED)

        else:
            textarea.delete(1.0, END)
            messagebox.showinfo('Information', 'Please type a correct word')
            enterwordentry.delete(0, END)
    else:
        messagebox.showerror(
            'Error', 'The word doesnt exist.Please double check it.')
        enterwordentry.delete(0, END)


root = Tk()  # to create window
# we can use " " as well to set 'width*height + distance from x axis + distance from y axis' without distance from x and y axis position of window will change each time
root.geometry('1000x700+100+50')
root.title('Talking Dictionary (RPPOOP project) ')  # title

root.resizable(0, 0)  # to remove maximize button ,to fix weight and height

# to give baghground image as it is same folde so passing only name (can we .jpg image?)
bgimage = PhotoImage(file='bg1.png')

# label= build in class  (scree, icon/text)
bgLabel = Label(root, image=bgimage)
bgLabel.place(x=0, y=0)  # to place label on window (must to see the button)

enterwordLabel = Label(root,
                       text='Enter Word',
                       font=('castellar', 29, 'bold'),
                       fg='dark turquoise',
                       bg='white')   # label(screen,text/image,)bg= background
enterwordLabel.place(x=530, y=20)

enterwordentry = Entry(root,
                       # entry(on line i/p) class (screen,i/p styling,)
                       font=('arial', 23, 'bold'),
                       bd=8,
                       relief=SUNKEN,
                       justify=CENTER)  # justify=position of curson, bd=boarder,relief(for boarder styling)
enterwordentry.place(x=510, y=80)

tip = Balloon(root)  # creating a tooltip
searchimage = PhotoImage(file='search.png')
searchButton = Button(root,
                      image=searchimage,
                      bd=0, bg='white',
                      activebackground='whitesmoke',
                      cursor='hand2',
                      command=search)  # cursor (to show hand if hoverr on it), acvtivebackgroung (to change the background colour when clicked)
searchButton.place(x=620, y=150)
# binding toolkit with button
tip.bind_widget(searchButton, balloonmsg="search the meaning of enterd word")


micimage = PhotoImage(file='mic.png')
micButton_ = Button(root,
                    image=micimage,
                    bd=0, bg='white',
                    activebackground='white',
                    cursor='hand2',
                    command=wordaudio)  # bd= boarder
micButton_.place(x=720, y=153)
tip.bind_widget(micButton_, balloonmsg="pronounce the word")

meaninglabel = Label(root, text='Meaning', font=(
    'castellar', 29, 'bold'), fg='turquoise3', bg='white')
meaninglabel.place(x=580, y=240)

textarea = Text(root,
                font=('Bell MT', 18, 'bold'),
                # class= text(for multiple line i/p), baher jau naye mhanun height &width fix keliye
                height=8,
                width=34,
                bd=8,
                relief=SUNKEN,
                wrap='word')  # relife= styling
textarea.place(x=460, y=320)

audioimage = PhotoImage(file='microphone.png')
audioButton = Button(root,
                     image=audioimage,
                     bd=0, bg='white',
                     activebackground='white',
                     cursor='hand2',
                     command=meaningaudio)
audioButton.place(x=530, y=600)
tip.bind_widget(audioButton, balloonmsg="pronounce the meaning")

clearimage = PhotoImage(file='clear.png')
clearButton = Button(root,
                     image=clearimage,
                     bd=0, bg='white',
                     activebackground='white',
                     cursor='hand2',
                     command=clear)  # comaand= def written
clearButton.place(x=790, y=600)
tip.bind_widget(clearButton, balloonmsg="clear the word and meaning")

exitimage = PhotoImage(file='exit.png')
exitButton = Button(root,
                    image=exitimage,
                    bd=0, bg='white',
                    activebackground='white',
                    cursor='hand2',
                    command=iexit)
tip.bind_widget(exitButton, balloonmsg="exit")

exitButton.place(x=660, y=600)

rate_label = Label(root, text='Rate ', font=(
    'castellar', 10, 'bold'), fg='magenta4', bg='white')
rate_label.place(x=930, y=350)
tip.bind_widget(rate_label, balloonmsg="you can change the rate")
rate_1 = Button(root,
                text='1',
                bd=0, bg='plum1',

                cursor='hand2',
                command=rate1)
rate_1.place(x=947, y=400)
tip.bind_widget(rate_1, balloonmsg="slow")

rate_2 = Button(root,
                text='2',
                bd=0, bg='plum2',

                cursor='hand2',
                command=rate2)
rate_2.place(x=947, y=450)
tip.bind_widget(rate_2, balloonmsg="normal")

rate_3 = Button(root,
                text='3',
                bd=0, bg='plum3',

                cursor='hand2',
                command=rate3)
rate_3.place(x=947, y=500)

tip.bind_widget(rate_3, balloonmsg="fast")


root.mainloop()  # to keep window visible
