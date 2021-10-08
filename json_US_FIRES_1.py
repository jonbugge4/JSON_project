import json

infile = open ('US_fires_9_1.json', 'r')
outfile = open ('readable_fire_data_9_1.json', 'w')

firedata = json.load(infile)

json.dump(firedata, outfile, indent = 4)

list_of_fires = firedata

lats, longs, bright = [], [], []

for fr in list_of_fires:
    lat = fr["latitude"]
    longit = fr["longitude"]
    brightness = fr["brightness"]
    lats.append(lat)
    longs.append(longit)
    if brightness > 450:
        bright.append(brightness)

print(lats[:5])
print(longs[:5])
print(bright[:5])


from plotly.graph_objs import Scattergeo, Layout 
from plotly import offline

data = [Scattergeo(lon = longs, lat = lats)]

my_layout = Layout(title = 'California Fires on Septemeber 1st')

fig = {'data': data, 'layout': my_layout}

offline.plot(fig, filename = 'US_Fires_9_1.html')
