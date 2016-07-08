from django.db import models

# Create your models here.

class Batch(models.Model):
    #this all comes from the config.yaml file for each batch so assertions already in pipeline
    batch_primary_key = models.AutoField(primary_key=True)
    flowcell_id = models.CharField(max_length=200, blank=True)
    ftp_url = models.CharField(max_length=200, blank=True)
    batch_id = models.CharField(max_length=200, blank=True)
    platform = models.CharField(max_length=200, blank=True)
    java_path = models.CharField(max_length=200, blank=True)
    bwa_path = models.CharField(max_length=200, blank=True)
    picard_path = models.CharField(max_length=200, blank=True)
    gatk_path = models.CharField(max_length=200, blank=True)
    gatk_version = models.CharField(max_length=200, blank=True)
    reference_path = models.CharField(max_length=200, blank=True)
    known_indels_path = models.CharField(max_length=200, blank=True)
    common_variants_nkmi_path = models.CharField(max_length=200, blank=True)
    common_artefacts_path = models.CharField(max_length=200, blank=True)
    dbsnp_path = models.CharField(max_length=200, blank=True)
    alamut_path = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.batch_id

#one_to_many with Sample on proviso that sample has a surrogate key

class Sample(models.Model):
    #autoincrementing primary key
    sample_primary_key = models.AutoField(primary_key=True)
    #one_to_many with Batch i.e. each sample can only have one batch
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
    #this can be parsed from the assembly directory of each batch, will need to include some assertions to make sure
      #a we only get one bam file
      #b it is actually a correct filepath
      #c it is in the format we would expect - if it isn't get it any way but pring to screen that the bam format is
      #not as expected
    bam_file_path = models.CharField(max_length=200, blank=True)

#sample_id (surrogate_key_made_by_database - autoincrement)
#historic_sample_id
#ex number
#date
#dob

#one to onewith metrics

class Ngs_test(models.Model):
    capture_method = models.CharField(max_length=200, blank=True)
    capture_version = models.CharField(max_length=200, blank=True)
    virtual_panel_phenotype = models.CharField(max_length=200, blank=True)
    date_of_analysis = models.CharField(max_length=200, blank=True)

class test_interval_list(models.Model):
    interval_list_primary_key = models.AutoField(primary_key=True)
    Ngs_test = models.ForeignKey(Ngs_test, on_delete=models.CASCADE)
    #to do this we need to read in the interval file as a JSON object (a dictionary essentially)
    #comes in format: chrom,start,end,strand, gene_and_exon
    #interval_dict = { 'gene_and_exon' : 'gene_and_exon'
    #to minimise redeundancy, and only includethe targets relevant to the test we should only use the intervals of the test phenotype.
    #this will need to be put into the manager script an I think is e.g. v602_phenotype.code_metrics.interval_list
    interval_list = models.JSONField()
    variant_calling_intervals = models.JSONField()

class Sample_metrics(models.Model):
    sample_metrics_path = models.CharField(max_length=200, blank=True)
    phenotype_metrics_path = models.CharField(max_length=200, blank=True)
    sample_pct_target_bases_20x = models.CharField(max_length=200, blank=True)
    sample_pct_target_bases_30x = models.CharField(max_length=200, blank=True)
    phen_pct_target_bases_20x = models.CharField(max_length=200, blank=True)
    phen_pct_target_bases_30x = models.CharField(max_length=200, blank=True)

class Variant_data():
alamut annotated

class Cnv_data():
exomedepth_needs consideration stil
