
from pytube import YouTube,Playlist

type=input("0：下载单个视频 | 1：下载PlayList")
if type=='0':
    urlVideo=input('输入视频url：')
    #'https://www.youtube.com/watch?v=jixLhz-3vXE'
    Videopath=input('输入视频存放路径：')
    #下载单个视频
    if len(Videopath)>0:
        yt= YouTube(urlVideo).streams.first().download(Videopath)
    else:
        yt = YouTube(urlVideo).streams.first().download()
else:
    #下载播单
    urllist = input('输入播单url：')
    # 'https://www.youtube.com/watch?v=jixLhz-3vXE'
    Listpath = input('输入播单存放路径：')
    # 下载playlist
    pl = Playlist(urllist)
    if len(Listpath) > 0:
        pl.download_all(Listpath)
    else:
        pl.download_all()
#streams.filter(res='xxxxx').all()

print("Download finish.")