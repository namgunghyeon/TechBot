import requests
import feedparser
from src.crawling.crawler import Crawler
from db.bot_db import BotDB
from bs4 import BeautifulSoup

class Baemin(Crawler):
  def __init__(self):
    self._web_base_url = "http://woowabros.github.io"
    self._feed_base_url = "http://woowabros.github.io/feed.xml"
    self._bot_db = BotDB()

  def crawling(self):
    return self._fetch_latest_post()

  def _fetch_latest_post(self):
    feed = feedparser.parse(self._feed_base_url)

    posts = []
    for post in feed.entries:
      posts.append({
        'title': post.title,
        'link': post.link
      })

    return posts

  def get_new_post_and_update(self):
    posts = self.crawling()
    last_post = self._get_latest_post_from_db()

    if len(posts) > 0:
      new_post = posts[0]

      if (new_post["title"] != last_post["title"]) and \
        (new_post["link"] != last_post["link"]):
        self._bot_db.save("baemin", new_post["title"], new_post["link"])

        return new_post

    return None

  def _get_latest_post_from_db(self):
    latest_post = self._bot_db.get("baemin")
    new_latest_post = {
      'title': '',
      'link': ''
    }

    if latest_post != None and len(latest_post) > 0:
      new_latest_post['title'] = latest_post[1]
      new_latest_post['link'] = latest_post[2]

    return new_latest_post