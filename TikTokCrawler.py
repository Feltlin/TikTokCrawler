from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time
import pickle
import requests
import datetime
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

#TikTok Creative Center: https://ads.tiktok.com/business/creativecenter/pc/en

def Upload():
    path = filedialog.askopenfilename()
    url = "https://www.tiktok.com"
    driver = OpenDriver(url)
    Login(driver, url)

    #Upload video.
    upload = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Upload"))
    )
    upload.click()

    file_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//input[@type="file"]'))
    )
    file_input.send_keys(path)
    input("Uploading! Press Enter to continue...")
    
    time.sleep(5)
    driver.quit()

def Download():
    userid = "oliverprochazka_"
    url = "https://www.tiktok.com"
    driver = OpenDriver(url + "/@" + userid)

    time.sleep(5)
    driver.quit()

def DownloadByLink():
    downloadWindow = Toplevel()
    downloadWindow.geometry("400x300")
    downloadWindow.config(bg = "#000000")
    downloadWindow.attributes('-topmost', True)
    Label(downloadWindow, text = "Paste the Link", fg = "#ffffff", bg = "black").pack()
    linkEntry = Entry(downloadWindow, fg = "#ffffff", bg = "black")
    linkEntry.pack()
    linkButton = Button(
        downloadWindow,
        text = "Download",
        image = download_logo,
        bg = "black",
        fg = "white",
        compound = LEFT,
        width = 100,
        command = lambda:LinkDownload(linkEntry),
    )
    linkButton.pack()

def LinkDownload(linkEntry):
    link = linkEntry.get()
    driver = OpenDriver(link)
    # Login(driver, link)
    #Upload video.
    captcha = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="captcha_close_button"]'))
    )
    print("captcha found.")
    captcha.click()
    print("captcha closed.")
    videoLink = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "source"))
    )
    videoLink = videoLink.get_attribute("src")
    print("Got the link.")
    cookies = driver.get_cookies()
    cookies = {cookie["name"]: cookie["value"] for cookie in cookies}
    response = requests.get(videoLink, stream=True, cookies = cookies)
    print("Got the cookies.")

    if response.status_code == 200:
        name = link.split('@')[1].split('/')[0]
        date = datetime.datetime.fromtimestamp(int(bin(int(link.split('/')[-1]))[2:][:31], 2)).strftime('%Y-%m-%d_%H-%M-%S')
        if not os.path.exists("./ByLink"):
            os.makedirs("./ByLink")
        with open(f"./ByLink/{name}_{date}.mp4", "wb") as file:
            for chunk in response.iter_content(chunk_size = None):
                if chunk:
                    file.write(chunk)
        print("Video downloaded successfully!")
    else:
        print(f"Failed to download video. Status code: {response.status_code}")
    
    time.sleep(10)
    driver.quit()
    
def OpenDriver(url):
    service = Service(executable_path="./Driver/chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.get(url)
    return driver

def Login(driver, url):
    try:
        #Open cookies to auto login.
        with open("cookies.pkl", 'rb') as f:
            cookies = pickle.load(f)
            for cookie in cookies:
                driver.add_cookie(cookie)
            driver.refresh()

    #Login manually if cookies not found.
    except FileNotFoundError:
        print("No cookies found.")
        driver.get(url)
        input("Please log in manually this time and press Enter to continue......")
        with open("cookies.pkl", 'wb') as f:
            pickle.dump(driver.get_cookies(), f)
        driver.get(url)
    
window = Tk()
# window.attributes('-topmost', True)
notebook = ttk.Notebook(window)

window.geometry("800x600")
window.title("TikTok Crawler")
icon = PhotoImage(file = "./Image/TikTok_Logo.png")
window.iconphoto(True, icon)
window.config(bg = "#000000")
currentState = 0

download_logo = PhotoImage(file = "./Image/material-symbols--download-rounded.png")
upload_logo = PhotoImage(file = "./Image/material-symbols--upload-rounded.png")

uploadTab = Frame(notebook, bg = "#000000")
downloadTab = Frame(notebook, bg = "#000000")
notebook.add(uploadTab, text = "Upload")
notebook.add(downloadTab, text = "Download")
notebook.pack(expand = True, fill = "both")

# uploadMenu = Menu(menubar, tearoff = 0)
# menubar.add_command(label = "Upload")

uploadButton = Button(
    uploadTab,
    text = "Upload     ",
    image = upload_logo,
    bg = "black",
    fg = "white",
    compound = LEFT,
    width = 100,
    command = Upload,
)
uploadButton.pack()

downloadByLinkButton = Button(
    downloadTab,
    text = "By Link",
    image = download_logo,
    bg = "black",
    fg = "white",
    compound = LEFT,
    width = 100,
    command = DownloadByLink,
)
downloadByLinkButton.pack()

downloadByIDButton = Button(
    downloadTab,
    text = "By User ID",
    image = download_logo,
    bg = "black",
    fg = "white",
    compound = LEFT,
    width = 100,
    command = Download,
)
downloadByIDButton.pack()

window.mainloop()

# service = Service(executable_path="./Driver/chromedriver.exe")
# driver = webdriver.Chrome(service=service)
# url = "https://www.tiktok.com"

# driver.get(url)
# try:
#     #Open cookies to auto login.
#     with open("cookies.pkl", 'rb') as f:
#         cookies = pickle.load(f)
#         for cookie in cookies:
#             driver.add_cookie(cookie)
#         driver.refresh()
#         input("Log in successfully! Press Enter to continue...")

#         #Upload video.
#         upload = WebDriverWait(driver, 10).until(
#             EC.presence_of_element_located((By.LINK_TEXT, "Upload"))
#         )
#         upload.click()
#         input("Clicked! Press Enter to continue...")

#         file_input = driver.find_element(By.XPATH, '//input[@type="file"]')
#         video_path = r"D:\Code\Python\WebCrawler\bjarnson_fitness\video\2024-09-30_15-23-15_2.mp4"
#         file_input.send_keys(video_path)
#         input("Uploading! Press Enter to continue...")

# #Login manually if cookies not found.
# except FileNotFoundError:
#     print("No cookies found.")
#     driver.get(url)
#     input("Please log in manually this time and press Enter to continue......")
#     with open("cookies.pkl", 'wb') as f:
#         pickle.dump(driver.get_cookies(), f)
#     driver.get(url)

# time.sleep(5)
# driver.quit()