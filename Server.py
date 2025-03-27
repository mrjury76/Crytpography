class Server:
     
     import time
     
     sleepInterval = 0.1
     timeAlive = 0
     totalRequests = 0
     loadAmount = 0
     LOADCAP = 100
     loadPercentage = 0
     
     userIds = []
     userValues = [0,10,5,3]
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
     
     messageBuffer = []
     
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
          self.provinceIds.append(deviceId)
          self.provinceValues.append(0)
          self.provinceTimeSinceUse.append(10)
     
     
     def __init__(self, myId):
          self.looping()
     
     # comes in an array of 4
     def incrementUse(self, ids):
          userValues[ids[0]] = (5 + userValues[ids[0]]) * 1.5
          deviceValues[ids[1]] = (4 + userValues[ids[1]]) * 1.3
          cityValues[ids[2]] = (5 + userValues[ids[2]]) * 1.05
          provinceValues[ids[3]] = (1.5 + provinceValues[ids[3]]) * 1.03
          userTimeSinceUse[ids[0]] = 0
          deviceTimeSinceUse[ids[1]] = 0
          cityTimeSinceUse[ids[2]] = 0
          provinceTimeSinceUse[ids[3]] = 0
        
     # loops through all
     def decrementUse(self):
          for i in userValues.length:
               userValues[i] -= sleepInterval
               userTimeSinceUse[i] += sleepInterval
          for j in deviceValues.length:
               deviceValues[j] -= sleepInterval
               deviceTimeSinceUse[j] += sleepInterval
          for k in cityValues.length:
               cityValues[k] -= sleepInterval
               cityTimeSinceUse[k] += sleepInterval
          for l in provinceValues.length:
               provinceValues[l] -= sleepInterval
               provinceTimeSinceUse[l] += sleepInterval
          
     def message(self, userId, deviceId, cityId, provinceId, messageTxt):
          messageBuffer.append(userId, deviceId, cityId, provinceId, messageTxt)
               
     def handleBuffer(self):
          for i in messageBuffer:
               if (verifyIds(userId, deviceId, cityId, provinceId)):
                    which = getIdIndexes(userId, deviceId, cityId, provinceId)
                    incrementUse(which)
                    print("new message processed")
          messageBuffer = []
     
     # convert a validated set of Ids ino indexes to access them
     def getIdIndexes(self, userId, deviceId, cityId, provinceId):
          indexes = [-1,-1,-1,-1]
          counters = [0,0,0,0]
          for a in userIds:
               if (userId == a):
                    indexes[0] = counters[0]
               counters[0] += 1
          for b in deviceIds:
               if (deviceId == b):
                    indexes[1] = counters[1]
               counters[1] += 1
          for c in cityIds:
               if (userId == c):
                    indexes[2] = counters[2]
               counters[2] += 1
          for d in provinceIds:
               if (provinceId == d):
                    indexes[3] = counters[3]
               counters[3] += 1
          return indexes
     
     # validate the set of IDs
     def verifyIds(self, userId, deviceId, cityId, provinceId):
          if (userId not in userIds):
               print("unregistered user")
               return False
          if (deviceId not in deviceIds):
               print("unregistered device")
               return False
          if (provinceId not in provinceIds):
               print("unregistered province")
               return False
          if (cityId not in cityIds):
               print("unregistered city")
               return False
     
     def banThreats(self):
          for i in userValues.length:
               if (userValues[i]) >= userThreshold:
                    blockedPersons.append(userIds[i])
              
          for j in deviceValues.length:
               if (deviceValues[j]) >=  deviceThreshold:
                    blockedPersons.append(deviceIds[i])
               
          for k in cityValues.length:
               if (cityValues[k]) >= cityThreshold:
                    blockedPersons.append(cityIds[i])
               
          for l in provinceValues.length:
               if (provinceValues[l]) >=  provinceThreshold:
                    blockedPersons.append(provinceIds[i])
               
     def looping(self):
          while (True):
               start_time = time.time()
               timeAlive += sleepInterval
               decrementUse()
               handleBuffer()
               banThreats()
               elapsed_time = time.time() - start_time
               time.sleep(max(0,interval-elapsed_time))
          
