#pip install icrawler
#pip install PIL

from icrawler.builtin import GoogleImageCrawler
import glob
from PIL import Image


def search_img(key_word):
    search_item = str(key_word)
    google_crawler = GoogleImageCrawler(storage={'root_dir': "C:/Users/darah/OneDrive/Documents/GitHub/Project-Whatdowecallit/Raw_images"})
    google_crawler.crawl(keyword=search_item, max_num=10)

    image_names = glob.glob(r"C:/Users/darah/OneDrive/Documents/GitHub/Project-Whatdowecallit/Raw_images\*.jpg")

    new_width = 256
    new_height = 256

    count = 0

    for i in image_names:
        img = Image.open(i)
        img = img.resize((new_width, new_height), Image.ANTIALIAS)
        # img = img.crop((new_width, new_height))
        img.save(r"C:/Users/darah/OneDrive/Documents/GitHub/Project-Whatdowecallit/Processed_images\\" + str(count) + ".jpg")
        count += 1

        print("Images Resized " + str(count) + "/" + str(len(image_names)), end='\r')


search_img("Shrek")
