from Server import Server
from Person import Person
from Device import Device
from Cryptography import Cryptography
import plotly.graph_objs as go
import plotly.io as pio
import time
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
         output = []
         for i in range(len(person_list)):
             if person_list[i].mode == "Bad Actor":
                    repeat = random.randrange(0,5)
                    while (repeat > 0):
                         repeat -= 1
                         output[i] = person_list[i].runtime()

             # Initialize empty lists for data storage
             x_data = []
             y_data = []

             x_data.append(i)
             y_data.append(random.randint(0, 100))  # Generate random data

             fig = go.Figure()
             print(i)
             print(output[i])
             fig.add_trace(go.Scatter(x=output[i], y=y_data, mode='lines+markers', name='Live Data'))
             fig.update_layout(title='Live Updating Line Graph', xaxis_title='Time', yaxis_title='Value')

             # Show or update the graph
             pio.show(fig)

         time.sleep(random.randrange(2,5))
    
         
     
