from api_objects.base import ApiObject

__all__ = [
	'EnrichedCompany',
	'EnrichedCompanyLocation',
	'EnrichedCompanyMasterData',
	'EnrichedCorporateHierarchy',
	'EnrichedOrgChart',
	'SearchedCompany'
]


class EnrichedCompany(ApiObject):
	datetime_fields = ['lastUpdatedDate']
	
	def __init__(self, **kwargs):
		self.alexaRank = None
		self.businessModel = None
		self.certificationDate = None
		self.certified = None
		self.city = None
		self.companyFunding = None
		self.companyStatus = None
		self.companyStatusDate = None
		self.competitors = None
		self.continent = None
		self.country = None
		self.createdDate = None
		self.departmentBudgets = None
		self.descriptionList = None
		self.domainList = None
		self.employeeCount = None
		self.employeeGrowth = None
		self.employeeRange = None
		self.fax = None
		self.foundedYear = None
		self.hashtags = None
		self.id = None
		self.industries = None
		self.isDefunct = None
		self.lastUpdatedDate = None
		self.locationCount = None
		self.locationMatch = None
		self.logo = None
		self.metroArea = None
		self.naicsCodes = None
		self.name = None
		self.numberOfContactsInZoomInfo = None
		self.parentId = None
		self.parentName = None
		self.phone = None
		self.primaryIndustry = None
		self.products = None
		self.recentFundingAmount = None
		self.recentFundingDate = None
		self.revenue = None
		self.revenueRange = None
		self.sicCodes = None
		self.socialMediaUrls = None
		self.state = None
		self.street = None
		self.subUnitCodes = None
		self.subUnitIndustries = None
		self.subUnitType = None
		self.techAttributes = None
		self.ticker = None
		self.totalFundingAmount = None
		self.type = None
		self.ultimateParentEmployees = None
		self.ultimateParentId = None
		self.ultimateParentName = None
		self.ultimateParentRevenue = None
		self.website = None
		self.zipCode = None
		super().__init__(**kwargs)


class EnrichedCompanyLocation(ApiObject):
	def __init__(self, **kwargs):
		self.city = None
		self.companyAddressStatus = None
		self.companyId = None
		self.companySubUnitType = None
		self.country = None
		self.fax = None
		self.phone = None
		self.state = None
		self.street = None
		self.zipCode = None
		super().__init__(**kwargs)


class EnrichedCompanyMasterData(ApiObject):
	def __init__(self, **kwargs):
		self.zi_c_address_confidence_score = None
		self.zi_c_alexa_rank = None
		self.zi_c_c_suite_contacts = None
		self.zi_c_cbsa_name = None
		self.zi_c_city = None
		self.zi_c_company_cbsa_name = None
		self.zi_c_company_city = None
		self.zi_c_company_country = None
		self.zi_c_company_county = None
		self.zi_c_company_employee_range = None
		self.zi_c_company_employees = None
		self.zi_c_company_fax = None
		self.zi_c_company_id = None
		self.zi_c_company_latitude = None
		self.zi_c_company_longitude = None
		self.zi_c_company_name = None
		self.zi_c_company_phone = None
		self.zi_c_company_revenue = None
		self.zi_c_company_revenue_range = None
		self.zi_c_company_state = None
		self.zi_c_company_street = None
		self.zi_c_company_street_2 = None
		self.zi_c_company_url = None
		self.zi_c_company_verified_address = None
		self.zi_c_company_zip = None
		self.zi_c_country = None
		self.zi_c_county = None
		self.zi_c_currency_code = None
		self.zi_c_domestic_parent_city = None
		self.zi_c_domestic_parent_company_id = None
		self.zi_c_domestic_parent_country = None
		self.zi_c_domestic_parent_name = None
		self.zi_c_domestic_parent_state = None
		self.zi_c_domestic_parent_street = None
		self.zi_c_domestic_parent_street_2 = None
		self.zi_c_domestic_parent_url = None
		self.zi_c_domestic_parent_zip = None
		self.zi_c_ein = None
		self.zi_c_employee_growth_1yr = None
		self.zi_c_employee_growth_2yr = None
		self.zi_c_employee_range = None
		self.zi_c_employees = None
		self.zi_c_employees_confidence_score = None
		self.zi_c_engineering_contacts = None
		self.zi_c_estimated_age = None
		self.zi_c_facebook_url = None
		self.zi_c_fax = None
		self.zi_c_finance_contacts = None
		self.zi_c_finance_sophistication = None
		self.zi_c_finance_spend = None
		self.zi_c_finance_strength = None
		self.zi_c_franchisor_city = None
		self.zi_c_franchisor_company_id = None
		self.zi_c_franchisor_country = None
		self.zi_c_franchisor_name = None
		self.zi_c_franchisor_state = None
		self.zi_c_franchisor_street = None
		self.zi_c_franchisor_street_2 = None
		self.zi_c_franchisor_url = None
		self.zi_c_franchisor_zip = None
		self.zi_c_funding_strength = None
		self.zi_c_funding_type = None
		self.zi_c_global_parent_city = None
		self.zi_c_global_parent_company_id = None
		self.zi_c_global_parent_country = None
		self.zi_c_global_parent_name = None
		self.zi_c_global_parent_state = None
		self.zi_c_global_parent_street = None
		self.zi_c_global_parent_street_2 = None
		self.zi_c_global_parent_url = None
		self.zi_c_global_parent_zip = None
		self.zi_c_has_mobile_app = None
		self.zi_c_hierarchy_code = None
		self.zi_c_hierarchy_level = None
		self.zi_c_hr_contacts = None
		self.zi_c_hr_sophistication = None
		self.zi_c_hr_spend = None
		self.zi_c_hr_strength = None
		self.zi_c_immediate_parent_city = None
		self.zi_c_immediate_parent_company_id = None
		self.zi_c_immediate_parent_country = None
		self.zi_c_immediate_parent_name = None
		self.zi_c_immediate_parent_state = None
		self.zi_c_immediate_parent_street = None
		self.zi_c_immediate_parent_street_2 = None
		self.zi_c_immediate_parent_url = None
		self.zi_c_immediate_parent_zip = None
		self.zi_c_inactive_flag = None
		self.zi_c_industries = None
		self.zi_c_industry_primary = None
		self.zi_c_investor_names = None
		self.zi_c_is_b2b = None
		self.zi_c_is_b2c = None
		self.zi_c_is_domestic_hq = None
		self.zi_c_is_fortune_100 = None
		self.zi_c_is_fortune_500 = None
		self.zi_c_is_franchisee = None
		self.zi_c_is_franchisor = None
		self.zi_c_is_global_parent = None
		self.zi_c_is_hq = None
		self.zi_c_is_public = None
		self.zi_c_is_s_and_p_500 = None
		self.zi_c_is_small_business = None
		self.zi_c_is_subsidiary = None
		self.zi_c_it_contacts = None
		self.zi_c_keywords = None
		self.zi_c_last_updated_date = None
		self.zi_c_latest_funding_age = None
		self.zi_c_latest_funding_amount = None
		self.zi_c_latest_funding_date = None
		self.zi_c_latitude = None
		self.zi_c_legal_contacts = None
		self.zi_c_legal_entity_type = None
		self.zi_c_linkedin_url = None
		self.zi_c_location_id = None
		self.zi_c_longitude = None
		self.zi_c_marketing_contacts = None
		self.zi_c_marketing_sophistication = None
		self.zi_c_marketing_spend = None
		self.zi_c_marketing_strength = None
		self.zi_c_medical_contacts = None
		self.zi_c_naics2 = None
		self.zi_c_naics4 = None
		self.zi_c_naics6 = None
		self.zi_c_naics_confidence_score = None
		self.zi_c_naics_top3 = None
		self.zi_c_naics_top3_confidence_scores = None
		self.zi_c_name = None
		self.zi_c_name_confidence_score = None
		self.zi_c_name_display = None
		self.zi_c_names_other = None
		self.zi_c_num_funding_rounds = None
		self.zi_c_num_keywords = None
		self.zi_c_num_locations = None
		self.zi_c_num_of_investors = None
		self.zi_c_operations_contacts = None
		self.zi_c_parent_child_confidence_score = None
		self.zi_c_phone = None
		self.zi_c_phone_confidence_score = None
		self.zi_c_release_date = None
		self.zi_c_revenue = None
		self.zi_c_revenue_confidence_score = None
		self.zi_c_revenue_range = None
		self.zi_c_sales_contacts = None
		self.zi_c_sales_sophistication = None
		self.zi_c_sales_spend = None
		self.zi_c_sales_strength = None
		self.zi_c_sic2 = None
		self.zi_c_sic3 = None
		self.zi_c_sic4 = None
		self.zi_c_sic_confidence_score = None
		self.zi_c_sic_top3 = None
		self.zi_c_sic_top3_confidence_scores = None
		self.zi_c_social_sophistication = None
		self.zi_c_state = None
		self.zi_c_street = None
		self.zi_c_street_2 = None
		self.zi_c_sub_industries = None
		self.zi_c_sub_industry_primary = None
		self.zi_c_tech_ids = None
		self.zi_c_tech_sophistication = None
		self.zi_c_tech_spend = None
		self.zi_c_tech_strength = None
		self.zi_c_ticker = None
		self.zi_c_tickers_alt = None
		self.zi_c_tier_grade = None
		self.zi_c_top_keywords = None
		self.zi_c_total_funding_amount = None
		self.zi_c_twitter_url = None
		self.zi_c_url = None
		self.zi_c_url_confidence_score = None
		self.zi_c_url_last_updated = None
		self.zi_c_url_status = None
		self.zi_c_urls_alt = None
		self.zi_c_verified_address = None
		self.zi_c_year_founded = None
		self.zi_c_yelp_url = None
		self.zi_c_zip = None
		self.zi_es_domestic_parent_ecid = None
		self.zi_es_domestic_parent_location_id = None
		self.zi_es_ecid = None
		self.zi_es_employee_growth = None
		self.zi_es_franchisor_ecid = None
		self.zi_es_franchisor_location_id = None
		self.zi_es_global_parent_ecid = None
		self.zi_es_global_parent_location_id = None
		self.zi_es_growth = None
		self.zi_es_hq_ecid = None
		self.zi_es_hq_location_id = None
		self.zi_es_immediate_parent_ecid = None
		self.zi_es_immediate_parent_location_id = None
		self.zi_es_industries_top3 = None
		self.zi_es_industries_top3_confidence_scores = None
		self.zi_es_industry = None
		self.zi_es_industry_confidence_score = None
		self.zi_es_location_id = None
		self.zi_es_percent_employee_growth = None
		self.zi_es_percent_revenue_growth = None
		self.zi_es_revenue_growth = None
		self.zi_match_reason = None
		super().__init__(**kwargs)


class EnrichedCorporateHierarchy(ApiObject):
	def __init__(self, **kwargs):
		self.companyId = None
		self.familyTree = None
		self.parentage = None
		super().__init__(**kwargs)


class EnrichedOrgChart(ApiObject):
	def __init__(self, **kwargs):
		self.companyId = None
		self.companyName = None
		self.contentAccuracyScore = None
		self.department = None
		self.firstName = None
		self.hasDirectPhone = None
		self.hasEmail = None
		self.id = None
		self.jobFunction = None
		self.jobTitle = None
		self.lastName = None
		self.lastUpdatedDate = None
		self.middleName = None
		self.orgChartSubTier = None
		self.orgChartTier = None
		super().__init__(**kwargs)


class SearchedCompany(ApiObject):
	def __init__(self, **kwargs):
		self.id = None
		self.name = None
		super().__init__(**kwargs)
