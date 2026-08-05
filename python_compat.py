import pkgutil
import importlib.util


def patch_pkgutil_find_loader() -> None:
    if hasattr(pkgutil, "find_loader"):
        return

    def find_loader(name):
        spec = importlib.util.find_spec(name)
        return None if spec is None else getattr(spec, "loader", None)

    pkgutil.find_loader = find_loader  # type: ignore[attr-defined]
