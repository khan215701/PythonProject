from pytube import YouTube

# download single video from youtube
try:
    yt_url = YouTube('https://www.youtube.com/watch?v=nqye02H_H6I')
    stream = yt_url.streams.first()
    stream.download("D:/")
    print("download successfully: ", yt_url)
except:
    print("something is wrong!")


# download a list of video from file
try:
    yt_list = open("url_list.txt", 'r')
    for list_url in yt_list:
        yt_listing = YouTube(list_url)
        stream_video = yt_listing.streams.first()
        stream_video.download("D:/")
        print("download successfully: ", list_url)
except:
    print("something is wrong!")


