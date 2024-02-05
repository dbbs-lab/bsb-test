import importlib
import pathlib


def get_test_config(name: str):
    from bsb.config import Configuration

    module = importlib.import_module(f".{name}", package=get_config.__module__)
    return Configuration(getattr(module, "tree"))


def get_all_test_configs():
    return [get_test_config(n) for n in list_test_configs()]


def list_test_configs():
    return [p.stem for p in pathlib.Path(__file__).parent.glob("*.py") if p.name != "__init__.py"]
