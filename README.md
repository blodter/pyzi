PyZI
=======

PyZI is a straightforward Python wrapper for [ZoomInfo's API](https://api-docs.zoominfo.com/). 
Instantiating the client and making calls against the API is as simple as this:

	zoom = PyZI(username='morpheus@nebuchadnezzar.com', password='th3_m4tr1x')

	the_one = None
	search_results = zoom.search.contact(companyName='Meta Cortex', metroRegion='usa.illinois.chicago')

	for contact in search_results:
	    if contact.firstName == 'Thomas' and contact.lastName == 'Anderson':
	        the_one = contact
	        print('Wake up, Neo...')
	        print('The Matrix has you...')
	        print('Follow the white rabbit.')
	        print('Knock, knock, Neo.')
	        break 


Current functioning features are:

- All enrich endpoints (I think), including WebSights and Compliance.
- All lookup endpoints, to a degree, including Usage.
- All search endpoints; however, automatic pagination is not yet functioning.
- Webhooks 'get' endpoint (this endpoint is not accessible to me, so I have no way of verifying).

Current features in progress are:

- Caching
- Pagination for search endpoints, with a simple-to-use generator to iterate over
- Ratelimiting
- Register this package with PyPI (Python Package Index)
- Unit testing


This project is still a work in progress and has a multitude of features that still need to be implemented. 
With that said, if you - dear reader - are interested in contributing, 
please feel free to fork off and make some [pull requests](https://github.com/blodter/pyzi/pulls).
Additionally, if you have any issues or feature requests, 
please feel free to [submit them](https://github.com/blodter/pyzi/issues)!

More examples of this code:

Enrich
------

	zoom = PyZI(username='morpheus@nebuchadnezzar.com', password='th3_m4tr1x')

	enriched_contacts = zoom.enrich.contact(
	    firstName='Thomas', 
	    lastName='Anderson', 
	    companyName='Meta Cortex'
	)
	for contact in enriched_contacts:
	    print(f'{contact.firstName} {contact.lastName}')
	    print(f'{contact.phone}, {contact.email}')
	    print(f'{contact.street} {contact.city} {contact.state} {contact.zipCode}')



Lookup
------

    zoom = PyZI(username='morpheus@nebuchadnezzar.com', password='th3_m4tr1x')
    usages = zoom.lookup.usage()
    for usage in usages:
        print(usage.limitType)
        print(usage.description)
        print(f'{usage.currentUsage}/{usage.totalLimit} -- {usage.usageRemaining} remaining\n')
