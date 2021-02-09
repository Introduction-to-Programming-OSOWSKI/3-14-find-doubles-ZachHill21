#DO NOT TAMPER WITH THIS FILE
#ANY EDITS YOU MAKE TO THIS FILE WILL BE SAVED TO YOUR PUBLIC GITHUB HISTORY
#TAMPERING WITH THIS FILE WILL BE OBVIOUS AND WILL RESULT IN A ZERO

import main;
import datetime;

year = 2021
month = 2
day = 9

def test_code():
    assert main.findDoubles("qwertyuiop") == False, 'main.findDoubles("qwertyuiop") == False failed'
    assert main.findDoubles("yellow") == True, 'main.findDoubles("yellow") == True failed'

def test_late():
    assert datetime.datetime.now() < datetime.datetime(year, month, day + 1, 4, 0), "Submitted Late"
