import pathlib
from pycli.config import settings


def test_project_root():
    assert isinstance(settings.PROJECT_ROOT, pathlib.Path)
    assert settings.PROJECT_ROOT.exists()


def test_timezone():
    assert settings.TIMEZONE == "UTC"


def test_api_key():
    assert settings.API_KEY == "secret1234567890"
