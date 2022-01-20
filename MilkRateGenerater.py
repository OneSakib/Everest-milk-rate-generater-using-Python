from tkinter import *
from PIL import Image, ImageTk
import datetime
from tkinter.filedialog import *
from tkinter import messagebox as mb

# GUI Decleration
root = Tk()
root.title("Milk Rate Generator")
root.geometry('738x415')
photo = Image.open(r'background.jpeg')
bg = ImageTk.PhotoImage(photo)
logophoto = Image.open(r'logo.jpeg')
logo = ImageTk.PhotoImage(logophoto)
root.iconphoto(False, logo)
label1 = Label(root, image=bg)
label1.place(x=0, y=0)
root.resizable(0, 0)
label = Label(root, text="Milk Rate Generator", font='TimesNewRoman 25 bold italic underline', fg='red', bd=5, bg=None)
label.place(relx=0.3, rely=0.01)
dateis = datetime.datetime.now()
label = Label(root, text=f"Today: {dateis.day}/{dateis.month}/{dateis.year}",
              font='TimesNewRoman 15 bold italic underline', fg='red', bd=5, bg=None)
label.place(relx=0.4, rely=0.12)
rate = DoubleVar()
snfstart = IntVar()
snfend = IntVar()
fatstart = IntVar()
fatend = IntVar()

pricestring = ""


# generate Rate Chart
def generate():
    global pricestring
    if rate.get() == 0:
        mb.showinfo("Rate Value", "Please Enter Rate")
    elif snfstart.get() == 0:
        mb.showinfo("SNF Value", "Please Enter Start SNF Value")
    elif snfend.get() == 0:
        mb.showinfo("SNF Value", "Please Enter END SNF Value")
    elif fatstart.get() == 0:
        mb.showinfo("FAT Value", "Please Enter Start FAT Value")
    elif fatend.get() == 0:
        mb.showinfo("FAT Value", "Please Enter END FAT Value")
    else:
        try:
            newsnf = 0
            newfat = 0
            price = 0
            day = dateis.day
            month = dateis.month
            year = str(dateis.year)[2:4]
            if day < 10:
                day = f'0{day}'
            if month < 10:
                month = f'0{month}'
            pricestring = f"j000000{day}{month}{year}00000000000000000000\nj"
            count = 0
            fatunit = (rate.get() * 52) / 650
            snfunit = (rate.get() * 48) / 900
            for snf in range(snfstart.get(), snfend.get() + 1):
                for fat in range(fatstart.get(), fatend.get() + 1):
                    if fat > 65:
                        if fat > 99 and snf > 99:
                            price = int(
                                (((snf * snfunit) + (fat * fatunit)) / 10) * 100)
                        else:
                            price = int(
                                (((snf * snfunit) + (fat * fatunit)) / 10 + (rate.get() * (fat - 65) / 65)) * 100)
                    if fat < 66:
                        price = int(((snf * snfunit) + (fat * fatunit)) * 10)
                    if count == 3:
                        pricestring += '00\nj'
                        count = 0
                    if snf < 100:
                        newsnf = f'0{snf}'
                    if snf > 99:
                        newsnf = snf
                    if fat < 100:
                        newfat = f'0{fat}'
                    if fat > 99:
                        newfat = fat
                    if fat == fatend.get():
                        count += 1
                        if (fatend.get() - fatstart.get() + 1) % 3 == 0:
                            pricestring += f'{newsnf}{newfat}{price}'
                            if fat == fatend.get() and snf == snfend.get():
                                pricestring += '00'
                        elif (fatend.get() - fatstart.get() + 1) % 3 == 1:
                            pricestring += f'{newsnf}{newfat}{price}'
                            pricestring += f'0000000000000000000000\n'
                            if not (snf == snfend.get() and fat == fatend.get()):
                                pricestring += 'j'
                            count = 0
                        elif (fatend.get() - fatstart.get() + 1) % 3 == 2:
                            pricestring += f'{newsnf}{newfat}{price}'
                            pricestring += f'000000000000\n'
                            if not (snf == snfend.get() and fat == fatend.get()):
                                pricestring += 'j'
                            count = 0
                        else:
                            pass
                    else:
                        pricestring += f'{newsnf}{newfat}{price}'
                        count += 1

            mb.showinfo("Generate Rate Chart", "Successfully Generate Chart")
        except Exception as e:
            mb.showerror(" Error is ", f" Error is {e}")


# save generated file
def savefile():
    try:
        name = asksaveasfile(mode='w', defaultextension='.txt')
        text = pricestring
        name.write(text)
        name.close()
        mb.showinfo("Save File", "File Save Successfully")
    except Exception as e:
        mb.showerror("Error on Save", f"Error is : {e}")


if __name__ == '__main__':
    # Lables for Input VaLue
    ratelabel = Label(root, text='Enter Rate: ', font='TimesNewRoman 15 bold italic', fg='blue')
    rateentry = Entry(root, font='TimesNewRoman 15 bold italic', textvariable=rate, width=10,
                      bd=3)
    snfstartlabel = Label(root, text='SNF Limit Start: ', font='TimesNewRoman 15 bold italic', fg='blue')
    snfstartentry = Entry(root, font='TimesNewRoman 15 bold italic', textvariable=snfstart, width=10,
                          bd=3)
    snfendlabel = Label(root, text='SNF Limit End: ', font='TimesNewRoman 15 bold italic', fg='blue')
    snfendentry = Entry(root, font='TimesNewRoman 15 bold italic', textvariable=snfend, width=10,
                        bd=3)
    fatstartlabel = Label(root, text='FAT Limit Start: ', font='TimesNewRoman 15 bold italic', fg='blue')
    fatstartentry = Entry(root, font='TimesNewRoman 15 bold italic', textvariable=fatstart, width=10,
                          bd=3)
    fatendlabel = Label(root, text='FAT Limit End: ', font='TimesNewRoman 15 bold italic', fg='blue')
    fatendentry = Entry(root, font='TimesNewRoman 15 bold italic', textvariable=fatend, width=10,
                        bd=3)
    # btn for action performed
    genbtn = Button(root, text='Generate', font='TimesNewRoman 15 bold italic', fg='white', bg='green', bd=3,
                    command=generate)
    savebtn = Button(root, text='Save File', font='TimesNewRoman 15 bold italic', fg='white', bg='green', bd=3,
                     command=savefile)
    exitbtn = Button(root, text='Exit', font='TimesNewRoman 15 bold italic', fg='white', bg='red', bd=3,
                     command=root.destroy)
    ratelabel.place(relx=0.05, rely=0.3)
    rateentry.place(relx=0.3, rely=0.3)
    snfstartlabel.place(relx=0.5, rely=0.3)
    snfstartentry.place(relx=0.75, rely=0.3)
    snfendlabel.place(relx=0.05, rely=0.4)
    snfendentry.place(relx=0.3, rely=0.4)
    fatstartlabel.place(relx=0.5, rely=0.4)
    fatstartentry.place(relx=0.75, rely=0.4)
    fatendlabel.place(relx=0.05, rely=0.5)
    fatendentry.place(relx=0.3, rely=0.5)
    genbtn.place(relx=0.6, rely=0.6)
    savebtn.place(relx=0.75, rely=0.6)
    exitbtn.place(relx=0.8, rely=0.8)
    root.mainloop()
