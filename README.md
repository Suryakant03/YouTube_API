# Youtube Fetch API

An API to fetch latest videos sorted in reverse chronological order of their publishing date-time from YouTube for a given tag/search query in a paginated response.

Server calls the YouTube API continuously in background (async) with interval **100 seconds** for fetching the latest videos for a predefined search query stores the data of videos (specifically these fields - Video title, description, publishing datetime, thumbnails URLs ) in a database with proper indexes.

## Method

 - Django for Rest API and running the asynchronus task for collecting the data from Youtube API
 - Postgres Database has been used to store and read the data.
 - Docker has been used to containerize the application.

## Setup - Docker Only


    git clone https://github.com/Suryakant03/YouTube_API.git
    cd YouTube_API

Now you must have docker in your device with the needed CLI. Also ensure you have docker-compose.
if not then run below command

    pip install docker-compose

Now run the below docker-compose commands:

    docker-compose build
    docker-compose up

Now you can assess the Application on http://localhost:8000/
    
**Note that you have to wait for atleast 100 seconds for a batch of database to scrape and appear on WebUI**
## Setup Manually


    git clone https://github.com/Suryakant03/YouTube_API.git
    cd YouTube_API

Setup Database in  `settings.py`

    DATABASES = {
	    'default': {
		    'ENGINE': 'django.db.backends.postgresql',
		    'HOST': os.environ.get('DB_HOST'),
		    'NAME': os.environ.get('DB_NAME'),
		    'USER': os.environ.get('DB_USER'),
		    'PASSWORD': os.environ.get('DB_PASS')
	    }
    }

Setup Google - Youtube API KEYS in `settings.py`


    GCP_API_KEYS = [
	    'AIzaSyDf4iBTTUzFutM7pp0TAGrSFYhYsT8tl3g',
	    'AIzaSyAMQ8v-3QtdYFhJFeUZxyFOmrc93hjJwQI',
	    '.......................................',
    ]

For default API runs every **100 seconds** and collect the data from youtube. To chnage the interval time chnage `UPDATE_IN_SECONDS` Key in `settings.py` from 100 to anything.

For default the serach query for collecting data from Youtube is **cricket.** To change the search query change `SEARCH_QUERY` Key in `settings.py`.

After the basic settings run following commands:

    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver --noreload 127.0.0.1:8000



## Web UI

Django builtin web UI has been used to display and filter the data. 
![Basic Dashboard to display data](https://github.com/Suryakant03/YouTube_API/blob/main/images/dashboard.png)
![Basic Dashboard Filters](https://github.com/Suryakant03/YouTube_API/blob/main/images/dashboard_filters.png)
