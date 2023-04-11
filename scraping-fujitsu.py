from ast import arguments
from cmath import log
import sys
import requests
from bs4 import BeautifulSoup

arg = sys.argv
host = arg[1]
placa = int(arg[2])
rxref = int(arg[3])

#IPS BAIXADA
ipimp = '10.1.55.170' #IMPERATRIZ
ipbal = '10.1.55.178' #BALSAS

#IPS PI - CE
ipthe = '10.1.55.194' #TERESINA
ipfor = '10.1.55.202' #FORTALEZA

