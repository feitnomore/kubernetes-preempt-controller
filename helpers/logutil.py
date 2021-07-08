# logutil - Main Log Handler
# Helpers to print our status to the stdout, as well
# as saving termination-log.
#
# Marcelo Feitoza Parisi (marcelo@feitoza.com.br)

import datetime
from helpers import globalholders

# This is responsible for general message printing to stdout
def printMessage(message):
    # Getting the actual date/time
    my_time = datetime.datetime.now().strftime("%a %Y-%m-%d %H:%M:%S")
    # Print the log to the console
    print("[%s] %s" % (str(my_time), str(message)))
