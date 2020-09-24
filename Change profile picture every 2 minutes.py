#احتياطا اذا ما فهمت شي من الكود او الشرح الخايس حسابي
#Y1z1n.programs
from datetime import datetime
import requests, json, urllib3, re, random
from getpass import getpass
from os import path
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning) #بس يشيل التحذيرات في حال كنت مشغل اي برنامج يراقب الاتصالات
NowH, NowM = datetime.now().hour, datetime.now().minute #المتغير الاول لعدد الساعات والثاني للدقائق
NumberOfErrors, NumberOfCorrect = 0, 0
Images = [] #حط مجموعه صور مع مسارها الكامل ونهايه اسماء الملفات
username = input("Username => ")
password = getpass(prompt="Password => ", stream=None) #تخفي الي انت تكتبه بس للخصوصيه
def login(user, password): 
    rHeaders= {"Accept": "*/*" , "Accept-Language": "ar,en-US;q=0.7,en;q=0.3" , "Content-Type": "application/x-www-form-urlencoded", "Cookie": "Y1z1n" , "Host": "www.instagram.com" , "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0" , "X-CSRFToken": "Y1z1n", "X-IG-App-ID": "936619743392459" , "X-Instagram-AJAX": "Y1z1n", "X-Requested-With": "XMLHttpRequest"}
    rData = {"username": user, "enc_password": "#PWD_INSTAGRAM_BROWSER:0:1596498182:"+password, "queryParams": "{}" , "optIntoOneTap": "false"}
    r = requests.post("https://www.instagram.com/accounts/login/ajax/" ,  headers=rHeaders , data=rData, verify=False)
    res = r.json()
    if "userId" in res:
        print("Done login :)")
        csrf = str(r.headers)
        full_cookies = "".join(re.findall(r'csrftoken=.*?;', csrf)) +   "".join(re.findall(r'ds_user_id=.*?;', csrf)) + "".join(re.findall(r'ig_did=.*?;', csrf))  + "".join(re.findall(r'mid=.*?;', csrf)) + "".join(re.findall(r'rur=.*?;', csrf)) + "".join(re.findall(r'sessionid=.*?;', csrf)) + "".join(re.findall(r'shbid=.*?;', csrf)) + "".join(re.findall(r'shbts=.*?;', csrf)) #اوله
        return full_cookies
    else:
        print("Wrong username or password, or a banned account")
        return False
Cookies = ""
csrf = ""
rData = {"Content-Disposition": "form-data", "name": "profile_pic", "filename":"profilepic.jpg", "Content-Type": "image/jpeg"}
files = {'profile_pic': ""} #rData, files, rHeaders | كلها بنستخدمها في تغير صوره العرض
rHeaders = {"Accept": "*/*","Accept-Encoding": "gzip, deflate","Accept-Language": "ar-SA,ar;q=0.9,en-SA;q=0.8,en;q=0.7,en-US;q=0.6","Content-Length": "","Cookie": Cookies,"Host": "www.instagram.com","Origin": "https://www.instagram.com","Referer": "https://www.instagram.com/create/style/","User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Mobile Safari/537.36","X-CSRFToken" : "None","X-IG-App-ID": "1217981644879628","X-Requested-With": "XMLHttpRequest"}
def change(Image): #فنكشن تغير الصوره
    global username,password, Cookies, rData, rHeaders, files #نستدعي المتغيرات من البرنامج كامل الى هذا الفنكشن
    Cookies = login(username, password)
    csrf = "".join(re.findall(r'csrftoken=.*?;', Cookies)).split("=")[1][:-1]
    rHeaders['X-CSRFToken'] = csrf #نعدل القيم بداخل rHeaders
    rHeaders['Cookie'] = Cookies
    rHeaders['Content-Length'] = str(path.getsize(Image))
    files['profile_pic'] = open(Image, "rb") #ناخذ البايتز من الصوره
    r = requests.post("https://www.instagram.com/accounts/web_change_profile_picture/", headers=rHeaders, data=rData, files=files, verify=False)#, proxies=proxies)
    if r.status_code == 200: #200 يعني ان الارسال نجح
        print("Image url \n\n" + json.loads(r.content)['profile_pic_url_hd']) #يعطيك رابط الصوره
    return r.status_code
def checktime(): #فنكشن الوقت
    global NowH, NowM, Images, Cookies, NumberOfErrors, NumberOfCorrect
    while True:
        if NowM + 2 == datetime.now().minute:
            print(f"Time : {NowH}:{NowM} | OLD")
            NowM += 2
            if NowM >= 59:
                NowM = 0
                NowH += 1
                if NowH == 24:
                    NowH = 0
            print(f"Time : {NowH}:{NowM} | NEW")
            if change(random.choice(Images)) == 200:
                NumberOfCorrect += 1
                print(f"Good Number : {NumberOfCorrect}")
            else:
                NumberOfErrors += 1
                print(f"Eeh Error number : {NumberOfErrors}")
checktime()