# Task 1: API Automation Using Requests 
    # Use the public API https://jsonplaceholder.typicode.com/posts
    # Write a Python script to:
        # Fetch all posts.
        # Validate that the response status code is 200.
        # Verify each post contains the keys: userId, id, title, body.
        # Save the first 5 posts into a local JSON file.


import requests
import json


url = 'https://jsonplaceholder.typicode.com/posts'
res = requests.get(url=url, timeout=2)

# Fetch all posts.
res_data = res.json()
print("Respose data : ",res_data)
print()

# Validate that the response status code is 200.
res_code = res.status_code
assert res_code==200
print("Respose code validation : ", res_code==200)
print()

# Verify each post contains the keys: userId, id, title, body.
post_len = len(res_data)
expected_keys = {'userId', 'id', 'title', 'body'}
post_count = 0
for post in res_data:
    key_flag = expected_keys.issubset(post.keys())
    if(key_flag):
        post_count = post_count + 1
print("Validation of keys : ", post_count==post_len)
print()

# Save the first 5 posts into a local JSON file.
with open("Post.json", "w") as final:
    json.dump(res_data[:5], final, indent=4)
