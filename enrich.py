from typing import Callable, List

from exceptions import PyZiException


class Enrich:
	match_input: str
	output_fields: List[str]
	enrichment_class: Callable
	
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
		if cls.enrichment_class:
			return {cls.match_input: [cls.enrichment_class(**i) for i in inputs], 'outputFields': fields}
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
	enrichment_class = ContactEnrich
	match_input = 'matchPersonInput'
	output_fields = [
		'id',
		'firstName',
		'middleName',
		'lastName',
		'email',
		'hasCanadianEmail',
		'phone',
		'directPhoneDoNotCall',
		'street',
		'city',
		'region',
		'metroArea',
		'zipCode',
		'state',
		'country',
		'continent',
		'personHasMoved',
		'withinEu',
		'withinCalifornia',
		'withinCanada',
		'lastUpdatedDate',
		'validDate',
		'noticeProvidedDate',
		'salutation',
		'suffix',
		'jobTitle',
		'jobFunction',
		'companyDivision',
		'education',
		'hashedEmails',
		'picture',
		'mobilePhoneDoNotCall',
		'externalUrls',
		'companyId',
		'companyName',
		'companyDescriptionList',
		'companyPhone',
		'companyFax',
		'companyStreet',
		'companyCity',
		'companyState',
		'companyZipCode',
		'companyCountry',
		'companyContinent',
		'companyLogo',
		'companySicCodes',
		'companyNaicsCodes',
		'contactAccuracyScore',
		'companyWebsite',
		'companyRevenue',
		'companyRevenueNumeric',
		'companyEmployeeCount',
		'companyType',
		'companyTicker',
		'companyRanking',
		'isDefunct',
		'companySocialMediaUrls',
		'companyPrimaryIndustry',
		'companyIndustries',
		'companyRevenueRange',
		'companyEmployeeRange',
		'employmentHistory',
		'managementLevel',
		'locationCompanyId'
	]


class EnrichCompanies(Enrich):
	match_input = 'matchCompanyInput'
	output_fields = [
		'id',
		'ticker',
		'name',
		'website',
		'domainList',
		'logo',
		'socialMediaUrls',
		'revenue',
		'employeeCount',
		'numberOfContactsInZoomInfo',
		'phone',
		'fax',
		'street',
		'city',
		'state',
		'zipCode',
		'country',
		'continent',
		'companyStatus',
		'companyStatusDate',
		'descriptionList',
		'sicCodes',
		'naicsCodes',
		'competitors',
		'ultimateParentId',
		'ultimateParentName',
		'ultimateParentRevenue',
		'ultimateParentEmployees',
		'subUnitCodes',
		'subUnitType',
		'subUnitIndustries',
		'primaryIndustry',
		'industries',
		'parentId',
		'parentName',
		'locationCount',
		'locationMatch',
		'alexaRank',
		'metroArea',
		'lastUpdatedDate',
		'createdDate',
		'certificationDate',
		'certified',
		'hashtags',
		'products',
		'techAttributes',
		'revenueRange',
		'employeeRange',
		'companyFunding',
		'recentFundingAmount',
		'recentFundingDate',
		'totalFundingAmount',
		'employeeGrowth',
		'type',
		'foundedYear',
		'businessModel',
		'isDefunct',
		'departmentBudgets'
	]
