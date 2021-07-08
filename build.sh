#!/bin/sh
# Build and Exec
# I am too lazy to do this by hand

docker rm kubernetes-preempt-controller:1.0
docker rmi kubernetes-preempt-controller:1.0 --force
docker build -t kubernetes-preempt-controller:1.0 .

# Pushing to remote repository
export MY_REPO="feitnomore"
docker tag kubernetes-preempt-controller:1.0 $MY_REPO/kubernetes-preempt-controller:1.0
docker push $MY_REPO/kubernetes-preempt-controller:1.0

docker tag kubernetes-preempt-controller:1.0 $MY_REPO/kubernetes-preempt-controller:latest
docker push $MY_REPO/kubernetes-preempt-controller:latest
