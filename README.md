# kubernetes-preempt-controller


**Maintainers:** [feitnomore](https://github.com/feitnomore/)

This is a simple hack to implement a controller for [Kubernetes](https://kubernetes.io) responsible for deleting `Pods` that are in `Shutdown` status due to a `Node` preemption.

*WARNING:* Use it at your own risk.

## INTRODUCTION

The idea of this Controller is to be able to clear the list of `Pods` in the cluster by deleting the `Pods` that were left in `Shutdown` status due to a `Node` preemption.
The Controller watches for `Events` of type `Pod`. 

## HOW TO INSTALL IT

The details below assume you are creating a `ServiceAccount`, a `ClusterRole`, a `ClusterRoleBinding`, a `Deployment` and a `Pod`, all on the *kube-system* `Namespace`. Please, adjust as necessary.  
*Note:* We are adding `patch, get, watch, list, update, delete` as verbs on `Pods` as well as `get, watch, list` verbs on `Nodes` for the `ClusterRole` we are creating.

### Create a Service Account
```sh
$ kubectl apply -f https://raw.githubusercontent.com/feitnomore/kubernetes-prempt-controller/master/examples/kubernetes-preempt-controller_ServiceAccount.yaml
```
### Create the Cluster Role
```sh
$ kubectl apply -f https://raw.githubusercontent.com/feitnomore/kubernetes-preempt-controller/master/examples/kubernetes-preempt-controller_ClusterRole.yaml
```
### Create the Cluster Role Binding
```sh
$ kubectl apply -f https://raw.githubusercontent.com/feitnomore/kubernetes-preempt-controller/master/examples/kubernetes-preempt-controller_ClusterRoleBinding.yaml
```

### Apply the Deployment
```sh
$ kubectl apply -f https://raw.githubusercontent.com/feitnomore/kubernetes-preempt-controller/master/examples/kubernetes-preempt-controller_Deployment.yaml
```


### Verify the Controller Logs
```sh
PVM_CONTROLLER=`kubectl get pods -n kube-system | grep kubernetes-preempt-controller | awk '{print $1}'`
kubectl logs $PVM_CONTROLLER -n kube-system
```
*Note:* the Controller is running on *kube-system* `Namespace`.  


## REFERENCES AND IDEAS

1. [Kubernetes](https://kubernetes.io/)
2. [Python 2.7](https://www.python.org/)
3. [Kubernetes Python Client](https://github.com/kubernetes-client/python)
4. [Docker Hub](https://hub.docker.com/r/feitnomore/kubernetes-preempt-controller/)

## DOCUMENTATION

1. [Building](https://github.com/feitnomore/kubernetes-preempt-controller/blob/master/BUILD.md)


