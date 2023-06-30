#!/bin/bash
#sends data to server using POST
curl -s -d "test=test@gmail.com&subject=I will always be here for PLD" "$1"
