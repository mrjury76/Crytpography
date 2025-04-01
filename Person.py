import random

class Person:
     
     myId = 10381 # some big number
     interval = 5
     device = None
     messages = ["Hello","Whats the news","Whats the weather"]

     # person has device passed to it in the constructor, person has an id and a mode
     def runtime(self):
          #encrypt
          if (self.device != None):
               print(self.myId)
               print("sent message from person")
               print()
               self.device.message(self.myId, self.random_message())
          
     def random_message(self):
          return self.messages[random.randrange(0,2)]
     
     def __init__(self, myId, mode, device):
          self.myId = myId
          self.mode = mode
          self.device = device
