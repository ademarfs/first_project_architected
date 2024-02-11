from typing import Dict
from src.drivers.barcode_handler import BarcodeHandler

class TagCreatorController:
    '''
    responsability for implementing business rules
    '''
    def create(self, product_code: str) -> Dict:
        path_from_tag = self.__create__tag(product_code)
        formatted_response = self.__format__response(path_from_tag)
        return (formatted_response)

    def __create__tag(self, product_code: str) -> str:
        barcode_handler = BarcodeHandler()
        path_from_tag = barcode_handler.create_barcode(product_code)
        return path_from_tag
    
    def __format__response(self, path_from_tag: str) -> Dict:
        return {
            "data": {
                "type": "Tag_image",
                "count": 1,
                "path": f'{path_from_tag}.png'
            }
        }