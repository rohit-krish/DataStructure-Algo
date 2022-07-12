
'''
    QUESTION 1.

    nyc_weather.csv contains new york city weather for first few days in the month of January. Write a program that can answer following,
        - What was the average temperature in first week of Jan
        - What was the maximum temperature in first 10 days of Jan
'''
weather_data = {}
with open('./nyc_weather_data.csv', 'r') as f:
    for index, data in enumerate(f):
        if index != 0:
            weather_data[data.split(',')[0]] = data.split(',')[
                1].removesuffix('\n')

avg_tmp = 0
max_tmp = 0
for i in range(1, 7):
    tmp = int(weather_data['Jan {}'.format(i)])
    avg_tmp += tmp
    if tmp > max_tmp:
        max_tmp = tmp

avg_tmp /= 7
print(avg_tmp)
print(max_tmp)

'''
    QUESTION 2.

    nyc_weather.csv contains new york city weather for first few days in the month of January. Write a program that can answer following,
        - What was the temperature on Jan 9?
        - What was the temperature on Jan 4?

'''
print(weather_data['Jan 9'])
print(weather_data['Jan 4'])
