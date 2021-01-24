print("------------ created by alhassan alharbi ------------")

print("\033[0;37m twitter ===>\033[3;34m @alhassanAlharb7 \033[0;37m<=== ")
print("""\033[0;32m download picture [1]  
 download video [2]\033[1;37m""")
op=input("\033[3;36m choose the options \n")
if op=="1":
    import requests
    r=requests.get(input("\033[0;31m enter the link for picture >> >> "))
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
