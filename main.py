import sys
import pytube
from pytube import YouTube
import urllib

def getRequest(url: str):
    try:
        yt = YouTube(url)
        print("\nTitle of Video:", yt.title)
    except urllib.error.URLError:
        print("\nNo Internet. Please make sure you have an active internet connection.")
        exit()
    except pytube.exceptions.RegexMatchError:
        print("\nInvalid address for youtube video. ")
        exit()
    except:
        print("\nSome unknown error occured. Please report it at https://github.com/shubhanshu02/Youtube-Downloader/issues")
        exit()
    return yt
def AvailableRes(yt):
    AvailableResolutions = set()
    for i in yt.streams.filter(progressive=True):
        if type(i.resolution)==str:
            AvailableResolutions.add(i.resolution)
    print("\nAvailable resolutions:", *AvailableResolutions)

def main(url="",res=None):
    if url=="":
        url = input("Enter the URL of the youtube video: ")
    yt = getRequest(url)
    AvailableRes(yt)
    
    if res != None:
        res=res[1:]
    else:
        res=str(input("Specify the resolution: "))
        
    if res!=None and len(res)!=0:
        try:
            stream = yt.streams.filter(progressive=True, file_extension='mp4',res=str(res))
        except:
            print("Some Error Occured")
        finally:
            if (stream == None):
                print("Resolution Not Found")
                exit()
    else:
        stream = yt.streams.filter(progressive=True, file_extension='mp4')
    stream = stream.order_by('resolution')
    stream = stream.desc()
    stream = stream.first()
    print(stream)
    stream = stream.download()
    print("Done Downloading", stream)

if  __name__=="__main__":
    if len(sys.argv)==3:
        main(sys.argv[2],sys.argv[1])
    elif len(sys.argv)==2:
        main(sys.argv[1])
    elif len(sys.argv)==1:
        main()
    else :
        print("Wrong arguement please input:")
        print("python main.py -res url")
