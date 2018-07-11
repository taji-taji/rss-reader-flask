from domains.feed_list_use_cases import FeedListUseCase

class FeedListAdapter(object):

    def __init__(self, usecase):
        self.usecase = usecase

    def get_list(self):
        feed_list = self.usecase.get_list()
        return [f.__dict__ for f in feed_list]