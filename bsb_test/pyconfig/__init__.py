import importlib


def get_config(name: str):
    from bsb.config import Configuration

    print(get_config.__module__)
    module = importlib.import_module(name, package=get_config.__module__)
    return Configuration(getattr(module, "tree"))
