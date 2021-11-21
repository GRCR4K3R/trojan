#!/bin/python

#module
import os
import sys
import time



#menu
def menu():
  nomor = raw_input("Masukkan Nomor Target : ") # input untuk si user memasukkan nomornya
  jumlah = int(input("Masukkan jumlahnya : ") # input untuk menyuruh si user memasukkan jumlahnya
  time.sleep(1)

  try:
      for i in range(jumlah):
               print "Mencoba mengirim Virus Ke ↣",nomor
               time.sleep(0.1)
  except KeyboardInterrupt:
      print "### Selesai ###"
               
menu()
