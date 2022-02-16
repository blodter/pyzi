import logging
from typing import Callable, Union

from fuzzywuzzy import fuzz

from api_config import ApiConfigType, ApiConfigs, DummyApiConfig
from error import ERRORS
from exceptions import PyZiException, ZoomInfoError

log = logging.getLogger(__name__)


class BaseApi:
	def __init__(
			self,
			*,
			session,
			url,
			api_config: ApiConfigType = None
	):
		self.api_config = api_config
		self.session = session
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
		return self.api_config.mapping_method(response_data)
	
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
		return f'{self.url}/{endpoint if endpoint else self.api_config.endpoint}'


class CallableApi(BaseApi):
	def __call__(self, call_method: Callable = None, **kwargs):
		return getattr(self, call_method if call_method else self.api_config.call_method)(payload=kwargs)


class IOFieldsApi(CallableApi):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, api_config=kwargs.pop('api_config'), **kwargs)
		self.input_fields = CallableApi(*args, api_config=self.api_config.input_fields, **kwargs)
		self.output_fields = CallableApi(*args, api_config=self.api_config.output_fields, **kwargs)


class SearchAndEnrichApi(BaseApi):
	def __init__(self, *args, config_name, **kwargs):
		super().__init__(*args, **kwargs)
		self.enrich = IOFieldsApi(*args, api_config=ApiConfigs(f'enrich.{config_name}'), **kwargs)
		self.search = IOFieldsApi(*args, api_config=ApiConfigs(f'search.{config_name}'), **kwargs)


class LookupApi(BaseApi):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		lookup_configs = ApiConfigs('lookup')
		self._set_endpoints(*args, configs=lookup_configs.items(), **kwargs)
		
	def _set_endpoints(self, *args, configs, **kwargs):
		for name, config in configs:
			if not isinstance(config, DummyApiConfig):
				setattr(self, name, CallableApi(*args, api_config=config, **kwargs))
			else:
				setattr(self, name, BaseApi(*args, **kwargs))
				sub_endpoint = getattr(self, name)
				for name_, config_ in config.items():
					setattr(sub_endpoint, name_, CallableApi(*args, api_config=config_, **kwargs))
				
	def _set_sub_endpoints(self, *args, name, configs, **kwargs):
		setattr(self, name, BaseApi(*args, **kwargs))
		sub_endpoint = getattr(self, name)
		for name_, config in configs:
			setattr(sub_endpoint, name_, CallableApi(*args, api_config=config, **kwargs))


class WebhookApi(BaseApi):
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
