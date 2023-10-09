from teams.models import Team, Match


class FileUploadService:
    def __init__(self, csv_file):
        self.csv_file = csv_file

    def validate_csv_file_exist(self):
        pass

    def process_csv_file(self):

        # read csv data
        # match_data = self.csv_file.read().decode('UTF-8')

        # for match in match_data:
        #     Match.objects.get_or_create()
        # register team

        # register match
        pass

    def process_csv_match_input(self):
        pass

        
