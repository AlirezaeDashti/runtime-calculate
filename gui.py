from tkinter import *
from tkinter import messagebox
import api


def raise_frame(frame):
    frame.tkraise()


root = Tk()
root.title("big0 Calculator")
root.geometry('700x700')
root.resizable(False, False)

f1 = Frame(root)
f2 = Frame(root)
f3 = Frame(root)

for frame in (f1, f2, f3):
    frame.grid(row=0, column=0, sticky='news')


###########
# FRAME 1 #
###########
photo = PhotoImage(file="ss.png")
Label(f1, image=photo).place(x=0, y=0)
Button(f1, text='           Calculation          ', bg="white", fg="black", command=lambda: raise_frame(f2)).place(
    x=280, y=580)


def f3_handle():
    root.geometry('817x720')
    raise_frame(f3)


Button(f1, text='          Comparison          ', bg="white", fg="black", command=f3_handle).place(x=280,
                                                                                                   y=620)

###########
# FRAME 2 #
###########
Label(f2, image=photo).place(x=0, y=0)

f2entry = Text(f2, bg="white", fg="black", height=30, width=65)
f2entry.place(x=85, y=30)
f2entry.insert(END, "//Use C programming language"
                    "\n"
                    "#include<stdio.h>"
                    "\n"
                    "\n"
                    "int main()"
                    "\n{"
                    "\n"
                    "\n"
                    "\treturn 0;"
                    "\n}")

scrollbar = Scrollbar(f2, command=f2entry.yview)
scrollbar.place(x=597, y=30)
f2entry['yscrollcommand'] = scrollbar.set


def calc_handle():
    api1 = api.Api(f2entry.get("1.0", "end-1c"))
    messagebox.showinfo("Jobs Done", "CPUTIME: {}".format(api1.finalstring["cpuTime"]))
    print("Status code: {}\n".format(api1.response.status_code))
    print(" memory used was: {}\n".format(api1.finalstring['memory']),
          "cputime was {}\n".format(api1.finalstring["cpuTime"]))
    print("\noutput: \n\n", api1.finalstring['output'])


btn = Button(f2, text="Calculate", bg="white", fg="black", command=calc_handle).place(x=320, y=580)

###########
# Frame 3 #
###########
photo2 = PhotoImage(file="sss.png")

Label(f3, image=photo2).place(x=0, y=0, relwidth=1, relheight=1)
f3entry = Text(f3, bg="white", fg="black", height=40, width=50)
f3entry.insert(END, "//Use C programming language"
                    "\n"
                    "#include<stdio.h>"
                    "\n"
                    "\n"
                    "int main()"
                    "\n{"
                    "\n"
                    "\n"
                    "\treturn 0;"
                    "\n}")
f3entry.grid(column=1, row=1)

lbl = Label(f3, bg="white", fg="black", text="  ")
lbl.grid(column=2, row=1)

f3entry2 = Text(f3, bg="white", fg="black", height=40, width=50)
f3entry2.insert(END, "//Use C programming language"
                     "\n"
                     "#include<stdio.h>"
                     "\n"
                     "\n"
                     "int main()"
                     "\n{"
                     "\n"
                     "\n"
                     "\treturn 0;"
                     "\n}")
f3entry2.grid(column=3, row=1)


def compare_handle():
    api1 = api.Api(f3entry.get("1.0", "end-1c"))
    api2 = api.Api(f3entry2.get("1.0", "end-1c"))
    fcpu = float(api1.finalstring['cpuTime'])
    scpu = float(api2.finalstring['cpuTime'])
    print("first Status code: {} and second Status code: {}\n".format(api1.response.status_code,
                                                                      api2.response.status_code))

    print(" first memory: {} and second memory: {}\n".format(api1.finalstring['memory'],
                                                             api2.finalstring['memory']),

          "first cputime: {} and second cputime: {}\n".format(fcpu, scpu))
    print("\nfirst output: \n\n", api1.finalstring['output'])
    print("\nsecond output: \n\n", api2.finalstring['output'])

    if fcpu > scpu:
        better = "Second"
    elif fcpu < scpu:
        better = "First"
    else:
        better = "No idea which"
    messagebox.showinfo("Compare Successful", "{} algorithm is better.".format(better))


compare_btn = Button(f3,
                     text="                                                  Compare                                               ",
                     bg="white", fg="black", command=compare_handle)
compare_btn.grid(row=3, columnspan=4)

raise_frame(f1)
root.mainloop()
