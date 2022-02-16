from typing import Callable, Iterable

import dateutil.parser


class Subclass:
	def __init__(self, param: str, obj: Callable):
		self.param = param
		self.obj = obj


class QueryObject:
	def __init__(self, **kwargs):
		for key, val in kwargs.items():
			setattr(self, key, val)


class ApiObject:
	datetime_fields: Iterable[str] = []
	subclasses: Iterable[Subclass] = []
	
	def __init__(self, **kwargs):
		self.id = None
		self.__dict__ = kwargs
		for cls in self.subclasses:
			setattr(self, cls.param, cls.obj(**kwargs.pop(cls.param)))
		for key, val in kwargs.items():
			if key in self.datetime_fields:
				val = self._parse_datetime(val)
			setattr(self, key, val)
	
	@staticmethod
	def _parse_datetime(datetime_: str):
		if datetime_ and datetime_ != '':
			return dateutil.parser.parse(datetime_)
