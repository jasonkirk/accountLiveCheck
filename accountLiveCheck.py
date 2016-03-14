import socket
#mypath = '/var/cpanel/users/'
mypath = './test/' # For test purposes
from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

for account in onlyfiles:
    #print(account)
    with open(mypath + account) as f:
        content = f.readlines()
    for line in content:
        if "IP=" in line:
            line = line.split("=",1)[-1]
            line = line.rstrip('\r\n') #removes return line from string
            storedIP = line
            #print(storedIP)
        if "DNS=" in line:
            line = line.split("=",1)[-1]
            line = line.rstrip('\r\n') #removes return line from string
            storedDNS = line
            if ".res" in storedDNS:
                break
            #print(storedDNS)

    try:
        oldIP = socket.gethostbyname(storedDNS)
    except socket.gaierror:
        oldIP = "0.0.0.0"
    currentIP = storedIP
    if oldIP:

        if (oldIP != currentIP):
            print(storedDNS + " " + currentIP + " " + oldIP + " IP doesn't match")

    #        else:
    #            print(storedDNS + " IP matches")





#print(socket.gethostbyname('webfor.com'))
