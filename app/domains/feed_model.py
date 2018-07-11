class FeedModel(object):
    
    def __init__(self, title, summary, link, image=None):
        self.title = title
        self.summary = summary
        self.image = image
        self.link = link