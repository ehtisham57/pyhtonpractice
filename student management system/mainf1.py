import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry


# main frame ==========

win = tk.Tk()
win.geometry("1350x700+0+0")
win.title("Student Management")

# main label ==========

title_label = tk.Label(win, text="Student Management System", font=("Arial", 25), border=12, relief=tk.GROOVE, bg="lightgrey")
title_label.pack(pady=20, fill=tk.X, side=tk.TOP)

# detail Frame ==================

detail_frame = tk.LabelFrame(win, text="Enter Details", font=("Arial", 25), border=12, relief=tk.GROOVE)
detail_frame.place(x=20, y=90, width=420, height=575)

# data frame ===============

data_frame = tk.Frame(win, relief=tk.GROOVE)
data_frame.place(x=470, y=90, width=810, height=575)

data_frame.config(bg="lightgrey")

# Entry Fields

# Roll No ====================
rollno_lbl = tk.Label(detail_frame, text="Roll No", font=("Arial", 14), relief=tk.GROOVE, bg="lightgrey")
rollno_lbl.grid(row=0, column=0, padx=2, pady=2)

rollno_ent = tk.Entry(detail_frame,width=18, bd=7, font=("Arial", 14))
rollno_ent.grid(row=0, column=1, padx=2, pady=2)

# Name ======================
name_lbl = tk.Label(detail_frame, text="Name", font=("Arial", 14), relief=tk.GROOVE, bg="lightgrey")
name_lbl.grid(row=1, column=0, padx=2, pady=2)

name_ent = tk.Entry(detail_frame,width=18, bd=7, font=("Arial", 14))
name_ent.grid(row=1, column=1, padx=2, pady=2)

# Class =====================

class_lbl = tk.Label(detail_frame, text="Class", font=("Arial", 14), relief=tk.GROOVE, bg="lightgrey")
class_lbl.grid(row=2, column=0, padx=2, pady=2)

class_ent = tk.Entry(detail_frame,width=18, bd=7, font=("Arial", 14))
class_ent.grid(row=2, column=1, padx=2, pady=2)

# Section =====================
section_lbl = tk.Label(detail_frame, text="Section", font=("Arial", 14), relief=tk.GROOVE, bg="lightgrey")
section_lbl.grid(row=3, column=0, padx=2, pady=2)

section_ent = tk.Entry(detail_frame, width=18, bd=7, font=("Arial", 14))
section_ent.grid(row=3, column=1, padx=2, pady=2)

# Contact =====================

contact_lbl = tk.Label(detail_frame, text="Contact", font=("Arial", 14), relief=tk.GROOVE, bg="lightgrey")
contact_lbl.grid(row=4, column=0, padx=2, pady=2)

contact_ent = tk.Entry(detail_frame,width=18, bd=7, font=("Arial", 14))
contact_ent.grid(row=4, column=1, padx=2, pady=2)

# Father name =====================

fName_lbl = tk.Label(detail_frame, text="Father Name", font=("Arial", 14), relief=tk.GROOVE, bg="lightgrey")
fName_lbl.grid(row=5, column=0, padx=2, pady=2)

fName_ent = tk.Entry(detail_frame,width=18, bd=7, font=("Arial", 14))
fName_ent.grid(row=5, column=1, padx=2, pady=2)

# Address ===========
adress_lbl = tk.Label(detail_frame, text="Address", font=("Arial", 14), relief=tk.GROOVE, bg="lightgrey")
adress_lbl.grid(row=6, column=0, padx=2, pady=2)

adress_ent = tk.Text(detail_frame, width=18, height=6, bd=7, font=("Arial", 14))
adress_ent.grid(row=6, column=1, padx=2, pady=2)

# Gender==================

gender_lbl = tk.Label(detail_frame, text="Gender", font=("Arial", 14), relief=tk.GROOVE, bg="lightgrey")
gender_lbl.grid(row=7, column=0, padx=2, pady=2)

gender_ent = ttk.Combobox(detail_frame, width=18, font=("Arial", 14))
gender_ent['values'] = ("Male", "Female", "Others")
gender_ent.grid(row=7, column=1, padx=2, pady=2)

# Date of Birth =====================

dob_lbl = tk.Label(detail_frame, text="Date of Birth", font=("Arial", 14), relief=tk.GROOVE, bg="lightgrey")
dob_lbl.grid(row=8, column=0, padx=2, pady=2)

dob_ent = DateEntry(detail_frame, width=15, font=("Arial", 14), background='darkblue',
                    foreground='white', borderwidth=2, date_pattern='dd-mm-yyyy')
dob_ent.grid(row=8, column=1, padx=2, pady=2)

win.mainloop()