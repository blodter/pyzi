from typing import Union

from api_objects import *
from mapping import *
from objects import DictAttrsObject


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
	
	
EF = EndpointFactory


def map_list_data(data: list, api_object: Callable):
	return [api_object(**obj) for obj in data]


class BaseMapping:
	def __init__(self, api_object: Callable, response_mapping: Callable = None):
		self.api_object = api_object
		self.response_mapping = response_mapping
	
	def map_response(self, data: dict):
		if self.response_mapping:
			return self.response_mapping(api_object=self.api_object, **data)
		else:
			if isinstance(data, dict):
				return self.api_object(**data)
			else:
				return data
	
	def __call__(self, *args, **kwargs):
		return self.map_response(*args, **kwargs)


class EnrichMapping(BaseMapping):
	def __init__(self, api_object: Callable):
		super().__init__(response_mapping=EnrichResponse, api_object=api_object)


class SearchMapping(BaseMapping):
	def __init__(self, api_object: Callable):
		super().__init__(response_mapping=ResultsResponse, api_object=api_object)


class BaseEndpointConfig:
	def __init__(
			self,
			obj_name: str,
			api_object: Union[ApiObject, EnrichObject],
			mapping_method: Callable,
			call_method: str = None,
			endpoint: str = None,
	):
		self.call_method = call_method
		self.endpoint = endpoint
		self.obj_name = obj_name
		self.api_object = api_object
		self.mapping_method = mapping_method


class InputFieldsEndpointConfig(BaseEndpointConfig):
	def __init__(self, obj_name, *args, **kwargs):
		super().__init__(
			obj_name,
			*args,
			call_method='get',
			endpoint=EF.input_fields(obj_name),
			**kwargs)


class OutputFieldsEndpointConfig(BaseEndpointConfig):
	def __init__(self, obj_name, *args, **kwargs):
		super().__init__(
			obj_name,
			*args,
			call_method='get',
			endpoint=EF.output_fields(obj_name),
			**kwargs
		)


class IOFieldsEndpointConfig(BaseEndpointConfig):
	def __init__(self, obj_name, *args, **kwargs):
		self.input_fields = InputFieldsEndpointConfig(obj_name, api_object=InputField, mapping_method=map_list_data)
		self.output_fields = OutputFieldsEndpointConfig(obj_name, api_object=OutputField, mapping_method=map_list_data)
		super().__init__(obj_name, *args, **kwargs)


class EnrichEndpointConfig(IOFieldsEndpointConfig):
	def __init__(self, obj_name, api_object, mapping_method=None, endpoint=None):
		if not mapping_method:
			mapping_method = EnrichMapping(api_object)
		super().__init__(
			obj_name,
			api_object,
			mapping_method,
			call_method='post',
			endpoint=EF.enrich(obj_name) if not endpoint else endpoint
		)


class SearchEndpointConfig(IOFieldsEndpointConfig):
	def __init__(self, obj_name, api_object, mapping_method=None):
		if not mapping_method:
			mapping_method = SearchMapping(api_object)
		super().__init__(
			obj_name,
			api_object,
			mapping_method,
			call_method='post',
			endpoint=EF.search(obj_name)
		)


class LookupEndpointConfig(BaseEndpointConfig):
	def __init__(self, obj_name, api_object=None, mapping_method=None):
		if not api_object:
			api_object = ApiObject
		if not mapping_method:
			mapping_method = BaseMapping(api_object)
		super().__init__(
			obj_name,
			api_object,
			mapping_method,
			call_method='get',
			endpoint=EF.lookup(obj_name)
		)


EndpointConfigType = Union[BaseEndpointConfig, EnrichEndpointConfig, LookupEndpointConfig, SearchEndpointConfig]


class DummyEndpointConfig(DictAttrsObject):
	def __init__(self, **kwargs):
		for key, val in kwargs.items():
			setattr(self, key, val)
	
	def dict(self):
		return {k: v for k, v in self.__dict__.items() if not k.startswith('_')}
	
	def items(self):
		return self.dict().items()


class EnrichEndpointConfigs(DictAttrsObject):
	company = EnrichEndpointConfig('company', EnrichedCompany)
	company_location = EnrichEndpointConfig('location', EnrichedCompanyLocation)
	company_master_data = EnrichEndpointConfig('company-master', EnrichedCompanyMasterData)
	contact = EnrichEndpointConfig('contact', EnrichedContact)
	corporate_hierarchy = EnrichEndpointConfig('corporatehierarchy', EnrichedCorporateHierarchy)
	hashtag = SearchEndpointConfig('hashtag', ApiObject)
	intent = EnrichEndpointConfig('intent', Intent)
	ip = EnrichEndpointConfig('ip', IP)
	news = EnrichEndpointConfig('news', News)
	orgchart = EnrichEndpointConfig('orgchart', EnrichedOrgChart)
	scoop = EnrichEndpointConfig('scoop', Scoop)
	tech = SearchEndpointConfig('tech', ApiObject)


class LookupEndpointConfigs(DictAttrsObject):
	board_member = LookupEndpointConfig('boardMember')
	company_ranking = LookupEndpointConfig('companyranking')
	company_type = LookupEndpointConfig('companytype')
	continent = LookupEndpointConfig('continent')
	country = LookupEndpointConfig('country')
	department = LookupEndpointConfig('department')
	employee_category_band = LookupEndpointConfig('employee_category_band')
	employee_count = LookupEndpointConfig('employeecount')
	hashtag = LookupEndpointConfig('hashtag')
	hierarchy_code = LookupEndpointConfig('hierarchy_code')
	industry = LookupEndpointConfig('industry')
	intent = DummyEndpointConfig(topics=LookupEndpointConfig('intent/topics'))
	intent_topics = LookupEndpointConfig('intent_topics')
	job_function = LookupEndpointConfig('jobfunction')
	job_title_hierarchy = LookupEndpointConfig('jobtitlehierarchy')
	management_level = LookupEndpointConfig('managementLevel')
	metro_area = LookupEndpointConfig('metroarea')
	naics_code = LookupEndpointConfig('naicscode')
	news = DummyEndpointConfig(categories=LookupEndpointConfig('news/categories'))
	revenue_category_band = LookupEndpointConfig('revenue_category_band')
	revenue_range = LookupEndpointConfig('revenuerange')
	scoop_department = LookupEndpointConfig('scoopdepartment')
	scoop_topic = LookupEndpointConfig('scooptopic')
	scoop_type = LookupEndpointConfig('scooptype')
	sic_code = LookupEndpointConfig('siccode')
	state = LookupEndpointConfig('state')
	subunit_types = LookupEndpointConfig('subunittypes')
	tech = DummyEndpointConfig(
		category=LookupEndpointConfig('tech/category'),
		product=LookupEndpointConfig('tech/product'),
		vendor=LookupEndpointConfig('tech/vendor'),
	)
	usage = LookupEndpointConfig('usage')


class SearchEndpointConfigs(DictAttrsObject):
	company = SearchEndpointConfig('company', SearchedCompany)
	contact = SearchEndpointConfig('contact', SearchedContact)
	intent = SearchEndpointConfig('intent', Intent)
	news = SearchEndpointConfig('news', News)
	scoop = SearchEndpointConfig('scoop', Scoop)


class WebhookEndpointConfigs(DictAttrsObject):
	create = ...
	update = ...
	delete = ...
	validate = ...
	generate_token = ...
	subscription_types = ...


class EndpointConfigs(DictAttrsObject):
	compliance = EnrichEndpointConfig('compliance', Compliance, endpoint='compliance')
	enrich = EnrichEndpointConfigs()
	lookup = LookupEndpointConfigs()
	search = SearchEndpointConfigs()
	webhooks = WebhookEndpointConfigs()
	
	def __new__(cls, name: str):
		attrs = name.split('.')
		attr = cls
		for a in attrs:
			attr = getattr(attr, a)
		return attr
