def make_album():
  
  while True:
    artist_name = input("Please input artist name. You can press q at any time to quit program")
    if artist_name == 'q':
      break
    album_title = input("\nPlease input album name. You can press q at any time to quit program")
    if album_title == 'q':
      break
    songs = input("\nPlease input number of songs. You can press q at any time to quit program")
    if songs == 'q':
      break
    

    artist_dic = {'artist':artist_name.title(),
    'album':album_title.title(),
    'Number of songs': songs}
  return artist_dic

dict = make_album()
print(dict)