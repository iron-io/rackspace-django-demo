from iron_mq import IronMQ
try:
    import json
except:
    import simplejson as json

class QueueRequestMiddleware:
    queue = None

    def __init__(self):
        mq = IronMQ(host="mq-rackspace-ord.iron.io") # instantiate our IronMQ client once
        self.queue = mq.queue("requests") # set our queue

    def process_request(self, request):
        # push our request headers as a message to our queue
        data = {}
        for key in request.META.keys():
            if key.startswith("HTTP_"):
                data[key] = request.META[key]
        self.queue.post(json.dumps(data))
        return None # pass on to the next middleware/application
