from django.test import TestCase

# Create your tests here.
# should get sleep list

sample_data = "Crazy Ones, 3, Rebels, 3"


def test_process_csv_match_input():
    response = "pass"
    assert response == 200
