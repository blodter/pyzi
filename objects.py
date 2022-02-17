class DictAttrsObject:
	def dict(self):
		return {k: v for k, v in self.__dict__.items() if not k.startswith('_')}
	
	def items(self):
		return self.dict().items()
	
	def keys(self):
		return self.dict().keys()
	
	def values(self):
		return self.dict().values()


class ClsDictAttrsObject:
	@classmethod
	def dict(cls):
		return {k: v for k, v in cls.__dict__.items() if not k.startswith('_')}
	
	@classmethod
	def items(cls):
		return cls.dict().items()
	
	@classmethod
	def keys(cls):
		return cls.dict().keys()
	
	@classmethod
	def values(cls):
		return cls.dict().values()
