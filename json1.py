import json

infile = open('eq_data_1_day_m1.json', 'r')
outfile = open('readable_eq_data.json', 'w')

eqdata = json.load(infile)

json.dump(eqdata, outfile,indent = 4)

list_of_eqs = eqdata['features']

mags = []
lats = []
longs = []

for eq in list_of_eqs:
    mag = eq['properties']['mag']
    lat = eq['geometry']['coordinates'][0]
    longit = eq['geometry']['coordinates'][1]
    mags.append(mag)
    lats.append(lat)
    longs.append(longit)

print(mags)
print(lats)
print(longs)
