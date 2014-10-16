# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'CityDetail'
        db.create_table(u'osmwatch_citydetail', (
            (u'city_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cities.City'], unique=True, primary_key=True)),
            ('min_lat', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('max_lon', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('min_lon', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('max_lat', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'osmwatch', ['CityDetail'])


    def backwards(self, orm):
        # Deleting model 'CityDetail'
        db.delete_table(u'osmwatch_citydetail')


    models = {
        u'cities.alternativename': {
            'Meta': {'object_name': 'AlternativeName'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_colloquial': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_preferred': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_short': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        u'cities.city': {
            'Meta': {'object_name': 'City'},
            'alt_names': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['cities.AlternativeName']", 'symmetrical': 'False'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cities.Country']"}),
            'elevation': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kind': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'location': ('django.contrib.gis.db.models.fields.PointField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'db_index': 'True'}),
            'name_std': ('django.db.models.fields.CharField', [], {'max_length': '200', 'db_index': 'True'}),
            'population': ('django.db.models.fields.IntegerField', [], {}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cities.Region']", 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'subregion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cities.Subregion']", 'null': 'True', 'blank': 'True'}),
            'timezone': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        u'cities.country': {
            'Meta': {'ordering': "['name']", 'object_name': 'Country'},
            'alt_names': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['cities.AlternativeName']", 'symmetrical': 'False'}),
            'area': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'capital': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '2', 'db_index': 'True'}),
            'code3': ('django.db.models.fields.CharField', [], {'max_length': '3', 'db_index': 'True'}),
            'continent': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'currency': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True'}),
            'currency_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'languages': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'db_index': 'True'}),
            'neighbours': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'neighbours_rel_+'", 'to': u"orm['cities.Country']"}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'population': ('django.db.models.fields.IntegerField', [], {}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'tld': ('django.db.models.fields.CharField', [], {'max_length': '5'})
        },
        u'cities.region': {
            'Meta': {'object_name': 'Region'},
            'alt_names': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['cities.AlternativeName']", 'symmetrical': 'False'}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '200', 'db_index': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cities.Country']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'db_index': 'True'}),
            'name_std': ('django.db.models.fields.CharField', [], {'max_length': '200', 'db_index': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'cities.subregion': {
            'Meta': {'object_name': 'Subregion'},
            'alt_names': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['cities.AlternativeName']", 'symmetrical': 'False'}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '200', 'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'db_index': 'True'}),
            'name_std': ('django.db.models.fields.CharField', [], {'max_length': '200', 'db_index': 'True'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cities.Region']"}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
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
        },
        u'osmwatch.citydetail': {
            'Meta': {'object_name': 'CityDetail', '_ormbases': [u'cities.City']},
            u'city_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['cities.City']", 'unique': 'True', 'primary_key': 'True'}),
            'max_lat': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'max_lon': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'min_lat': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'min_lon': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['osmwatch']