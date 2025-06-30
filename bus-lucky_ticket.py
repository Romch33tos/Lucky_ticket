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

if __name__ == "__main__":
  app = LuckyTicket()
