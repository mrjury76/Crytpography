class ddosTester:
     
     from Server import Server
     from Person import Person
     from Device import Device

     server = Server(0)
     device1 = Device(10, 'kamloops', 'BC', server)
     device2 = Device(20, 'kamloops', 'BC', server)
     device3 = Device(30, 'calgary', 'AB', server)
     device4 = Device(40, 'calgary', 'AB', server)
     person1 = Person(1, 'Nice', device1)
     person2 = Person(2, 'Nice', device2)
     person3 = Person(3, 'Bad Actor', device3)
     person4 = Person(4, 'Nice', device1)
     person5 = Person(5, 'Nice', device2)
     person6 = Person(6, 'Bad Actor', device3)
     
     
