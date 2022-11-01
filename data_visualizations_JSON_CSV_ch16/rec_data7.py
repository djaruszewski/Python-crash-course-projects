import json

# Explore the structure of the data.
filename = 'data/recent_7_day_eq_16-8.geojson'
with open(filename) as f:
    all_eq_data = json.load(f)

readable_file = 'data/readable_eq_data2.json'
with open(readable_file, 'w') as f:
    json.dump(all_eq_data, f, indent=4)

