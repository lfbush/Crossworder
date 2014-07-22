__author__ = 'laurabush'

json_data=open('7-7-14.json', 'r')
data = json.load(json_data)
json_data.close()

print data

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
