#Created on Oct 17, 2015
#@author: Ben Maxfield
#
#    RUN THIS (main.py) TO START THE WEB-APP!
#    This is the MAIN Flask web-app routing page.
#

### Imports:
from time import time
from flask import Flask, render_template
from scraper import Scraper
###


app = Flask(__name__)
application = app

# Create the Scraper/Scheduler
scraper = Scraper()

# Utility method that formats the timestamp for the most recently performed webscraping.
def getSDtimediff():
    secs = int((time() - scraper.SDtimestamp) % 60)
    mins = int((time() - scraper.SDtimestamp) / 60)
    return `mins` + " mins, " + `secs` + " secs"

# ROUTES AND RENDERS FRONT PAGE w/ all scraping data:
@app.route('/')
def redirect_front_page():
    return render_template('/front_bootstrapped.html', titles=scraper.SDtitles, links=scraper.SDlinks, githubHTML=scraper.GithubHTML, githubCSS=scraper.GithubCSS, timediff=getSDtimediff(), script=scraper.script)
#    return render_template('/front.html', titles=scraper.SDtitles, links=scraper.SDlinks, githubHTML=scraper.GithubHTML, githubCSS=scraper.GithubCSS, timediff=getSDtimediff(), script=scraper.script)

if __name__ == '__main__':
    app.run()