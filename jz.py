import os
#import sys

#fname = os.path.basename(sys.argv[1])
#fpath = sys.argv[1].split('\\')[-2]



bookname = r"INTENSIVE THAI 1 B"
outpath = "outpath"
g = os.walk(bookname)  

for path,dir_list,file_list in g:  
    for file_name in file_list:  
        #print(os.path.join(path, file_name) )
        mp3_file_path = os.path.join(path, file_name)
        print(mp3_file_path)
        #updateID3(bookname,year,mp3_file_path)
        #print(file_name)

        cmd = "ffmpeg -i \""+mp3_file_path+"\" -af \"afftdn=nf=-25, afftdn=nf=-25, afftdn=nr=12, highpass=f=200, lowpass=f=3000\" \""+outpath+"/"+file_name+"\""
        r_v = os.system(cmd) 
        print (r_v )
#print(cmd)

#r_v = os.system(cmd) 
#print (r_v )