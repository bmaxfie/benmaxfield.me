# These are essentially, the installations necessary to create the AMI for benmaxfield.me

sudo yum install gcc python27-lxml.x86_64 libxslt.x86_64 libxslt-devel.x86_64 libxslt-python27.x86_64 libxml2.x86_64 libxml2-devel.x86_64 libxml2-python27.x86_64 python27-devel.x86_64
sudo pip install lxml==3.7.1
sudo pip install apscheduler
sudo pip install feedparser
sudo pip install Flask==0.11

# May want to include these into the AMI if I ever have to do that again.

sudo yum install httpd mod_wsgi-python27
sudo yum install mod_ssl openssl
