from Server import Server
from Person import Person
from Device import Device
from Cryptography import Cryptography
from Crypto.Random import get_random_bytes
# import matplotlib.pyplot as plt
import random
import time

class ddosTester:
     crypto = Cryptography()
     aes_key = crypto.generate_aes_key()
     
     server = Server(aes_key)
     device1 = Device(10, 'kamloops', 'BC', server)
     device2 = Device(20, 'kamloops', 'BC', server)
     device3 = Device(30, 'calgary', 'AB', server)
     device4 = Device(40, 'calgary', 'AB', server)
     person1 = Person(1, 'Nice', device1, aes_key)
     person2 = Person(2, 'Nice', device2, aes_key)
     person3 = Person(3, 'Bad Actor', device3, aes_key)
     person4 = Person(4, 'Nice', device1, aes_key)
     person5 = Person(5, 'Nice', device2, aes_key)
     person6 = Person(6, 'Bad Actor', device3, aes_key)
     person_list = [person1, person2, person3, person4, person5, person6]
     while True:
         for i in range(len(person_list)):
             if person_list[i].mode == "Bad Actor":
                    repeat = random.randrange(0,5)
                    while (repeat > 0):
                         repeat -= 1
                         person_list[i].runtime()
             time.sleep(random.randrange(2,5))
    
         
     
