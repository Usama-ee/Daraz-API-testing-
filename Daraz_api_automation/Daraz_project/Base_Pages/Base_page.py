import requests
import json
from Daraz_project.Common import Constants
import jsonpath

class Api_base_page:
    """
    Base page for all test apis
    """
    @staticmethod
    def request_headers():
        '''
        save all the request headers in the dictionary
        '''
        return {}

    @staticmethod
    def load_get_request(url):
        '''
        take url for the test cases and
        submit the response of the request
        '''
        return requests.get(url=url)

    def load_post_request(self,url,body):
        '''
        get url and take body return
        response of post request
        '''
        return requests.post(url=url , json=body , headers=self.request_headers())

    @staticmethod
    def get_code(response):
        '''
        return: status code of response
        '''
        return response.status_code


    @staticmethod
    def get_content(response):
        '''
        return: content of response
        '''
        return json.load(response.text)

    @staticmethod
    def get_header(response):
        '''
        return: response header
        '''
        return response.header


    @staticmethod
    def get_json_response(url):
        '''
        return json response
        '''
        response = requests.get(url=url)
        return response.json()

    @staticmethod
    def verify_value_condition_and_type(actual_price):
        '''
        for verify the value is valid and exist
        in response body return boolean output
        '''
        for value in actual_price:
            if value > 0 and isinstance(value, int):
                continue
            raise Exception(Constants.result_not_found.format(value))

        return True


    @staticmethod
    def match_product_title(name_list):
        '''
        Match the product title get from the
        response return boolean output
        name = title of product
        '''
        for title in name_list:
            if title == Constants.product_title:
                continue
            raise Exception(Constants.failed_to_match_value.format(title))

        return True

    @staticmethod
    def verify_discount_less_than_actual(actual_price,discounted_price_list):
        '''
        check the product actual price is less than
        discounted price of the product and is integer
        '''
        for discounted_value in discounted_price_list:
            if isinstance(discounted_value,int) and discounted_value < actual_price:
                continue
            raise Exception(Constants.result_not_found.format(discounted_value, actual_price))

        return True
    @staticmethod
    def verify_rating(rating):
        '''
        verify rating number is greater than and
        equal to 0
        '''
        for value in rating:
            if value >= 4.5:
                continue
            raise Exception(Constants.result_not_found.format(value))

        return True