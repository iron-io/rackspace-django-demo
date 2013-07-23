A demo application showing off how to use Django middleware and IronMQ to do analytics on each request.

## Installation

1. [Install Django](http://djangoproject.com)
2. [Install Redis](http://redis.io)
3. [Install py-redis](http://pypi.python.org/pypi/redis)
4. [Sign up for IronMQ](http://iron.io/mq)
5. Set your IronMQ credentials:

		export IRON_PROJECT_ID="insert your project ID here"
		export IRON_TOKEN="insert your oauth token here"

6. Clone this repo
7. Set up your push queues
	* Go into the Iron.io [HUD](https://hud.iron.io) and browse to your requests queue
	* In the box labeled “Push Information”, select “multicast” for the Push Type.
	* Leave Retries and Retries Delay at their default values.
	* Hit “Update Queue”. You’ve turned the queue into a push queue.
8. Start redis: `redis-server`
9. Start the app: `python manage.py runserver`
10. Start the request worker: `python req_worker.py`
11. Start the UA worker: `python ua_worker.py`

Now when you load the page and refresh it a few times, your statistics should be collected.
