# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Changeset'
        db.create_table(u'osmwatch_changeset', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('flag', self.gf('django.db.models.fields.BooleanField')()),
            ('ekip', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('osm_username', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('changesetid', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('editor', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('comment', self.gf('django.db.models.fields.TextField')()),
            ('datetime', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'osmwatch', ['Changeset'])


    def backwards(self, orm):
        # Deleting model 'Changeset'
        db.delete_table(u'osmwatch_changeset')


    models = {
        u'osmwatch.changeset': {
            'Meta': {'object_name': 'Changeset'},
            'changesetid': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'comment': ('django.db.models.fields.TextField', [], {}),
            'datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'editor': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'ekip': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'flag': ('django.db.models.fields.BooleanField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'osm_username': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['osmwatch']