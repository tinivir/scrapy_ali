import random
import scrapy
from scrapy.conf import settings
from privoxy_pool import PrivoxyController
from scrapy.exceptions import NotConfigured, NotSupported
from scrapy.http import Response, Request


PrivoxyController._start_ip = 8150
privoxy_controller = PrivoxyController(maximum_instances=2)
privoxy_controller.run()

class RandomUserAgentMiddleware(object):
    def process_request(self, request, spider):
        ua  = random.choice(settings.get('USER_AGENT_LIST'))
        if ua:
            request.headers.setdefault('User-Agent', ua)

class ProxyMiddleware(object):
	def process_request(self, request, spider):
		proxy = "http://127.0.0.1:{port}".format(port=privoxy_controller.next())
		request.meta['proxy'] = proxy


	def process_response(self, request, response, spider):
		if random.randint(1,2)==1:
			proxy = request.meta['proxy']
			port = proxy.split(':')[-1]
			print ('Removing failed proxy <%s>' % (port))
			privoxy_controller.set_bad(int(port))
			request.dont_filter=True
			return request
		return response



    

    