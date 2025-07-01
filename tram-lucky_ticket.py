from tkinter import Tk

class LuckyTramTicket:
  def __init__(self):
    self.window = Tk()
    self.window.title("Счастливый билет")
    self.window.configure(bg='snow')
    self.window.resizable(width=False, height=False)
    self.window.geometry("360x220")
    self.window.mainloop()

if __name__ == "__main__":
  app = LuckyTramTicket()
