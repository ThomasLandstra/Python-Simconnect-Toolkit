# Import SimConnect
from SimConnect import *
import time

# Create SimConnect link
sc = SimConnect()

# Create aircraft requests
ar = AircraftRequests(sc)

# External variable moniter
def variableMoniter(key):
   print("") # Blank line for readability
   while True:
      print(ar.get(key))
      time.sleep(0.1)

# Main App
if __name__ == '__main__':
   key:str = input('Enter the Simulation Variable: ').upper().replace(' ', '_')

   # Does the key exist
   if ar.find(key) == None:
      raise ValueError("Key not found")

   variableMoniter(key)
