import re, sys, time
import hashlib
import icloud_mail
with open('log/lastmd5.txt', "r") as f:
    lastmd5 = f.readline()

with open('log/article-list.txt', "wb") as f:
    filename = 'log/page-{}.html'.format(time.strftime("%H"))
    for line in open(filename):
        if 'article-list-link' in line:
            m=re.match(".+<a.+>(.*)</a>", line)
            f.write(bytes(f"{m.group(1)}\n".encode('utf8')))

def calculate_md5(file_path):
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

currentMd5=calculate_md5('log/article-list.txt')

if lastmd5 != currentMd5:
    print("update md5")
    icloud_mail.notice()
    with open('log/lastmd5.txt', "w") as f:
        f.write(currentMd5)
