from youtubesearchpython import VideosSearch
import yt_dlp as youtube_dl
import sys

ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': '%(title)s.%(ext)s',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'nooverwrites': True,
}

def Get_Url(human_undersandable_title):
    human_undersandable_title = human_undersandable_title.strip()
    print(f"Trying to get the link for: {human_undersandable_title}")

    VideoSearch = VideosSearch(human_undersandable_title, limit = 5)
    link = ""

    if VideoSearch.result():
        link = [x['link'] for x in VideoSearch.result()['result']]
        print(f"Links: {link}\n")
    else:
        print(f"Video search has no results.\n")
    
    return link

if __name__ == "__main__":
    if len(sys.argv) == 1:
        sys.exit("Filename not provided\nPlease use this template: py -3.8 script_name.py filename_with_songnames.txt")

    filename = sys.argv[1]

    with open(filename) as f:
        songs_descriptions = f.readlines()

    songs_descriptions = [Get_Url(x) if x else "" for x in songs_descriptions] #Get URL from titles
    #songs_descriptions = list(filter(None, songs_descriptions))
    
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        for list_of_links in songs_descriptions:
            for url in list_of_links:
                try:
                    ydl.download([url])
                    break
                except Exception as ex:
                    pass
                    
