<h1>README 4 benmaxfield.me</h1>
<h3>General</h3>

Benmaxfield.me was created for the primary purpose to display my most recent 
Resume and links to my professional sites (LinkedIn and Github). 

I chose to make the website themed to be something really only a Computer Scientist would understand while still looking 'cool' to the outside observer. I didn't want my website to simply be another 'pretty' personal website, but rather show that it's not a completely static page and to display some more uncommon (but still modest) web development knowledge, which is why I chose to perform some background webscraping.

I took this project idea as an opportunity to learn about some things I had never used before, primarily: 
<ul>
<li>Python</li> 
<li>Flask</li>
<li>Web Scraping</li>
<li>CSS Animations</li>
<li>Bootstrap CSS</li>
<li>And AWS Resources such as ElasticBeanstalk and their EBCLI.</li>
</ul>

<h3>How Benmaxfield.me Works (and What I've Learned from it):</h3>

FLASK:
The Flask web-app starts up (initializes all other parts of the app) and handles all 'pre-accepted' routing routes in the application.py file. In my case, application.py creates a Scraper class instance that handles all of the webscraping and its scheduling. Besides initializing the Scraper, application.py doesn't do much besides route the rendering of the front page (taking Scraper's data collection).
The Scraper class works by using a couple python packages to schedule, retreive and parse html during webscraping. These packages and their uses are outlined in the list below:
<ul>
<li>apscheduler - keeps track of timing and calls update() on my assigned interval of 1 hour.</li>
<li>lxml - performs the more complex parsing of the Github page. Using xpath() to find the css and contributions calendar.</li>
<li>feedparser - performs the requesting and parsing of the xml from ScienceDaily.</li>
<li>requests - since lxml can't perform the get to retrieve the html from Github, I used requests.get.</li>
</ul>
So to the normal observer it may seem that my website is performing the webscraping in front of you (on the client computer; as you are watching the browser), and that's what I originally wanted my site to do, but I found that wouldn't be possible with javascript and in fact, even if I could find a way to client-side webscrape it would be kind of risky (legally) and might get me into trouble so I went with strictly controlling the amount of scraping myself and left links back to ScienceDaily for the full article.

The only other purpose scraper.py held was to contain the scraped and formatted data as well as the hardcoded "script" for the console.

ANIMATIONS:
When starting this project I had just learned about CSS3 Animations and I was really excited that I might be able to perform all of the animations I required in CSS3! However, that ended up not being the case, unfortunately. I was able to perform at least 70% of the animations in CSS but when I came to the part of the project where I wanted the console to 'scroll' down, CSS3 simply didn't have powerful enough control to allow me to do the correct timing of changing the visibility of two elements at the same time so I resorted these parts and the progress bar to jQuery. 

Unfortunately, I am a little disappointed in my jQuery code as it's not elegant at all and almost 100% hardcoded, the progress bar especially. The trouble was, I simply could not get jQuery's .delay() function to operate properly! The only other timing based function I found that I could use for the animation was setTimeout(), and that function required an individual function to call with no parameters to pass along with it (however, now that I'm writing this, I may have been able to store that value in a global variable. I'll add that to my TODO list...). But either way, the animations all now work as I wanted them to. The only other loophole I found was switching tabs during the animations. If the user changes tabs in their browser to another site, the timing counter will continue for the js and css, but the code becomes inactive resulting in the animation never occuring, leaving the site (once the user switches their tab back to it) with gaping holes where text was supposed to appear, etc.

BOOTSTRAP & MOBILE:
Making my website mobile friendly wasn't super high on my list of priorities with this website, but I decided if I'm going to try Bootstrap out I might as well put a little effort into it. In retrospect, there's definitely some improvements I could make to make the mobile side better. I primarily used Bootstrap for its powerful row/column formatting. Allowing my website to collapse into one column (console and dashboard change from side by side to top and bottom). The only issue that still remains is on mobile, the Github calendar and console are wider than the screen which when the user moves to put those into view, the header (that contains my important links) is stuck to the side of the page at the top, and isn't centered correctly.

Lastly,

DEPLOYING ON AWS EB:
Now, personally I am fascinated by Amazon's top-notch web services so obviously they were my go-to to deploy my website. I decided to put my website on their ElasticBeanstalk service w/ a load balancer for scalability (despite my expected humble amount website demand). Deploying with a load balancer ended up making linking my domain with my site harder than I expected as my original domain registrar (domain.com) did not allow the DNS servers to redirect to another domain rather than a solid IPs (AWS load balancers don't have constant ip's). So instead I moved to AWS Route 53 which made hooking my website and domian up easy, finishing in only 15 minutes.

Another issue I ran into during deployment was correctly installing all of the Python libraries necessary to run my Flask app. Most of the packages installed perfectly fine with the distinguished exception of lxml.... Installing lxml on AWS servers (and even on my own computer) was not easy, and required more than a 'requirements.txt' to specify what needed to be installed. For the specifics, see the files in both the scripts folder and the .ebextensions folder (note: I still included lxml in the requirements) but essentially I had to use commands and container_commands in a config file in .ebextensions to separately install files on my deployment before lxml was installed via the automatic requirements.txt.

My last gripe with deployment occured when I first was able to successfully load my homepage. It seemed that none of my static files could be accessed! I was being 403 Forbidden from opening that folder. When I logged on via EBCLI ssh I found that not even via termianl I could access the static folder (or some other less important ones). It turns out that after some research I had to explicitly give permissions to read the folder for some reason. It turned out that applying sudo chmod +xw to the static folder would allow me to open it. So to make a more permenant solution I created another command in the config file in .ebextensions to give permissions to the folder across every re-deployment.

Overall, this was a great learning experience for me and I hope you learned something too, reading this.

<h3>Things I Learned (not mentioned above, that may save you time):</h3>
<ul>
<li>AWS requires your Flask app's starting file to be named application.py (with some variants).</li>
</ul>
