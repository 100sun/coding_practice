import requests

# GET request
response = requests.get("http://api.open-notify.org/astros.json")
print(response)  # Response<200>
response.content()  # Return the raw bytes of the data payload
response.text()  # Return a string representation of the data payload
response.json()  # This method is convenient when the API returns JSON

# GET request w params
query = {'lat': '45', 'lon': '180'}
response = requests.get('http://api.open-notify.org/iss-pass.json', params=query)
print(response.json())

# POST/ PUT request
response = requests.post('https://httpbin.org/post', data={'key': 'value'})# Create a new resource
requests.put('https://httpbin.org/put', data={'key': 'value'})# Update an existing resource
print(response.headers["date"])  # 'Wed, 11 June 2020 19:32:24 GMT'

# https://www.nylas.com/blog/use-python-requests-module-rest-apis/
