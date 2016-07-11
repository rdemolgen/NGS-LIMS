from django.db import models

#models each ngs batch
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
    sample_list_path = models.CharField(max_length=200, blank=True)
    #take path from .yaml file and store conents as JSON object in db
    sample_list = models.JSONField()

    def __str__(self):
        return self.batch_id

#one_to_many with Sample on proviso that sample has a surrogate key

#models each sample on each batch
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
      #write this in the test in the manage_db.py script
    bam_file_path = models.CharField(max_length=200, blank=True)

    #historic_sample_id
    #ex number
    #gender
    #date
    #dob

    #one to one with metrics
    #one to one with ngs_test

    def __str__(self):
        return self.


#models the ngs test used - method and version, if tngs the virtual panel phenotype, intervals covered
#and intervals for variant calling
class Ngs_test(models.Model):
    Ngs_test_primary_key = models.AutoField(primary_key=True) 
    capture_method = models.CharField(max_length=200, blank=True)
    capture_version = models.CharField(max_length=200, blank=True)
    virtual_panel_phenotype = models.CharField(max_length=200, blank=True)
    #format for gene panel = { 'panel_list' : '[gene_and_exon, gene_and_exon, ... ]'} 
    virtual_panel_genes_and_transcript = models.JSONField()
    date_of_analysis = models.CharField(max_length=200, blank=True)
    covered_interval_list_by_phenotype = models.JSONField()
    variant_calling_intervals = models.JSONField()
    sample = models.ForeignKey(Sample, on_delete=models.CASCADE)
    #to do this we need to read in the interval file as a JSON object (a dictionary essentially)
    #interval file comes in format: chrom,start,end,strand, gene_and_exon
    #json object as a dictionary of dictionaries where each dictionary states the target gene and exon and the targets associated
    #interval_dict = {{ 'gene_and_exon' : '<gene_and_exon>', 'bed_intervals' = ['<chrom>', 'start', 'end', 'strand']},{same_again}}
    #to minimise redeundancy, and only includethe targets relevant to the test we should only use the intervals of the test phenotype.
    #this will need to be put into the manager script an I think is e.g. v602_phenotype.code_metrics.interval_list
    #/mnt/Data1/targeted_sequencing/intervals/v5
    def __str__(self):
        return self.capture_version

#where overall is targeted capture and phen is virtual panel metrics
class Sample_metrics(models.Model):
    overall_metrics_path = models.CharField(max_length=200, blank=True)
    phenotype_metrics_path = models.CharField(max_length=200, blank=True)
    overall_pct_target_bases_20x = models.CharField(max_length=200, blank=True)
    overall_pct_target_bases_30x = models.CharField(max_length=200, blank=True)
    phen_pct_target_bases_20x = models.CharField(max_length=200, blank=True)
    phen_pct_target_bases_30x = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.phen_pct_target_bases_20x

#alamut annotated
#e.g. v501_nnnn_gender_phen.alamut.alltrans.txt
class Variant_data():

    def __str__(self):
        return self.


class Cnv_data():
#exomedepth_needs consideration stil
