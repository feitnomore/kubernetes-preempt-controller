# kubeclient - Main API Handler
# Handles the interaction with Kubernetes.
# Most of the changes and updates are here.
#
# Marcelo Feitoza Parisi (marcelo@feitoza.com.br)

import urllib3
from helpers import globalholders
from helpers import logutil
from kubernetes import client
from kubernetes import config

# Loads configuration from Cluster
def loadConfig():
    try:
        # Disable SSL Warnings:
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

        # Load config from the Cluster (will use ServiceAccount)
        config.load_incluster_config()
        
        return True
        
    except Exception as e:
        logutil.printMessage("EXCEPTION - Kubeclient - " + str(e))
        return False

# Performs the API Connection
def connectApi():
    try:
        globalholders.coreApi = client.CoreV1Api()
        return True
    except Exception as e:
        logutil.printMesage("EXCEPTION - Kubeclient - " + str(e))
        return False
