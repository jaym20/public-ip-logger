import datetime # PREinstalled
from requests import get #Needs to be installed using pip install requests

ip = get('https://api.ipify.org').text

path = 'C:/Users/jmmak/Desktop/' # Change to the current directory PATH where script is placed
filename = "iplog.txt" # Give you log a file name

with open(path + filename, 'a') as log:
    log.write("|" + str(datetime.datetime.now()) + "  " + str(ip) + "|" + '\n')
