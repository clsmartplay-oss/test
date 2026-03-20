import urllib.request
import re

url = 'https://whiteglobalmarketing.co/elementor-2345/'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    html = urllib.request.urlopen(req).read().decode('utf-8')
    imgs = re.findall(r'src=\"(https://whiteglobalmarketing.co/wp-content/uploads/[^\"]+)\"', html)
    print("IMAGES:")
    for img in set(imgs):
        print(img)
except Exception as e:
    print("Error:", e)
