from django.db import models

# Create your models here.

class Batch():
flowcell_id (scripts/config/config.yaml) - run data from config.ymal
batch_id
project_number
platform
software versions e.g. alamut etc
filtering steps

one_to_many with Sample on proviso that sample has a surrogate key

class Sample():
sample_id (surrogate_key_made_by_database - autoincrement)
historic_sample_id
ex number
date
dob

one to onewith metrics

class Sample_metrics():
sample_metrics_id
pct_target_bases_20x
"" 		30x

class Variant_data():
alamut annotated

class Cnv_data():
exomedepth_needs consideration stil
