import yaml
from ClinSci.models import Batch

with open('../../../data/tngs_output_files/2016-05-22_1234678/scripts/configuration/config.yaml', 'r') as input_file:
    for i in range(1):
        _ = input_file.readline()
    loaded_file = yaml.load(input_file)
#    print (loaded_file)
    batch_details = Batch(
	platform = loaded_file['sequencer_name'],
	batch_id = loaded_file['batch_id'],
	sample_list_path = loaded_file['sample_list_path']
    )
print(batch_details)
