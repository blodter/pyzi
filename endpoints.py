class Endpoint:
	def __init__(self, path: str):
		self.path = path
	
	def __call__(self, *endpoints):
		return self.path.format(*endpoints)


class EndpointFactory:
	enrich = Endpoint('enrich/{}')
	input_fields = Endpoint('lookup/inputfields/{}/search')
	lookup = Endpoint('lookup/{}')
	output_fields = Endpoint('lookup/outputfields/{}/search')
	search = Endpoint('search/{}')
	
	def __new__(cls, endpoint: str):
		endpoints = endpoint.split('.')
		return getattr(cls, endpoints[0])('/'.join(endpoints[1:]))
