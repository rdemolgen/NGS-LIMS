from django.db import models

# Create your models here.
class Sample_list(models.Model):
    sequencing_panel_version = models.CharField(max_length=100, blank=True)
    capture_number = models.CharField(max_length=100, blank=True)
    mody_number = models.CharField(max_length=100, blank=True)
    ex_number = models.CharField(max_length=100, blank=True)
    gender = models.CharField(max_length=100, blank=True)
    profile = models.CharField(max_length=100, blank=True)
    sample_type = models.CharField(max_length=100, blank=True)
    comments = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.ex_number

#class Al_batch_output(models.Models):

#class Coverage_by_base(models.Model):
#    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
#    chromosome = models.CharField(max_length=2)
#    genomic_coordinate = models.CharField(max_length=30)
#    depth_of_coverage = models.CharField(max_length=30)

#    def __str__(self):
#        cov = self.chromosome + ' ' + self.genomic_coordinate + ' ' + self.depth_of_coverage
#        return cov
