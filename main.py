from tkinter import *
from post import calculate


#--------------------Buttons--------------------#

def append_digit(digit):    #also appends brackets, and maths functions(math functions are not appended directly)
    old = entry.get()
    new = old + digit
    entry.delete(0, END)
    entry.insert(0, new)

def check_rep(func_char):   # func_char is the maths functions like +-*/
    func = ['+','-','*','/']
    exp = entry.get()
    if exp[len(exp)-1] in func: #checks if the last character is a mathamatical function, to prevent maths errors during calculation
        return False
    else:
        return True

def append_char(character):
    if check_rep(character):
        append_digit(character)
    else:
        append_digit('')

def cut():
    old = entry.get()
    new = ''
    for i  in range(0, len(old)-1):
        new+=old[i]
    entry.delete(0, END)
    entry.insert(0,new)

def clear():
    entry.delete(0, END)

def equal():
	expression = entry.get()
	answer = str(calculate(expression))
	entry.delete(0,END)
	entry.insert(0,answer)
#--------------------UI--------------------#
window = Tk()
window.title("Calculator")
window.config(padx=5, pady=5)

#----------Display Window----------#
display = Frame()
display.config(height = 50,bd = 5, relief = "sunken")
display.grid(column = 0 , row = 0,columnspan = 4)
entry = Entry(display,bg = "grey")
entry.config(width = 9,font = ("Roboto", 25), justify = "right")
entry.pack(fill = BOTH, ipadx = 70, ipady = 20)
entry.focus()
#----------Buttons----------#
#numbers
a = [9,8,7,6,5,4,3,2,1,0]
num_butt = []   #list of button functions for numbers 

#creating buttons
for i in a:
    num_butt.append(Button(text = f'{i}', pady = 10, width = 10, command = lambda x=str(i):append_digit(x)))

#placing the created buttons 
but_pos = [(2,0),(2,1),(2,2),(3,0),(3,1),(3,2),(4,0),(4,1),(4,2)]
for i in range(0,len(num_butt)-1):
    num_butt[i].grid(row = but_pos[i][0], column = but_pos[i][1])

#placing unique buttons like:
#0
zero = Button(text = '0', pady = 10, width = 10, command = lambda x='0':append_digit(x))
zero.grid(row = 5, column = 1)
#decimal
decimal = Button(text = '.', pady = 10, width = 10)
decimal.grid(row = 5, column = 2)
#functions
plus = Button(text = '+', pady = 10, width = 10, command = lambda x='+':append_char(x))
plus.grid(row = 4 , column = 3)

minus = Button(text = '-', pady = 10, width = 10,command = lambda x='-':append_char(x))
minus.grid(row = 3, column = 3)

mult = Button(text = '*', pady = 10, width = 10, command = lambda x='*':append_char(x))
mult.grid(row = 2, column = 3)

div = Button(text = '/', pady = 10, width = 10, command = lambda x='/':append_char(x))
div.grid(row = 1, column = 3)

eq = Button(text = '=', pady = 10, width = 10, command = equal)
eq.grid(row = 5, column = 3)

cut = Button(text = 'C', pady = 10, width = 10, command = cut)
cut.grid(row = 1, column = 0)

p_open = Button(text = '(', pady = 10, width = 10, command = lambda x = '(':append_digit(x))
p_open.grid(row = 1, column = 1)

p_close = Button(text = ')', pady = 10, width = 10, command = lambda x = ')':append_digit(x))
p_close.grid(row = 1, column = 2)

clear = Button(text = 'AC', pady = 10, width = 10, command = clear)
clear.grid(row = 5, column = 0)


window.mainloop()
