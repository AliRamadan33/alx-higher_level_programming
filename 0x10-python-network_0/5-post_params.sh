#!/bin/bash
# take in a URL, sends a POST request to the passed URL, and display the body of the response
curl -sX POST $1 -d "email=alitoba335@gmail.com&subject=I will always be here for PLD" -L
