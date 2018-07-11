from configparser import ConfigParser
import feedparser
import json

class FeedRepository(object):

    def __init__(self, config_path=None):
        self.__config = ConfigParser()
        if config_path is None:
            config_path = 'config/config.ini'
        self.__config.read(config_path)
        self._urls = json.loads(self.__config['rss']['urls'])

    def get_list(self):
        results = []
        results = self.__fetch_all()
        return results
    
    def __fetch_all(self):
        urls = json.loads(self.__config['rss']['urls'])
        feeds = []
        for url in self._urls:
            feeds.extend(self.__fetch(url))
        return feeds

    def __fetch(self, url):
        feed = feedparser.parse(url)
        return feed.entries