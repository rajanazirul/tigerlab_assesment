import pytest
from storages.utils import FileUploadService
import os
from sports_app.utils import read_csv_file

sample_data = "Crazy Ones, 3, Rebels, 3"


@pytest.mark.django_db
def test_process_csv_match_input():
    response = FileUploadService(sample_data).process_match_input()
    assert response.name == "Crazy Ones"


def test_process_csv_file():
    # Specify the filename with an absolute path from the root directory
    root_path = os.path.dirname(
        os.path.abspath(__file__)
    )  # Get the absolute path of the current script
    filename = os.path.join(root_path, "sample_input.csv")

    # Check if the CSV file exists
    assert os.path.isfile(filename)

    # Read CSV data
    data = read_csv_file(filename)

    # Check if the CSV has the expected number of rows
    expected_rows = 5  # Including the header row
    assert len(data) == expected_rows
