from tkinter import *
import os.path
import csv

entry = ""


def press(num):
	"""
	A function that enters the number of the button pressed into the entry textbox.
	"""
	global entry
	entry = entry + str(num)
	equation.set(entry)


def equal_press():
	"""
	A function that computes the result, shows it, and deals with errors if they occur. Also outputs result to a csv file.
	"""
	try:
		global entry
		total = str(eval(entry))
		if os.path.isfile("history.csv"):
			with open("history.csv", "a", newline="") as history_file:
				csv_writer = csv.writer(history_file)
				output = [entry, total]
				csv_writer.writerow(output)
		else:
			with open("history.csv", "w", newline="") as history_file:
				csv_writer = csv.writer(history_file)
				header = ["Operation", "Result"]
				output = [entry, total]
				csv_writer.writerow(header)
				csv_writer.writerow(output)
		equation.set(total)
		entry = ""
	except:
		equation.set("Error")
		entry = ""


def clear():
	"""
	A function that clears the entry textbox.
	"""
	global entry
	entry = ""
	equation.set("")


if __name__ == "__main__":
	"""
	Includes all of the gui setup, such as the buttons, and also starts the gui.
	"""
	gui = Tk()
	gui.configure(background="black")
	gui.title("Calculator")
	gui.geometry("400x335")
	gui.resizable(False, False)
	equation = StringVar()
	expression_field = Entry(gui, textvariable=equation)
	expression_field.grid(columnspan=4, ipadx=70, pady=20)
	button1 = Button(gui, text=' 1 ', fg='black', bg='white', command=lambda: press(1), height=3, width=15)
	button1.grid(row=2, column=0)
	button2 = Button(gui, text=' 2 ', fg='black', bg='white', command=lambda: press(2), height=3, width=15)
	button2.grid(row=2, column=1)
	button3 = Button(gui, text=' 3 ', fg='black', bg='white', command=lambda: press(3), height=3, width=15)
	button3.grid(row=2, column=2)
	button4 = Button(gui, text=' 4 ', fg='black', bg='white', command=lambda: press(4), height=3, width=15)
	button4.grid(row=3, column=0)
	button5 = Button(gui, text=' 5 ', fg='black', bg='white', command=lambda: press(5), height=3, width=15)
	button5.grid(row=3, column=1)
	button6 = Button(gui, text=' 6 ', fg='black', bg='white', command=lambda: press(6), height=3, width=15)
	button6.grid(row=3, column=2)
	button7 = Button(gui, text=' 7 ', fg='black', bg='white', command=lambda: press(7), height=3, width=15)
	button7.grid(row=4, column=0)
	button8 = Button(gui, text=' 8 ', fg='black', bg='white', command=lambda: press(8), height=3, width=15)
	button8.grid(row=4, column=1)
	button9 = Button(gui, text=' 9 ', fg='black', bg='white', command=lambda: press(9), height=3, width=15)
	button9.grid(row=4, column=2)
	button0 = Button(gui, text=' 0 ', fg='black', bg='white', command=lambda: press(0), height=3, width=15)
	button0.grid(row=5, column=0)
	plus = Button(gui, text=' + ', fg='black', bg='white', command=lambda: press("+"), height=3, width=7)
	plus.grid(row=2, column=3)
	minus = Button(gui, text=' - ', fg='black', bg='white', command=lambda: press("-"), height=3, width=7)
	minus.grid(row=3, column=3)
	multiply = Button(gui, text=' * ', fg='black', bg='white', command=lambda: press("*"), height=3, width=7)
	multiply.grid(row=4, column=3)
	divide = Button(gui, text=' / ', fg='black', bg='white', command=lambda: press("/"), height=3, width=7)
	divide.grid(row=5, column=3)
	equal = Button(gui, text=' = ', fg='black', bg='white', command=equal_press, height=3, width=15)
	equal.grid(row=5, column=2)
	clear = Button(gui, text='Clear', fg='black', bg='white', command=clear, height=3, width=15)
	clear.grid(row=6, column=0)
	Decimal = Button(gui, text='.', fg='black', bg='white', command=lambda: press('.'), height=3, width=15)
	Decimal.grid(row=5, column=1)
	gui.mainloop()
