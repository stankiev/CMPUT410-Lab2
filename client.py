# Most code copied from: http://www.binarytides.com/python-socket-programming-tutorial/
# Original author: Silver Moon
# 
# Code edited by: Dylan Stankievech
# For the purposes of CMPUT410-Lab2
#


import socket   #for sockets
import sys  #for exit
 
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, msg:
    print 'Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1]
    sys.exit();
 
host = 'localhost'
port = 8000
 
try:
    remote_ip = socket.gethostbyname( host )
 
except socket.gaierror:
    print 'Hostname could not be resolved. Exiting'
    sys.exit()
 
#Connect to remote server
s.connect((remote_ip , port))
 
# Get a message from user
message = raw_input('Enter a message: ')

# Loop until user enters a message beginning with 'q'
while (message[0] != 'q' and message[0] != 'Q'):
    try :
        #Send the user message to the socket
        s.sendall(message)
    except socket.error:
        #Send failed
        print 'Send failed'
        sys.exit()
     
    #Now receive data from the server socket
    reply = s.recv(4096)
         
    print 'Server response: ' + reply
    
    #Get another user message
    message = raw_input('Enter a message: ')

#Close the socket before exiting
s.close()