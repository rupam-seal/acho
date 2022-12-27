import requests
from bs4 import BeautifulSoup
import lxml
import

def photo_downloader(url):
    request = requests.get(url,allow_redirects = True)
    data = BeautifulSoup(request.text,'lxml')
    all_image=data.find_all('figure',itemprop="image")
    count =0
    os.chdir('..\\pictures')
    for i in all_image:
        url=i.find('a',rel="nofollow")
        if url != None:
            i_url = url['href']
            photo_bytes = requests.get(i_url,allow_redirects=True)
            with open(f'{count}3d.jpg','wb') as photo:
                photo.write(photo_bytes.content)
                count +=1

    print("Done")



if __name__ == "__main__":
    photo_downloader("https://unsplash.com/s/photos/3d")