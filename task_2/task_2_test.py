# Task 2 : Pytest Test Suite
    # Create a Pytest test suite for the API in Section A.
    # Cover:
        # Response time < 2 seconds
        # Schema validation (use pydantic or jsonschema)
        # Parameterized test: Validate multiple endpoints (e.g., /posts, /comments, /users).
        # Ensure the suite can be executed with pytest -v.


import json
import pytest
import requests
import jsonschema
from jsonschema import validate


@pytest.mark.parametrize("endpoint", ["posts", "comments", "users"])
def test_get_endpoints(endpoint):
    url = 'https://jsonplaceholder.typicode.com/{}'.format(endpoint)
    res = requests.get(url=url)

    # Response time validation.
    res_time = res.elapsed.total_seconds()
    print("Respose time : ",res_time)
    assert res_time < 2

    # Fetch all posts.
    res_data = res.json()
    print("Respose data : ",res_data)

    # Validate that the response status code is 200.
    assert res.status_code == 200
    print("Respose code validation : ", res.status_code==200)

    # Save the first 5 posts into a local JSON file.
    with open("{}.json".format(endpoint), "w") as final:
        json.dump(res_data[:5], final, indent=4)


    # Schema validation (by jsonschema)
    schema_dict = {
	"posts": {
		"type": "array",
		"items": {
			"type": "object",
			"properties": {
				"userId": {
					"type": "integer"
				},
				"id": {
					"type": "integer"
				},
				"title": {
					"type": "string"
				},
				"body": {
					"type": "string"
				}
			},
			"required": ["userId", "id", "title", "body"]
		}
	},

	"comments": {
		"type": "array",
		"items": {
			"type": "object",
			"properties": {
				"postId": {
					"type": "integer"
				},
				"id": {
					"type": "integer"
				},
				"name": {
					"type": "string"
				},
				"email": {
					"type": "string",
					"format": "email"
				},
				"body": {
					"type": "string"
				}
			},
			"required": ["postId", "id", "name", "email", "body"]
		}
	},

	"users": {
		"type": "array",
		"items": {
			"type": "object",
			"properties": {
				"id": {
					"type": "integer"
				},
				"name": {
					"type": "string"
				},
				"username": {
					"type": "string"
				},
				"email": {
					"type": "string",
					"format": "email"
				},
				"address": {
					"type": "object",
					"properties": {
						"street": {
							"type": "string"
						},
						"suite": {
							"type": "string"
						},
						"city": {
							"type": "string"
						},
						"zipcode": {
							"type": "string",
							"pattern": "^[0-9]{5}(-[0-9]{4})?$"
						},
						"geo": {
							"type": "object",
							"properties": {
								"lat": {
                                    "type": "string",
                                    "pattern": "^-?\\d+(\\.\\d+)?$" 
								},
								"lng": {
                                    "type": "string",
                                    "pattern": "^-?\\d+(\\.\\d+)?$" 
								}
							},
							"required": ["lat", "lng"]
						}
					},
					"required": ["street", "suite", "city", "zipcode", "geo"]
				},
				"phone": {
					"type": "string"
				},
				"website": {
					"type": "string"
				},
				"company": {
					"type": "object",
					"properties": {
						"name": {
							"type": "string"
						},
						"catchPhrase": {
							"type": "string"
						},
						"bs": {
							"type": "string"
						}
					},
					"required": ["name", "catchPhrase", "bs"]
				}
			},
			"required": ["id", "name", "username", "email", "address", "phone", "website", "company"]
            }
        }
    }
    
    # Validating data as per endpoints
    try:
        validate(instance=res_data, schema=schema_dict[endpoint])
        print("JSON data is valid.")
    except jsonschema.exceptions.ValidationError as e:
        print(f"JSON data is invalid: {e.message}")
        assert False


