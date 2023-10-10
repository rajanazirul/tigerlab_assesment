import pytest
from teams.models import Team
from storages.utils import FileUploadService
from teams.utils import PointsRankingCalculator, RankingService


sample_data = [
    ["Crazy Ones, 3, Rebels, 3"],
    ["Fantastics, 1, FC Super, 0"],
    ["Crazy Ones, 1, FC Super, 1"],
    ["Fantastics, 3, Rebels, 1"],
    ["Crazy Ones, 4, Misfits, 0"],
]


@pytest.mark.django_db
def test_points_ranking_calculator():
    # create match data
    for data in sample_data:
        FileUploadService(data[0]).process_match_input()

    team = Team.objects.get(name="Crazy Ones")

    point = PointsRankingCalculator().calculate_point(team)

    assert point == 5


@pytest.mark.django_db
def test_ranking_positioning():
    # create match data
    for data in sample_data:
        FileUploadService(data[0]).process_match_input()

    point = PointsRankingCalculator()
    rankings = RankingService(points_ranking_calculator=point).calculate_rankings()

    assert rankings[0]['points'] == 6
    assert rankings[4]['points'] == 0
