from django.http import HttpResponse
import redis

r = redis.StrictRedis()

def index(request):
    num_reqs = r.get("requests")
    ua_reqs = r.hgetall("user_agent_requests")
    response = "%s requests\r\n" % num_reqs
    for ua in ua_reqs.keys():
        response += "\r\n%s from %s" % (us_reqs[ua], ua)
    return HttpResponse(response)
