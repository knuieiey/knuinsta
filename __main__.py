import os
import sys
import time
import requests
import threading
from InstagramAPI import InstagramAPI

InstagramAPI = InstagramAPI(sys.argv[1], sys.argv[2])
tmp_path = os.path.dirname(os.path.realpath(__file__)) + '/tmp'

def main(argv):
    InstagramAPI.login()
    threading.Thread(target=start).start()

def start():
    while True:
        try:
            r = requests.get('http://aws.random.cat/meow')
            file_addr = r.json()["file"]
            file = requests.get(file_addr)

            extension = file_addr[file_addr.rfind('.'):]
            file_path = os.path.normpath(tmp_path + '/cat' + str(int(time.time())) + extension)

            if not os.path.exists(tmp_path):
                os.makedirs(tmp_path)

            print("\nDownloading " + file_addr)
            open(file_path, 'wb').write(file.content)

            print("Uploading it")
            InstagramAPI.uploadPhoto(file_path)
            os.remove(file_path)

            time.sleep(1 * 60 * 60)
        except:
            pass


if __name__ == '__main__':
    main(sys.argv)