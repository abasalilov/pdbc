import requests
from blockchain import Blockchain

r = requests.get('http://127.0.0.1:3000/part')
print('here')

print(r)

bc = Blockchain()
hun = '5YJSA1DG9DFP14705'
h = bc.getVinDecoded('5YJSA1DG9DFP14705')
print('h', h)