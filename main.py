from pytube import YouTube

url = input("Enter the URL of the youtube video: ")

try:
    yt = YouTube(url)
    print("\nTitle of Video:", yt.title)
except:
    print("\nConnection Error\n")

stream = yt.streams.filter(progressive=True, file_extension='mp4')
stream = stream.order_by('resolution')
stream = stream.desc()
stream = stream.first()
print(stream)
stream = stream.download()

print("Done Downloading", stream)

