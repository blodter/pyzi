from typing import Callable, Iterable, List, Union

__all__ = ['ResultsResponse', 'EnrichResult', 'EnrichData', 'EnrichResponse']


class ResultsResponse:
	# TODO: Add pagination generator to results
	def __init__(self, query: dict = None, maxResults: int = None, totalResults: int = None, currentPage: int = None, data: List[dict] = None, object_mapping: Callable = None):
		self.query: dict = query
		self.maxResults: int = maxResults
		self.totalResults: int = totalResults
		self.currentPage: int = currentPage
		self.object_mapping: Callable = object_mapping
		self.data: Iterable = self._map_data(data, object_mapping) if object_mapping else data
	
	def __iter__(self) -> Iterable:
		return iter(self.data)
	
	@staticmethod
	def _map_data(data: List[dict], object_mapping: Callable) -> list:
		return [object_mapping(**obj) for obj in data]


class EnrichResult:
	def __init__(self, object_mapping: Callable = None, input: dict = None, matchStatus: str = None, data: List[dict] = None):
		self.object_mapping = object_mapping
		self.input = input
		self.matchStatus = matchStatus
		self.data: Iterable = self._map_data(data, object_mapping) if object_mapping else data
	
	@staticmethod
	def _map_data(data: List[dict], object_mapping: Callable) -> list:
		return [object_mapping(**obj) for obj in data]
	
	def __iter__(self) -> Iterable:
		return iter(self.data)


class EnrichData:
	def __init__(self, outputFields: List[str] = None, result: List[dict] = None, requiredFields: List = None, object_mapping: Callable = None):
		self.outputFields: List[str] = outputFields
		self.requiredFields: List = requiredFields
		self.result: List[Union[dict, EnrichResult]] = self._map_result(result, object_mapping) if object_mapping else result
	
	@staticmethod
	def _map_result(result: List[dict], object_mapping: Callable) -> list:
		return [EnrichResult(object_mapping=object_mapping, **r) for r in result]
	
	def get_result_data(self):
		result_data = []
		for data in self.result:
			for d in data:
				result_data.append(d)
		return result_data


class EnrichResponse:
	def __init__(self, success: bool = None, data: dict = None, object_mapping: Callable = None):
		self.success: bool = success
		self.data: EnrichData = EnrichData(object_mapping=object_mapping, **data)
		self.object_mapping: Callable = object_mapping
		self.enriched_data = self.data.get_result_data()
	
	def __iter__(self) -> Iterable:
		return iter(self.enriched_data)
	
	@staticmethod
	def _map_data(data: List[dict], object_mapping: Callable) -> list:
		return [object_mapping(**obj) for obj in data]
