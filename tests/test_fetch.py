from project0 import project0
import pytest

def test_fetchincident ():
    url = "https://www.normanok.gov/sites/default/files/documents/2023-02/2023-02-09_daily_incident_summary.pdf"
    data = project0.fetchincidents(url)
    assert data != b""
