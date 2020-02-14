import requests
import json
# Use this to pretty print the JSON

from pprint import pprint


url = #enter url get requests to retrieve data

#print response object on teh console
print(requests.get(url).json())


# PRETTY PRINT JSON
response = requests.get(url).json()
print(json.dumps(response, indent=4, sort_keys=True))

# Pretty print JSON for a specific launchpad
response = requests.get(url + "/ksc_lc_39a").json()
print(json.dumps(response, indent=4, sort_keys=True))

# Create a url with a specific character id
character_id = '4'
url = url + character_id

# Storing the JSON response within a variable
data = response.json()


# Performing a GET Request and saving the 
# API's response within a variable
response = requests.get(url)
response_json = response.json()
print(json.dumps(response_json, indent=4, sort_keys=True))


# It is possible to grab a specific value 
# from within the JSON object
print(response_json["Key NAME"])


# It is also possible to perform some
# analysis on values stored within the JSON object
var = len(response_json["KEY NAME"])

# indexing
my_var= data["starships"][0]
ship_response = requests.get(my_var).json()


#reference the values stored within sub-dictionaries and sub-lists
var = response_json["Key NAME"][0]["SUB-KEY NAME"]

# for a url with contatenated api key 
movie = requests.get(url + "Key Name").json()

#################################################
##################################################

# Create an empty list to store the responses
response_json = []

# Create random indices representing
# a user's choice of posts
indices = random.sample(list(range(1, 100)), 10)


# Make a request for each of the indices
for x in range(len(indices)):
    print(f"Making request number: {x} for ID: {indices[x]}")

    # Get one of the posts
    post_response = requests.get(url + str(indices[x]))

    # Save post's JSON
    response_json.append(post_response.json())
	
###############################################


	
	
	




