import jsonpath
from Daraz_project.Base_Pages.Base_page import Api_base_page
from Daraz_project.Common import Constants

class productpage(Api_base_page):
    @staticmethod
    def extract_details(response):

        price = response['data']['module1']['products'][1]['price']
        actual_price = jsonpath.jsonpath(price, "originalPriceNumber")
        discount_price = jsonpath.jsonpath(price, 'priceNumber')
        title_rating = response['data']['module1']['products'][1]
        title = jsonpath.jsonpath(title_rating, 'title')
        rating = jsonpath.jsonpath(title_rating, 'ratingNumber')
        actual_value_greater_than_zero_and_integer = Api_base_page.verify_value_condition_and_type(actual_price)
        verify_product_title = Api_base_page.match_product_title(title)
        strings = [str(integer) for integer in actual_price]
        a_string = "".join(strings)
        actual_price_int = int(a_string)
        actual_price_greater_discount_price = Api_base_page.verify_discount_less_than_actual(actual_price_int, discount_price)
        rating_number = Api_base_page.verify_rating(rating)
        details = [actual_value_greater_than_zero_and_integer, verify_product_title, actual_price_greater_discount_price, rating_number]
        return details