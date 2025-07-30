from rest_framework import serializers
from netbox.api.serializers import NetBoxModelSerializer
from ..models import (
    DNS, IPv4Routes, IPv6Routes, IPSecProfile, TLSProfile, 
    Termination, RemoteAccessTunnel
)


class DNSSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_vpnaas-api:dns-detail'
    )

    class Meta:
        model = DNS
        fields = [
            'id', 'url', 'display', 'name', 'group', 'ipv4', 'description',
            'created', 'last_updated', 'custom_fields', 'tags'
        ]


class IPv4RoutesSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_vpnaas-api:ipv4routes-detail'
    )

    class Meta:
        model = IPv4Routes
        fields = [
            'id', 'url', 'display', 'name', 'group', 'ipv4_routes', 'description',
            'created', 'last_updated', 'custom_fields', 'tags'
        ]


class IPv6RoutesSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_vpnaas-api:ipv6routes-detail'
    )

    class Meta:
        model = IPv6Routes
        fields = [
            'id', 'url', 'display', 'name', 'group', 'ipv6_routes', 'description',
            'created', 'last_updated', 'custom_fields', 'tags'
        ]


class IPSecProfileSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_vpnaas-api:ipsecprofile-detail'
    )

    class Meta:
        model = IPSecProfile
        fields = [
            'id', 'url', 'display', 'name', 'group', 'setup', 'description',
            'created', 'last_updated', 'custom_fields', 'tags'
        ]


class TLSProfileSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_vpnaas-api:tlsprofile-detail'
    )

    class Meta:
        model = TLSProfile
        fields = [
            'id', 'url', 'display', 'name', 'group', 'protocol', 
            'min_tls_version', 'max_tls_version', 'setup', 'description',
            'created', 'last_updated', 'custom_fields', 'tags'
        ]


class TerminationSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_vpnaas-api:termination-detail'
    )

    class Meta:
        model = Termination
        fields = [
            'id', 'url', 'display', 'name', 'group', 'description',
            'ipv4_vpn_ip_pool', 'ipv6_vpn_ip_pool', 'type',
            'virtual_machine', 'vm_outside_interface', 'device', 
            'device_outside_interface', 'vpn_gateway_ip',
            'created', 'last_updated', 'custom_fields', 'tags'
        ]


class RemoteAccessTunnelSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_vpnaas-api:remoteaccesstunnel-detail'
    )

    class Meta:
        model = RemoteAccessTunnel
        fields = [
            'id', 'url', 'display', 'name', 'group', 'server_certificate',
            'technology', 'ipsec_profile', 'tls_profile', 'status',
            'primary_dns', 'secondary_dns', 'ipv4_vpn_ip_pool', 'ipv6_vpn_ip_pool',
            'ipv4_routes_to_vpn', 'ipv4_routes_to_local_breakout',
            'ipv6_routes_to_vpn', 'ipv6_routes_to_local_breakout',
            'terminations', 'tags', 'tenant', 'contacts',
            'description', 'comments',
            'created', 'last_updated', 'custom_fields'
        ]
