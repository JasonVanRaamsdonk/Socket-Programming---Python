# Socket-Programming---Python
client server programming in python

Why use TCP (transmission control protocol):
-
- <b>Is reliable:</b> packets dropped in the Network are detected and retransmitted by the sender
- <b>Has in-order data delivery:</b> data is read by your application in the order it was written by the sender 

What is a Socket:
-
- A socket is the endpoint that receives data, which sits at an IP in a port.

Socket Functions:
-

- <b>bind()</b> - defines a relationship between the socket you created and the addresses that are available on your host.
  <br><i>parameters:</i> 'ip address' & 'port'
  
- <b>listen()</b>  - marks the connected socket as a passive socket, that is, the socket that will be used to accept incoming connection requests.
   <br><i>parameters:</i> 'queue length'
   
 
 