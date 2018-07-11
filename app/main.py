from flask import Flask, render_template
from data.feed_repository import FeedRepository
from domains.feed_list_use_cases import FeedListUseCase
from presenters.feed_list_adapter import FeedListAdapter
app = Flask(__name__)

@app.route("/")
def index():
    repository = FeedRepository()
    usecase = FeedListUseCase(repository)
    adapter = FeedListAdapter(usecase)

    feed_list = adapter.get_list()

    return render_template('index.html', feed_list=feed_list)