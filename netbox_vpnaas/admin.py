from django.contrib import admin
from .models import (
    DNS, IPv4Routes, IPv6Routes, IPSecProfile, TLSProfile,
    Termination, RemoteAccessTunnel
)

@admin.register(DNS)
class DNSAdmin(admin.ModelAdmin):
    list_display = ['name', 'group', 'ipv4', 'description']
    list_filter = ['group']
    search_fields = ['name', 'ipv4']

@admin.register(IPv4Routes)
class IPv4RoutesAdmin(admin.ModelAdmin):
    list_display = ['name', 'group', 'description']
    list_filter = ['group']
    search_fields = ['name', 'description']

@admin.register(IPv6Routes)
class IPv6RoutesAdmin(admin.ModelAdmin):
    list_display = ['name', 'group', 'description']
    list_filter = ['group']
    search_fields = ['name', 'description']

@admin.register(IPSecProfile)
class IPSecProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'group', 'description']
    list_filter = ['group']
    search_fields = ['name', 'description']

@admin.register(TLSProfile)
class TLSProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'group', 'protocol', 'min_tls_version', 'max_tls_version', 'description']
    list_filter = ['group', 'protocol', 'min_tls_version', 'max_tls_version']
    search_fields = ['name', 'description']

@admin.register(Termination)
class TerminationAdmin(admin.ModelAdmin):
    list_display = ['name', 'group', 'type', 'description']
    list_filter = ['group', 'type']
    search_fields = ['name', 'description']

@admin.register(RemoteAccessTunnel)
class RemoteAccessTunnelAdmin(admin.ModelAdmin):
    list_display = ['name', 'group', 'technology', 'status', 'tenant', 'description']
    list_filter = ['group', 'technology', 'status', 'tenant']
    search_fields = ['name', 'description']
    filter_horizontal = ['terminations', 'tags', 'contacts']
