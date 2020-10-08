import os
import shutil
from tkinter import *
root=Tk()
root.title('file handeler')

def file_type(extention,files,source, path):
    for name in files:
        if name.endswith(extention):
            print(name)
            shutil.move(source+name,path)

   

def filter():
    path=e.get()
    paths=Label(root,text=path,fg='red')
    paths.grid(row=1,column=2,columnspan=5)
    source=str(path)
    print(source)
    files=os.listdir(source)
    #destination="/run/media/swaraj/New Volume2/code/vidio/notes/DBDA_NOTES/python/png/"
    print(files)
    file=['.pdf','docx','.png','.jpg','.txt']
    for i in file:
        print(i)
        path=os.path.join(source+i)   
        print(path)
        #os.mkdir(path)
        os.makedirs(path, exist_ok=True)
        print(path)
        file_type(i,files,source, path)
e=Entry(root)
Label1=Label(root,text='enter the directory')
Label1.grid(row=0,column=0)
e.grid(row=0,column=2,columnspan=5)
source=Button(root,text='source',padx=40,pady=5,command=filter)
source.grid(row=1,column=0, columnspan=2)






    #file_type('.docx',files,source, destination)"""

mainloop()