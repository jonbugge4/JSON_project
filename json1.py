import json

infile = open('eq_data_30_day_m1.json', 'r')
outfile = open('readable_eq_data.json', 'w')

eqdata = json.load(infile)

json.dump(eqdata, outfile,indent = 4)

list_of_eqs = eqdata['features']

mags = []
lats = []
longs = []

for eq in list_of_eqs:
    mag = eq['properties']['mag']
    lat = eq['geometry']['coordinates'][1]
    longit = eq['geometry']['coordinates'][0]
    mags.append(mag)
    lats.append(lat)
    longs.append(longit)

print(mags[:5])
print(lats[:5])
print(longs[:5])
# How ould you list the top 5 elements? brackets
# :5 is grabbing the first 5 elements. You can specify a range with X:X


from plotly.graph_objs import Scattergeo, Layout 
from plotly import offline

data = [Scattergeo(lon=longs, lat=lats)]

my_layout = Layout(title = 'Global Earthquakes 1 Day')

fig = {'data': data, 'layout': my_layout}

offline.plot(fig, filename = 'gloalearthquakes1day.html')