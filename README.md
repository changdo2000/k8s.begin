# k8s.begin

# 1. Install minikube

``` bash
    curl -LO https://github.com/kubernetes/minikube/releases/latest/download/minikube-linux-amd64
    sudo install minikube-linux-amd64 /usr/local/bin/minikube && rm minikube-linux-amd64
```

# 2. Install kube command line
``` bash
    sudo apt-get update
    sudo apt-get install -y apt-transport-https ca-certificates curl

    sudo curl -fsSLo /usr/share/keyrings/kubernetes-archive-keyring.gpg \
    https://packages.cloud.google.com/apt/doc/apt-key.gpg

    echo "deb [signed-by=/usr/share/keyrings/kubernetes-archive-keyring.gpg] \
    https://apt.kubernetes.io/ kubernetes-xenial main" | \
    sudo tee /etc/apt/sources.list.d/kubernetes.list

    sudo apt-get update
    sudo apt-get install -y kubectl
```
# 3. Start cluster

``` bash
    minikube start
```

# 4. Get nodes

``` bash
    kubectl get nodes
```


