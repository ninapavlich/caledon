# Django Application

## Backend
---

### Dependencies
**[Homebrew - for OSX](http://brew.sh/)**

    ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
    #Verify installation:
    brew --version

**[PIP](https://pip.pypa.io/en/latest/installing.html)**    

    wget https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py -O - | python
    #Verify installation:
    pip --version

**[Virtualenv](https://virtualenv.pypa.io/en/latest/installation.html)**    

    pip install virtualenv
    #Verify installation:
    virtualenv --version

### Installation

The first time you set up the project, run the following commands:
    
    git clone git@bitbucket.org/cgpartners/nmaahc.git
    cd nmaahc
    virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt
    python manage.py migrate

    python manage.py loaddata dgb/fixtures/configuration.json #Note this may take several minutes to complete...
    
    python manage.py runserver

To connect to the Heroku project:
    
    #Ensure you have access to the Heroku project

    #Install the heroku toolbelt: https://toolbelt.heroku.com/
    #Once installed, log in to your Heroku account
    heroku login

    #Link nmaahc folder with heroku project:
    heroku git:remote -a nmaahc

    #To push to heroku
    git push heroku master



## Database Fixtures

Dump a configuration database fixture (contains all content, but no user-generated content):

    python manage.py dumpdata --natural-foreign --indent=4 -e sessions -e admin -e contenttypes -e auth.Permission -e reversion -e tastypie -e kiosk.Entry -e kiosk.Donation -e kiosk.Membership -e kiosk.PandaMember -e monomail.EmailReceipt -e metrics.Event > dgb/fixtures/configuration.json

Dump a complete database fixture with user-generated content:

    python manage.py dumpdata --natural-foreign --indent=4 -e sessions -e admin -e contenttypes -e auth.Permission -e reversion -e tastypie > dgb/fixtures/example_data.json


Load a fixture file:
    
    python manage.py loaddata dgb/fixtures/configuration.json

