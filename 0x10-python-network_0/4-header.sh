#!/bin/bash
# take in a URL as an argument, send a GET request to the URL, and display the body of the response
curl -sX GET $1 -H "X-LocakHost-Id: 98" -L
