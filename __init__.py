from typing import Any, Union

import requests
import zi_api_auth_client
from requests.adapters import HTTPAdapter
from requests.packages.urllib3 import Retry

from api import LookupApi, SearchAndEnrichApi, WebhookApi
from exceptions import PyZiException


class ZoomInfo:
	def __init__(
			self,
			*,
			client_id: str = None,
			domain='zoominfo.com',
			password: str = None,
			private_key: str = None,
			session: Any = None,
			subdomain='api',
			token: str = None,
			username: str = None,
	):
		self.username = username
		self.password = password
		self.client_id = client_id
		self.private_key = private_key
		self.token = token
		self.session = self._init_session(session)
		self.url = f'https://{subdomain}.{domain}'
		config = dict(
			session=self.session,
			url=self.url,
		)
		# TODO: Some of these endpoints are a work in progress
		self.company = SearchAndEnrichApi(config_name='company', **config)
		self.company_location = ...
		self.company_master_data = ...
		self.contact = SearchAndEnrichApi(config_name='contact', **config)
		self.corporatehierarchy = ...
		self.hashtag = ...
		self.intent = SearchAndEnrichApi(config_name='intent', **config)
		self.ip = ...
		self.lookup = LookupApi(**config)
		self.news = SearchAndEnrichApi(config_name='news', **config)
		self.orgchart = ...
		self.scoop = SearchAndEnrichApi(config_name='scoop', **config)
		self.tech = ...
		self.webhooks = WebhookApi(**config)
	
	def _get_auth_token(self) -> str:
		if self.username and self.password:
			return zi_api_auth_client.user_name_pwd_authentication(self.username, self.password)
		elif self.username and self.client_id and self.private_key:
			return zi_api_auth_client.pki_authentication(self.username, self.client_id, self.private_key)
	
	def _init_session(self, session):
		if not session:
			session = requests.Session()
			session.mount(
				'https://',
				HTTPAdapter(max_retries=Retry(
					total=3, status_forcelist=[retry for retry in requests.status_codes.codes if retry != 429]
				))
			)
		if not hasattr(session, 'authorized') or not session.authorized:
			if (not self.username and not self.password) and (not self.username and not self.client_id and not self.private_key) and not self.token:
				raise PyZiException('Either a username and password, username, client_id, and private key, or just a token are required!')
			if not self.token:
				self.token = self._get_auth_token()
			session.headers.update({'Authorization': f'Bearer {self.token}'})
		return session
	
	def authenticate(self):
		self.token = self._get_auth_token()
