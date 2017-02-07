import os, shutil
#from hsaudiotag import auto
Dir_Lst = os.listdir()#some dir
Folder_Flag = []
Counter = -1
for Line in Dir_Lst:
    Counter += 1
    if '.' not in Line:
        Folder_Flag.append(Counter)#Append locations where folders are present

for x in range(Counter):
    Count = 0
    if x not in Folder_Flag and '.py' not in Dir_Lst[x]:
        Temp = auto.File(Dir_Lst[x])
        Artist = Temp.artist
        Album = Temp.album
        if not os.path.exists(Artist) or len(Artist) < 1:
            if not len(Artist) > 0:
                Artist = 'Unknown'
            try:
                os.makedirs(Artist)
            except:pass
        
        Album_Array = os.listdir(Artist)
        if Album not in Album_Array:
            
            if not len(Album) > 0:
                Album = 'Unknown'
               
            Holder = (Artist + '/' + Album)
            if not os.path.exists(Holder):
                try:
                    os.makedirs(Holder)
                except:
                    Count = 1
                    TempStr = ''
                    for i in Album:
                        if i not in['"','?','!','.', '/', chr(92)]:
                            TempStr += i

                        else: pass
                    Holder = (Artist + '/' + TempStr)
                    try:
                        if not os.path.exists(Holder):
                            os.makedirs(Holder)
                            print(Holder)
                    except:
                        print('Ettempt 2 failed')
            else:
                pass

        Source = r''
        Destination = r''
        Source = Dir_Lst[x]
        if Count == 0:
            Destination = Artist + '/' + Album
        else:
            Destination = Artist + '/' + TempStr
        try:
            shutil.move(Source, Destination)
        except:
            pass
           
 
        
