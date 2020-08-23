import urllib.request
import xml.etree.ElementTree as ET
import re
# url = "http://feeds.bbci.co.uk/news/rss.xml"
def get_xml(url):
    xml = urllib.request.urlopen(url).read()
    tree = ET.fromstring(xml)
    item = tree.findall("channel/item")
    rss=[]
    for i in item:
        d=dict()
        d["title"]= i.find("title").text
        d["description"]= i.find("description").text
        d["link"] = i.find("link").text
        d["pubDate"] = i.find("pubDate").text
        rss.append(d)
    r = dict()
    r["rss"] = rss
    return r