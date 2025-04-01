import random
from Cryptography import Cryptography

class Person:
     
     myId = 10381 # some big number
     interval = 5
     device = None
     messages = ["Hello","Whats the news","Whats the weather"]
     key = 0
     crypto = Cryptography()

     # person has device passed to it in the constructor, person has an id and a mode
     def runtime(self):
          #encrypt
          if (self.device != None):
               print(self.myId)
               print("sent message from person, encrypted")
               print()
               ciphertext = self.crypto.encrypt_aes(self.key, self.random_message())
               self.device.message(self.myId, ciphertext)
          
     def random_message(self):
          return self.messages[random.randrange(0,2)]
     
     def __init__(self, myId, mode, device, key):
          self.myId = myId
          self.mode = mode
          self.device = device
          self.key = key

