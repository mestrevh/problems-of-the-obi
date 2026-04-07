#!/usr/local/bin/python

from random import randint
import string, sys, os
from sets import Set

def itos(i):

  s = ""
  s += chr(ord('a') + (i/1000)%10)
  s += chr(ord('a') + (i/100)%10)
  s += chr(ord('a') + (i/10)%10)
  s += chr(ord('a') + i%10)
  return s

def rands(a):

  s = ""
  for i in range(a):
    s += chr(ord('a') + randint(0, 10))
  return s


def randtest(nc, nr):

  ts = ""
  
  n = []
  for i in range(nc):
    n.append(itos(i))
  
  ts += str(nr) + '\n'
  
  x = Set([])
  v = {}
  for i in range(nr):
    a = randint(0,nc-1)
    b = randint(0,nc-1)
    while a == b:
      b = randint(0,nc-1)
    x.add(a)
    x.add(b)
    ts += n[a] + ' ' + n[b] + '\n'
    
  a = randint(0,nc-1)
  while a not in x:
    a = randint(0,nc-1)
  b = randint(0,nc-1)
  while a == b or b not in x:
    b = randint(0,nc-1)
    
  ts += '\n' + n[a] + ' ' + n[b] + '\n'
  return ts
  
t = []
for i in range(20):
  t.append([])

#Define testes:

#Manualmente de 0 a 7

#t[0]
s = '''1
a b

a b'''
t[0].append(s)

s = '''2
a c
b a

a c'''
t[0].append(s)

#t[1]
s = '''3
a c
b c
a c

c a'''
t[1].append(s)

#t[2]
s = '''3
c a
c b
b a

a c'''
t[2].append(s)

#t[3]
s = '''2
A a
A B

a A'''
t[3].append(s)

s = '''2
a A
a b

A a'''
t[3].append(s)


#t[4]
s = rands(99)
big1 = s+'a'
big2 = s+'b'
big3 = s+'c'
s = '''2\n''' + big1 + ' ' + big2 + '\n' + big2 + ' ' + big3 + '\n\n' + big1 + ' ' + big3 
t[4].append(s)

#t[5]
aux = rands(96)
s = '''1000\n'''
for i in range(1000):
  s += aux + itos(i) + ' ' + aux + itos(i+1) + '\n'
s += '\n' + aux + itos(1000) + ' ' + aux + itos(0)
t[5].append(s)

#t[6]
s = '''3
A b
b a
c b

A c'''
t[6].append(s)

#t[7]
s = '''1000\n'''
for i in range(1000):
  s += itos(2*i) + ' ' + itos(2*i+1) + '\n'
s += '\n' + itos(1999) + ' ' + itos(0)
t[7].append(s)

s = '''1000\n'''
for i in range(1000):
  s += itos(2*i) + ' ' + itos(2*i+1) + '\n'
s += '\n' + itos(0) + ' ' + itos(1999)
t[7].append(s)

#automatico de 8 a 19

for i in range(9,21):
  for j in range(1):
    t[i-1].append(randtest(30*i, 50*i))
    
    
#Escreve e roda os testes    

os.mkdir('C:/acm/wiki/tests')
for i in range(1,21):
  os.mkdir('C:/acm/wiki/tests/test' + str(i))
  
os.system('g++ C:/acm/wiki/wiki.cpp -o C:/acm/wiki/wiki.exe')
#os.system('g++ C:/acm/wiki/w2.cpp -o C:/acm/wiki/w2.exe')

for i in range(1,21):
  for j in range(1,len(t[i-1])+1):
    ifi = 'C:/acm/wiki/tests/test' + str(i) + '/in' + str(j)
    ofi = 'C:/acm/wiki/tests/test' + str(i) + '/out' + str(j)
    ofi2 = 'C:/acm/wiki/tests/test' + str(i) + '/out2' + str(j)
    f=open(ifi, 'w')
    f.write(t[i-1][j-1])
    f.close()
    cmd='C:/acm/wiki/wiki.exe < ' + ifi + " > " + ofi
    os.system(cmd)
    #cmd='C:/acm/wiki/w2.exe < ' + ifi + " > " + ofi2
    #os.system(cmd)
    #print i, j
    #os.system('diff ' + ofi + ' ' + ofi2)
    
    
    