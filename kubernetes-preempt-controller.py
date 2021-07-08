# kubernetes-preempt-controller - Main Controller Module
# This is where we instantiate everything.
#
# Marcelo Feitoza Parisi (marcelo@feitoza.com.br)

import sys
from helpers import globalholders
from helpers import logutil
from helpers import kubeclient
from helpers import events

# Main :-)
def main():

    # Load Kubernetes API Configuration
    if(kubeclient.loadConfig() is False):
        logutil.printMessage("Error loading Kubernetes Config")
        sys.exit(1)

    # Create Kubernetes API Connection
    if(kubeclient.connectApi() is False):
        logutil.printMessage("Error connecting to Kubernetes API")
        sys.exit(1)

    # Launch our Event Monitor/Handler
    logutil.printMessage("Starting the event handler.")
    events.launchHandler()
    logutil.printMessage("Event handler terminated.")
    sys.exit(1)

if __name__ == '__main__':
    main()
