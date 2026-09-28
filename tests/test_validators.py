import pytest

from app.validators import safe_path


def test_plain_name_is_allowed():
    assert safe_path("/srv/uploads", "report.pdf") == "/srv/uploads/report.pdf"


def test_parent_directory_is_refused():
    with pytest.raises(ValueError):
        safe_path("/srv/uploads", "../etc/passwd")
