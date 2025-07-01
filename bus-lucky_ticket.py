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

  def validate_input(self, event):
    digits = [
      self.digit1.get(),
      self.digit2.get(),
      self.digit3.get(),
      self.digit4.get(),
      self.digit5.get(),
      self.digit6.get()
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
      int(self.digit1.get()),
      int(self.digit2.get()),
      int(self.digit3.get()),
      int(self.digit4.get()),
      int(self.digit5.get()),
      int(self.digit6.get())
    ]
    
    if sum(digits[:3]) == sum(digits[3:]):
      mb.showinfo(
        title="О билете",
        message="Это счастливый билет!"
      )
    else:
      mb.showinfo(
        title="О билете",
        message="Это обычный билет."
      )
    
    self.clear_fields()

  def clear_fields(self):
    self.digit1.delete(0, 'end')
    self.digit2.delete(0, 'end')
    self.digit3.delete(0, 'end')
    self.digit4.delete(0, 'end')
    self.digit5.delete(0, 'end')
    self.digit6.delete(0, 'end')
    self.digit1.focus()

  def create_widgets(self):
    Label(
      self.window,
      text="   Минтранс РФ",
      font=("Calibri", 10),
      bg="snow1",
      fg="chartreuse4"
    ).grid(row=0, column=0, sticky=NW, padx=20, pady=5)

    Label(
      self.window,
      text="АО «КТК»                                ОДНА ПОЕЗДКА",
      font=("Calibri", 12, 'bold'),
      bg="snow1",
      fg="chartreuse4"
    ).grid(row=1, column=0, sticky=NW, padx=20, pady=5)

    Label(
      self.window,
      text="А В Т О Б У С",
      font=("Calibri", 14, 'bold'),
      bg="snow1",
      fg="chartreuse4"
    ).grid(row=2, column=0, sticky=NW, padx=20, pady=5)

    Label(
      self.window,
      text="ТЕРМИНАЛ (Транспортная карта)",
      font=("Calibri", 12, 'bold'),
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
