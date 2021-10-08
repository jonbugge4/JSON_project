import json

infile = open ('US_fires_9_14.json', 'r')
outfile = open ('readable_fire_data_9_14.json', 'w')

firedata = json.load(infile)

json.dump(firedata, outfile, indent = 4)

list_of_fires = firedata

lats, longs, bright, hover_texts = [], [], [], []

for fr in list_of_fires:
    lat = fr["latitude"]
    longit = fr["longitude"]
    brightness = fr["brightness"]
    if brightness > 450:
        bright.append(brightness)
        lats.append(lat)
        longs.append(longit)
        hover_texts.append(brightness)

print(lats[:5])
print(longs[:5])
print(bright[:5])


from plotly.graph_objs import Scattergeo, Layout 
from plotly import offline

#data = [Scattergeo(lon = longs, lat = lats)]

data = [{
    'type': 'scattergeo',
    'lon': longs,
    'lat': lats,
    'text': hover_texts,
    'marker':{
        'size': [.035*b for b in bright],
        'color': bright, 
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': {'title': 'Brightness'}

    }
}]

my_layout = Layout(title = 'US Fires - 9/14/2020 through 9/20/2020')

fig = {'data': data, 'layout': my_layout}

offline.plot(fig, filename = 'US_Fires_9_14.html')