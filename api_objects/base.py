from typing import Callable, Iterable, List

import dateutil.parser

from exceptions import PyZiException
from objects import ClsDictAttrsObject


class Subclass:
	def __init__(self, param: str, obj: Callable = None):
		self.param = param
		self.obj = obj
		
	def map(self, param):
		if self.obj:
			if isinstance(param, dict):
				return self.obj(**param)
			else:
				return self.obj(param)
		else:
			return param

class QueryObject:
	def __init__(self, **kwargs):
		for key, val in kwargs.items():
			setattr(self, key, val)


class ApiObject:
	_datetime_fields: Iterable[str] = []
	_subclasses: Iterable[Subclass] = []
	
	def __init__(self, **kwargs):
		self.id = None
		self.__dict__ = kwargs
		for subclass in self._subclasses:
			param = kwargs.pop(subclass.param, None)
			if not param:
				continue
			if not isinstance(param, list):
				setattr(self, subclass.param, subclass.map(param))
			else:
				setattr(self, subclass.param, [subclass.map(i) for i in param])
		for key, val in kwargs.items():
			if key in self._datetime_fields:
				val = self._parse_datetime(val)
			setattr(self, key, val)
			
	@staticmethod
	def _parse_datetime(datetime_: str):
		if datetime_ and datetime_ != '':
			return dateutil.parser.parse(datetime_)


class EnrichObject(ApiObject, ClsDictAttrsObject):
	_enrich_match_input: str
	
	@classmethod
	def build_enrich_query(cls, inputs, fields: List[str] = None, exclude: List[str] = None) -> dict:
		subclass_fields = [subclass.param for subclass in cls._subclasses]
		output_fields = [field for field in cls.keys() if field not in subclass_fields]
		if fields and exclude:
			raise PyZiException("Error building enrich: the parameters 'fields' and 'exclude' cannot both be used")
		elif fields:
			for field in fields:
				if field not in output_fields:
					raise PyZiException(f"Error building enrich: '{field}' is not a valid output field; valid fields are {output_fields}")
		elif exclude:
			for field in exclude:
				if field not in output_fields:
					raise PyZiException(f"Error building enrich: '{field}' is not a valid output field; valid fields are {output_fields}")
			fields = []
			for field in output_fields:
				if field not in exclude:
					fields.append(field)
		else:
			fields = output_fields
		return {cls._enrich_match_input: inputs, 'outputFields': fields}
