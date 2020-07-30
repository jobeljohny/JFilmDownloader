import requests
import shutil
from prettytable import PrettyTable
from colorama import Fore, Back, Style,init
init()
import os
def clipper(txt):
    subprocess.run(['clip.exe'], input=txt.strip().encode('utf-16'), check=True)
def printmovie(movie,title,year,rating,duration,genres,torrents):
    global mid
    global magnets
    columns = shutil.get_terminal_size().columns
    #print(columns)
    trackers='&tr=udp://open.demonii.com:1337/announce&tr=udp://tracker.openbittorrent.com:80'
    
    print(("TITLE : "+Fore.RED+title+"\t"+Fore.WHITE+"YEAR : "+Fore.RED+str(year)+"\n").center(columns))
    print("\n")
    
    print(Fore.WHITE+"\tGENRES : ",Fore.LIGHTMAGENTA_EX+" , ".join(genres))

    print(Fore.WHITE+"\n\n\tRATING :",Back.GREEN,rating,Back.BLACK,"\t DURATION :"+Style.NORMAL,duration)
    print("\n\n"+Style.BRIGHT)
    
    print(Fore.GREEN+"TORRENTS".center(60))
   
    
    #X
    t = PrettyTable(['Quality','Type','Size','Seeds','Peers','Magnet ID'])
    for torrent in torrents:
        
        magnet='magnet:?xt=urn:btih:'+torrent['hash']+'&dn='+movie['title_long']+trackers
        t.add_row([torrent['quality'],torrent['type'],torrent['size'],torrent['seeds'],torrent['peers'],mid])
        magnets[mid]=[title,torrent['quality'],torrent['size'],magnet,torrent['url']]
        mid=mid+1
    #print(Fore.CYA)
    print(Fore.LIGHTCYAN_EX)
    print(t)
    print(Fore.WHITE)
    
magnets={}
mid=1
print(Style.BRIGHT)
column=shutil.get_terminal_size().columns
site="https://yts.mx/api/v2/list_movies.json"
print(Fore.LIGHTCYAN_EX)
print("TORRENT FILM DOWNLOADER".center(column))
print(Fore.LIGHTRED_EX)
print(("   DEVELOPED BY : "+Fore.WHITE+"JOBEL JOHNY").center(column))
q=input("\n\n Enter movie name : ")
params={"query_term":q,"limit":8}
result=requests.get(site,params=params).json()['data']
total=result['movie_count']
print(Fore.LIGHTGREEN_EX+"\n TOTAL MOVIES :"+Fore.WHITE,str(total),"\n\n")
movies=result['movies']
#print(movies)
for movie in movies:
    title=movie['title']
    year=movie['year']
    rating=movie['rating']
    duration=str(movie['runtime']//60)+" Hours "+str(movie['runtime']%60)+" Minutes"
    genres=movie['genres']
    torrents=movie['torrents']
    printmovie(movie,title,year,rating,duration,genres,torrents)
    print()
    print(Back.BLUE+Fore.LIGHTGREEN_EX)
    print("-".center(shutil.get_terminal_size().columns,"-"))
    print(Back.BLACK+Fore.WHITE)
    print()
idx=int(input("\n\nEnter Magnet ID : "))
d=magnets[idx]
print("\n\n Title : ",Fore.RED+d[0]+Fore.WHITE)
print("\n Quality :",Fore.YELLOW+d[1]+Fore.WHITE,"\tSize :",Fore.LIGHTCYAN_EX+d[2]+Fore.WHITE)
print("\n")
print("MAGENET LINK".center(shutil.get_terminal_size().columns))
print()
print(d[3])
r=requests.get(d[4])
with open("file.torrent" ,"wb") as f:
    f.write(r.content)
#path="C:/Users/Owner/Downloads/"
os.startfile('file.torrent')
print("\n\ndone!")
input()

#print("\n\n Copied to clipboard...")
