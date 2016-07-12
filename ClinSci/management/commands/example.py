import yaml

#import the model you want to update here

def batch_model_update():
#open the input file
    with open('/home/sjccannon/Documents/lims_project/test_project/data/tngs_output_files/2016-05-22_1234678/scripts/configuration/config.yaml', 'r') as input_file:
    #skip first line/remove it from the file

    #load the file into a python dictionary
        input_file_dict = yaml.load(input_file)
    #print to check it is loaded correctly
    #create a variable that can be used to update the model
        sample_list_location = input_file_dict['sample_list_path']
        print(sample_list_location)
        with open('/home/sjccannon/Documents/lims_project/test_project/data/tngs_output_files/2016-05-22_1234678/scripts/configuration/sample_list_all.csv') as sample_list:
            header_list = sample_list.readline().strip(' \n\t\r').split(',')
            dict_for_json_dump = {input_file_dict['batch_id'] : []}
            for line in sample_list:
                sample_dict = {}
                strip_line = line.strip(' \n\t\r')
                line = strip_line.split(',')
                if line != ['']:
                    for key, value in zip(header_list, line):
                        sample_dict[key] = value
                    for v in dict_for_json_dump.values():
                        v.append(sample_dict)
                        print(v)
    #<variable_name> = <model_name>(<name_of_model_column> = <dictionary_variable_name>['what_its_called_in the dictionary']
    #update_batch_model = Batch(ftp_url = input_file_dict['ftp_url'])
    #update_batch_model.save()

import glob

def sample_model_update():
    path = '/home/sjccannon/Documents/lims_project/test_project/data/tngs_output_files/2016-05-22_1234678/assembly'
    bam_file = glob.glob(path + '/*realigned.bam') 
    print(bam_file)


batch_model_update()
sample_model_update()
