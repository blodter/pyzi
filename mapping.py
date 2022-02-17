from typing import Callable

from api_objects import EnrichResponse, ResultsResponse


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
