#!/bin/bash
# Script that sents a data for post method
curl -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" $1
