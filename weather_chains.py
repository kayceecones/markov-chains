import random

weather_chain = {
    # For this current weather,
    # v
    'sun': ['sun', 'sun', 'sun', 'sun', 'sun', 'sun', 'sun', 'sun', 'sun', 'rain'],
    'rain': ['sun', 'rain']
    #         ^ These are the next day's choices (by probability)
}

# the initial state is chosen randomly
weather = [random.choice(list(weather_chain.keys()))]

 # this is how you generalize the (fake) random weather data. 
for i in range(10):   
    weather.append(random.choice(weather_chain[weather[i]]))

print(weather)

