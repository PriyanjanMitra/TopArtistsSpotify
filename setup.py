import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv
import collections
from operator import itemgetter


spotify_top50_artists = open('topartists.csv', 'w', newline='')
csv_writer = csv.writer(spotify_top50_artists)
spotify_list = pd.read_csv('top_10000_1960-now.csv')
spotify_artist = list(spotify_list['Artist Name(s)'])
spotify_artist_dict = {}
list_count = [count for item, count in collections.Counter(spotify_artist).items() if count > 1]
list_artist = [item for item, count in collections.Counter(spotify_artist).items() if count > 1]
for i, j in zip(list_artist, list_count):
    spotify_artist_dict[i] = j
sort_dict = dict(sorted(spotify_artist_dict.items(), key=itemgetter(1), reverse=True))
for i in sort_dict:
    csv_writer.writerow([i, sort_dict[i]])

spotify_top50_artists.close()

