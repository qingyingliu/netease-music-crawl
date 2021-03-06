# encoding=utf8
import requests
from lxml import etree
from setting import HEADERS
from music_item import MusicItem


def download_list():
    play_url = 'http://music.163.com/playlist?id=2217611952'

    s = requests.session()
    response = s.get(play_url, headers=HEADERS)

    html = etree.HTML(response.text)

    for item in html.xpath('//ul[@class="f-hide"]//a'):
        # yield {
        #    "music_name":music.text,
        #    "music_id":music['href'][9:]
        #}
        href = item.xpath('./@href')[0]
        name = item.xpath('./text()')[0]
        yield MusicItem(href[9:], name)

if __name__ == "__main__":
    print(list(download_list()))
    print('{} : {}'.format(music.text, music['href']))
