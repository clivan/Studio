from importlib.metadata import version

import studio
from studio import cli, core, gui, plugins


def test_package_import():
    assert studio.__name__ == "studio"
    assert all(m is not None for m in (core, plugins, gui, cli))


def test_version_matches_pyproject():
    assert version("studio") == "0.1.0"
