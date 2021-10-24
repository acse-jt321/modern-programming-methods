from urllib.request import Request, urlopen
req = Request("https://api.tfl.gov.uk/Occupancy/BikePoints/BikePoints_187", method="GET")
response = urlopen(req) # we could just use urlopen("https://api.tfl.gov.uk/Occupancy/BikePoints/BikePoints_187")，Open the URL url, which can be either a string or a Request object.
print(response.read()) 