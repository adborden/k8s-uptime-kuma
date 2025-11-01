# Uptime Kuma Kubernetes deployment

This project provides Kustomize resources for deploying [Uptime Kuma](https://uptime.kuma.pet/).

## Usage

Render the manifests with Kustomize and apply them to your cluster:

    kubectl create namespace uptime-kuma
    kustomize build github.com/adborden/k8s-uptime-kuma.git//uptime-kuma | kubectl -n uptime-kuma apply -f -

If you need to Kustomize the deployment, you can include this Kustomization in your own:

```yaml
---
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization

namespace: uptime-kuma

resources:
  - https://github.com/adborden/k8s-uptime-kuma.git/uptime-kuma?ref=0.1.0

images:
  - name: louislam/uptime-kuma
    newTag: 2.0.2
```

## Development

Lint the code.

    make lint

Render the Kustomizeation.

    make test

## Releases

           ts

Releases are made automatically by CI on merge. Make sure to use [Conventional Commit](https://www.conventionalcommits.org/) syntax for your commit messages.
