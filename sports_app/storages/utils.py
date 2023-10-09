from teams.models import Team, Match


class FileUploadService:
    def __init__(self, match_input: str):
        self.match_input = match_input

    def process_match_input(self):
        # read csv data
        match_list = self.match_input.split(",")

        # parse the input
        teams = {}
        for i in range(0, len(match_list), 2):
            team_name = match_list[i].strip()
            team_score = int(match_list[i + 1])
            teams[team_name] = team_score

        home_team, home_score = list(teams.items())[0]
        away_team, away_score = list(teams.items())[1]

        # register team
        team1, created = Team.objects.get_or_create(name=home_team)
        team2, created = Team.objects.get_or_create(name=away_team)

        # register match
        match, created = Match.objects.get_or_create(
            home_team=team1,
            home_score=home_score,
            away_team=team2,
            away_score=away_score,
        )

        return match.home_team
