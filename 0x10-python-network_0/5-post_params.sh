#!/bin/bash
# post request
curl -s -I -d email: "test@gmail.com" -d subject: "I will always be here for PLD" $1
