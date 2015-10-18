'''
Created on Oct 17, 2015

@author: Ben Maxfield
'''

from apscheduler.schedulers.background import BackgroundScheduler
from lxml import html
#import xml.etree.ElementTree as lxml
import requests
import feedparser
from urllib2 import urlopen

class Scripter():
    
    scheduler = None
    SDtitles = ['', '', '']
    SDlinks = ['', '', '']
    GithubHTML = None


    def __init__(self):
        self.update()
        scheduler = BackgroundScheduler()
        scheduler.start()
        scheduler.add_job(self.update, 'interval', hours=1)
        
    def update(self):
        # Saves the top 3 article titles and links from ScienceDaily.com under the Technology category.
        feed = feedparser.parse('http://feeds.sciencedaily.com/sciencedaily/top_news/top_technology?format=xml')
        for i in range(0,3):
            self.SDtitles[i] = feed.entries[i].title
            self.SDlinks[i] = feed.entries[i].link
        
        # Gets bmaxfie@Github data
        page = requests.get('https://github.com/bmaxfie')
        tree = html.fromstring(page.text)
        self.GithubHTML = tree.xpath('//div[@class="boxed-group flush"]')[1]
        print(self.GithubHTML)
        
        #page = urlopen('http://feeds.sciencedaily.com/sciencedaily/top_news/top_technology?format=xml')
        #print(page.read())
        #html = page.read()
        #xml = lxml.parse(html)
        #print(xml.__sizeof__())
        #item = xml.getroot().find('channel')[1].keys()
        #print(item)
        
