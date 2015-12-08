#!/usr/bin/python

while True:
   reply=input('Enter text: ')
   if reply == 'stop': 
      break
   elif not reply.isdigit():
      print('Bad!' * 8)
   else:
      num= int(reply)
      if num < 20:
         print('low')
      else:
         print(num**2)
print('Bye')
