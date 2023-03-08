from project0 import project0
import pytest
def test_incident_data():
    url = r"https://www.normanok.gov/sites/default/files/documents/2023-02/2023-02-09_daily_incident_summary.pdf"
    data = project0.fetchincidents(url)
    storedata=project0.extractIncidents(data)
    assert storedata is not None





