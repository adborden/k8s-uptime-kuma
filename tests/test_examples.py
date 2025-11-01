import os

import pytest


def get_example_dirs():
    """Get a list of examples from the examples directory for validation."""
    examples_dir = "examples"
    return [
        name
        for name in os.listdir(examples_dir)
        if os.path.isdir(os.path.join(examples_dir, name))
    ]


@pytest.mark.parametrize("example", get_example_dirs())
def test_examples(example, kustomize_snapshot):
    """Assert the example manifests render as expected."""
    kustomize_snapshot(example)
