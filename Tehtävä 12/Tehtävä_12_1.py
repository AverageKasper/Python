import requests
import json

answer = input("Would you like to read a chuck norris joke? (Y/N) ").upper().strip()
while answer != "Y" and answer != "N":
    answer = input("Invalid input, try again. (Y/N) ")
while answer != "N":
    try:
        joke = "https://api.chucknorris.io/jokes/random"
        result = requests.get(joke).json()

        print(result["value"])

    except requests.exceptions.RequestException as e:
        print("Could not complete request")
    answer = input("Would you like to read another chuck norris joke? (Y/N) ").upper().strip()
    while answer != "Y" and answer != "N":
        answer = input("Invalid input, try again. (Y/N) ")
print("Goodbye!")
