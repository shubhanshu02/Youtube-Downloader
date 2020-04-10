import sys
from pytube import YouTube
main(url=""):
    if url=="":
        url = input("Enter the URL of the youtube video: ")
    
    try:
        yt = YouTube(url)
        print("\nTitle of Video:", yt.title)
        stream = yt.streams.filter(progressive=True, file_extension='mp4')
        stream = stream.order_by('resolution')
        stream = stream.desc()
        stream = stream.first()
        print(stream)
        stream = stream.download()
        print("Done Downloading", stream)
    
    except:
        print("\nConnection Error\n")
        print("TRY AGAIN LATER!")

if  __name__=="__main__":
    main(sys[1])
