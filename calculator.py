from tkinter import *

root = Tk()
root.geometry('300x400')
root.minsize(300, 400)
root['bg'] = '#33302f'
root.title('Calculator')
root['padx'] = 20
root['pady'] = 20

# Display
distext = StringVar('')

display = Entry(root, bg='#5D6E37', font=('Arial', 20, 'bold'), textvariable=distext, borderwidth=3, relief='sunken')
display.grid(row=0, column=0, columnspan=4, sticky='nsew', padx=5, pady=15)


def focus():
    display.icursor(len(distext.get()))
    display.focus()


def clear():
    distext.set(distext.get()[:-1])
    focus()


def clear_all():
    distext.set('')
    focus()


def buttonpress(v):
    distext.set(distext.get() + v)
    display.xview_moveto(1)
    focus()


def getresult(event=None):
    try:
        distext.set(str(eval(distext.get())))
        display.xview_moveto(0)

    except:
        distext.set('Error')
    focus()


# Buttons
btn_0 = Button(root, text='0', command=lambda: buttonpress("0"), borderwidth=2, relief='raised', bg='#9ca674')
btn_0.grid(row=5, column=1, sticky='nsew', padx=5, pady=5)

btn_dot = Button(root, text='.', command=lambda: buttonpress("."), borderwidth=2, relief='raised', bg='#9ca674')
btn_dot.grid(row=5, column=0, sticky='nsew', padx=5, pady=5)

btn_equal = Button(root, text='=', command=getresult, bg='#f2f2f7')
btn_equal.grid(row=5, column=2, sticky='nsew', padx=5, pady=5)

btn_1 = Button(root, text='1', command=lambda: buttonpress("1"), borderwidth=2, relief='raised', bg='#9ca674')
btn_1.grid(row=4, column=0, sticky='nsew', padx=5, pady=5)

btn_2 = Button(root, text='2', command=lambda: buttonpress("2"), borderwidth=2, relief='raised', bg='#9ca674')
btn_2.grid(row=4, column=1, sticky='nsew', padx=5, pady=5)

btn_3 = Button(root, text='3', command=lambda: buttonpress("3"), borderwidth=2, relief='raised', bg='#9ca674')
btn_3.grid(row=4, column=2, sticky='nsew', padx=5, pady=5)

btn_4 = Button(root, text='4', command=lambda: buttonpress("4"), borderwidth=2, relief='raised', bg='#9ca674')
btn_4.grid(row=3, column=0, sticky='nsew', padx=5, pady=5)

btn_5 = Button(root, text='5', command=lambda: buttonpress("5"), borderwidth=2, relief='raised', bg='#9ca674')
btn_5.grid(row=3, column=1, sticky='nsew', padx=5, pady=5)

btn_6 = Button(root, text='6', command=lambda: buttonpress("6"), borderwidth=2, relief='raised', bg='#9ca674')
btn_6.grid(row=3, column=2, sticky='nsew', padx=5, pady=5)

btn_7 = Button(root, text='7', command=lambda: buttonpress("7"), borderwidth=2, relief='raised', bg='#9ca674')
btn_7.grid(row=2, column=0, sticky='nsew', padx=5, pady=5)

btn_8 = Button(root, text=' 8', command=lambda: buttonpress("8"), borderwidth=2, relief='raised', bg='#9ca674')
btn_8.grid(row=2, column=1, sticky='nsew', padx=5, pady=5)

btn_9 = Button(root, text=' 9', command=lambda: buttonpress("9"), borderwidth=2, relief='raised', bg='#9ca674')
btn_9.grid(row=2, column=2, sticky='nsew', padx=5, pady=5)

btn_plus = Button(root, text='+', command=lambda: buttonpress("+"), borderwidth=2, relief='raised', bg='#5254b3')
btn_plus.grid(row=4, rowspan=2, column=3, sticky='nsew', padx=5, pady=5)

btn_minus = Button(root, text='-', command=lambda: buttonpress("-"), borderwidth=2, relief='raised', bg='#5254b3')
btn_minus.grid(row=3, column=3, sticky='nsew', padx=5, pady=5)

btn_mul = Button(root, text='*', command=lambda: buttonpress("*"), borderwidth=2, relief='raised', bg='#5254b3')
btn_mul.grid(row=2, column=3, sticky='nsew', padx=5, pady=5)

btn_div = Button(root, text=' / ', command=lambda: buttonpress("/"), borderwidth=2, relief='raised', bg='#5254b3')
btn_div.grid(row=1, column=3, sticky='nsew', padx=5, pady=5)

btn_clr = Button(root, text=' C ', command=clear, borderwidth=2, relief='raised', bg='#de3a0d')
btn_clr.grid(row=1, column=2, sticky='nsew', padx=5, pady=5)

btn_clrall = Button(root, text='AC', command=clear_all, borderwidth=2, relief='raised', bg='#de3a0d')
btn_clrall.grid(row=1, column=0, sticky='nsew', padx=5, pady=5)

for i in range(6):
    root.rowconfigure(i, weight=1)

for i in range(4):
    root.columnconfigure(i, weight=1)

root.bind('<Return>', getresult)
focus()

root.mainloop()
