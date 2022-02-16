from api_objects.base import ApiObject
from api_objects.company import *
from api_objects.contact import *
from api_objects.results import *


class Compliance(ApiObject):
	def __init__(self, **kwargs):
		self.companyName = None
		self.emailAddresses = None
		self.employmentHistory = None
		self.firstName = None
		self.hasCanadianEmail = None
		self.hasMoved = None
		self.id = None
		self.lastName = None
		self.looksLikeCalifornia = None
		self.looksLikeCanada = None
		self.looksLikeEu = None
		self.noticeProvidedDate = None
		self.pastEmailAddresses = None
		self.title = None
		self.withinCalifornia = None
		self.withinCanada = None
		self.withinEu = None
		super().__init__(**kwargs)


class EnrichedIP(ApiObject):
	def __init__(self, **kwargs):
		self.city = None
		self.country = None
		self.employeeCount = None
		self.id = None
		self.industries = None
		self.name = None
		self.revenue = None
		self.state = None
		self.street = None
		self.ticker = None
		self.website = None
		self.zipCode = None
		super().__init__(**kwargs)


class InputField(ApiObject):
	def __init__(self, **kwargs):
		self.description = None
		self.fieldName = None
		self.fieldType = None
		super().__init__(**kwargs)


class Intent(ApiObject):
	def __init__(self, **kwargs):
		self.audienceStrength = None
		self.category = None
		self.companyHasOtherTopicConsumption = None
		self.companyId = None
		self.companyName = None
		self.companyWebsite = None
		self.id = None
		self.recommendedContacts = None
		self.signalDate = None
		self.signalScore = None
		self.topic = None
		super().__init__(**kwargs)


class News(ApiObject):
	def __init__(self, **kwargs):
		self.categories = None
		self.companyId = None
		self.companyName = None
		self.domain = None
		self.imageUrl = None
		self.pageDate = None
		self.title = None
		self.url = None
		super().__init__(**kwargs)


class OutputField(ApiObject):
	def __init__(self, **kwargs):
		self.description = None
		self.fieldName = None
		super().__init__(**kwargs)


class Scoop(ApiObject):
	def __init__(self, **kwargs):
		self.companyId = None
		self.companyName = None
		self.contacts = None
		self.description = None
		self.id = None
		self.link = None
		self.linkText = None
		self.originalPublishedDate = None
		self.publishedDate = None
		self.topics = None
		self.types = None
		self.updateText = None
		super().__init__(**kwargs)


class Webhook(ApiObject):
	def __init__(self, **kwargs):
		self.createdDate = None
		self.enabled = None
		self.id = None
		self.subscriptions = None
		self.targetUrl = None
		self.title = None
		self.verificationToken = None
		super().__init__(**kwargs)
