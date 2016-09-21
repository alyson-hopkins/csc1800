# Matt O'Neill, Alyson Hopkins, Gisu Eom

import sys

class Team:
    for line in sys.stdin:
        inp = line.upper()
        try:
            inp.replace(" \n", "")
            print inp
        break
        except:
            print ("The line " + inp + " is invalid.")
