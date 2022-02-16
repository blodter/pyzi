from typing import Callable, Union

from api_objects import *
from endpoints import EndpointFactory as EF


def map_list_data(data: list, object_mapping: Callable):
	return [object_mapping(**obj) for obj in data]


class BaseMapping:
	def __init__(self, object_mapping: Callable, response_mapping: Callable = None):
		self.object_mapping = object_mapping
		self.response_mapping = response_mapping
	
	def map_response(self, data: dict):
		if self.response_mapping:
			return self.response_mapping(object_mapping=self.object_mapping, **data)
		else:
			if isinstance(data, dict):
				return self.object_mapping(**data)
			else:
				return data
	
	def __call__(self, *args, **kwargs):
		return self.map_response(*args, **kwargs)


class EnrichMapping(BaseMapping):
	def __init__(self, object_mapping: Callable):
		super().__init__(response_mapping=EnrichResponse, object_mapping=object_mapping)


class SearchMapping(BaseMapping):
	def __init__(self, object_mapping: Callable):
		super().__init__(response_mapping=ResultsResponse, object_mapping=object_mapping)


class BaseApiConfig:
	def __init__(
			self,
			obj_name: str,
			object_mapping: Callable,
			mapping_method: Callable,
			call_method: str = None,
			endpoint: str = None,
	):
		self.call_method = call_method
		self.endpoint = endpoint
		self.obj_name = obj_name
		self.object_mapping = object_mapping
		self.mapping_method = mapping_method


class InputFieldsApiConfig(BaseApiConfig):
	def __init__(self, obj_name, *args, **kwargs):
		super().__init__(
			obj_name,
			*args,
			call_method='get',
			endpoint=EF.input_fields(obj_name),
			**kwargs)


class OutputFieldsApiConfig(BaseApiConfig):
	def __init__(self, obj_name, *args, **kwargs):
		super().__init__(
			obj_name,
			*args,
			call_method='get',
			endpoint=EF.output_fields(obj_name),
			**kwargs
		)


class IOFieldsApiConfig(BaseApiConfig):
	def __init__(self, obj_name, *args, **kwargs):
		self.input_fields = InputFieldsApiConfig(obj_name, object_mapping=OutputField, mapping_method=map_list_data)
		self.output_fields = OutputFieldsApiConfig(obj_name, object_mapping=OutputField, mapping_method=map_list_data)
		super().__init__(obj_name, *args, **kwargs)


class EnrichApiConfig(IOFieldsApiConfig):
	def __init__(self, obj_name, object_mapping, mapping_method=None):
		if not mapping_method:
			mapping_method = EnrichMapping(object_mapping)
		super().__init__(
			obj_name,
			object_mapping,
			mapping_method,
			call_method='post',
			endpoint=EF.enrich(obj_name)
		)


class SearchApiConfig(IOFieldsApiConfig):
	def __init__(self, obj_name, object_mapping, mapping_method=None):
		if not mapping_method:
			mapping_method = SearchMapping(object_mapping)
		super().__init__(
			obj_name,
			object_mapping,
			mapping_method,
			call_method='post',
			endpoint=EF.search(obj_name)
		)


class LookupApiConfig(BaseApiConfig):
	def __init__(self, obj_name, object_mapping=None, mapping_method=None):
		if not object_mapping:
			object_mapping = ApiObject
		if not mapping_method:
			mapping_method = BaseMapping(object_mapping)
		super().__init__(
			obj_name,
			object_mapping,
			mapping_method,
			call_method='get',
			endpoint=EF.lookup(obj_name)
		)


ApiConfigType = Union[BaseApiConfig, EnrichApiConfig, LookupApiConfig, SearchApiConfig]


class DictConfig:
	@classmethod
	def dict(cls):
		return {k: v for k, v in cls.__dict__.items() if not k.startswith('_')}
	
	@classmethod
	def items(cls):
		return cls.dict().items()


class DummyApiConfig:
	def __init__(self, **kwargs):
		for key, val in kwargs.items():
			setattr(self, key, val)
	
	def dict(self):
		return {k: v for k, v in self.__dict__.items() if not k.startswith('_')}
	
	def items(self):
		return self.dict().items()
		


class EnrichApiConfigs:
	company = EnrichApiConfig('company', EnrichedCompany)
	company_location = EnrichApiConfig('location', EnrichedCompanyLocation)
	company_master_data = EnrichApiConfig('company-master', EnrichedCompanyMasterData)
	contact = EnrichApiConfig('contact', EnrichedContact)
	corporatehierarchy = EnrichApiConfig('corporatehierarchy', EnrichedCorporateHierarchy)
	hashtag = SearchApiConfig('hashtag', ApiObject)
	intent = EnrichApiConfig('intent', Intent)
	ip = EnrichApiConfig('ip', EnrichedIP)
	news = EnrichApiConfig('news', News)
	orgchart = EnrichApiConfig('orgchart', EnrichedOrgChart)
	scoop = EnrichApiConfig('scoop', Scoop)
	tech = SearchApiConfig('tech', ApiObject)


class LookupApiConfigs(DictConfig):
	boardMember = LookupApiConfig('boardMember')
	companyranking = LookupApiConfig('companyranking')
	companytype = LookupApiConfig('companytype')
	continent = LookupApiConfig('continent')
	country = LookupApiConfig('country')
	department = LookupApiConfig('department')
	employee_category_band = LookupApiConfig('employee_category_band')
	employeecount = LookupApiConfig('employeecount')
	hashtag = LookupApiConfig('hashtag')
	hierarchy_code = LookupApiConfig('hierarchy_code')
	industry = LookupApiConfig('industry')
	intent = DummyApiConfig(topics=LookupApiConfig('intent/topics'))
	intent_topics = LookupApiConfig('intent_topics')
	jobfunction = LookupApiConfig('jobfunction')
	jobtitlehierarchy = LookupApiConfig('jobtitlehierarchy')
	managementLevel = LookupApiConfig('managementLevel')
	metroarea = LookupApiConfig('metroarea')
	naicscode = LookupApiConfig('naicscode')
	news = DummyApiConfig(categories=LookupApiConfig('news/categories'))
	revenue_category_band = LookupApiConfig('revenue_category_band')
	revenuerange = LookupApiConfig('revenuerange')
	scoopdepartment = LookupApiConfig('scoopdepartment')
	scooptopic = LookupApiConfig('scooptopic')
	scooptype = LookupApiConfig('scooptype')
	siccode = LookupApiConfig('siccode')
	state = LookupApiConfig('state')
	subunittypes = LookupApiConfig('subunittypes')
	tech = DummyApiConfig(
		category=LookupApiConfig('tech/category'),
		product=LookupApiConfig('tech/product'),
		vendor=LookupApiConfig('tech/vendor'),
	)
	usage = LookupApiConfig('usage')


class SearchApiConfigs:
	company = SearchApiConfig('company', SearchedCompany)
	contact = SearchApiConfig('contact', SearchedContact)
	intent = SearchApiConfig('intent', Intent)
	news = SearchApiConfig('news', News)
	scoop = SearchApiConfig('scoop', Scoop)


class ApiConfigs:
	lookup = LookupApiConfigs()
	enrich = EnrichApiConfigs()
	search = SearchApiConfigs()
	
	def __new__(cls, name: str):
		attrs = name.split('.')
		attr = cls
		for a in attrs:
			attr = getattr(attr, a)
		return attr
