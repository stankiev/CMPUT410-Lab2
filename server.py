# Most code copied from: http://www.binarytides.com/python-socket-programming-tutorial/
# Original author: Silver Moon
# 
# Code edited by: Dylan Stankievech
# For the purposes of CMPUT410-Lab2
#

import socket
import sys
from thread import *
 
HOST = ''   # Symbolic name meaning all available interfaces
PORT = 8000 # Arbitrary non-privileged port
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((HOST, PORT))
except socket.error , msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()
 
s.listen(10)
print 'Socket now listening...'
 
#Function for handling connections. This will be used to create threads
def clientthread(conn):
     
    #infinite loop so that the function does not terminate and the thread does not end.
    while True:
         
        #Receiving from client
        data = conn.recv(1024)
        data = data.rstrip('\r\n')
        reply = data + " Dylan"
        if not data:
            break
     
        conn.sendall(reply)
     
    #came out of loop, close the connection
    conn.close()
 
#now keep talking with the client
while 1:
    #wait to accept a connection - blocking call
    conn, addr = s.accept()
     
    #start new thread takes 1st argument as a function name to be run, second is the tuple of arguments to the function.
    start_new_thread(clientthread ,(conn,))
 
s.close()