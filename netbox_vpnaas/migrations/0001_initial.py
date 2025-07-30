from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('extras', '0002_custom_links'),
        ('ipam', '0001_initial'),
        ('tenancy', '0001_initial'),
        ('dcim', '0001_initial'),
        ('virtualization', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DNS',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict)),
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('group', models.CharField(blank=True, max_length=100)),
                ('ipv4', models.GenericIPAddressField(help_text='IPv4 DNS server address', protocol='IPv4')),
                ('description', models.CharField(blank=True, max_length=200)),
                ('tags', models.ManyToManyField(blank=True, to='extras.tag')),
            ],
            options={
                'verbose_name': 'DNS Server',
                'verbose_name_plural': 'DNS Servers',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='IPv4Routes',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict)),
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('group', models.CharField(blank=True, max_length=100)),
                ('ipv4_routes', models.TextField(help_text='IPv4 routes, one per line in CIDR format (e.g., 10.10.10.10/32)')),
                ('description', models.CharField(blank=True, max_length=200)),
                ('tags', models.ManyToManyField(blank=True, to='extras.tag')),
            ],
            options={
                'verbose_name': 'IPv4 Routes',
                'verbose_name_plural': 'IPv4 Routes',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='IPv6Routes',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict)),
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('group', models.CharField(blank=True, max_length=100)),
                ('ipv6_routes', models.TextField(help_text='IPv6 routes, one per line in CIDR format (e.g., ::/0)')),
                ('description', models.CharField(blank=True, max_length=200)),
                ('tags', models.ManyToManyField(blank=True, to='extras.tag')),
            ],
            options={
                'verbose_name': 'IPv6 Routes',
                'verbose_name_plural': 'IPv6 Routes',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='IPSecProfile',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict)),
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('group', models.CharField(blank=True, max_length=100)),
                ('setup', models.TextField(help_text='IPSec configuration setup')),
                ('description', models.CharField(blank=True, max_length=200)),
                ('tags', models.ManyToManyField(blank=True, to='extras.tag')),
            ],
            options={
                'verbose_name': 'IPSec Profile',
                'verbose_name_plural': 'IPSec Profiles',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='TLSProfile',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict)),
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('group', models.CharField(blank=True, max_length=100)),
                ('protocol', models.CharField(blank=True, choices=[('tcp', 'TCP'), ('udp', 'UDP')], help_text='Transport protocol', max_length=10)),
                ('min_tls_version', models.CharField(blank=True, choices=[('1.2', 'TLS 1.2'), ('1.3', 'TLS 1.3')], help_text='Minimum TLS version', max_length=10)),
                ('max_tls_version', models.CharField(blank=True, choices=[('1.2', 'TLS 1.2'), ('1.3', 'TLS 1.3')], help_text='Maximum TLS version', max_length=10)),
                ('setup', models.TextField(help_text='TLS configuration setup')),
                ('description', models.CharField(blank=True, max_length=200)),
                ('tags', models.ManyToManyField(blank=True, to='extras.tag')),
            ],
            options={
                'verbose_name': 'TLS Profile',
                'verbose_name_plural': 'TLS Profiles',
                'ordering': ['name'],
            },
        ),
        # Additional model creation operations would continue here...
    ]
