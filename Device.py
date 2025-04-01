class Device:
     
     myId = 1838301 # some number
     city = 'Test'
     province = 'Land'
     myServer = None
     blockedPersons = []

     #device is passed the server when called and has an id city and province
     def __init__(self, myId, city, province, myServer):
          self.myId = myId
          self.city = city
          self.province = province
          self.myServer = myServer
     
     def message(self, personId, messageTxt):
          if (personId not in self.blockedPersons):
               if (self.myServer != None):
                    self.myServer.new_message(self.myId, personId, self.city, self.province, messageTxt)

     def addBlockedUser(self, Uid):
          self.blockedPersons.append(Uid)
     

def main(args):
    return 0
