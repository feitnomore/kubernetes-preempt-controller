# kubernetes-preempt-controller


**Maintainers:** [feitnomore](https://github.com/feitnomore/)

## BUILD

Here you can find some simple information on how to build this project by yourself.

### Clone the Repository
```sh
git clone https://github.com/feitnomore/kubernetes-preempt-controller.git
```

### Make your changes

*Note:* Remember to edit `Dockerfile` according to your changes. 

### Build the Image
```sh
cd kubernetes-preempt-controller
docker build -t kubernetes-preempt-controller .
```

### Push the image to the Repository
```sh
export MY_REPO="my_local_repository"
docker tag kubernetes-preempt-controller:latest $MY_REPO/kubernetes-preempt-controller:latest
docker push $MY_REPO/kubernetes-preempt-controller:latest
```
*Note:* Remember to set `MY_REPO`.  


### Create the Deployment Descriptor
Create a simple *Deployment.yaml* file:  
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: kubernetes-preempt-controller
  namespace: kube-system
  labels:
    k8s-app: kubernetes-preempt-controller
spec:
  selector:
    matchLabels:
      k8s-app: kubernetes-preempt-controller
  replicas: 1
  strategy:
    type: Recreate
  template:
    metadata:
      labels:
        k8s-app: kubernetes-preempt-controller
    spec:
      containers:
        - name: kubernetes-preempt-controller
          image: my_local_repository/kubernetes-preempt-controller:latest
          imagePullPolicy: Always
      serviceAccountName: kubernetes-preempt-controller
      restartPolicy: Always
```
*Note:* Remember to set the `image` to the repository you used in the last step.   

### Execute the Deployment
```sh
kubectl apply -f Deployment.yaml
```

*Note:* Remember to create the `ServiceAccount`, `ClusterRole` and `ClusterRoleBinding` before executing the `Deployment`. Check [examples](https://github.com/feitnomore/kubernetes-preempt-controller/tree/master/examples) for further information on the `ServiceAccount` and `ClusterRole`.
