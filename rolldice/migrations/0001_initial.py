# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Advert'
        db.create_table(u'rolldice_advert', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('dice1', self.gf('django.db.models.fields.IntegerField')()),
            ('dice2', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'rolldice', ['Advert'])


    def backwards(self, orm):
        # Deleting model 'Advert'
        db.delete_table(u'rolldice_advert')


    models = {
        u'rolldice.advert': {
            'Meta': {'object_name': 'Advert'},
            'dice1': ('django.db.models.fields.IntegerField', [], {}),
            'dice2': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['rolldice']