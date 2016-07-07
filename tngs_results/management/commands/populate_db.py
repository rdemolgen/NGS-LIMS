#import from here so that django software recognises this as a management script
#__init__.py in the commands directory means the manage.py script looks here for scripts
#useage: python manage.py populate_db /home/sjccannon/Documents/lims_project/test_project/data/sample_list_all_anon.csv --sample_list
from django.core.management.base import BaseCommand

#import the models that are to be updated
from tngs_results.models import Sample_list

#this is the nomenclature recognised by manage.py
class Command(BaseCommand):
    #documentation string
    help = 'handles computational input of data into database'

    #function to add arguments to the command script to call with diffeent options
    def add_arguments(self, parser):
	#enables an input file to be specified and not hardcoded
        parser.add_argument('input_file', nargs='+', type=str)
	#specifies the type of input file as a sample_list
        parser.add_argument('--sample_list',action='store_true',dest='samples',default=False,help='initialize Sample_list class each row',)

    #test function to check the format of each smaple_list - hard coded so that it will alert if it is changed upstream in the pipeine
    #ensures the data is in the input file column that matches the database model column
    #e.g. the sample_id is in the column expected by the script
    #needs extending - possibly list comprehension
    def test_sample_list_format(self, header_list):
        required_header = ['sequencing_panel_version', 'capture_number', 'mody_number', 'ex_number', 'gender', 'profile', 'sample_type', 'comments']
        assert(header_list[0] == required_header[0]), "panel_list input error: put sequencing_panel_version in column 0"
        #check the list against each other: for item in list a check is at the same location. In list b.

#    def test_tngs_results_format(self, header_list)

    #function to read each line of the sample list file and update the database with one entry per line/sample
    def create_sample_list(self, filepath):
        #opens file for reading only
        with open(filepath, 'r') as input:
            #reads the first line, removes new line characters, splits by comma
            header_list = input.readline().strip('\n').split(',')
            #calls the test function to test the format of the input
            self.test_sample_list_format(header_list)
            #iterates through every other line in the input
            for line in input:
                #creates an empty dictionary to be updated
                dict = {}
                #strips newline characters
                strip_line = line.strip('\n')
                #splits by comma - could turn this into a function to reduce redundant code
                line = strip_line.split(',')
                #use the zip method to creat an array of tuples where the nth header list iterable
                #is paired with the nth line iterable
                for (key, value) in zip(header_list, line):
                    #update the dictionary to contain the header as the key and the column contents on that line
                    #as the value
                    dict[key] = value
                #crete a Sample_list instance (as specified by the imported class from model.py) based on the
                #parsed input data
                list_entry = Sample_list(sequencing_panel_version = dict['sequencing_panel_version'], capture_number = dict['capture_number'], mody_number = dict['mody_number'], ex_number = dict['ex_number'], gender = dict['gender'], profile = dict['profile'], sample_type = dict['sample_type'], comments = dict['comments'])
                #prints to screen the ex number and panel version of the created Sample_list object
                #(one for each line in the file) - this is possible because of the def __str__ function
                print(list_entry.ex_number + ' ' + list_entry.sequencing_panel_version)
                #djando syntax for saving the object instance into the database
                list_entry.save()

    #manager function to read in the output results to the database.
    def full_tngs_results(self, filepath):
        with open(filepath, 'r') as input:
            header_list = input.readline().strip('\n').split(',')
            #self.test_tngs_results_format(header_list) needs making

    #handler function - handles the flags and executes the required functions
    def handle(self, *args, **options):
        if options['input_file'] and options['samples']:
            for file in options['input_file']:
                self.create_sample_list(file)
        elif options['input_file'] and options['filtered']:
            for file in options['input_file']:
                self.import_tngs_results(file)
