import time
import sys
from os import system

for x in range(10):
    time.sleep(1)
    system('cls')
    sys.stdout.write(str(x))
    time.sleep(1)
    sys.stdout.flush()
