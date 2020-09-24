**A Simple python function to change profile picture
```python
def change(): #You need to login to get "cookies"
    rHeaders = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "ar-SA,ar;q=0.9,en-SA;q=0.8,en;q=0.7,en-US;q=0.6",
        "Content-Length": str(path.getsize(image)),
        "Cookie": cookies,
        "Host": "www.instagram.com",
        "Origin": "https://www.instagram.com",
        "Referer": "https://www.instagram.com/create/style/",
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Mobile Safari/537.36",
        "X-CSRFToken" : "".join(re.findall(r'csrftoken=.*?;', cookies)).split("=")[1][:-1],
        "X-IG-App-ID": "1217981644879628",
        "X-Requested-With": "XMLHttpRequest"
    }
    rData = {"Content-Disposition": "form-data", "name": "profile_pic", "filename":"profilepic.jpg", "Content-Type": "image/jpeg"}
    files = {'profile_pic': open(image, "rb")}
    r = requests.post("https://www.instagram.com/accounts/web_change_profile_picture/", headers=rHeaders, data=rData, files=files, verify=False)
 ```
