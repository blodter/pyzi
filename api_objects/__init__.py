from api_objects.base import ApiObject, EnrichObject
from api_objects.company import *
from api_objects.contact import *
from api_objects.results import *


class Compliance(EnrichObject):
	_enrich_match_input = 'matchPersonInput'
	
	companyName = None
	emailAddresses = None
	employmentHistory = None
	firstName = None
	hasCanadianEmail = None
	hasMoved = None
	id = None
	lastName = None
	looksLikeCalifornia = None
	looksLikeCanada = None
	looksLikeEu = None
	noticeProvidedDate = None
	pastEmailAddresses = None
	title = None
	withinCalifornia = None
	withinCanada = None
	withinEu = None


class IP(ApiObject):
	city = None
	country = None
	employeeCount = None
	id = None
	industries = None
	name = None
	revenue = None
	state = None
	street = None
	ticker = None
	website = None
	zipCode = None


class InputField(ApiObject):
	description = None
	fieldName = None
	fieldType = None


class Intent(ApiObject):
	audienceStrength = None
	category = None
	companyHasOtherTopicConsumption = None
	companyId = None
	companyName = None
	companyWebsite = None
	id = None
	recommendedContacts = None
	signalDate = None
	signalScore = None
	topic = None


class News(ApiObject):
	categories = None
	companyId = None
	companyName = None
	domain = None
	imageUrl = None
	pageDate = None
	title = None
	url = None


class OutputField(ApiObject):
	description = None
	fieldName = None


class Scoop(ApiObject):
	companyId = None
	companyName = None
	contacts = None
	description = None
	id = None
	link = None
	linkText = None
	originalPublishedDate = None
	publishedDate = None
	topics = None
	types = None
	updateText = None


class Webhook(ApiObject):
	createdDate = None
	enabled = None
	id = None
	subscriptions = None
	targetUrl = None
	title = None
	verificationToken = None
