#!/bin/sh
# Build and Exec
# I am too lazy to do this by hand

docker rm kubernetes-preempt-controller:1.1
docker rmi kubernetes-preempt-controller:1.1 --force
docker build -t kubernetes-preempt-controller:1.1 .

# Pushing to remote repository
export MY_REPO="feitnomore"
docker tag kubernetes-preempt-controller:1.1 $MY_REPO/kubernetes-preempt-controller:1.1
docker push $MY_REPO/kubernetes-preempt-controller:1.1

docker tag kubernetes-preempt-controller:1.1 $MY_REPO/kubernetes-preempt-controller:latest
docker push $MY_REPO/kubernetes-preempt-controller:latest
