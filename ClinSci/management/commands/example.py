import yaml

#import the model you want to update here

#open the input file
with open('config.yaml', 'r') as input_file:
    #skip first line/remove it from the file

    #load the file into a python dictionary
    input_file_dict = yaml.load(input_file)
    #print to check it is loaded correctly
    #create a variable that can be used to update the model
    sample_list_location = input_file_dict['sample_list_path']
    print(sample_list_location)
    #<variable_name> = <model_name>(<name_of_model_column> = <dictionary_variable_name>['what_its_called_in the dictionary']
    #update_batch_model = Batch(ftp_url = input_file_dict['ftp_url'])
    #update_batch_model.save()

