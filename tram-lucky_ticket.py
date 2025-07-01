from tkinter import Tk, Label, Entry
import random

class LuckyTramTicket:
  def __init__(self):
    self.window = Tk()
    self.window.title("Счастливый билет")
    self.window.configure(bg='snow')
    self.window.resizable(width=False, height=False)
    self.window.geometry("360x220")

    self.transport_numbers = ['AА', 'АБ', 'АВ', 'АГ', 'АЖ', 'АЗ', 'АК', 'АЛ', 'АМ', 'АН', 'АП', 'АР', 'АС', 'АТ']

    self.create_widgets()
    self.window.mainloop()

  def create_widgets(self):
    Label(
      self.window,
      text="Минтранс РФ",
      font=("Calibri", 12),
      bg="snow"
    ).grid(row=0, column=0, sticky="nw", padx=130, pady=5)

    Label(
      self.window,
      text="АО «КЭТК», г. Кемерово",
      font=("Calibri", 14),
      bg="snow"
    ).grid(row=1, column=0, sticky="nw", padx=80, pady=5)

    Label(
      self.window,
      text="ТРАМВАЙ, ТРОЛЛЕЙБУС",
      font=("Calibri", 16, 'bold'),
      bg="snow"
    ).grid(row=2, column=0, sticky="nw", padx=60, pady=5)

    Label(
      self.window,
      text="ЛЬГОТНЫЙ БИЛЕТ",
      font=("Calibri", 14),
      bg="snow"
    ).grid(row=3, column=0, sticky="nw", padx=100, pady=5)

    Label(
      self.window,
      text=random.choice(self.transport_numbers),
      bg="snow",
      fg="maroon1",
      font=("Calibri", 16)
    ).grid(row=4, column=0, sticky="nw", padx=40, pady=10)

    self.digit1_entry = Entry(self.window, width=3, justify="center",
                     foreground="maroon1", font=("Calibri", 16))
    self.digit1_entry.grid(row=4, column=0, sticky="nw", padx=80, pady=10)

    self.digit2_entry = Entry(self.window, width=3, justify="center",
                     foreground="maroon1", font=("Calibri", 16))
    self.digit2_entry.grid(row=4, column=0, sticky="nw", padx=120, pady=10)

    self.digit3_entry = Entry(self.window, width=3, justify="center",
                     foreground="maroon1", font=("Calibri", 16))
    self.digit3_entry.grid(row=4, column=0, sticky="nw", padx=160, pady=10)

    self.digit4_entry = Entry(self.window, width=3, justify="center",
                     foreground="maroon1", font=("Calibri", 16))
    self.digit4_entry.grid(row=4, column=0, sticky="nw", padx=200, pady=10)

    self.digit5_entry = Entry(self.window, width=3, justify="center",
                     foreground="maroon1", font=("Calibri", 16))
    self.digit5_entry.grid(row=4, column=0, sticky="nw", padx=240, pady=10)

    self.digit6_entry = Entry(self.window, width=3, justify="center",
                     foreground="maroon1", font=("Calibri", 16))
    self.digit6_entry.grid(row=4, column=0, sticky="nw", padx=280, pady=10)

if __name__ == "__main__":
  app = LuckyTramTicket()
