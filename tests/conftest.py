import os
import shutil
import subprocess
import re

import pytest


@pytest.fixture
def kustomize_snapshot(snapshot, request, tmp_path):
    def _kustomize_snapshot(example_name):
        test_name = request.node.name

        # Slugify the test_name for filesystem safety
        slugified_test_name = re.sub(r"[^\w-]", "_", test_name).rstrip("_")
        snapshot.snapshot_dir = os.path.join("tests/snapshots", slugified_test_name)

        # Create a temporary directory and copy the example files
        temp_dir = tmp_path / example_name
        shutil.copytree(os.path.join("examples", example_name), temp_dir)

        # Read the kustomization.yml from the temporary directory
        kustomization_path = temp_dir / "kustomization.yml"
        with open(kustomization_path, "r") as f:
            kustomization_content = f.read()

        # Get the absolute path to the project root and the uptime-kuma directory
        project_root = os.path.abspath(".")
        local_manifests_path_abs = os.path.join(project_root, "uptime-kuma")

        # Calculate the relative path from the temporary directory to the uptime-kuma directory
        relative_path = os.path.relpath(local_manifests_path_abs, temp_dir)

        # Use regex to replace the GitHub URL with the relative path, ignoring the ref
        modified_content = re.sub(
            r"https://github.com/adborden/k8s-uptime-kuma.git/uptime-kuma\?ref=.*",
            relative_path,
            kustomization_content,
        )

        # Write the modified kustomization.yml to the temporary directory
        with open(kustomization_path, "w") as f:
            f.write(modified_content)

        result = subprocess.run(
            ["kustomize", "build", str(temp_dir)],
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0

        snapshot.assert_match(
            result.stdout, os.path.join(example_name, "rendered.yaml")
        )

    return _kustomize_snapshot
