from netbox.filtersets import NetBoxModelFilterSet
from .models import (
    DNS, IPv4Routes, IPv6Routes, IPSecProfile, TLSProfile,
    Termination, RemoteAccessTunnel
)

class DNSFilterSet(NetBoxModelFilterSet):
    class Meta:
        model = DNS
        fields = ['id', 'name', 'group', 'ipv4']

class IPv4RoutesFilterSet(NetBoxModelFilterSet):
    class Meta:
        model = IPv4Routes
        fields = ['id', 'name', 'group']

class IPv6RoutesFilterSet(NetBoxModelFilterSet):
    class Meta:
        model = IPv6Routes
        fields = ['id', 'name', 'group']

class IPSecProfileFilterSet(NetBoxModelFilterSet):
    class Meta:
        model = IPSecProfile
        fields = ['id', 'name', 'group']

class TLSProfileFilterSet(NetBoxModelFilterSet):
    class Meta:
        model = TLSProfile
        fields = ['id', 'name', 'group', 'protocol', 'min_tls_version', 'max_tls_version']

class TerminationFilterSet(NetBoxModelFilterSet):
    class Meta:
        model = Termination
        fields = ['id', 'name', 'group', 'type']

class RemoteAccessTunnelFilterSet(NetBoxModelFilterSet):
    class Meta:
        model = RemoteAccessTunnel
        fields = ['id', 'name', 'group', 'technology', 'status', 'tenant']