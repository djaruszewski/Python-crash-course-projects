import csv
from datetime import datetime

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline


filename = 'data/world_fires_1_day.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    # Printing headers and their index positions:
    #for index, column_header in enumerate(header_row):
        #print(index, column_header)

    # Get brightness, long, lat, and dates.
    dates, brightnesses, lats, lons = [], [], [], []
    hover_text = []
    for row in reader:
        date = datetime.strptime(row[5], '%Y-%m-%d')
        brightness = float(row[2])
        label = f"{date.strftime('%m/%d/%y')} - {brightness}"

        dates.append(date)
        brightnesses.append(brightness)
        lats.append(row[0])
        lons.append(row[1])
        hover_text.append(label)


# Map the fires.
data =[{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_text,
    'marker': {
        'size': [brightness/20 for brightness in brightnesses],
        'color': brightnesses,
        'colorscale': 'YlOrRd',
        'reversescale': True,
        'colorbar': {'title': 'Brightness'},
    },
}]

my_layout = Layout(title='Global Fire Activity')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_fires.html')

