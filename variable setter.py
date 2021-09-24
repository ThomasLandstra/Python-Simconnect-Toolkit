# Import SimConnect
from SimConnect import *
import time

# Create SimConnect link
sc = SimConnect()

# Create aircraft requests
ar = AircraftRequests(sc)

# External variable moniter
def variableSetter(key, val):
   while True:
      time.sleep(5)
      ar.set(key, val)
      input()

# Main App
if __name__ == '__main__':
   key:str = input('Enter the Simulation Variable: ').upper().replace(' ', '_')
   val = float(input('Enter the New Value: '))

   # Does the key exist
   if ar.find(key) == None:
      raise ValueError("Key not found")

   variableSetter(key, val)
