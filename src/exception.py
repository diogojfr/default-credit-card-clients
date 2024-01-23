import sys
from src.logger import logging

def error_message_detail(error, error_detail:sys):
    # get the error info from sys
    _,_,exc_tb = error_detail.exc_info()

    # get the file name where the error occured
    file_name = exc_tb.tb_frame.f_code.co_filename

    # get the line number where the error occured
    line_number=exc_tb.tb_lineno

    # return error message string
    error_message = "Error occured in python script name [{0}], line number [{1}] with the error message: [{2}]".format(file_name,line_number,str(error))

    return error_message



class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message
    

if __name__ == '__main__':
    try:
        a = 1/0
    except Exception as e:
        logging.info('An error occured')
        raise CustomException(e,sys)


