import requests
import json
import jsonpath
from Daraz_project.Common import Constants
from Daraz_project.Base_Pages.Base_page import Api_base_page
from Daraz_project.Api_executation.Pages.Product_page import productpage


class TestProductPageDetails:
    '''
    run two test for check the response
    '''
    def test_verify_for_first_product(self):
        product = productpage()
        response = product.load_get_request(Constants.first_product_api)
        statuscode = product.get_code(response)
        assert statuscode == Constants.STATUS_CODE_200
        return True

    def test_verify_for_second_product(self):
        product = productpage()
        response = product.load_get_request(Constants.second_product_api)
        statuscode = product.get_code(response)
        assert statuscode == Constants.STATUS_CODE_200
        json_response = product.get_json_response(Constants.second_product_api)
        details = product.extract_details(json_response)
        return details
