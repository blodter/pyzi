ERRORS = {
	400: {
		'Exceeded the max limit to enrich new Contacts or Companies': 'See the rate and usage limiting data in the response header. Refer to "Rate and usage limiting" for details.',
		'Missing outputFields parameter': 'Some requests (specifically the Enrich API) require at least one outputfields parameter to be specified',
		'No roles found for login': 'Contact your ZoomInfo sales representative.',
		'Page number (page) is not a number': 'Ensure that the value conforms to the correct data type (integer)',
		'Page number (page) requested is greater than the available results': 'Input a page number that falls within the results per page (rpp) and total results',
		'Request body has malformed JSON': 'Check the request JSON for proper syntax',
		'Results per page (rpp) is not a number': 'Ensure that the value conforms to the correct data type (integer)',
		'Results per page (rpp) is over max allowed value (100)': 'The number of returned objects exceeds the maximum allowed value of 100',
		'The parameter passed for sortBy is invalid': 'Results can only be sorted on specific fields. See the endpoint field descriptions for valid sortBy options.',
		'There are invalid fields in your request.': 'Check field names used in the request',
		'There is insufficient information for this request': 'Check your request syntax and ensure it meets specifications described for the endpoint',
		'Total record pagination is over max allowed value (1000)': 'The number of returned objects exceeds the maximum allowed value of 100',
	},
	401: {
		'Authentication failed': 'Ensure you are using valid credentials or token',
	},
	403: {
		'There are fields that are not allowed under your subscription': 'Check your subscription details. Contact your ZoomInfo sales representative.',
		'You do not have access to the enrich endpoint': 'You are not provisioned to access this endpoint. Contact your ZoomInfo sales representative.',
		'You do not have access to the search endpoint': 'You are not provisioned to access this endpoint. Contact your ZoomInfo sales representative.',
		'You do not have access to this endpoint': 'You are not provisioned to access this endpoint. Contact your ZoomInfo sales representative.',
		'You have used up all of your allowed request limit': 'See the rate and usage limiting data in the response header. Refer to "Rate and usage limiting" for details.',
		'You have used up all of your allowed request limit for WebSights API': 'See the rate and usage limiting data in the response header. Refer to "Rate and usage limiting" for details.',
		'You have used up all of your allowed record limit': 'See the rate and usage limiting data in the response header. Refer to "Rate and usage limiting" for details.',
		'You have used up all of your allowed record limit for WebSights API': 'See the rate and usage limiting data in the response header. Refer to "Rate and usage limiting" for details.',
		'You do not have permission to access the ZoomInfo API': 'Confirm that your access credentials are valid',
	},
	429: {
		'You have exceeded your API query rate limit. Please decrease the frequency of your API requests': 'See the rate and usage limiting data in the response header. Refer to "Rate and usage limiting" for details.',
	},
	500: {
		'An unexpected error has occurred. Please try again and if this continues to occur, please contact us and reference the error id provided above': 'The request could be too large in scope, too long to return, or experiencing a system or network issue. Contact support.',
		'Search failed. Please try again and if this continues to occur, please contact us and reference the error id provided above': 'The request could be too large in scope, too long to return, or experiencing a system or network issue. Contact support.',
	}
}
