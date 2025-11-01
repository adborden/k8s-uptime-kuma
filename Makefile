.PHONY: lint test

lint:
	yamllint .

test:
	kustomize build uptime-kuma
