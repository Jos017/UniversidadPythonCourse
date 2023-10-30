# The logging module, defines functions and classes that helps us to implement
# flexible logs for applications and libraries

# The logging functions are the following:
# - Loggers expose the interface that application code directly uses
# - Handlers sed the log records (created by loggers) to the appropriate destination.
# - Filters provide a finer grained facility for determining which log records to output.
# - Formatters specify the layout of log records in the final output.

import logging as log
import os

# There are multiple leves of logs
# - NOTSET (0)      => Shows all logs
# - DEBUG (10)      => Detailed info to diagnose a problem
# - INFO (20)       => Confirmation that this are working as expected
# - WARNING (30)    => An indication that something unexpected happened
# - ERROR (40)      => More serious problem, some function did not perform
# - CRITICAL (50)   => Serious error, the program cannot continue

file_path = os.path.abspath(__file__)
dir_path = os.path.dirname(file_path)

log.basicConfig(
    # When the level is set the logs that are shown are the selected level and higher
    # The log level by default is WARNING
    level=log.DEBUG,
    # Format to the logs can be applied
    format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
    # Format the date time
    datefmt='%H:%M:%S',
    # Handles log data
    handlers=[
        # Write logs to file
        log.FileHandler(os.path.join(dir_path, 'data_layer.log')),
        # Write logs to a stream
        log.StreamHandler()
    ]
)

if __name__ == '__main__':

    print(os.path.abspath(__file__))
    print(os.path.dirname(os.path.abspath(__file__)))
    log.debug('Debug level message')
    log.info('Info level message')
    log.warning('Warning level message')
    log.error('Error level message')
    log.critical('Critical level message')
