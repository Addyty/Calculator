# import everything from tkinter module
from tkinter import *
expression = ""
# Function to update expression
def press(num):
  global expression
  # concatenation of string
  expression = expression + str(num)
  equation.set(expression)
# Function to evaluate the final expression
def equalpress():
#Try block for exceptions
  try:
    global expression
    total = str(eval(expression))
    equation.set(total)
    expression = ""
#except block
  except:
    equation.set(" error ")
    expression = ""
# Function to clear the contents
def clear():
  global expression
  expression = ""
  equation.set("")
if __name__ == "__main__":
  # create a GUI window
  gui = Tk()
  gui.iconbitmap('cal.ico')
  # set the background colour
  gui.configure(background="thistle2")
  # set the title
  gui.title("Calculator")
  gui.geometry("224x314")
  equation = StringVar()
  Entry(gui, relief=RIDGE, textvariable=equation,justify='right', bd=8, bg="thistle2").grid(row=0,column=0,columnspan=4,ipadx=43,ipady=10)
  equation.set('')
  # create Buttons
  button1 = Button(gui, text=' 1 ', fg='black', bg='pale turquoise',
          command=lambda: press(1), height=3, width=7,relief="groove")
  button1.grid(row=2, column=0)
  button2 = Button(gui, text=' 2 ', fg='black', bg='pale turquoise',
          command=lambda: press(2), height=3, width=7,relief="groove")
  button2.grid(row=2, column=1)
  button3 = Button(gui, text=' 3 ', fg='black', bg='pale turquoise',
          command=lambda: press(3), height=3, width=7,relief="groove")
  button3.grid(row=2, column=2)
  button4 = Button(gui, text=' 4 ', fg='black', bg='pale turquoise',
          command=lambda: press(4), height=3, width=7,relief="groove")
  button4.grid(row=3, column=0)
  button5 = Button(gui, text=' 5 ', fg='black', bg='pale turquoise',
          command=lambda: press(5), height=3, width=7,relief="groove")
  button5.grid(row=3, column=1)
  button6 = Button(gui, text=' 6 ', fg='black', bg='pale turquoise',
          command=lambda: press(6), height=3, width=7,relief="groove")
  button6.grid(row=3, column=2)
  button7 = Button(gui, text=' 7 ', fg='black', bg='pale turquoise',
          command=lambda: press(7), height=3, width=7,relief="groove")
  button7.grid(row=4, column=0)
  button8 = Button(gui, text=' 8 ', fg='black', bg='pale turquoise',
          command=lambda: press(8), height=3, width=7,relief="groove")
  button8.grid(row=4, column=1)
  button9 = Button(gui, text=' 9 ', fg='black', bg='pale turquoise',
          command=lambda: press(9), height=3, width=7,relief="groove")
  button9.grid(row=4, column=2)
  button0 = Button(gui, text=' 0 ', fg='black', bg='pale turquoise',
          command=lambda: press(0), height=3, width=7,relief="groove")
  button0.grid(row=5, column=0)
  plus = Button(gui, text=' + ', fg='Black', bg='AntiqueWhite2',
        command=lambda: press("+"), height=3, width=5,relief="groove")
  plus.grid(row=2, column=3)
  minus = Button(gui, text=' - ', fg='Black', bg='AntiqueWhite2',
        command=lambda: press("-"), height=3, width=5,relief="groove")
  minus.grid(row=3, column=3)
  multiply = Button(gui, text=' * ', fg='Black', bg='AntiqueWhite2',
          command=lambda: press("*"), height=3, width=5,relief="groove")
  multiply.grid(row=4, column=3)
  divide = Button(gui, text=' / ', fg='Black', bg='AntiqueWhite2',
          command=lambda: press("/"), height=3, width=5,relief="groove")
  divide.grid(row=5, column=3)
  equal = Button(gui, text=' = ', fg='Black', bg='AntiqueWhite2',
        command=equalpress, height=3, width=7,relief="groove")
  equal.grid(row=5, column=2)
  clear = Button(gui, text='Clear', fg='Black', bg='AntiqueWhite2',
        command=clear, height=3, width=7,relief="groove")
  clear.grid(row=5, column='1')
  name = Label(gui, text="Powered By Addy Developer", fg='Black', bg='thistle2',width=31,height=2,relief="groove").place(x = 0, y = 278)
  #RUN
  gui.mainloop()