import json
import yaml
import string
from freqs import LetterFrequency

def ascii_encode_dict(data):
    ascii_encode = lambda x: x.encode('ascii')
    return dict(map(ascii_encode, pair) for pair in data.items())

json_data=open('7-7-14.json', 'r')
data = json.loads(json_data, object_hook=ascii_encode_dict)
json_data.close()

'''
data['grid']
rowlen = data['size']['rows']
collen = data['size']['cols']
'''

freq = LetterFrequency()
print (data['grid'])
for letter in data['grid']:
    if letter != '.':
        freq.increment(letter)

print(freq.getFrequencies());
