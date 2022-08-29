import os

x = 0
photo_dir=os.path.dirname(__file__)+"\\traindata1\\"
extension = ".jpg"
for i in os.listdir(photo_dir): 
    if  i.endswith(extension):
        os.rename(photo_dir+i, photo_dir+str(x)+extension)
        x+=1