from django.core.management.base import BaseCommand
from tngs_results.models import *
'''
class Command(BaseCommand):
    args = '<foo bar ...>'
    help = 'insert help string'

#    def create_patient_entry(self, p_object):
#        new_patient =  Patient(patient_id=p_object.p_id, name=p_object.

#one to update patients, take that id then create an associated result:



p = Patient.objects.get(just_updated)

r = p.entry_set.create(
      [enter_args from json]

#to do this I need a json object that has all the data to satisfy the 
    def create_or_update_and_get(patient_model_class, results_class, json_data):
        get_or_create_kwargs = {
            model_class._meta.pk.name: json_data.pop(model_class._met.pk.name)
        }
        try:
            instance = model_class.objects.get(**get_or_create_kwargs)
        except model_class.DoesNotExist:
            print 'model does not exist please check json object'
        for key, value in json_data.items():
            field = model_class._meta.get_field(key)
            if not field:
                continue
            if isinstance(field, models.ManyToManyField):
                continue
            elif isinstance(field, models.ForeignKey) and hasattr(value, 'items'):
                rel_instance = create_or_update_and_get(field.rel.to, value)
                setattr(instance, key, rel_instance)
            else:
                setattr(instance, key, value)
        instance.save()
        for field in model_class._meta.many_to_many:
            if filed.name in json_data and hasattr(json_data[field.name], 'append'):
                for obj in json_data[field.name]:
                    rel_instance = create_or_update_and_get(field.rel.to, obj)
                    getattr(instance, filed.name).add(rel_instance)
        instance.save()

from django.utils.simplejson import simplejson as json

json_data = json.loads(json_file)
create_or_update_and_get(models.Patient, json_data)
'''
