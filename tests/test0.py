from src.plsl import Logging
from src.plsl.formating import datetime as time_only, message as message_only

"""

Simple test to use Logging Class.
Functions used:
    .info() -> Creates info log
    .debug() -> Creates debug log
    .warning() -> Creates warning log
    .error() -> Creates error log
    
Website: https://tory1103.github.io/pls-logging/
Documentation: https://tory1103.github.io/pls-logging/docs.html
Issues: https://github.com/tory1103/pls-logging/issues

"""

log = Logging()
log.info("info test")
log.warning("warning test", str_format=time_only)
log.debug("debug test", str_format=message_only)
log.error("error test", "2_args", str_format="{0} / {2} <--> {user}", user="test_user")
