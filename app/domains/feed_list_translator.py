from domains.feed_model import FeedModel
from bs4 import BeautifulSoup
from urllib.request import urlopen

class FeedListTranslator(object):
    
    def translate(self, feed_dicts):
        feed_list = []
        for feed_dict in feed_dicts:
            title = feed_dict['title'] if 'title' in feed_dict else ''
            title = self.__cut_text(self.__get_text(title), 20)
            summary = feed_dict['summary'] if 'summary' in feed_dict else ''
            summary = self.__cut_text(self.__get_text(summary), 30)
            link = feed_dict['link'] if 'link' in feed_dict else ''
            html = urlopen(link)
            og_img = BeautifulSoup(html, "html.parser").find('meta', attrs={'property': 'og:image', 'content': True})
            if og_img is not None:
                image = og_img['content']
            else:
                image = ''

            feed_list.append(
                FeedModel(
                    title=title,
                    summary=summary,
                    link=link,
                    image=image
                )
            )
        return feed_list

    def __cut_text(self, content, length):
        cutted = content[0:length]
        if len(content) > len(cutted):
            cutted += '...'
        return cutted

    def __get_text(self, html):
        return BeautifulSoup(html, "html.parser").getText()  