from mutagen.easyid3 import EasyID3
import os

mp3_file_path = "outpath\\01 บทที่ 1.mp3"

tags = EasyID3(mp3_file_path)

print(os.path.basename(mp3_file_path).split('.')[0])
# 辞書型で格納されたメタデータ表示
for key, value in tags.items():
    print(key,":", value[0])