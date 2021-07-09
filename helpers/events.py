# events - Main Event Handler
# We monitor for events on Kubernetes. Here is the
# place were we are handling it.
# Events monitored are for Pods, and work is done
# on Pods that are in Shutdown
#
# Marcelo Feitoza Parisi (marcelo@feitoza.com.br)

from kubernetes import watch
from helpers import globalholders
from helpers import logutil

# This is the Handler
def launchHandler():
    w = watch.Watch()
    try: 
        while True:
            # Watching for event stream on Pods
            for event in w.stream(globalholders.coreApi.list_pod_for_all_namespaces):
                my_pod = event['object']
                # Check if Pod is Shutdown and Node not None
                if ( my_pod.metadata.namespace != "kube-system" and
                     my_pod.status.reason == "Shutdown" and
                     my_pod.status.phase == "Failed" and
                     my_pod.spec.node_name is not None
                    ):
                    message = "DELETING - pod: " + str(my_pod.metadata.name) + " namespace: " + str(my_pod.metadata.namespace) + " node: " + str(my_pod.spec.node_name)
                    logutil.printMessage(message)
                    try: 
                        deleted_pod = globalholders.coreApi.delete_namespaced_pod(my_pod.metadata.name, my_pod.metadata.namespace, grace_period_seconds=0)
                    except Exception as e:
                        # Pod probably lost
                        if ( str(e.reason) != "Not Found"):
                            logutil.printMessage("EXCEPTION PodDeletion - " + str(e.status) + " " + e.reason)

    except Exception as e:
        logutil.printMessage("EXCEPTION Watcher - " + str(e.status) + " " + e.reason)

