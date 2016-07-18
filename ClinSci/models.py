from django.contrib.postgres.fields import JSONField
from django.db import models

# sample - batch = many_many
# sample - test = many_many
# test - cov_metrics = one_many
# test - snps_results = one_many
# test - cnv_results = one_many

# models each ngs batch
class Batch(models.Model):
    # this all comes from the config.yaml file for each batch so assertions already in pipeline
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
    profile = ManyToManyField(Sample, through='Profile')
    # take path from .yaml file and store contents as JSON object in db
    sample_list = JSONField()

    def __str__(self):
        return self.batch_id

# one_to_many with Sample, proviso that sample has a surrogate key
# May need to make many-many to so one sample can have many batches + test

# models each sample on each batch
class Sample(models.Model):
    # many_to_many with Batch i.e. each sample can be put on multiple batches - sample synonymous with person
    sample_primary_key = models.AutoField(primary_key=True)
    # batch = models.ManyToManyField(Batch)
    bam_file_path = models.CharField(max_length=200, blank=True)
    capture_number = models.CharField(max_length=10, blank=True)
    mody_number = models.CharField(max_length=200, blank=True)
    ex_number = models.CharField(max_length=200, blank=True)
    gender = models.CharField(max_length=200, blank=True)
    comments = models.CharField(max_length=200, blank=True)
    # one to many with Ngs_test

    def __str__(self):
        return self.capture_number

# models the ngs test used - method and version, if tngs the virtual panel phenotype, intervals covered
# and intervals for variant calling
class Profile(models.Model):
    Ngs_test_primary_key = models.AutoField(primary_key=True)
    capture_method = models.CharField(max_length=200, blank=True)
    capture_version = models.CharField(max_length=200, blank=True)
    capture_profile = models.CharField(max_length=200, blank=True)
    # format for gene panel = { 'panel_list' : '[gene_and_exon, gene_and_exon, ... ]'}
    virtual_panel_genes_and_transcript = JSONField()
    date_of_analysis = models.CharField(max_length=200, blank=True)
    covered_interval_list_by_phenotype = JSONField()
    variant_calling_intervals = JSONField()
    batch = models.ForeignKey(Batch)
    sample = models.ForeignKey(Sample, on_delete=models.CASCADE)
    # to do this we need to read in the interval file as a JSON object (a dictionary essentially)
    # interval file comes in format: chrom,start,end,strand, gene_and_exon
    # json object as a dictionary of dictionaries where each dictionary states the target gene and exon and the targets associated
    # interval_dict = {{ 'gene_and_exon' : '<gene_and_exon>', 'bed_intervals' = ['<chrom>', 'start', 'end', 'strand']},{same_again}}
    # to minimise redeundancy, and only includethe targets relevant to the test we should only use the intervals of the test phenotype.
    # this will need to be put into the manager script an I think is e.g. v602_phenotype.code_metrics.interval_list
    # /mnt/Data1/targeted_sequencing/intervals/v5
    def __str__(self):
        return self.capture_version

# where overall is targeted capture and phen is virtual panel metrics
class Ngs_test_metrics(models.Model):
    overall_metrics_path = models.CharField(max_length=200, blank=True)
    phenotype_metrics_path = models.CharField(max_length=200, blank=True)
    overall_pct_target_bases_20x = models.CharField(max_length=200, blank=True)
    overall_pct_target_bases_30x = models.CharField(max_length=200, blank=True)
    phen_pct_target_bases_20x = models.CharField(max_length=200, blank=True)
    phen_pct_target_bases_30x = models.CharField(max_length=200, blank=True)
    # one-one with ngs_test

    def __str__(self):
        return self.phen_pct_target_bases_20x

# where information is taken from .alamut.alltrans.txt filetaken from each sample
# e.g. v501_nnnn_gender_phen.alamut.alltrans.txt

class Variant_data():
    chrom = models.IntegerField()
    gene = models.CharField(max_length=200, blank=True)
    pos = models.IntegerField()
    transcript = models.CharField(max_length=200, blank=True)
    varType = models.CharField(max_length=200, blank=True)
    codingEffect = models.CharField(max_length=200, blank=True)
    varLocation = models.CharField(max_length=200, blank=True)
    assembly = models.CharField(max_length=200, blank=True)
    gDNAstart = models.IntegerField()
    gDNAend = models.IntegerField()
    gNomen = models.CharField(max_length=200, blank=True)
    sample = models.ForeignKey(Sample)

    def __str__(self):
        return self.pos


# class Cnv_data():
# exomedepth_needs consideration still

# Joining the sample and the batch together via the profile (test used)
