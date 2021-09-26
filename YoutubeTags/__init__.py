import html5lib
import requests 
import bs4
from bs4 import BeautifulSoup


def videotags(url):
    """
    Use videotage(url) for tags of the video
    """
    try:
        request = requests.get(url)
        soup = BeautifulSoup(request.content, 'html5lib') 
        tags = ', '.join([ meta.attrs.get("content") for meta in soup.find_all("meta",{"property": "og:video:tag"}) ])
        return tags
    except:
        return None


def channeltags(url):
    """
    Use channeltags(url) for tags of channel
    """
    try:
        request = requests.get(url)
        soup = BeautifulSoup(request.content, 'html5lib') 
        tags = ', '.join([ meta.attrs.get("content") for meta in soup.find_all("meta",{"property": "og:video:tag"}) ])
        return tags
    except:
        return None
