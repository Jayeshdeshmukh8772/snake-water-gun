from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    import random
    computer = random.choice([-1,1,0])
    youstr = random.choice(["s","w","g"])
    youDict = {"s":1, "w":-1, "g":0}
    reversedDict = {1:"snake", -1:"water", 0:"gun"}
    you = youDict[youstr]

    print(f"you choose {reversedDict[you]} \ncomputer choose {reversedDict[computer]}")

    if computer==you:
      print("IT'S DRAW !!!")
      anvil.Notification("its draw").show()
    else:
      if computer==-1 and you==1:
        print("YOU WIN !!!")
        anvil.Notification("you win").show()

      elif computer==-1 & you==0:
        print("YOU LOSE !!!")
        anvil.Notification("you lose").show()

      elif computer==1 & you==-1:
        print("YOU LOSE !!!")
        anvil.Notification("you lose").show()
    
      elif computer==1 & you==0:
        print("YOU WIN !!!")
        anvil.Notification("you win").show()
    
      elif computer==0 & you==-1:
        print("YOU WIN !!!")
        anvil.Notification("you win").show()
    
      elif computer==0 & you==1:
        print("YOU LOSE !!!") 
        anvil.Notification("you lose").show()
    
      else:
        print("SOMETHING WENT WRONG")
        anvil.Notification("error occured").show()

      # Notification(("game ends ~ time khatam baby ...")).show()



