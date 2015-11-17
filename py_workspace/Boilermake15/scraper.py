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

class Scraper():
    
    scheduler = None
    script = Markup('''
        <span id="script1">> python scraper.py<span id="pipe1">|</span></br></span>
        <span class="script" id="script2">STARTING WEB SCRAPER...</br></span>
        <span class="script" id="script3">=========================|</br></span>
        <span class="script" id="script4">000%|====================|</br></span>
        <span class="script" id="script5">=========================|</br></span>
        <span id="space1"></br></span>
        <span class="script" id="script6">GETting first target:</br></span>
        <span class="script" id="script7">address=\"https://github.com/bmaxfie\"</br></span>
        <span class="script" id="script8">.</span></br>
        <span class="script" id="script9">.</span></br>
        <span class="script" id="script10">.</span></br>
        <span class="script" id="script11">RETRIEVED .html, {} KB</span></br>
        <span class="script" id="script12">PARSING .html</span></br>
        <span class="script" id="script13">FOUND commit stats!</span></br>
        <span class="script" id="script14">ADDED markup to front.html template</span></br>
        <span class="script" id="script15">FOUND .css links!</span></br>
        <span class="script" id="script16">ADDED markup to front.html template</span></br>
        <span class="script" id="script17">FOUND .js links!</span></br>
        <span class="script" id="script18">ADDED markup to front.html template</span></br>
        <span class="script" id="script19">ANIMATING...</span></br>
        </br>
        <span class="script" id="script20">GETting second target:</span></br>
        <span class="script" id="script21">address=\"http://feeds.sciencedaily.com/sciencedaily/top_news/top_technology?format=xml\"</span></br>
        <span class="script" id="script22">.</span></br>
        <span class="script" id="script23">.</span></br>
        <span class="script" id="script24">.</span></br>
        <span class="script" id="script25">RETRIEVED .xml, {} KB</span></br>
        <span class="script" id="script26">PARSING .xml</span></br>
        <span class="script" id="script27">FOUND top 3 articles!</span></br>
        <span class="script" id="script28">ADDED markup to front.html template</span></br>
        <span class="script" id="script29">ANIMATING...</span></br>
        <span id="space3"></br></span>
        <span class="script" id="script30">=========================|</span></br>
        <span class="script" id="script31">WEB SCRAPER COMPLETE</span></br>
        <span id="space4"></br></span>
        <span class="script" id="script32">> <span id="pipe2">|</span></span>
        ''')
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
        SDsize = feed.__sizeof__() * 100.0 / 1000 # SOMETHING IS WRONG HERE, This XML is not ~508 Bytes... its at least 5 KB.
        
        # Gets bmaxfie@Github public data and .css from page
        page = requests.get('https://github.com/bmaxfie')
        tree = html.fromstring(page.text)
        self.GithubHTML = Markup(etree.tostring(tree.xpath('//div[@class="boxed-group flush"]')[1], pretty_print=True))
        GithubSize = page.__sizeof__() * 1000.0 / 1000 # SOMETHING IS WRONG HERE, see above comment
        
        strings = ""
        for element in tree.xpath('//link[@rel="stylesheet"]'):
            strings = strings + etree.tostring(element, pretty_print=True)
        self.GithubCSS = Markup(strings)
        
        self.script = self.script.format(SDsize, GithubSize)
        
