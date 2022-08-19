import tkinter as tk
import os
import sys
from datetime import date
customer_name = ""
pm_name = ""
date = str(date.today())[5:7] + "/"+str(date.today())[8:]
time_start = ""
time_end = ""
surveyor_name = ""

#Dropdown options
options = ["Email","Text"]


def GUI_build():
  if(dropdown_output.get()=="Email"):
    dd_label.grid_forget()
    drop.grid_forget()
    build_button.grid_forget()
    cn_label.grid(row = 0, column = 0)
    cn_entry.grid(row=0, column =1,columnspan=3)
    pm_label.grid(row = 1, column = 0)
    pm_entry.grid(row = 1, column = 1, columnspan=3)
    date_label.grid(row = 2, column = 0)
    date_entry.grid(row = 2, column = 1,columnspan=3)
    time_label.grid(row = 3, column =0)
    time_start_entry.grid(row=3, column = 1,sticky="ew")
    to_label.grid(row=3,column=2,sticky="ew")
    #ampm_entry.grid(row=3,column=3)
    time_end_entry.grid(row=3,column=3,sticky="ew")
    surveyor_label.grid(row=4, column =0)
    surveyor_entry.grid(row=4, column=1,columnspan=3)
    calculate.grid(row=5,column = 2,columnspan =1)
    return_button.grid(row=5,column = 0)
  if(dropdown_output.get()=="Text"):
    dd_label.grid_forget()
    drop.grid_forget()
    build_button.grid_forget()
    date_label.grid(row = 0, column = 0,columnspan = 2)
    date_entry.grid(row = 0, column = 2,columnspan=3)
    time_label.config(text = "Time Window: ")
    time_label.grid(row = 1, column =0,columnspan=2,sticky='w')
    time_start_entry.grid(row=1, column = 2,columnspan=1)
    to_label.grid(row=1,column=3)
    #ampm_entry.grid(row=1,column=4,sticky='w')
    time_end_entry.grid(row=1,column=4,sticky='w')
    surveyor_label.grid(row=2, column =0,columnspan=2)
    surveyor_entry.grid(row=2, column=2,columnspan=3)
    calculate.grid(row=3,column = 3,columnspan=2)
    return_button.grid(row=3,column = 2)
    calculate.config(command = get_info_text)
def restart_program():
    """Restarts the current program.
    Note: this function does not return. Any cleanup action (like
    saving data) must be done before calling this function."""
    python = sys.executable
    os.execl(python, python, * sys.argv)
def get_info_text():
  surveyor_name = str(surveyor_entry.get())
  time_start = str(time_start_entry.get())
  time_end = str(time_end_entry.get())
  date = str(date_entry.get())
  #ampm = str(ampm_entry.get())
  script = "Powur Site Survey Confirmation\n\nDate: " + date + "\nArrival: " + time_start + "-"+time_end+ "\nSurveyor: " + surveyor_name + "\n\nThe Surveyor will contact you 30 minutes prior to their arrival. If any issues may pop up in the meantime, please reach back out so we can reschedule things right away. Thank you!"
  print(script)  
  with open("Customer.txt", 'w') as file:
    file.write(script)
def get_info_email():
  customer_name = str(cn_entry.get())
  pm_name = str(pm_entry.get())
  date = str(date_entry.get())
  time_start = str(time_start_entry.get())
  time_end = str(time_end_entry.get())
  surveyor_name = str(surveyor_entry.get())
  #ampm = str(ampm_entry.get())
  script = "Hi "+customer_name + ",\nThanks for your time today! I am sending this follow-up email to introduce you to your Project Manager, " +pm_name +" , who is CC’d here. They will be your main point of contact moving forward. \nAs mentioned in our call, your site survey is scheduled for "+ date + " with our surveyor "+  surveyor_name +". Your surveyor is set to arrive between " + time_start  + "-" + time_end +" and they will contact you 30 minutes prior to their arrival. \nThank you for choosing Powur!"
  print(script)  
  with open("Customer.txt", 'w') as file:
    file.write(script)
window = tk.Tk()
window.title("Paul Project")
window.resizable(False,False)

dd_label = tk.Label(window , text = "Output Type" )
dropdown_output = tk.StringVar()
dropdown_output.set("Text")
drop = tk.OptionMenu( window , dropdown_output , *options )
build_button = tk.Button(window, text = "Build",command = GUI_build)
dd_label.grid(row=0,column=0)
drop.grid(row=0,column=1)
build_button.grid(row=1,column=0,columnspan=2)
ampm_entry = tk.Entry(window,text="pm",width = 3)
ampm_entry.insert(0,"pm")
cn_label = tk.Label(window,text = "Customer Name: ")
pm_label = tk.Label(window,text = "Project Manager Name: ")
date_label = tk.Label(window,text = "Date: ")
time_label = tk.Label(window,text = "Time window(start finish ampm): ")
surveyor_label = tk.Label(window,text = "Surveyor")
to_label = tk.Label(window, text = " to ")
return_button = tk.Button(text = "Restart", command = restart_program)
calculate = tk.Button(text = "Output Text", command = get_info_email)
cn_entry = tk.Entry(window)
pm_entry = tk.Entry(window)
date_entry = tk.Entry(window)
date_entry.insert(0,date)
time_start_entry = tk.Entry(window, width = 5, text = "start")
time_end_entry = tk.Entry(window, width = 5,text ="end")
surveyor_entry = tk.Entry(window)
window.mainloop()