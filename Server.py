import time

class Server:

     sleepInterval = 0.1
     last_time = 0
     totalRequests = 0
     loadAmount = 0
     LOADCAP = 100
     loadPercentage = 0
     
     userIds = []
     userValues = []
     userTimeSinceUse = []
     
     deviceIds = []
     deviceValues = []
     deviceTimeSinceUse = []
     
     cityIds = []
     cityValues = []
     cityTimeSinceUse = []
     
     provinceIds = []
     provinceValues = []
     provinceTimeSinceUse = []
     
     blockedPersons = []
     blockedDevices = []
     blockedCities = []
     blockedProvinces = []
     
     userThreshold = 25
     deviceThreshold = 50
     cityThreshold = 1000
     provinceThreshold = 10000
     
     def newDevice(self, deviceId):
          self.deviceIds.append(deviceId)
          self.deviceValues.append(0)
          self.deviceTimeSinceUse.append(10)
          
     def newPerson(self, personId):
          self.userIds.append(personId)
          self.userValues.append(0)
          self.userTimeSinceUse.append(10)
          
     def newCity(self, cityId):
          self.cityIds.append(cityId)
          self.cityValues.append(0)
          self.cityTimeSinceUse.append(10)
          
     def newProvince(self, provinceId):
          self.provinceIds.append(provinceId)
          self.provinceValues.append(0)
          self.provinceTimeSinceUse.append(10)
     
     
     
     # comes in an array of 4
     def incrementUse(self, ids):
          self.userValues[ids[0]] = (5 + self.userValues[ids[0]]) * 1.5
          self.deviceValues[ids[1]] = (4 + self.deviceValues[ids[1]]) * 1.3
          self.cityValues[ids[2]] = (5 + self.cityValues[ids[2]]) * 1.05
          self.provinceValues[ids[3]] = (1.5 + self.provinceValues[ids[3]]) * 1.03
          self.userTimeSinceUse[ids[0]] = 0
          self.deviceTimeSinceUse[ids[1]] = 0
          self.cityTimeSinceUse[ids[2]] = 0
          self.provinceTimeSinceUse[ids[3]] = 0
        
     # loops through all
     def decrementUse(self, amount):
          for i in range(len(self.userValues)):
              if self.userValues[i] > 0:
                   self.userValues[i] -= amount
                   self.userTimeSinceUse[i] += amount
          for j in range(len(self.deviceValues)):
              if self.deviceValues[j] > 0:
                   self.deviceValues[j] -= amount
                   self.deviceTimeSinceUse[j] += amount
          for k in range(len(self.cityValues)):
              if self.cityValues[k] > 0:
                   self.cityValues[k] -= amount
                   self.cityTimeSinceUse[k] += amount
          for l in range(len(self.provinceValues)):
              if self.provinceValues[l] > 0:
                   self.provinceValues[l] -= amount
                   self.provinceTimeSinceUse[l] += amount
          
     
     # convert a validated set of Ids ino indexes to access them
     def getIdIndexes(self, userId, deviceId, cityId, provinceId):
      indexes = [0,0,0,0]
      counters = [0,0,0,0]
      for a in self.userIds:
            if (userId == a):
                  indexes[0] = counters[0]
            else:
                  counters[0] += 1
      for b in self.deviceIds:
            if (deviceId == b):
                  indexes[1] = counters[1]
            else:
                  counters[1] += 1
      for c in self.cityIds:
            if (userId == c):
                  indexes[2] = counters[2]
            else:
                  counters[2] += 1
      for d in self.provinceIds:
            if (provinceId == d):
                  indexes[3] = counters[3]
            else:
                  counters[3] += 1
      return indexes
     
     # validate the set of IDs
     def verifyIds(self, userId, deviceId, cityId, provinceId):
          if (userId not in self.userIds):
               print("unregistered user")
               self.newPerson(userId)
          elif(userId in blockedPersons):
               print("blocked message")
               return False
          if (deviceId not in self.deviceIds):
               print("unregistered device")
               self.newDevice(deviceId)
          elif (deviceId in blockedDevices):
               print("blocked message")
               return False
          if (provinceId not in self.provinceIds):
               print("unregistered province")
               self.newProvince(provinceId)
          elif (provinceId in blockedProvinces):
               print("blocked message")
               return False
          if (cityId not in self.cityIds):
               print("unregistered city")
               self.newCity(cityId)
          elif (cityId in blockedCities):
               print("blocked message")
               return False
          return True # just means no errors
     
     def banThreats(self):
          for i in range(len(self.userValues)):
               if (self.userValues[i]) >= self.userThreshold:
                    self.userStrikes[i] += 1
                    if (self.userStrikes[i] == 3):
                         self.blockedPersons.append(self.userIds[i])
              
          for j in range(len(self.deviceValues)):
               if (self.deviceValues[j]) >=  self.deviceThreshold:
                    self.deviceStrikes[i] += 1
                    if (self.deviceStrikes[i] == 3):
                        self.blockedDevices.append(self.deviceIds[i])
               
          for k in range(len(self.cityValues)):
               if (self.cityValues[k]) >= self.cityThreshold:
                    self.cityStrikes[i] += 1
                    if (self.cityStrikes[i] == 3):
                         self.blockedCities.append(self.cityIds[i])
               
          for l in range(len(self.provinceValues)):
               if (self.provinceValues[l]) >=  self.provinceThreshold:
                    self.provinceStrikes[i] += 1
                    if (self.provinceStrikes[i] == 3):
                         self.blockedProvince.append(self.provinceIds[i])
               
     def new_message(self, userId, deviceId, cityId, provinceId, messageTxt):
           self.new_time = time.time() - self.last_time
           self.timeAlive += self.new_time
           if (self.verifyIds(userId, deviceId, cityId, provinceId)):
                which = self.getIdIndexes(userId, deviceId, cityId, provinceId)
                print(which)
                print(self.deviceValues)
                self.incrementUse(which)
                print("new message processed")
           self.banThreats()
           self.decrementUse(self.new_time)
           self.last_time = time.time()

     def get_metrics(self):
      return {
           "totalRequests": self.totalRequests,
           "loadPercentage": self.loadPercentage,
           "blockedPersons": len(self.blockedPersons),
           "blockedDevices": len(self.blockedDevices),
           "blockedCities": len(self.blockedCities),
           "blockedProvinces": len(self.blockedProvinces),
           "userValues": self.userValues,
           "deviceValues": self.deviceValues,
           "cityValues": self.cityValues,
           "provinceValues": self.provinceValues,
      }



