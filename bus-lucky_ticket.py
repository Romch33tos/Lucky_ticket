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

if __name__ == "__main__":
  app = LuckyTicket()
