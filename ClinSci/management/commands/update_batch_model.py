#python script to extract data from a yaml format, put it into a python dictionary format, and then save to a database based on a django model

#import modules
#import #yaml
#import #the class/model to be updated

#open the yaml file in read mode
    ##remove the first line##
    #create a variable that is an empty array
    #loop through each line in the file
        #add each line to the empty array
    #remove the first object from the array using del and list index(starts at 0)
    #open a new and temporary .yaml file in write mode
        #loop through each element in the array that doesn't have the first one
            #write each line to a new line in the yaml file (the temp file should look like the original without the first line)
    #load yaml file into python dictionary
    #print the yaml file to check it was read correctly
    #create updates to the Batch class/model in the following format
    #<variable_name> = <model_name>(<name_of_model_column> = <dictionary_variable_name>['what_its_called_in the dictionary']

