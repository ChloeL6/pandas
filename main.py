import pandas as pd
import numpy as np

#%%
albums = pd.read_csv('./data/spotify_albums.csv', header=0)

print(albums.shape)           #return total rows and columns
print(albums.tail())          #return the last n row, the name of all columns and the values of each one
print(albums.head())          #return the first n row, the name of all columns and the values of each one

print(albums.loc[10:20, ['name', 'release_date']]) #show just rows 10-20 of the 'name' and 'release_date' columns

albums.drop_duplicates(inplace=True)        #Remove duplicated rows
print(f'albums shape after drop_duplicates(): {albums.shape}')    



#%%
artists = pd.read_csv('./data/spotify_artists.csv', header=0)

print(artists.shape)          #return total rows and columns
print(artists.tail())         #return the last n row, the name of all columns and the values of each one
print(artists.head())         #return the first n row, the name of all columns and the values of each one

artists.drop_duplicates(inplace=True)   #Remove duplicated rows
print(f'artists shape after drop_duplicates(): {artists.shape}')

def replace_empty_list(value):        #replace empty list [] with nan 
    if len(value) == 2:
        return np.nan
    else:
        return value

artists['genres']= artists['genres'].map(replace_empty_list)
print(artists.head(5))

#join artist to albums
#not every artist has albums
# Join artists and albums on the artist ID. Print the head() and shape of the resulting DataFrame.

# Since some artist does not have albums, merge() with how='inner' returns a dataframe returns matched rows between artists and albums
#if artist does not has album, or the album does not has matched artist, that rows will be discarded. 
artists_albums = artists.merge(albums.set_index('No'), left_on='id', right_on='artist_id', how='inner', suffixes=['_art', '_alb']).drop_duplicates()
print(artists_albums.shape)
artists_albums.head(5)



#%%
tracks = pd.read_csv('./data/spotify_tracks.csv', header=0)

print(tracks.shape)       #return total rows and columns
print(tracks.tail())      #return the last n row, the name of all columns and the values of each one
print(tracks.head())      #return the first n row, the name of all columns and the values of each one

tracks.drop_duplicates(inplace=True)
print(f'tracks shape after drop_duplicates(): {tracks.shape}')

cols = list(tracks.columns)       #print name of columns in Tracks
print(cols)

tracks.drop(labels='lyrics', axis=1, inplace=True)  #drop lyrics column
print(list(tracks.columns))

#since some albums does not include in tracks, merge() with how='inner' will only return the matched rows between two dataframes
albums_tracks = albums.merge(tracks, left_on='id', right_on='album_id', how='inner')

print(f'albums: \n {albums.shape}')
print(f'tracks: \n {tracks.shape}')
print(albums_tracks.shape)
albums_tracks.head()



#%%
high_appearance = artists['name'].value_counts()      #find artist with highest appearance
print(high_appearance)
print(f'Artists appear the most is: Haze and Sasha')



# %%
top_rank = artists.nlargest(n=10, columns=['artist_popularity'])        #artist with highest_ranking
top_rank[['name', 'artist_popularity']]