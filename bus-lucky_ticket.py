from tkinter import Tk, Label, Entry, Button, CENTER, NW, messagebox as mb
import random

class LuckyTicket:
  def __init__(self):
    self.window = Tk()
    self.window.title("Счастливый билет")
    self.window.configure(bg='snow1')
    self.window.resizable(width=False, height=False)
    self.window.geometry("350x200")

    self.bus_numbers = ['AА', 'АБ', 'АВ', 'АГ', 'АЖ', 'АЗ', 'АК', 'АЛ', 'АМ',
                       'АН', 'АО', 'АП', 'АР', 'АС', 'АТ']

    self.create_widgets()
    self.window.mainloop()

  def create_widgets(self):
    Label(
      self.window,
      text="Минтранс РФ",
      font=("Calibri", 10),
      bg="snow1",
      fg="chartreuse4"
    ).grid(row=0, column=0, sticky=NW, padx=20, pady=5)

    Label(
      self.window,
      text="АО «КТК»              ОДНА ПОЕЗДКА",
      font=("Calibri", 12),
      bg="snow1",
      fg="chartreuse4"
    ).grid(row=1, column=0, sticky=NW, padx=20, pady=5)

    Label(
      self.window,
      text="АВТОБУС",
      font=("Calibri", 14, 'bold'),
      bg="snow1",
      fg="chartreuse4"
    ).grid(row=2, column=0, sticky=NW, padx=20, pady=5)

    Label(
      self.window,
      text="ТЕРМИНАЛ (Транспортная карта)",
      font=("Calibri", 12),
      bg="snow1",
      fg="chartreuse4"
    ).grid(row=3, column=0, sticky=NW, padx=20, pady=5)

    Label(
      self.window,
      text=random.choice(self.bus_numbers),  
      font=("Calibri", 14),
      bg="snow1",
      fg="maroon1"
    ).grid(row=4, column=0, sticky=NW, padx=40, pady=10)

    self.digit1 = Entry(self.window, width=3, justify=CENTER,
                      font=("Calibri", 14), foreground="maroon1")
    self.digit1.grid(row=4, column=0, sticky=NW, padx=80, pady=10)
    self.digit1.bind('<Return>', self.validate_input)

    self.digit2 = Entry(self.window, width=3, justify=CENTER,
                      font=("Calibri", 14), foreground="maroon1")
    self.digit2.grid(row=4, column=0, sticky=NW, padx=120, pady=10)
    self.digit2.bind('<Return>', self.validate_input)

    self.digit3 = Entry(self.window, width=3, justify=CENTER,
                      font=("Calibri", 14), foreground="maroon1")
    self.digit3.grid(row=4, column=0, sticky=NW, padx=160, pady=10)
    self.digit3.bind('<Return>', self.validate_input)

    self.digit4 = Entry(self.window, width=3, justify=CENTER,
                      font=("Calibri", 14), foreground="maroon1")
    self.digit4.grid(row=4, column=0, sticky=NW, padx=200, pady=10)
    self.digit4.bind('<Return>', self.validate_input)

    self.digit5 = Entry(self.window, width=3, justify=CENTER,
                      font=("Calibri", 14), foreground="maroon1")
    self.digit5.grid(row=4, column=0, sticky=NW, padx=240, pady=10)
    self.digit5.bind('<Return>', self.validate_input)

    self.digit6 = Entry(self.window, width=3, justify=CENTER,
                      font=("Calibri", 14), foreground="maroon1")
    self.digit6.grid(row=4, column=0, sticky=NW, padx=280, pady=10)
    self.digit6.bind('<Return>', self.validate_input)

if __name__ == "__main__":
  app = LuckyTicket()
