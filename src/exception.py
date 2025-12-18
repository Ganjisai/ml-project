import sys
import traceback
'''
how to use this exception in folder?
      import sys
from ml_project.exception import CustomException

def divide(a, b):
    try:
        return a / b
    except Exception as e:
        raise CustomException(str(e), sys)

    '''

import sys
from ml_project.logging import logger
class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = CustomException.get_detailed_error(
            error_message, error_detail
        )

        logger.error(self.error_message)

    @staticmethod
    def get_detailed_error(error_message, error_detail: sys):
        _, _, exc_tb = error_detail.exc_info()

        file_name = exc_tb.tb_frame.f_code.co_filename
        line_number = exc_tb.tb_lineno

        return (
            f"Error in file [{file_name}] "
            f"at line [{line_number}] "
            f"message: {error_message}"
        )

    def __str__(self):
        return self.error_message
