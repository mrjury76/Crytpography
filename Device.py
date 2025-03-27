class Device:
     
     myId = 1838301 # some number
     city = 'Test'
     province = 'Land'
     myServer = None
     blockedPersons = []
     
     def __init__(self, myId, city, province, myServer):
          self.myId = myId
          self.city = city
          self.province = province
          self.myPersons = myPersons
          self.interval = interval
          self.myServer = myServer
     
     def message(self, personId, messageTxt):
          if (personId not in self.blockedPersons):
               if (self.myServer != None):
                    self.myServer.message(myId, personId, city, province, messageTxt)

     def addBlockedUser(self, Uid):
          self.blockedPersons.append(Uid)
     

def main(args):
    return 0
