from iron_mq import IronMQ
import redis
import time

mq = IronMQ(host="mq-rackspace-ord.iron.io")
q = mq.queue("all_requests")
r = redis.StrictRedis()

while True: # poll indefinitely
    msg = q.get() # ask the queue for messages
    if len(msg["messages"]) < 1: # if there are no messages
        time.sleep(1) # wait a second
        continue # try again
    # if we made it this far, we have a message
    r.incr("requests") # increment the number of requests
    q.delete(msg["messages"][0]["id"]) # delete the message
