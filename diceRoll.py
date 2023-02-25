import requests

def rollDice(diceString):
    url = 'http://localhost:80/diceRoll'
    diceData = {'diceData': diceString}
    x = requests.post(url, json = diceData)
    return x.json()['result']