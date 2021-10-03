import requests
import time

url = "https://jokes10.p.rapidapi.com/random"
headers = {
    'x-rapidapi-host': "jokes10.p.rapidapi.com",
    'x-rapidapi-key': "444714b3acmshc3f91a1cc67f9f9p15e367jsnf6256ecd9db3"
}

jokeResponse = requests.request("GET", url, headers=headers)
jokeJSON = (jokeResponse.json()) #Stores a variable named jokeJSON with the value of the request response formatted as a JSON
print(jokeJSON[0]["joke_text"]) #prints the jokeJSON variable's 1st dictionary (Zero indexed) then looks for the key "joke_text"
time.sleep(3)
print(jokeJSON[0]["joke_punchline"]) #prints the jokeJSON variable's 1st dictionary (Zero indexed) then looks for the key "joke_punchline"
