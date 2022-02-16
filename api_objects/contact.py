from typing import List, Optional, Union

from api_objects.base import ApiObject, QueryObject, Subclass
from api_objects.company import SearchedCompany, EnrichedCompany

__all__ = ['SearchedContact', 'EnrichedContact']


class ContactSearchQuery(QueryObject):
	def __init__(self, **kwargs):
		self.address: Optional[str] = None
		self.boardMember: Optional[str] = None
		self.companyDescription: Optional[str] = None
		self.companyId: Optional[str] = None
		self.companyName: Optional[str] = None
		self.companyPastOrPresent: Optional[str] = None
		self.companyRanking: Optional[str] = None
		self.companyStructureIncludedSubUnitTypes: Optional[str] = None
		self.companyTicker: Optional[List[str]] = None
		self.companyType: Optional[str] = None
		self.companyWebsite: Optional[str] = None
		self.contactAccuracyScoreMax: Optional[str] = None
		self.contactAccuracyScoreMin: Optional[str] = None
		self.continent: Optional[str] = None
		self.country: Optional[str] = None
		self.degree: Optional[str] = None
		self.department: Optional[str] = None
		self.emailAddress: Optional[str] = None
		self.employeeCount: Optional[str] = None
		self.employeeRangeMax: Optional[str] = None
		self.employeeRangeMin: Optional[str] = None
		self.excludedRegions: Optional[str] = None
		self.excludeJobTitle: Optional[str] = None
		self.excludeManagementLevel: Optional[str] = None
		self.excludePartialProfiles: Optional[bool] = None
		self.executivesOnly: Optional[bool] = None
		self.firstName: Optional[str] = None
		self.fullName: Optional[str] = None
		self.fundingAmountMax: Optional[int] = None
		self.fundingAmountMin: Optional[int] = None
		self.fundingEndDate: Optional[str] = None
		self.fundingStartDate: Optional[str] = None
		self.hasBeenNotified: Optional[str] = None
		self.hashedEmail: Optional[str] = None
		self.hashTagString: Optional[str] = None
		self.industryCodes: Optional[str] = None
		self.industryKeywords: Optional[str] = None
		self.jobFunction: Optional[str] = None
		self.jobTitle: Optional[str] = None
		self.lastName: Optional[str] = None
		self.lastUpdatedDateAfter: Optional[str] = None
		self.lastUpdatedInMonths: Optional[int] = None
		self.locationCompanyId: Optional[List[str]] = None
		self.locationSearchType: Optional[str] = None
		self.managementLevel: Optional[str] = None
		self.metroRegion: Optional[str] = None
		self.middleInitial: Optional[str] = None
		self.naicsCodes: Optional[str] = None
		self.oneYearEmployeeGrowthRateMax: Optional[str] = None
		self.oneYearEmployeeGrowthRateMin: Optional[str] = None
		self.page: Optional[int] = None
		self.parentId: Optional[str] = None
		self.personId: Optional[str] = None
		self.phone: Optional[List[str]] = None
		self.positionStartDateMax: Optional[str] = None
		self.positionStartDateMin: Optional[str] = None
		self.primaryIndustriesOnly: Optional[bool] = None
		self.requiredFields: Optional[str] = None
		self.revenue: Optional[str] = None
		self.revenueMax: Optional[int] = None
		self.revenueMin: Optional[int] = None
		self.rpp: Optional[int] = None
		self.school: Optional[str] = None
		self.sicCodes: Optional[str] = None
		self.sortBy: Optional[str] = None
		self.sortOrder: Optional[str] = None
		self.state: Optional[str] = None
		self.street: Optional[str] = None
		self.subUnitTypes: Optional[str] = None
		self.supplementalEmail: Optional[List[str]] = None
		self.techAttributeTagList: Optional[str] = None
		self.twoYearEmployeeGrowthRateMax: Optional[str] = None
		self.twoYearEmployeeGrowthRateMin: Optional[str] = None
		self.ultimateParentId: Optional[str] = None
		self.validDateAfter: Optional[str] = None
		self.zipCode: Optional[str] = None
		self.zipCodeRadiusMiles: Optional[str] = None
		self.zoominfoContactsMax: Optional[str] = None
		self.zoominfoContactsMin: Optional[str] = None
		super().__init__(**kwargs)


class ContactEnrichQuery(QueryObject):
	def __init__(self, **kwargs):
		self.companyId: Optional[Union[int, str]] = None
		self.companyName: Optional[str] = None
		self.emailAddress: Optional[str] = None
		self.externalURL: Optional[str] = None
		self.firstName: Optional[str] = None
		self.fullName: Optional[str] = None
		self.hashedEmail: Optional[str] = None
		self.jobTitle: Optional[str] = None
		self.lastName: Optional[str] = None
		self.lastUpdatedDateAfter: Optional[str] = None
		self.personId: Optional[Union[int, str]] = None
		self.phone: Optional[str] = None
		self.validDateAfter: Optional[str] = None
		super().__init__(**kwargs)


class EnrichedContact(ApiObject):
	datetime_fields = ['lastUpdatedDate', 'noticeProvidedDate', 'positionStartDate', 'validDate']
	subclasses = [Subclass('company', EnrichedCompany)]
	
	def __init__(self, **kwargs):
		self.city = None
		self.company = None
		self.companyCity = None
		self.companyContinent = None
		self.companyCountry = None
		self.companyDescriptionList = None
		self.companyDivision = None
		self.companyEmployeeCount = None
		self.companyEmployeeRange = None
		self.companyFax = None
		self.companyId = None
		self.companyIndustries = None
		self.companyLogo = None
		self.companyNaicsCodes = None
		self.companyName = None
		self.companyPhone = None
		self.companyPrimaryIndustry = None
		self.companyRanking = None
		self.companyRevenue = None
		self.companyRevenueNumeric = None
		self.companyRevenueRange = None
		self.companySicCodes = None
		self.companySocialMediaUrls = None
		self.companyState = None
		self.companyStreet = None
		self.companyTicker = None
		self.companyType = None
		self.companyWebsite = None
		self.companyZipCode = None
		self.contactAccuracyScore = None
		self.continent = None
		self.country = None
		self.directPhoneDoNotCall = None
		self.education = None
		self.email = None
		self.employmentHistory = None
		self.externalUrls = None
		self.firstName = None
		self.hasCanadianEmail = None
		self.hashedEmails = None
		self.id = None
		self.isDefunct = None
		self.jobFunction = None
		self.jobTitle = None
		self.lastName = None
		self.lastUpdatedDate = None
		self.locationCompanyId = None
		self.managementLevel = None
		self.metroArea = None
		self.middleName = None
		self.mobilePhoneDoNotCall = None
		self.noticeProvidedDate = None
		self.personHasMoved = None
		self.phone = None
		self.picture = None
		self.positionStartDate = None
		self.region = None
		self.salutation = None
		self.state = None
		self.street = None
		self.suffix = None
		self.validDate = None
		self.withinCalifornia = None
		self.withinCanada = None
		self.withinEu = None
		self.zipCode = None
		super().__init__(**kwargs)


class SearchedContact(ApiObject):
	datetime_fields = ['fundingEndDate', 'fundingStartDate', 'lastUpdatedDateAfter', 'validDateAfter']
	subclasses = [Subclass('company', SearchedCompany)]
	
	def __init__(self, **kwargs):
		self.company = None
		self.contactAccuracyScore = None
		self.firstName = None
		self.hasCompanyCountry = None
		self.hasCompanyEmployeeCount = None
		self.hasCompanyIndustry = None
		self.hasCompanyPhone = None
		self.hasCompanyRevenue = None
		self.hasCompanyState = None
		self.hasCompanyStreet = None
		self.hasCompanyZipCode = None
		self.hasDirectPhone = None
		self.hasEmail = None
		self.hasMobilePhone = None
		self.hasSupplementalEmail = None
		self.jobTitle = None
		self.lastName = None
		self.lastUpdatedDate = None
		self.middleName = None
		self.personId = None
		self.validDate = None
		super().__init__(**kwargs)
