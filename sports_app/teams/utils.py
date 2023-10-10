from .models import Team, Match, Ranking
from django.db.models import Q


class PointsRankingCalculator:
    def calculate_point(self, team: Team):
        """
        Calculate the total points based on team
        """

        # query match related to team
        matches = Match.objects.filter(Q(home_team=team) | Q(away_team=team))
        total_points = 0

        # calculate point per match
        for match in matches:
            if match.home_team == team:
                if match.home_score > match.away_score:
                    total_points += 3
                elif match.home_score == match.away_score:
                    total_points += 1
            else:
                if match.away_score > match.home_score:
                    total_points += 3
                elif match.home_score == match.away_score:
                    total_points += 1

        # save into ranking table
        ranking, created = Ranking.objects.get_or_create(team=team)
        ranking.points = total_points
        ranking.save()

        return total_points


class RankingService:
    def __init__(self, points_ranking_calculator: PointsRankingCalculator):
        self.points_ranking_calculator = points_ranking_calculator

    def calculate_rankings(self):
        teams = Team.objects.all()
        for team in teams:
            self.points_ranking_calculator.calculate_point(team)

        # display ranking in JSON format
        rankings = Ranking.objects.all().order_by('-points', 'team')
        return rankings
