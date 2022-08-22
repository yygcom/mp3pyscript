from mutagen.easyid3 import EasyID3
import os
import re

#mp3_file_path = "商务泰语会话教程\第1课 电话联络.mp3"

def updateID3(bookname,year,mp3_file_path):
    


    # メタデータ更新・追加・削除
    tags = EasyID3(mp3_file_path)
    tags["title"] = os.path.basename(mp3_file_path).split('.')[0]
    tags["artist"] = bookname
    tags["albumartist"] = bookname
    tags["album"] = bookname
    tags["date"] = year
    tags["tracknumber"] = re.findall(r"\d+",os.path.basename(mp3_file_path).split('.')[0])[0]
    tags["genre"] = "课文录音"
    tags.save()

    # 更新・追加・削除結果の確認
    tags = EasyID3(mp3_file_path)
    for key, value in tags.items():
        print(key,":", value[0])

bookname = r"INTENSIVE THAI 1 B"
year = "2019"
g = os.walk(bookname)  

for path,dir_list,file_list in g:  
    for file_name in file_list:  
        #print(os.path.join(path, file_name) )
        mp3_file_path = os.path.join(path, file_name)
        updateID3(bookname,year,mp3_file_path)
        #print(file_name)
        
