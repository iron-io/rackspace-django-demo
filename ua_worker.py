from iron_mq import IronMQ
import redis
import time

mq = IronMQ()
q = mq.queue("ua_requests")
r = redis.StrictRedis()

while True: # poll indefinitely
    msg = q.get() # ask the queue for messages
    if len(msg["messages"]) < 1: # if there are no messages
        time.sleep(1) # wait a second
        continue # try again
    # if we made it this far, we have a message
    # separate the user agent
    user_agent = msg["messages"][0]["body"]["HTTP_USER_AGENT"]
    # increment the number of requests from the user agent
    r.hincrby("user_agent_requests", user_agent, 1)
    q.delete(msg["messages"][0]["id"]) # delete the message
