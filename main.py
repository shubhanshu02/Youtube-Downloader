import sys
import pytube
from pytube import YouTube
from pytube.cli import on_progress
import urllib

def getRequest(url: str):
    try:
        yt = YouTube(url,on_progress_callback=on_progress)
        print("\nTitle of Video:", yt.title)
    except urllib.error.URLError:
        print("\nNo Internet. Please make sure you have an active internet connection.")
        exit()
    except pytube.exceptions.RegexMatchError:
        print("\nInvalid address for youtube video. ")
        exit()
    return yt

def AvailableRes(yt):
    AvailableResolutions = set()
    for i in yt.streams.filter(progressive=True):
        if isinstance(i.resolution, str):
            AvailableResolutions.add(i.resolution)
    print("\nAvailable resolutions:", *AvailableResolutions)

def main(url="",res=None):
    if url=="":
        url = input("Enter the URL of the youtube video: ")

    yt = getRequest(url)
    AvailableRes(yt)
    if res is None:
        res = str(input("Specify the resolution: "))
    else:
        res=res[1:]

    stream = yt.streams.filter(progressive=True, file_extension='mp4',res=str(res)).first()

    if (stream is None):
        print("\nResolution Not Found")
        exit()
        
    print("\nStream connected. Stream:\n", stream)
    print("\nStarting Download...")
    stream = stream.download()
    print("\nDone Downloading\nFile Location:", stream)


if  __name__=="__main__":
    if len(sys.argv)==3:
        main(sys.argv[2],sys.argv[1])
    elif len(sys.argv)==2:
        main(sys.argv[1])
    elif len(sys.argv)==1:
        main()
    else :
        print("You have entered the wrong format for arguments. Please input in the form:\npython main.py -resolution url")
