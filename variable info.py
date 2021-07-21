# Import SimConnect
from SimConnect import *

# Create SimConnect link
sc = SimConnect()

# Create aircraft requests
ar = AircraftRequests(sc)

# Get variable info
def variableInfo(key):
   keyData = ar.find(key)
   print('Name: ' + str(keyData._name))
   print('Data Def ID: ' + str(keyData.DATA_DEFINITION_ID))
   print('Description: ' + keyData.description)
   print('Definitions: ' + str(keyData.definitions))
   print('Defined: ' + str(keyData.defined))
   print('Attemps: ' + str(keyData.attemps))
   print('Settable: ' + str(keyData.settable))
   print('LastData: ' + str(keyData.LastData))
   print('LastID: ' + str(keyData.LastID))

# Main App
if __name__ == '__main__':
   while True:
      key:str = input('Enter the Simulation Variable: ').upper().replace(' ', '_')
      
      # Does the key exist
      if ar.find(key) == None:
         raise ValueError("Key not found")

      variableInfo(key)
      