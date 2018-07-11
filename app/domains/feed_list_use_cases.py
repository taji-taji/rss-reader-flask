from domains.feed_list_translator import FeedListTranslator

class FeedListUseCase(object):

    def __init__(self, repo):
        self.repo = repo

    def get_list(self):
        feed_list = self.repo.get_list()
        translator = FeedListTranslator()
        return translator.translate(feed_list)