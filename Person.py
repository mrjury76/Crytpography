class Person:
     import time
     import random
     
     myId = 10381 # some big number
     interval = 5
     device = None
     messages = ["Hello","Whats the news","Whats the weather"]
     
     def runtime(self):
          if (self.device != None):
               self.device.message(self.myId, random_message())
          
     def random_message(self):
          return self.messages[random.randrange(0,2)]
     
     def __init__(self, myId, mode, device):
          self.myId = myId
          self.mode = mode
          self.device = device
          looping(self)
     
     def looping(self):
          while (True):
               start_time = time.time()
          
               runtime(self)
               if (mode == "Bad Actor"):
                    repeat = random.randrange(0,5)
                    while (repeat > 0):
                         repeat -= 1
                         runtime()
               elapsed_time = time.time() - start_time
               time.sleep(max(0,interval-elapsed_time))


