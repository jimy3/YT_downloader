from pytube import YouTube

def Download(link):
    youtubeobject = YouTube(link)
    youtubeobject = youtubeobject.streams.get_highest_resolution()
    try:
        youtubeobject.download()
    except:
        print('There has been an error in downloading')
    print('Download has completed')

link = input('Input youtube link, URL:')
Download(link)