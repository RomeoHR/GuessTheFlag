# Romeo Adric - Hier ist mein erstes Projekt in der Programmiersprache Python,um meine bisherige Kenntisse zu zeigen.
#Kleines Spiel, wo man seine Kenntnisse über Flaggen prüfen kann. Mit Registration und Ergebnis Eigenschaften.

from tkinter import *
import os,sys
from tkinter import Label
from typing import List

from PIL import ImageTk,Image
import random
import Flags

global GUESS1
global GUESS2
global GUESS3
global GUESS4


def loging():
    global userinfos
    global un
    un = username1.get()
    pw = password1.get()
    userinfos = os.listdir()
    if un in (userinfos):
        file1 = open(un, "r")
        check = file1.read().splitlines()
        if pw in check:
            Label(log_in_window, text="Login Suaccess :)", bg="lightgreen", fg="green").pack()
            username_entry1.delete(0, END)
            password_entry1.delete(0, END)
            log_in_window.after(2000, log_in_window.destroy)
            start_btn["state"]=NORMAL
        else:
            Label(log_in_window, text="Login Failed(Wrong Password) :(", bg="lightgreen", fg="red").pack()
            log_in_window.after(2000, log_in_window.destroy)
    else:
        Label(log_in_window, text="Login Failed(Username Not Found) :(", bg="lightgreen", fg="red").pack()
        log_in_window.after(2000, log_in_window.destroy)
def log_in():
    global username_entry1
    global log_in_window
    global username1
    global password1
    global password_entry1

    username1 = StringVar()
    password1 = StringVar()

    log_in_window = Toplevel(dis)
    log_in_window.title("Log In")
    log_in_window.iconbitmap("flag_icon-icons.com_69377.ico")
    log_in_window.geometry("300x250")
    log_in_window.configure(bg="lightgreen")
    log_in_window.resizable(False, False)

    Label(log_in_window,text=" ", bg="lightgreen").pack()
    Label(log_in_window, text=" ", bg="lightgreen").pack()
    Label(log_in_window, text= "Username *", fg="lightgreen", bg="green").pack()
    username_entry1 = Entry(log_in_window, textvariable= username1)
    username_entry1.pack()

    Label(log_in_window, text=" ", bg="lightgreen").pack()

    Label(log_in_window, text="Password *", fg="lightgreen", bg="green").pack()
    password_entry1 = Entry(log_in_window, textvariable= password1)
    password_entry1.pack()

    Label(log_in_window, text=" ", bg="lightgreen").pack()

    Button(log_in_window, text="LogIn", fg="lightgreen", bg="green", command=loging).pack()
    def close1():
        log_in_window.destroy()
    cancel_btn1 = Button(log_in_window, text="CLOSE",font="calibri 12", bg="#FF6666", fg="#800000", command=close1)
    cancel_btn1.pack(side=BOTTOM)

def signing():
    Label(sign_up_window, text=" ", bg="lightgreen").pack()

    username_info = username.get()
    password_info = password.get()
    password1 = str(password_info)
    username1 = str(username_info)

    if username_info in (os.listdir()):
         Label(sign_up_window, text="Username Already Used :(", bg="#FF6666", fg="#800000" ).pack()
         sign_up_window.after(2000, sign_up_window.destroy)
    elif len(password1) < 3:
         Label(sign_up_window, text="Password too short :(", bg="#FF6666", fg="#800000").pack()
         sign_up_window.after(2000, sign_up_window.destroy)
    elif len(username1) < 3:
        Label(sign_up_window, text="Username too short :(", bg="#FF6666", fg="#800000").pack()
        sign_up_window.after(2000, sign_up_window.destroy)
    else :
        file = open(username_info, "w")
        file.write(username_info + "\n")
        file.write(password_info + "\n")
        file.write("0"+"\n")
        file.close()
        Label(sign_up_window, text="Registration completed :)", bg="green", fg="lightgreen").pack()
        sign_up_window.after(2500, sign_up_window.destroy)

def sign_up():
    global username_entry
    global sign_up_window
    global username
    global password
    global password_entry

    username = StringVar()
    password = StringVar()

    sign_up_window = Toplevel(dis)
    sign_up_window.title("Sign Up")
    sign_up_window.iconbitmap("flag_icon-icons.com_69377.ico")
    sign_up_window.geometry("300x250")
    sign_up_window.resizable(False, False)
    sign_up_window.configure(bg="lightgreen")

    Label(sign_up_window,text=" ", bg="lightgreen").pack()
    Label(sign_up_window, text=" ", bg="lightgreen").pack()

    Label(sign_up_window, text= "Username *", fg="lightgreen", bg="green").pack()
    username_entry = Entry(sign_up_window, textvariable= username)
    username_entry.pack()

    Label(sign_up_window, text=" ", bg="lightgreen").pack()

    Label(sign_up_window, text="Password *", fg="lightgreen", bg="green").pack()
    password_entry = Entry(sign_up_window, textvariable= password)
    password_entry.pack()

    Label(sign_up_window, text=" ", bg="lightgreen").pack()

    Button(sign_up_window, text="REGISTER", fg="lightgreen", bg="green", command=signing).pack()



    def close():
        sign_up_window.destroy()
    cancel_btn = Button(sign_up_window, text="CLOSE", bg="#FF6666", fg="#800000", command=close)
    cancel_btn.pack(side=BOTTOM)


def answerCHECK1():
    if str(GUESS1) == str(correct_answer):
        global scorecount
        scorecount = scorecount+1
        game.destroy()
        QuestionsLOOP()
    else:
        file2 = open(un, "r")
        lines = file2.read().splitlines()
        lastline = lines[-1]
        file2.close()
        file2 = open(un, "r")
        lines = file2.read().splitlines()
        lastline = lines[-1]
        file2.close()
        if int(lastline) >= scorecount:
            game.destroy()
        elif int(lastline) < scorecount:
            file2 = open(un, "a")
            file2.write(str(scorecount) + "\n")
            file2.close()
            game.destroy()
def answerCHECK2():
    if str(GUESS2) == str(correct_answer):
        global  scorecount
        scorecount = scorecount + 1
        game.destroy()
        QuestionsLOOP()
    else:
        file2 = open(un, "r")
        lines = file2.read().splitlines()
        lastline = lines[-1]
        file2.close()
        file2 = open(un, "r")
        lines = file2.read().splitlines()
        lastline = lines[-1]
        file2.close()
        if int(lastline) >= scorecount:
            game.destroy()
        elif int(lastline) < scorecount:
            file2 = open(un, "a")
            file2.write(str(scorecount) + "\n")
            file2.close()
            game.destroy()
def answerCHECK3():
    if str(GUESS3) == str(correct_answer):
        global scorecount
        scorecount = scorecount + 1
        game.destroy()
        QuestionsLOOP()
    else :
        file2 = open(un, "r")
        lines = file2.read().splitlines()
        lastline = lines[-1]
        file2.close()
        file2 = open(un, "r")
        lines = file2.read().splitlines()
        lastline = lines[-1]
        file2.close()
        if int(lastline) >= scorecount:
            game.destroy()
        elif int(lastline) < scorecount:
            file2 = open(un, "a")
            file2.write(str(scorecount) + "\n")
            file2.close()
            game.destroy()
def answerCHECK4():
    if str(GUESS4) ==str(correct_answer):
        global scorecount
        scorecount = scorecount + 1
        game.destroy()
        QuestionsLOOP()
    else:
        file2 = open(un, "r")
        lines = file2.read().splitlines()
        lastline = lines[-1]
        file2.close()
        file2 = open(un, "r")
        lines = file2.read().splitlines()
        lastline = lines[-1]
        file2.close()
        if int(lastline) >= scorecount:
            game.destroy()
        elif int(lastline) < scorecount:
            file2 = open(un, "a")
            file2.write(str(scorecount) + "\n")
            file2.close()
            game.destroy()
def QuestionsLOOP():
    global scorecount
    scorecount = scorecount+0
    global game
    game = Toplevel()
    game.title('FlagMaster')
    game.iconbitmap("flag_icon-icons.com_69377.ico")
    game.geometry('700x700')
    game.configure(bg="lightgreen")
    game.resizable(False, False)
    Label(game, text=" ", bg="lightgreen").pack()
    Label(game, text=" ", bg="lightgreen").pack()
    Label(game, text=" ", bg="lightgreen").pack()
    Label(game, text=" ", bg="lightgreen").pack()


    global flag
    global CorrectANSWER
    ALLFLAGS()
    flag = random.choice(allflags)
    global correct_answer
    correct_answer = str(flag)
    print(correct_answer)
    answers.remove(flag)
    allflags.remove(flag)
    flag = ImageTk.PhotoImage(Image.open("Flags/" + flag + ".png"))
    flag.upper = Label(game, image=flag)
    flag.upper.photo = flag
    flag.upper.pack()

    CorrectANSWER = correct_answer
    global WrongANSWERS
    WrongANSWERS = random.sample(answers, k=3)
    WrongANSWER1 = WrongANSWERS[0]
    WrongANSWER2 = WrongANSWERS[1]
    WrongANSWER3 = WrongANSWERS[2]
    guesses = [CorrectANSWER, WrongANSWER2, WrongANSWER3, WrongANSWER1]
    global GUESS
    GUESS = random.sample(guesses, k=4)
    global GUESS1
    global GUESS2
    global GUESS3
    global GUESS4
    GUESS1 = GUESS[0]
    GUESS2 = GUESS[1]
    GUESS3 = GUESS[2]
    GUESS4 = GUESS[3]

    Label(game, text=" ", bg="lightgreen").pack()
    global answer_a
    answer_a = Button(game, bg="green", fg="lightgreen", command=answerCHECK1, text="a) " + str(GUESS1)).pack()
    Label(game, text=" ", bg="lightgreen").pack()
    global answer_b
    answer_b = Button(game, bg="green", fg="lightgreen", command=answerCHECK2, text="b) " + str(GUESS2)).pack()
    Label(game, text=" ", bg="lightgreen").pack()
    global answer_c
    answer_c = Button(game, bg="green", fg="lightgreen", command=answerCHECK3, text="c) " + str(GUESS3)).pack()
    Label(game, text=" ", bg="lightgreen").pack()
    global answer_d
    answer_d = Button(game, bg="green", fg="lightgreen", command=answerCHECK4, text="d) " + str(GUESS4)).pack()
    Label(game, text=" ", bg="lightgreen").pack()
    Label(game, text=" ", bg="lightgreen").pack()
    Label(game, text=" ", bg="lightgreen").pack()
    Label(game, text=" ", bg="lightgreen").pack()
    Label(game, text=" ", bg="lightgreen").pack()
    Label(game, text=" ", bg="lightgreen").pack()
    Label(game, text=" ", bg="lightgreen").pack()
    Label(game, text=" ", bg="lightgreen").pack()
    Label(game, text=" ", bg="lightgreen").pack()

    Label(game, text=" ", bg="lightgreen").pack()
    Label(game, text="Score: "+ str(scorecount),font="Calibri 25 bold",bg="#8DEEEE", fg="#236B8E").pack(side=RIGHT)
def start():
    global scorecount
    scorecount = 0
    QuestionsLOOP()
    #SCOREWINDOW()
    return
def ALLFLAGS():
    global allflags
    allflags = ["Japan","Spain","Russia","China","France","Germany","Italy","USA","UK","India","Croatia","Austria","Mexico","Guatemala","Cuba","Dominican Republic","Puerto Rico","Bahamas","Cayman Islands","Turks and Caicos Islands","Jamaica","Haiti",
                "British Virgin Islands","Montserrat","Antigua and Barbuda","Dominica","Saint Lucia","Barbados","Grenada","Saint Vincent and Grenadines","Martinique","Guadeloupe","Anguilla","Belize","El Salvador","Nicaragua","Costa Rica","Panama","Colombia",
                "Venezuela","Trinidad and Tobago","Guyana","Suriname","French Guiana","Brazil","Bolivia","Paraguay","Uruguay","Argentina","Chile","Peru","Ecuador","Falkland Islands","South Georgia and The South Sandwich Islands","Coronation Island","Elephant Island",
                "South Shetland Islands","Islas Galapagos","Hawaii","Canada","Greenland","Kiribati","Iceland","Norway","Sweden","Finland","Estonia","Latvia","Lithuania","Poland","Denmark","Netherlands","Belgium","Luxembourg","England","Wales","Scotland","Northern Ireland",
                "Ireland","Switzerland","Liechtenstein","Andorra","Portugal","Gibraltar","Czechia","Slovakia","Hungary","Slovenia","Bosnia and Herzegovina","Serbia","Montenegro","Kosovo","San Marino","Vatican City","North Macedonia","Albania","Malta","Greece","Bulgaria",
                "Romania","Moldova","Ukraine","Belarus","Turkey","Cyprus","Syria","Iraq","Lebanon","Israel","Palestine","Jordan","Saudi Arabia","Kuwait","Bahrain","Qatar","Yemen","Oman","United Arab Emirates","Iran","Armenia","Azerbaijan","Georgia","Turkmenistan","Uzbekistan",
                "Kazakhstan", "Kyrgyzstan", "Tajikistan", "Afghanistan", "Pakistan", "Sri Lanka", "Bangladesh", "Nepal","Bhutan", "Myanmar(Burma)", "Thailand", "Laos", "Cambodia", "Vietnam", "Mongolia", "North Korea","South Korea", "Taiwan", "Philippines", "Malaysia", "Singapore", "Indonesia",
                "Brunei","Timor Leste","Papua New Guinea","Australia","New Zeland","Cocos Island","Christmas Island","Morroco","Algeria","Tunisia","Lybia","Egypt","Western Sahara","Mauritania","Mali","Niger","Sudan","Senegal","Gambia","Guinea Bissau","Sierra Leone","Liberia","Cote d'Ivore",
                "Burkina Faso","Ghana","Togo","Benin","Nigeria","Cameroon","Central African Republic","South Sudan","Eritrea","Dijibouti","Somalia","Equatorial Guinea","Gabon","Republic of Congo","Democratic Republic of Congo","Uganda","Kenya","Rwanda","Burundi","Tanzania","Angola","Zambia","Malawi",
                "Mozambique","Zimbabwe","Namibia","Botswana","South Africa","Lesotho","Eswatini","Madagascar"]

    global answers
    answers  = ["Japan","Spain","Russia","China","France","Germany","Italy","USA","UK","India","Croatia","Austria","Mexico","Guatemala","Cuba","Dominican Republic","Puerto Rico","Bahamas","Cayman Islands","Turks and Caicos Islands","Jamaica","Haiti",
                "British Virgin Islands","Montserrat","Antigua and Barbuda","Dominica","Saint Lucia","Barbados","Grenada","Saint Vincent and Grenadines","Martinique","Guadeloupe","Anguilla","Belize","El Salvador","Nicaragua","Costa Rica","Panama","Colombia",
                "Venezuela","Trinidad and Tobago","Guyana","Suriname","French Guiana","Brazil","Bolivia","Paraguay","Uruguay","Argentina","Chile","Peru","Ecuador","Falkland Islands","South Georgia and The South Sandwich Islands","Coronation Island","Elephant Island",
                "South Shetland Islands","Islas Galapagos","Hawaii","Canada","Greenland","Kiribati","Iceland","Norway","Sweden","Finland","Estonia","Latvia","Lithuania","Poland","Denmark","Netherlands","Belgium","Luxembourg","England","Wales","Scotland","Northern Ireland",
                "Ireland","Switzerland","Liechtenstein","Andorra","Portugal","Gibraltar","Czechia","Slovakia","Hungary","Slovenia","Bosnia and Herzegovina","Serbia","Montenegro","Kosovo","San Marino","Vatican City","North Macedonia","Albania","Malta","Greece","Bulgaria",
                "Romania","Moldova","Ukraine","Belarus","Turkey","Cyprus","Syria","Iraq","Lebanon","Israel","Palestine","Jordan","Saudi Arabia","Kuwait","Bahrain","Qatar","Yemen","Oman","United Arab Emirates","Iran","Armenia","Azerbaijan","Georgia","Turkmenistan","Uzbekistan",
                "Kazakhstan","Kyrgyzstan","Tajikistan","Afghanistan","Pakistan","Sri Lanka","Bangladesh","Nepal","Bhutan","Myanmar(Burma)","Thailand","Laos","Cambodia","Vietnam","Mongolia","North Korea","South Korea","Taiwan","Philippines","Malaysia","Singapore","Indonesia",
                "Brunei","Timor Leste","Papua New Guinea","Australia","New Zeland","Cocos Island","Christmas Island", "Morroco", "Algeria","Tunisia","Lybia","Egypt","Western Sahara","Mauritania","Mali","Niger","Sudan","Senegal","Gambia","Guinea Bissau","Sierra Leone","Liberia","Cote d'Ivore",
                "Burkina Faso","Ghana","Togo","Benin","Nigeria","Cameroon","Central African Republic","South Sudan","Eritrea","Dijibouti","Somalia","Equatorial Guinea","Gabon","Republic of Congo","Democratic Republic of Congo","Uganda","Kenya","Rwanda","Burundi","Tanzania","Angola","Zambia","Malawi",
                "Mozambique","Zimbabwe","Namibia","Botswana","South Africa","Lesotho","Eswatini","Madagascar"]


def blank():
    Blank = Label(dis, bg="lightgreen",
                  text="           ")
    Blank.pack()
def blank2():
    blank()
    blank()
def blank3():
    blank()
    blank2()




def loging():
    global userinfos
    global un
    un = username1.get()
    pw = password1.get()
    userinfos = os.listdir()

    if un in (userinfos):
        file1 = open(un, "r")
        check = file1.read().splitlines()
        if pw in check:
            Label(log_in_window, text="Logic Success", bg="lightgreen", fg="green").pack()
            username_entry1.delete(0, END)
            password_entry1.delete(0, END)
            log_in_window.after(2000, log_in_window.destroy)
            start_btn["state"]=NORMAL
            login_btn["state"]=DISABLED
        else:
            Label(log_in_window, text="Login Failed(Wrong Password)", bg="lightgreen", fg="red").pack()
            log_in_window.after(2000, log_in_window.destroy)
    else:
        Label(log_in_window, text="Login Failed(Username Not Found)", bg="lightgreen", fg="red").pack()
        log_in_window.after(2000, log_in_window.destroy)
def log_in():
    global username_entry1
    global log_in_window
    global username1
    global password1
    global password_entry1

    username1 = StringVar()
    password1 = StringVar()

    log_in_window = Toplevel(dis)
    log_in_window.title("Log In")
    log_in_window.iconbitmap("flag_icon-icons.com_69377.ico")
    log_in_window.geometry("300x250")
    log_in_window.configure(bg="lightgreen")

    Label(log_in_window,text=" ", bg="lightgreen").pack()
    Label(log_in_window, text=" ", bg="lightgreen").pack()

    Label(log_in_window, text= "Username *", fg="lightgreen", bg="green").pack()
    username_entry1 = Entry(log_in_window, textvariable= username1)
    username_entry1.pack()

    Label(log_in_window, text=" ", bg="lightgreen").pack()

    Label(log_in_window, text="Password *", fg="lightgreen", bg="green").pack()
    password_entry1 = Entry(log_in_window, textvariable= password1)
    password_entry1.pack()

    Label(log_in_window, text=" ", bg="lightgreen").pack()

    Button(log_in_window, text="LogIn", fg="lightgreen", bg="green", command=loging).pack()
    def close1():
        log_in_window.destroy()
    cancel_btn1 = Button(log_in_window, text="CLOSE",font="calibri 12", bg="#FF6666", fg="#800000", command=close1)
    cancel_btn1.pack(side=BOTTOM)

def score():
    SCORETAB = Toplevel()
    SCORETAB.title("score")
    SCORETAB.geometry("600x400")
    SCORETAB.resizable(False, False)
    SCORETAB.configure(bg="black")
    def ScoreCheck():
        global User_Name
        global UN
        UN = User_Name.get()
        if UN in os.listdir():
            file5 = open(UN, "r")
            lines = file5.read().splitlines()
            lastline = lines[-1]
            file5.close()
            Label(SCORETAB, text=UN+"'s"+"Score: " + lastline,bg="black",fg="white",font="helvetica 40 bold").pack()
            Submit_Btn["state"]=DISABLED
            USERNAMEENTRY["state"]=DISABLED
            SCORETAB.after(5000, SCORETAB.destroy)
        else:
            Label(SCORETAB, text="Given Username Does Not Exist !", bg="black", fg="red",
                  font="helvetica 20 bold").pack()
            SCORETAB.after(3000, SCORETAB.destroy)
    global User_Name
    global Submit_Btn
    global UN
    global USERNAMEENTRY
    User_Name = StringVar()
    Label(SCORETAB,text="SCORE",bg="black",fg="white", font="helvetica 40 bold").pack()
    Label(SCORETAB, text="",bg="black",fg="white", font="helvetica 20 bold").pack()
    Label(SCORETAB, text="Enter your Username: ", bg="black", fg="white", font="helvetica 20 bold").pack()
    USERNAMEENTRY = Entry(SCORETAB, textvariable=User_Name)
    USERNAMEENTRY["state"]=NORMAL
    USERNAMEENTRY.pack()
    Submit_Btn = Button(SCORETAB, text="SUBMIT", command=ScoreCheck)
    Submit_Btn["state"]=NORMAL
    Submit_Btn.pack()



def quit():
    dis.destroy()

def MainMenu():
    # DISPLAY
    global dis
    global img
    dis = Tk()
    dis.title('FlagMaster - Romeo Adric')
    dis.iconbitmap("flag_icon-icons.com_69377.ico")
    dis.geometry('750x505')
    dis.configure(bg="lightgreen")
    dis.resizable(False, False)
    blank2()
    img = ImageTk.PhotoImage(Image.open("309959-200.png"))
    panel = Label(dis, image=img, bg="lightgreen")
    panel.pack()
    Caption = Label(dis, text="Welcome to FlagMaster ", bg="green", fg="lightgreen", font=("times 35"), anchor=CENTER)
    Caption.pack()
    global start_btn
    start_btn = Button(dis, text="START", bg="lightgreen", highlightthickness=10, highlightcolor="red", fg="green",
                       font=("Courier 20 bold"), width=5, command=start )
    start_btn["state"] = DISABLED
    start_btn.pack()
    login_signup = Frame(dis)
    login_signup.pack()
    log = Frame(login_signup)
    log.pack(side=LEFT, fill=BOTH)
    sign = Frame(login_signup)
    sign.pack(side=RIGHT, fill=BOTH)
    global login_btn
    login_btn = Button(log, text="LogIn", bg="green", fg="lightgreen", font=("Courier 9 bold"), width=6,command=log_in )
    login_btn.pack()
    signUp_btn = Button(sign, text="SignUp", font=("Courier 9 bold"), bg="green", fg="lightgreen", width=6,
                        command=sign_up)
    signUp_btn.pack()
    blank3()
    quitframe = Frame(dis)
    quitframe.pack(side=RIGHT)
    quit_btn = Button(quitframe, text=" QUIT ", font=("helvetica 8 bold"), bg="#FF6666", fg="#800000", width=5,
                      height=2, command=quit)
    quit_btn.pack()
    scoreFrame = Frame(dis)
    scoreFrame.pack(side=LEFT)
    score_btn = Button(scoreFrame, text="SCORE", font=("helvetica 8 bold"), bg="#8DEEEE", fg="#236B8E", width=5,
                       height=2, command=score)
    score_btn.pack()


MainMenu()
dis.mainloop()