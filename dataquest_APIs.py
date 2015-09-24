## Set up the parameters we want to pass to the API.
# This is the latitude and longitude of SF.
parameters = {"lat": 37.78, "lon": -122.41}

# Make a get request with the parameters.
response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)
content = response.content

# Print the content of the response (the data the server returned)
print(response.content)
print(response.url)


## json library
# Make a list of fast food chains.
best_food_chains = ["Taco Bell", "Shake Shack", "Chipotle"]
print(type(best_food_chains))

# Use json.dumps to convert best_food_chains to a string.
import json
best_food_chains_string = json.dumps(best_food_chains)
print(type(best_food_chains_string))

# Convert best_food_chains_string back into a list
print(type(json.loads(best_food_chains_string)))

# Make a dictionary
fast_food_franchise = {
    "Subway": 24722,
    "McDonalds": 14098,
    "Starbucks": 10821,
    "Pizza Hut": 7600
}

# We can also dump a dictionary to a string and load it.
fast_food_franchise_string = json.dumps(fast_food_franchise)
print(type(fast_food_franchise_string))


## Getting JSON from a request
parameters = {"lat": 37.78, "lon": -122.41}
response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)

# Get the response data as a python object.  Verify that it's a dictionary.
data = response.json()
print(response.content)

# Headers is a dictionary
print(response.headers)
content_type =  response.headers['content-type']

print(type(data))
print(data)
print('\n===\n')

first_pass_duration = data['response'][0]['duration']

# API endpoint, number of astronauts
response = requests.get("http://api.open-notify.org/astros.json")
in_space_count = response.json()['number']
print(in_space_count)

