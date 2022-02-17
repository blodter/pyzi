from typing import Callable, Iterable, List, Union

__all__ = ['ResultsResponse', 'EnrichResult', 'EnrichData', 'EnrichResponse']


class ResultsResponse:
	# TODO: Add pagination generator to results
	def __init__(self, query: dict = None, maxResults: int = None, totalResults: int = None, currentPage: int = None, data: List[dict] = None, api_object: Callable = None):
		self.query: dict = query
		self.maxResults: int = maxResults
		self.totalResults: int = totalResults
		self.currentPage: int = currentPage
		self.api_object: Callable = api_object
		self.data: Iterable = self._map_data(data, api_object) if api_object else data
	
	def __iter__(self) -> Iterable:
		return iter(self.data)
	
	@staticmethod
	def _map_data(data: List[dict], api_object: Callable) -> list:
		return [api_object(**obj) for obj in data]


class EnrichResult:
	def __init__(self, api_object: Callable = None, input: dict = None, matchStatus: str = None, data: List[dict] = None):
		self.api_object = api_object
		self.input = input
		self.matchStatus = matchStatus
		self.data: Iterable = self._map_data(data, api_object) if api_object else data
	
	@staticmethod
	def _map_data(data: List[dict], api_object: Callable) -> list:
		return [api_object(**obj) for obj in data]
	
	def __iter__(self) -> Iterable:
		return iter(self.data)


class EnrichData:
	def __init__(self, outputFields: List[str] = None, result: List[dict] = None, requiredFields: List = None, api_object: Callable = None):
		self.outputFields: List[str] = outputFields
		self.requiredFields: List = requiredFields
		self.result: List[Union[dict, EnrichResult]] = self._map_result(result, api_object) if api_object else result
	
	@staticmethod
	def _map_result(result: List[dict], api_object: Callable) -> list:
		return [EnrichResult(api_object=api_object, **r) for r in result]
	
	def get_result_data(self):
		result_data = []
		for data in self.result:
			for d in data:
				result_data.append(d)
		return result_data


class EnrichResponse:
	def __init__(self, success: bool = None, data: dict = None, api_object: Callable = None):
		self.success: bool = success
		self.data: EnrichData = EnrichData(api_object=api_object, **data)
		self.api_object: Callable = api_object
		self.enriched_data = self.data.get_result_data()
	
	def __iter__(self) -> Iterable:
		return iter(self.enriched_data)
	
	@staticmethod
	def _map_data(data: List[dict], api_object: Callable) -> list:
		return [api_object(**obj) for obj in data]
