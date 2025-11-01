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
  - https://github.com/adborden/k8s-uptime-kuma.git/uptime-kuma?ref=v1.0.0

images:
  - name: louislam/uptime-kuma
    newTag: 2.0.2
```

## Development

### Requirements

- [poetry](https://python-poetry.org/) 2.x
- [kustomize](https://kustomize.io/) 5.x
- [node.js](https://nodejs.org/) LTS
- [GNU Make](https://www.gnu.org/software/make/)

### Development workflow

Render your manifests for inspection.

    make build

Lint the code.

    make lint

Render the Kustomization.

    make test

We use snapshot based testing to validate the rendered manifests. If your tests are failing due to differences, please inspect these carefully. If changes are intentional, update the snapshots.

    make snapshot-update

## Releases

Releases are made automatically by CI on merge. Make sure to use [Conventional Commit](https://www.conventionalcommits.org/) syntax for your commit messages.
