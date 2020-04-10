import sys
from pytube import YouTube
def main(url="",res=None):
    if url=="":
        url = input("Enter the URL of the youtube video: ")
    if res!=None:
        res=res[1:]
    try:
        yt = YouTube(url)
        print("\nTitle of Video:", yt.title)
        if res!=None:
            try:
                stream = yt.streams.filter(progressive=True, file_extension='mp4',res=str(res))
            except:
                print("the specified resoulution is not found")
        else:
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
    if len(sys.argv)==3:
        main(sys.argv[2],sys.argv[1])
    elif len(sys.argv)==2:
        main(sys.argv[1])
    elif len(sys.argv)==1:
        main()
    else :
        print("Wrong arguement please input:")
        print("python main.py -res url")
