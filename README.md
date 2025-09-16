Project:
Translation API Automation test

Tools used:
Postman - end point: https://01ab874a-b8f9-4252-9d82-5818920315d5.mock.pstmn.io/translate
Python 3
requests - for making HTTP calls
pytest - for running tests and assertions

Setup and test instructions: 
1. clone the repoository using the url: https://github.com/QAShell/AutomationAPIAssessment.git
2. run the test in solution or in terminal: pytest translator.py

Test objective:
Verify that the API returns the correct translation in Spanish to the word 'apple'

Expected output:
200 OK
"manzana"

Extra info:
-The mock API is hosted on Postman and is expected to respond to:
GET /translate?query=apple&locale=es-ES
-rate limits apply, in the event of the end point returning a 429 error code then set up a mock server and retest with new end point. 

