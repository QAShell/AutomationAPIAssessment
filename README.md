Project:
Translation API Automation test

Tools used:
1. Postman - end point to test: https://01ab874a-b8f9-4252-9d82-5818920315d5.mock.pstmn.io/translate
2. Python 3
3. Pycharm
4. requests - library for making HTTP calls
5. pytest - for running tests and assertions

Setup and test instructions: 
1. clone the repoository using the url: https://github.com/QAShell/AutomationAPIAssessment.git
2. run the test in solution or in terminal: pytest translator.py

Test objective:
Verify that the API returns the correct translation in Spanish to the word 'apple'

Expected output:
200 OK
"manzana"

Reporting:
1. in the terminal of solution install pip install pytest-html
2. run this command in the terminal: pytest translator.py --html=report.html --self-contained-html
3. a file url with html report will be generated

Extra info:
-The mock API is hosted on Postman and is expected to respond to:
GET /translate?query=apple&locale=es-ES
-rate limits apply, in the event of the end point returning a 429 error code then set up a mock server and retest with new end point. 

How to set up a new mock server and end point:
1. sign in or subscribe in postman
2. on the left panel click on Mock servers
3. click the + sign to create mock server
4. click radio button Create a new collection
5. give server name, should be a GET request, add url: query=apple&locale=es-ES, and put response body { "translation": "manzana" }, click create mock server
6. on left panel go to collections, you will see the new collection
7. within that will be the newly created GET request
8. test by clicking send, in the response body you should see 200 OK and { "translation": "manzana" }
9. to get the end point hover over the {{url}} and copy the url and paste to new browser, add this to the end /query=apple&locale=es-ES. Now you should see { "translation": "manzana" }
