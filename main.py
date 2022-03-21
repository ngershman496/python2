
from scapy.all import *
import socket
import datetime
# Gets the current date and returns in M/D/YYYY format
def getDate():
    now = datetime.date.today()
    return now.month,now.day,now.year;

#gets the current time of the machine and returns in H:M:S format
def getTime():
    now = datetime.datetime.now()
    return now.hour,now.minute,now.second;

# uses an opened socket to gather the current ip address of the machine
def getIP():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 443))
    ip = s.getsockname()[0]
    # make sure to close socket
    s.close()
    return ip

if __name__ == '__main__':

    date = getDate()    # get the date
    time = getTime()    # get the time
    ip = getIP()        # get the host ip

    print(f"Date: {date[0]}/{date[1]}/{date[2]}")   # Print the date
    print(f"Time: {time[0]}:{time[1]}:{time[2]}")   # Print the time
    sniff(filter=f"host {ip}",prn=lambda x:x.summary(), count=15, ) # Sniff traffic for the host ip address

