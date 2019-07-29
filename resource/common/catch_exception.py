import functools
from resource.common import output
from resource.extension.log import logging

def catch_exception(func,*args, **kwargs):
    '''
    :param func:
    :return:
    '''

    @functools.wraps(func, *args, **kwargs)
    def catch(request, *args, **kwargs):
        try:
            back = func(request, *args, **kwargs)
            return back
        except Exception as e:
            logging.error(str(e))
            return output.ErrorResponse(msg=str(e))


    return catch
