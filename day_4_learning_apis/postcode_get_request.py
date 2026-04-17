import requests

post_codes_req = requests.get("https://api.postcodes.io/postcodes/ne298lf")

print(f"Status code: {post_codes_req.status_code}")
print(f"Headers: {post_codes_req.headers}")
print(f"Content: {post_codes_req.content}")
print(f"Datatype for Content: {type(post_codes_req.content)}")
print(f"JSON: {post_codes_req.json()}")
print(f"Data type of JSON: {type(post_codes_req.json())}")

postcode_dict = post_codes_req.json()
print(postcode_dict['result']['region'])