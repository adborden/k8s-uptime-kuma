.PHONY: build lint setup snapshot-update test

build:
	kustomize build uptime-kuma

lint:
	yamllint .

setup:
	npm install
	poetry install

snapshot-update:
	poetry run pytest --snapshot-update

test:
	poetry run pytest
