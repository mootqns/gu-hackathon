import urllib.request
from pprint import pprint

def getSongTitles(): 
        fp = urllib.request.urlopen("https://www.billboard.com/charts/hot-100/%22") 
        mybytes = fp.read() 

        mystr = mybytes.decode("utf8") 
        fp.close() 

        lines = mystr.split('\n') 

        songTitles = [] 

        for i in range(len(lines)): 
            if '"title-of-a-story" class="c-title' in lines[i] and 'u-max-width-230@tablet-only' in lines[i]: 
                songTitle = lines[i + 5].strip() 
                songTitles.append(songTitle) 
        return songTitles 

def main():
    songTitles = getSongTitles() 
    pprint(songTitles)

main()
