'''
Created on Oct 17, 2015

@author: Ben Maxfield
'''

from time import clock
from flask import Markup
from apscheduler.schedulers.background import BackgroundScheduler
from lxml import html, etree
import requests
import feedparser
from urllib2 import urlopen
from __builtin__ import int

class Scripter():
    
    scheduler = None
    Script = '''
        STARTING WEB SCRAPER...\n
        ===========================================\n
        GETTING first target:\n
        \"http://feeds.sciencedaily.com/sciencedaily/top_news/top_technology?format=xml\"\n
        .\n
        .\n
        .\n
        '''
    SDtitles = ['', '', '']
    SDlinks = ['', '', '']
    SDtimestamp = 0
    GithubHTML = None
    GithubCSS = None


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
        self.SDtimestamp = clock()
        
        # Gets bmaxfie@Github public data and .css from page
        page = requests.get('https://github.com/bmaxfie')
        tree = html.fromstring(page.text)
        self.GithubHTML = Markup(etree.tostring(tree.xpath('//div[@class="boxed-group flush"]')[1], pretty_print=True))
        
        strings = ""
        for element in tree.xpath('//link[@rel="stylesheet"]'):
            strings = strings + etree.tostring(element, pretty_print=True)
        self.GithubCSS = Markup(strings)
        #self.GithubCSS = Markup(etree.tostring(tree.xpath('//link[@rel="stylesheet"]'), pretty_print=True))
        #print(etree.tostring(self.GithubHTML, pretty_print=True))
        #page = urlopen('http://feeds.sciencedaily.com/sciencedaily/top_news/top_technology?format=xml')
        #print(page.read())
        #html = page.read()
        #xml = lxml.parse(html)
        #print(xml.__sizeof__())
        #item = xml.getroot().find('channel')[1].keys()
        #print(item)
        
