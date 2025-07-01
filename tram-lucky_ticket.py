from tkinter import Tk, Label, Entry
from tkinter import messagebox as mb
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

  def validate_input(self, event=None):
    digits = [
      self.digit1_entry.get(),
      self.digit2_entry.get(),
      self.digit3_entry.get(),
      self.digit4_entry.get(),
      self.digit5_entry.get(),
      self.digit6_entry.get()
    ]
    
    for digit in digits:
      if not digit.isdigit() or len(digit) != 1:
        mb.showerror(
          title="Ошибка",
          message="Введите по одной цифре от 0 до 9 в каждое поле!"
        )
        return
    
    self.check_ticket()

  def check_ticket(self):
    digits = [
      int(self.digit1_entry.get()),
      int(self.digit2_entry.get()),
      int(self.digit3_entry.get()),
      int(self.digit4_entry.get()),
      int(self.digit5_entry.get()),
      int(self.digit6_entry.get())
    ]
    
    if sum(digits[:3]) == sum(digits[3:]):
      mb.showinfo(
        title="Результат",
        message="Это счастливый билет!",
      )
    else:
      mb.showinfo(
        title="Результат",
        message="Это обычный билет."
      )
    
    self.clear_fields()

  def clear_fields(self):
    self.digit1_entry.delete(0, 'end')
    self.digit2_entry.delete(0, 'end')
    self.digit3_entry.delete(0, 'end')
    self.digit4_entry.delete(0, 'end')
    self.digit5_entry.delete(0, 'end')
    self.digit6_entry.delete(0, 'end')
    self.digit1_entry.focus()

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
    self.digit1_entry.bind('<Return>', self.validate_input)

    self.digit2_entry = Entry(self.window, width=3, justify="center",
                     foreground="maroon1", font=("Calibri", 16))
    self.digit2_entry.grid(row=4, column=0, sticky="nw", padx=120, pady=10)
    self.digit2_entry.bind('<Return>', self.validate_input)

    self.digit3_entry = Entry(self.window, width=3, justify="center",
                     foreground="maroon1", font=("Calibri", 16))
    self.digit3_entry.grid(row=4, column=0, sticky="nw", padx=160, pady=10)
    self.digit3_entry.bind('<Return>', self.validate_input)

    self.digit4_entry = Entry(self.window, width=3, justify="center",
                     foreground="maroon1", font=("Calibri", 16))
    self.digit4_entry.grid(row=4, column=0, sticky="nw", padx=200, pady=10)
    self.digit4_entry.bind('<Return>', self.validate_input)

    self.digit5_entry = Entry(self.window, width=3, justify="center",
                     foreground="maroon1", font=("Calibri", 16))
    self.digit5_entry.grid(row=4, column=0, sticky="nw", padx=240, pady=10)
    self.digit5_entry.bind('<Return>', self.validate_input)

    self.digit6_entry = Entry(self.window, width=3, justify="center",
                     foreground="maroon1", font=("Calibri", 16))
    self.digit6_entry.grid(row=4, column=0, sticky="nw", padx=280, pady=10)
    self.digit6_entry.bind('<Return>', self.validate_input)


if __name__ == "__main__":
  app = LuckyTramTicket()
