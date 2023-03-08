from project0 import project0
def test_create_populateDatabase():
    # Define test input
    incidents = [
        ['2/9/2023 0:06', '2023-00002619', '301 E DALE ST', 'Falls', 'EMSSTAT'],
        ['2/9/2023 0:10', '2023-00001963', '2100 36TH AVE NW','Sick Person','14005'],
        ['2/9/2023 0:10', '2023-00002620', '2100 36TH AVE NW', 'Sick Person','EMSSTAT']
    ]

    # Call function under test
    result = project0.create_populateDatabase(incidents)

    # Check that the function returns the expected result
    assert result is None
