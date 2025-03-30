import matplotlib.pyplot as plt
from Server import Server
import time

# # Create a Server instance (or import it from ddosTester if already running)
# server = Server()

# # Initialize data for plotting
# time_points = []
# total_requests = []
# load_percentage = []
# blocked_persons = []
# user_values = []
# device_values = []
class MetricsPlotter:
    def __init__(self, server):
        self.server = server
        self.time_points = []
        self.total_requests = []
        self.load_percentage = []
        self.blocked_persons = []
        self.user_values = []
        self.device_values = []
        self.city_values = []
        self.province_values = []

    def collect_data(self, duration=10, interval=1):
        for t in range(1, duration + 1):
            metrics = self.server.get_metrics()
            self.time_points.append(t)
            self.total_requests.append(metrics["totalRequests"])
            self.load_percentage.append(metrics["loadPercentage"])
            self.blocked_persons.append(metrics["blockedPersons"])
            self.user_values.append(metrics["userValues"])
            self.device_values.append(metrics["deviceValues"])
            self.city_values.append(metrics["cityValues"])
            self.province_values.append(metrics["provinceValues"])

            # Simulate server activity (for proof of concept)
            self.server.totalRequests += 10  # Example increment
            self.server.loadPercentage = min(100, self.server.loadPercentage + 5)  # Example load increase
            self.server.blockedPersons.append(t) if t % 3 == 0 else None  # Example blocking logic

            time.sleep(interval)  # Simulate a delay between data points

    def plot_data(self):
        plt.figure(figsize=(10, 6))
        # plt.plot(self.time_points, self.total_requests, marker='o', label='Total Requests')
        # plt.plot(self.time_points, self.load_percentage, marker='x', label='Load Percentage')
        # plt.plot(self.time_points, self.blocked_persons, marker='s', label='Blocked Persons')
        plt.plot(self.time_points, self.user_values, marker='u', label='User Values')
        plt.plot(self.time_points, self.device_values, marker='d', label='Device Values')
        plt.plot(self.time_points, self.city_values, marker='C', label='City Values')
        plt.plot(self.time_points, self.province_values, marker='P', label='Province Values')

        # Add labels and title
        plt.xlabel('Time')
        plt.ylabel('Metrics')
        plt.title('DDoS Detection Metrics Over Time')
        plt.legend()

        # Show the plot
        plt.show()
# province_values = []

# # Simulate data collection over time
# for t in range(1, 11):  # Collect data for 10 time intervals
#     metrics = server.get_metrics()
#     time_points.append(t)
#     total_requests.append(metrics["totalRequests"])
#     load_percentage.append(metrics["loadPercentage"])
#     blocked_persons.append(metrics["blockedPersons"])
#     user_values.append(metrics["userValues"])
#     device_values.append(metrics["deviceValues"])
#     city_values.append(metrics["cityValues"])
#     province_values.append(metrics["provinceValues"])

#     # Simulate server activity (for proof of concept)
#     server.totalRequests += 10  # Example increment
#     server.loadPercentage = min(100, server.loadPercentage + 5)  # Example load increase
#     server.blockedPersons.append(t) if t % 3 == 0 else None  # Example blocking logic

#     time.sleep(1)  # Simulate a delay between data points

# # Plot the collected data
# plt.figure(figsize=(10, 6))
# # plt.plot(time_points, total_requests, marker='o', label='Total Requests')
# # plt.plot(time_points, load_percentage, marker='x', label='Load Percentage')
# # plt.plot(time_points, blocked_persons, marker='s', label='Blocked Persons')
# plt.plot(time_points, user_values, marker='u', label='User Values')
# plt.plot(time_points, device_values, marker='d', label='Device Values')
# plt.plot(time_points, city_values, marker='C', label='City Values')
# plt.plot(time_points, province_values, marker='P', label='Province Values')

# # Add labels and title
# plt.xlabel('Time')
# plt.ylabel('Metrics')
# plt.title('DDoS Detection Metrics Over Time')
# plt.legend()

# # Show the plot
# plt.show()