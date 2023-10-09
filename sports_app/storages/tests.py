import pytest
from .utils import FileUploadService

# Create your tests here.
# should get sleep list

sample_data = "Crazy Ones, 3, Rebels, 3"

@pytest.mark.django_db
def test_process_csv_match_input():
    response = FileUploadService(sample_data).process_match_input()
    assert response.name == "Crazy Ones"
