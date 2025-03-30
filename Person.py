import random

class Person:
     
     myId = 10381 # some big number
     interval = 5
     device = None
     messages = ["Hello","Whats the news","Whats the weather"]
     
     def runtime(self):
          if (self.device != None):
               print(self.myId)
               print("sent message")
               self.device.message(self.myId, self.random_message())
          
     def random_message(self):
          return self.messages[random.randrange(0,2)]
     
     def __init__(self, myId, mode, device):
          self.myId = myId
          self.mode = mode
          self.device = device
