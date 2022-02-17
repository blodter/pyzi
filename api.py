import logging
from typing import Callable, List, Union

from fuzzywuzzy import fuzz

from endpoint import DummyEndpointConfig, EndpointConfigs, EndpointConfigType
from error import ERRORS
from exceptions import PyZiException, ZoomInfoError

log = logging.getLogger(__name__)


class BaseApi:
	def __init__(
			self,
			*,
			session,
			timeout,
			url,
			_endpoint_config: EndpointConfigType = None
	):
		self._endpoint_config = _endpoint_config
		self.session = session
		self.timeout = timeout
		self.url = url
	
	def post(self, payload: dict, endpoint: str = None):
		return self._process_response(self._call_api(
			self.session.post, self._build_url(endpoint), json=payload, timeout=self.timeout
		))
	
	def put(self, payload: dict, endpoint: str = None):
		return self._process_response(self._call_api(
			self.session.put, self._build_url(endpoint), json=payload, timeout=self.timeout
		))
	
	def delete(self, payload: dict = None, endpoint: str = None):
		return self._process_response(self._call_api(
			self.session.delete, self._build_url(endpoint), json=payload, timeout=self.timeout
		))
	
	def get(self, payload: dict = None, endpoint: str = None):
		return self._process_response(self._call_api(
			self.session.get, self._build_url(endpoint), timeout=self.timeout, params=payload
		))
	
	def _call_api(self, http_method, url, **kwargs):
		response = http_method(url, **kwargs)
		self._check_response(response)
		return response
	
	def _process_response(self, response):
		try:
			response_data = response.json()
		except ValueError:
			response_data = response
		_raw = getattr(self, '_raw', False)
		if not _raw:
			return self._endpoint_config.mapping_method(response_data)
		else:
			return response_data
	
	def _check_response(self, response):
		if response.status_code > 299 or response.status_code < 200:
			log.debug(f'Received response code [{response.status_code}] - headers: {response.headers}')
			try:
				response_json = response.json()
				error_code = response_json.get('responseCode', None)
				error_message = response_json.get('message', None)
				code_errors = ERRORS.get(error_code, None)
				if not code_errors:
					raise PyZiException(f'Error code of "{error_code}" does not exist.\n{error_code}: {error_message}')
				for error, suggestion in code_errors.items():
					if fuzz.partial_ratio(error, error_message) >= 97:
						raise ZoomInfoError(f'{error_code} error: {error_message}\nSuggestion: {suggestion}')
				else:
					raise PyZiException(f'Error status of "{error_message}" does not exist.\n{error_code}: {error_message}')
			except ValueError:
				response.raise_for_status()
	
	def _build_url(self, endpoint: str = None):
		return f'{self.url}/{endpoint if endpoint else self._endpoint_config.endpoint}'


class CallableApi(BaseApi):
	def __call__(self, _call_method: Callable = None, _raw=False, **kwargs):
		self._raw = _raw
		return getattr(self, _call_method if _call_method else self._endpoint_config.call_method)(payload=kwargs)


class IOFieldsApi(CallableApi):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, _endpoint_config=kwargs.pop('_endpoint_config'), **kwargs)
		self.input_fields = CallableApi(*args, _endpoint_config=self._endpoint_config.input_fields, **kwargs)
		self.output_fields = CallableApi(*args, _endpoint_config=self._endpoint_config.output_fields, **kwargs)
		

class EnrichmentApi(CallableApi):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, _endpoint_config=kwargs.pop('_endpoint_config'), **kwargs)
		self.input_fields = CallableApi(*args, _endpoint_config=self._endpoint_config.input_fields, **kwargs)
		self.output_fields = CallableApi(*args, _endpoint_config=self._endpoint_config.output_fields, **kwargs)
		
	def __call__(self, *inputs, fields: List[str] = None, exclude: List[str] = None):
		payload = self._endpoint_config.api_object.build_enrich_query(inputs, fields, exclude)
		return getattr(self, self._endpoint_config.call_method)(payload=payload)


class EnrichApi(BaseApi):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.company = EnrichmentApi(*args, _endpoint_config=EndpointConfigs('enrich.company'), **kwargs)
		self.company_location = EnrichmentApi(*args, _endpoint_config=EndpointConfigs('enrich.company_location'), **kwargs)
		self.company_master_data = EnrichmentApi(*args, _endpoint_config=EndpointConfigs('enrich.company_master_data'), **kwargs)
		self.contact = EnrichmentApi(*args, _endpoint_config=EndpointConfigs('enrich.contact'), **kwargs)
		self.corporate_hierarchy = EnrichmentApi(*args, _endpoint_config=EndpointConfigs('enrich.corporate_hierarchy'), **kwargs)
		self.hashtag = EnrichmentApi(*args, _endpoint_config=EndpointConfigs('enrich.hashtag'), **kwargs)
		self.intent = EnrichmentApi(*args, _endpoint_config=EndpointConfigs('enrich.intent'), **kwargs)
		self.ip = EnrichmentApi(*args, _endpoint_config=EndpointConfigs('enrich.ip'), **kwargs)
		self.news = EnrichmentApi(*args, _endpoint_config=EndpointConfigs('enrich.news'), **kwargs)
		self.orgchart = EnrichmentApi(*args, _endpoint_config=EndpointConfigs('enrich.orgchart'), **kwargs)
		self.scoop = EnrichmentApi(*args, _endpoint_config=EndpointConfigs('enrich.scoop'), **kwargs)
		self.tech = EnrichmentApi(*args, _endpoint_config=EndpointConfigs('enrich.tech'), **kwargs)


class LookupApi(BaseApi):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		lookup_configs = EndpointConfigs('lookup')
		self._set_endpoints(*args, configs=lookup_configs.items(), **kwargs)
	
	def _set_endpoints(self, *args, configs, **kwargs):
		for name, config in configs:
			if not isinstance(config, DummyEndpointConfig):
				setattr(self, name, CallableApi(*args, _endpoint_config=config, **kwargs))
			else:
				setattr(self, name, BaseApi(*args, **kwargs))
				sub_endpoint = getattr(self, name)
				for name_, config_ in config.items():
					setattr(sub_endpoint, name_, CallableApi(*args, _endpoint_config=config_, **kwargs))


class SearchApi(BaseApi):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.company = IOFieldsApi(*args, _endpoint_config=EndpointConfigs('search.company'), **kwargs)
		self.contact = IOFieldsApi(*args, _endpoint_config=EndpointConfigs('search.contact'), **kwargs)
		self.intent = IOFieldsApi(*args, _endpoint_config=EndpointConfigs('search.intent'), **kwargs)
		self.news = IOFieldsApi(*args, _endpoint_config=EndpointConfigs('search.news'), **kwargs)
		self.scoop = IOFieldsApi(*args, _endpoint_config=EndpointConfigs('search.scoop'), **kwargs)


class WebhooksApi(BaseApi):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		# TODO: Work in progress
		self.create = ...
		self.update = ...
		self.delete = ...
		self.validate = ...
		self.generate_token = ...
		self.subscription_types = ...
	
	def __call__(self, id_: Union[str, int] = None):
		self.get(endpoint='webhooks' if not id_ else f'webhooks/{id_}')
		
		
class ComplianceApi(IOFieldsApi):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, _endpoint_config=EndpointConfigs('compliance'), **kwargs)
