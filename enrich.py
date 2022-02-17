from typing import Callable, List

from exceptions import PyZiException


class Enrich:
	match_input: str
	output_fields: List[str]
	api_object: Callable
	
	def __new__(cls, *inputs, fields: List[str] = None, exclude: List[str] = None):
		if fields and exclude:
			raise PyZiException("Error building enrich: the parameters 'fields' and 'exclude' cannot both be used")
		elif fields:
			for field in fields:
				if field not in cls.output_fields:
					raise PyZiException(f"Error building enrich: '{field}' is not a valid output field; valid fields are {cls.output_fields}")
		elif exclude:
			for field in exclude:
				if field not in cls.output_fields:
					raise PyZiException(f"Error building enrich: '{field}' is not a valid output field; valid fields are {cls.output_fields}")
			fields = []
			for field in cls.output_fields:
				if field not in exclude:
					fields.append(field)
		else:
			fields = cls.output_fields
		if cls.api_object:
			return {cls.match_input: [cls.api_object(**i) for i in inputs], 'outputFields': fields}
		else:
			return {cls.match_input: inputs, 'outputFields': fields}


class ContactEnrich:
	def __new__(cls, **kwargs):
		"""
		To match a contact, you must use one of the following combinations of parameters to construct your input:

		personId OR emailAddress OR hashedEmail OR phone.
			Because these values are unique to a single person,
			you can use any one of these values to search without providing any additional parameters.
			You can optionally combine one of these values with a companyId/companyName.

		firstName AND lastName AND companyId/companyName.
			Combining these values effectively results in a unique person.

		fullName AND companyId/companyName.
			Combining these values effectively results in a unique person.
		"""
		if 'personId' in kwargs or 'emailAddress' in kwargs or 'hashedEmail' in kwargs or 'phone' in kwargs:
			pass
		elif 'firstName' in kwargs and 'lastName' in kwargs and ('companyId' in kwargs or 'companyName' in kwargs):
			pass
		elif 'fullName' in kwargs and ('companyId' in kwargs or 'companyName' in kwargs):
			pass
		else:
			raise PyZiException(f'Contact enrich inputs are invalid. Please refer to docs. \n\tInputs provided: {kwargs}')
		return kwargs


class EnrichContacts(Enrich):
	api_object = ContactEnrich
	match_input = 'matchPersonInput'


class EnrichCompanies(Enrich):
	api_object = ContactEnrich
	match_input = 'matchCompanyInput'
