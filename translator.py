import requests

def test_translate_to_spanish():
    # url = "https://translate.free.beeceptor.com/translation"
    url_postman = "https://01ab874a-b8f9-4252-9d82-5818920315d5.mock.pstmn.io/translate"
    params = {
        "query": "apple",
        "locale": "es-ES"
    }

    try:
        response = requests.get(url_postman, params=params)
    except requests.exceptions.RequestException as e:
        assert False, f"Request failed: {e}"

    assert response.status_code == 200, f"Expected status 200, got {response.status_code}"
    try:
        data = response.json()
    except ValueError as e:
        assert False, f"Response was not valid: {e}"

    assert "translation" in data, f"'translation' key not found in response"
    assert data["translation"] == "manzana", f"expected 'manzana' but got {data["translation"]} instead"

#todo:
#create repo on github
#create readme file with instructions for tester how to run the test
#find out what tools they use and replicate here








