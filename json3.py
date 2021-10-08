import json

infile = open('US_fires_9_1.json', 'r')
outfile = open('readable_9_1_fire_data.json', 'w')


firedata =json.load(infile)

lats, longs, brightness = [],[],[]

for fr in firedata:
    lat = fr['latitude']
    longit = fr['longitude']
    brightness = fr['brightness']

print(lats[:5])
print(longs)
print(brightness)

