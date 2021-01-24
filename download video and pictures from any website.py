print(""" download picture [1] 
 download video [2]""")
op=input("choose the options \n")
if op=="1":
    import requests
    r=requests.get(input("enter the link for picture >> >> "))
    a=input("enter the file name >>>>")
    with open(a+'.png','wb')as f:
        f.write(r.content)
if op=="2":
    import requests
    chunk_size=256
    link=input("enter the link for video --> ")
    r=requests.get(link,stream=True)
    with open(input("enter the name foe video ==> ")+".mp4",'wb') as f:
        for video in r.iter_content(chunk_size=chunk_size):
            f.write(video)

