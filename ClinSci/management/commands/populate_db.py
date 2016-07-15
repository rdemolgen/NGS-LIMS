#import from here so that django software recognises this as a management script
#__init__.py in the commands directory means the manage.py script looks here for scripts
#useage: python manage.py populate_db /home/sjccannon/Documents/lims_project/test_project/data/sample_list_all_anon.csv --sample_list
from django.core.management.base import BaseCommand

#import the models that are to be updated
from tngs_results.models import Sample_list
from ClinSci.models import Batch
import yaml

#model workspace to enable removal of hard coded paths
#class workspace():


#this is the nomenclature recognised by manage.py
class Command(BaseCommand):
    #documentation string
    help = 'handles computational input of data into database'

    sample_sheet_json = {}

    #function to add arguments to the command script to call with diffeent options
    def add_arguments(self, parser):
	#enables an input file to be specified and not hardcoded
        parser.add_argument('--input_file', default=False, nargs = '+', type=str)
        #add an  argument to specify tngs output integration to database - update all models
        parser.add_argument('--batch', action='store_true', dest='batch', default=False, help='parse and store each batch, sample, sample metrics test details, snp/indels, cnv_data')

    #test function to check the format of each smaple_list - hard coded so that it will alert if it is changed upstream in the pipeine
    #ensures the data is in the input file column that matches the database model column
    #e.g. the sample_id is in the column expected by the script
    #needs extending - possibly list comprehension
    def test_sample_list_format(self, header_list):
        required_header = ['sequencing_panel_version', 'capture_number', 'mody_number', 'ex_number', 'gender', 'profile', 'sample_type', 'comments']
        assert(header_list[0] == required_header[0]), "panel_list input error: put sequencing_panel_version in column 0"
        #check the list against each other: for item in list a check is at the same location. In list b.

#    def test_batch_instance(self):
        #check the number of lines in the yaml file is as expected
        #check each is in the correct order/or is there. load the yaml file to dictionary and check all headers are present
        #check the format of each header's values is as expected using regular expression or hardcoded where it does not change

#    def test_sample_instance(self):

#    def test_Ngs_test_instance(self):

#    def test_Sample_metrics_instance(self):

#    def test_variant_data_instance(self):

#    def test_cnv_data_instance(self):

    #manager function to read in the output results to the database.
    #try as one function to see if it updates correctly so data is linked
    #then split into individual functions and call using arguments and handler function
#    def update_tngs_results(self, filepath):
        #Batch instance as dict
        #Sample instances as dicts with pk from batch as foreign key
        #Ngs_test as dict
        #Sample_metrics as dict
        #Variant_data as dict
        #Cnv_data as dict

    #manager function to read in the output results to the database.
    def full_tngs_results(self, filepath):
        with open(filepath, 'r') as input:
            header_list = input.readline().strip('\n').split(',')
            #self.test_tngs_results_format(header_list) needs making

    def update_batch(self):
        #update fields from the config file
        with open('/home/sjccannon/Documents/lims_project/test_project/data/tngs_output_files/2016-05-22_1234678/scripts/configuration/config.yaml', 'r') as input_file:
            for i in range(1):
                first_line = input_file.readline()
            loaded_file = yaml.load(input_file)
        #store the sample list as a class variable JSON object {batch_id_from_yaml : [{'header_0' : 'value_0', 'header_1' :value_1 etc.},{'header_0' : 'value_0', 'header_1' :value_1 etc.}]} 
        sample_list_location = loaded_file['sample_list_path']
        with open('/home/sjccannon/Documents/lims_project/test_project/data/tngs_output_files/2016-05-22_1234678/scripts/configuration/sample_list_all.csv') as sample_list:
            header_list = sample_list.readline().strip(' \n\t\r').split(',')
            self.sample_sheet_json[loaded_file['batch_id']] = []
            for line in sample_list:
                sample_dict = {}
                strip_line = line.strip(' \n\t\r')
                line = strip_line.split(',')
                if line != ['']:
                    for key, value in zip(header_list, line):
                        sample_dict[key] = value
                    for v in self.sample_sheet_json.values():
                        v.append(sample_dict)
        batch_details = Batch(
            platform = loaded_file['sequencer_name'],
            batch_id = loaded_file['batch_id'],
            sample_list_path = loaded_file['sample_list_path'],
            sample_list = self.sample_sheet_json
            )
        #batch_details.save()
        batch_pk = batch_details.pk
        #try return batch_instance, pass to sample_model_update and when creating declare batch=batch_details
        return batch_details

    import glob

    #need to work out how to query the db before creating a new sample object
    def sample_model_update(self, batch_details):
        print(batch_details)
            #locate bam file
        for v in self.sample_sheet_json.values():
            print(v)
            for item in v:
                sample_instance = Sample(
                    capture_number = item['capture_number']
                    gender = item['gender']
                    comments = item['comments']
                    mody_number = item['mody_number']
                    ex_number = item['ex_number']
                    )
                 sample_instance.save()
                 sample_instance.add(batch_details)


    #handler function - handles the flags and executes the required functions
    def handle(self, *args, **options):
        if options['input_file'] and options['samples']:
            for file in options['input_file']:
                self.create_sample_list(file)
        elif options['input_file'] and options['filtered']:
            for file in options['input_file']:
                self.import_tngs_results(file)
        elif options['batch']:
            batch_details = self.update_batch()
            self.sample_model_update(batch_details)
