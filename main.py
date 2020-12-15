from os import popen
from time import sleep
def download(link):
    try:
        do = popen((f"wget -v {link}"))
    except:
        print("[-]please check your connection!!!")

print("""
 _   _    _  _____ _____ ____   ___  _   _    _    ____  _  __
| | | |  / \|_   _|_   _/ ___| / _ \| \ | |  / \  |  _ \| |/ /
| |_| | / _ \ | |   | | \___ \| | | |  \| | / _ \ | |_) | ' / 
|  _  |/ ___ \| |   | |  ___) | |_| | |\  |/ ___ \|  __/| . \ 
|_| |_/_/   \_\_|   |_| |____/ \___/|_| \_/_/   \_\_|   |_|\_\
""")


while True:
    print("If your download is over enter 0 if not enter 1 :\n ")
    check = int(input("0 or 1 >>> "))
    if check == 0:
        print("Thank you for using HATTSONAPK program!!")
        break
    link = input("\nEnter the download link >>> ")
    download(link)
    sleep(5)
    print("\a\a\a\a\a\a\a\a Your download is done! I'm ready for next one.")

