#  Task 1: API Automation Using Requests
  Use the public API https://jsonplaceholder.typicode.com/posts
  Write a Python script to:
    1.  Fetch all posts.
    2.  Validate that the response status code is 200.
    3.  Verify each post contains the keys: userId, id, title, body.
    4.  Save the first 5 posts into a local JSON file.


#  Task 2 : Pytest Test Suite
  Create a Pytest test suite for the API in Section A.
  Cover:
    -  Response time < 2 seconds
    -  Schema validation (use pydantic or jsonschema)
    -  Parameterized test: Validate multiple endpoints (e.g., /posts, /comments, /users).
  Ensure the suite can be executed with pytest -v.


#  Task 3: Postman Automation
  Create a Postman collection with the following:
    1.  GET /posts – validate status = 200.
    2.  POST /posts – create a new post and verify the response contains the same title/body.
    3.  DELETE /posts/{id} – verify response status 200 or 204.
  Add test scripts in Postman to validate responses.
  Export and submit the Postman collection JSON file.


#  Task 4 : Selenium with Pytest or Pytest Playwright automation
    https://rahulshettyacademy.com/AutomationPractice/
    
  Select any elements and write Playwright code.


#  Task 5: Strategy & Leadership (Short Answers)
   1.  You are leading a team of 4 QA engineers. The sprint velocity is dropping due to flaky automation tests. How will you handle this situation?
   2.  During production release, you find 2 critical bugs reported by the client that were missed in QA. What’s your approach to fix gaps in process and testing?




