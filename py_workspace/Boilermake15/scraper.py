#Created on Oct 17, 2015
#@author: Ben Maxfield
#
#    The goal of Scraper is to:
#        * Schedule the updating of the web scraping service
#            (scrapes: github.com/bmaxfie and ScienceDaily.com)
#        * Perform the web scraping and html/xml parsing.
#            -Identifies top 3 technology news links and saves 
#                their titles and links.
#            -Saves the timestamp of the most recent web scrape.
#            -Parses the GitHub html to identify the user 
#                contibutions data container.
#            -Parses the GitHub html to identify the css link,
#                to properly style the container mentioned above.
#        * Hold the console's script to reduce cluttering the HTML 
#            that I will later need to refactor with Bootstrap.
#

### Imports:
from time import time
from flask import Markup
from apscheduler.schedulers.background import BackgroundScheduler
from lxml import html, etree
import requests
import feedparser
###

class Scraper():
    
    scheduler = None
    script = Markup('''
        <span id="script1">> python scraper.py<span id="pipe1">|</span><br></span>
        <span class="script" id="script2">STARTING WEB SCRAPER...<br></span>
        <span class="script" id="script3">==========================<br></span>
        <span class="script" id="script4"><br></span>
        <span id="space1"><br></span>
        <span class="script" id="script5">GET first target:<br></span>
        <span class="script" id="script6">address=\"https://github.com/bmaxfie\"<br></span>
        <span class="script" id="script7">.<br></span>
        <span class="script" id="script8">.<br></span>
        <span class="script" id="script9">.<br></span>
        <span class="script" id="script10">RETRIEVED .html, {} KB<br></span>
        <span class="script" id="script11">PARSING .html<br></span>
        <span class="script" id="script12">FOUND commit stats!<br></span>
        <span class="script" id="script13">ADDED markup to front.html template<br></span>
        <span class="script" id="script14">FOUND .css links!<br></span>
        <span class="script" id="script15">ADDED markup to front.html template<br></span>
        <span class="script" id="script16">FOUND .js links!<br></span>
        <span class="script" id="script17">ADDED markup to front.html template<br></span>
        <span class="script" id="script18">ANIMATING...<br></span>
        <span id="space2"><br></span>
        <span class="script" id="script19">GET second target:<br></span>
        <span class="script" id="script20">address=\"http://feeds.sciencedaily.com/sciencedaily/top_news/top_technology?format=xml\"<br></span>
        <span class="script" id="script21">.<br></span>
        <span class="script" id="script22">.<br></span>
        <span class="script" id="script23">.<br></span>
        <span class="script" id="script24">RETRIEVED .xml, {} KB<br></span>
        <span class="script" id="script25">PARSING .xml<br></span>
        <span class="script" id="script26">FOUND top 3 articles!<br></span>
        <span class="script" id="script27">ADDED markup to front.html template<br></span>
        <span class="script" id="script28">ANIMATING...<br></span>
        <span id="space3"><br></span>
        <span class="script" id="script29">=========================|<br></span>
        <span class="script" id="script30">WEB SCRAPER COMPLETE<br></span>
        <span id="space4"><br></span>
        <span class="script" id="script31">> <span id="pipe2">|</span></span>
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
        self.SDtimestamp = time()
        SDsize = feed.__sizeof__() * 100.0 / 1000 # SOMETHING IS WRONG HERE, This XML is not ~508 Bytes... its at least 5 KB.
        
        # Gets bmaxfie@Github public data and css stylesheet link.
        page = requests.get('https://github.com/bmaxfie')
        tree = html.fromstring(page.text)
        self.GithubHTML = Markup(etree.tostring(tree.xpath('//div[@class="boxed-group flush"]')[1], pretty_print=True))
        GithubSize = page.__sizeof__() * 1000.0 / 1000 # SOMETHING IS WRONG HERE, see above comment
        
        strings = ""
        for element in tree.xpath('//link[@rel="stylesheet"]'):
            strings = strings + etree.tostring(element, pretty_print=True)
        self.GithubCSS = Markup(strings)
        
        self.script = self.script.format(SDsize, GithubSize)
        
