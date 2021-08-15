#Vulnerability Name - Protected commands without authentication
import socket

#Logical error in parsing allows for protected commands to be issued
#without authentication
def get_temp(p) :
    s = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    s.sendto(b"LOGOUT a;GET_TEMP", ("127.0.0.1", p))
    msg, addr = s.recvfrom(1024)
    return msg.strip()

try:
    
    infPort = 23456
    incPort = 23457
    print("Issuing command LOGOUT a;GET_TEMP")
    incTemp = get_temp(incPort)

    # The message should return bad command, not the actual temperature
    assert(incTemp == b'Bad Command')
except Exception as ex:
    print ("Expected Bad Command, received", incTemp)
