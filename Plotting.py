# import plotly.graph_objs as go
# import plotly.io as pio
# import time
# import random
#
# # Initialize empty lists for data storage
# x_data = []
# y_data = []
#
# for i in range(50):  # Run for 50 iterations
#     x_data.append(i)
#     y_data.append(random.randint(0, 100))  # Generate random data
#
#     fig = go.Figure()
#     fig.add_trace(go.Scatter(x=x_data, y=y_data, mode='lines+markers', name='Live Data'))
#     fig.update_layout(title='Live Updating Line Graph', xaxis_title='Time', yaxis_title='Value')
#
#     # Show or update the graph
#     pio.show(fig)
#
#     time.sleep(1)  # Wait 1 second before updating
