from django.core.management.base import BaseCommand
from tngs_results.models import Sample_list

class Command(BaseCommand):
    help = 'handles computational input of data into database'

    def add_arguments(self, parser):
        parser.add_argument('input_file', nargs='+', type=str)
        parser.add_argument('--sample_list',action='store_true',dest='samples',default=False,help='initialize Sample_list class each row',)

    def test_sample_list_format(self, header_list):
        required_header = ['sequencing_panel_version', 'capture_number', 'mody_number', 'ex_number', 'gender', 'profile', 'sample_type', 'comments']
        assert(header_list[0] == required_header[0]), "panel_list input error: put sequencing_panel_version in column 0"
        #check the list against each other: for item in list a check is at the same location. In list b.

#    def test_tngs_results_format(self, header_list)

    def create_sample_list(self, filepath):
        with open(filepath, 'r') as input:
            header_list = input.readline().strip('\n').split(',')
            self.test_sample_list_format(header_list)
            for line in input:
                dict = {}
                strip_line = line.strip('\n')
                line = strip_line.split(',')
                for (key, value) in zip(header_list, line):
                    dict[key] = value
                list_entry = Sample_list(sequencing_panel_version = dict['sequencing_panel_version'], capture_number = dict['capture_number'], mody_number = dict['mody_number'], ex_number = dict['ex_number'], gender = dict['gender'], profile = dict['profile'], sample_type = dict['sample_type'], comments = dict['comments'])
                print(list_entry.ex_number + ' ' + list_entry.sequencing_panel_version)
                list_entry.save()

    #manager function to read in the output results to the database.
    def full_tngs_results(self, filepath):
        with open(filepath, 'r') as input:
            header_list = input.readline().strip('\n').split(',')
            #self.test_tngs_results_format(header_list) needs making

    def handle(self, *args, **options):
        if options['input_file'] and options['samples']:
            for file in options['input_file']:
                self.create_sample_list(file)
	elif options['input_file'] and options['filtered']:
            for file in options['input_file']:
                self.import_tngs_results(file)
