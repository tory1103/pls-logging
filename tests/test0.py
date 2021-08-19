from src.plsl import WebLogging

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

log = WebLogging()
log.info("info test")
log.warning("warning test", str_format=log.FMTS.TIME_ONLY)
log.debug("debug test", str_format=log.FMTS.MESSAGE_ONLY)
log.error("error test", "2_args", str_format="{0} / {2} <--> {user}", user="test_user")
