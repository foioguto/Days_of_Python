# import csv
#
# temperatures = []
#
# with open("../day_25/weather_data.csv") as weather_file:
#     weather_list = csv.reader(weather_file)
#     for weather in weather_list:
#         if weather[1] != "temp":
#             temperatures.append(weather[1])
#     print(temperatures)
import pandas

# data = pandas.read_csv("weather_data.csv")

""" 
print(data["temp"]
print(data.temp)
print(data[data.day == "Monday"]), to get a row data
print(data[data.temp == data.temp.max()]), maximum temp row
"""

# print(data)

data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("new_data.csv")
