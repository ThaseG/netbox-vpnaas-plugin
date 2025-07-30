from django import forms
from netbox.forms import NetBoxModelForm
from utilities.forms.fields import DynamicModelChoiceField, DynamicModelMultipleChoiceField
from .models import (
    DNS, IPv4Routes, IPv6Routes, IPSecProfile, TLSProfile,
    Termination, RemoteAccessTunnel, TechnologyChoices, StatusChoices,
    ProtocolChoices, TLSVersionChoices, TerminationTypeChoices
)

class DNSForm(NetBoxModelForm):
    class Meta:
        model = DNS
        fields = ['name', 'group', 'ipv4', 'description', 'tags']


class IPv4RoutesForm(NetBoxModelForm):
    class Meta:
        model = IPv4Routes
        fields = ['name', 'group', 'ipv4_routes', 'description', 'tags']
        widgets = {
            'ipv4_routes': forms.Textarea(attrs={'rows': 5})
        }


class IPv6RoutesForm(NetBoxModelForm):
    class Meta:
        model = IPv6Routes
        fields = ['name', 'group', 'ipv6_routes', 'description', 'tags']
        widgets = {
            'ipv6_routes': forms.Textarea(attrs={'rows': 5})
        }


class IPSecProfileForm(NetBoxModelForm):
    class Meta:
        model = IPSecProfile
        fields = ['name', 'group', 'setup', 'description', 'tags']
        widgets = {
            'setup': forms.Textarea(attrs={'rows': 10})
        }


class TLSProfileForm(NetBoxModelForm):
    class Meta:
        model = TLSProfile
        fields = [
            'name', 'group', 'protocol', 'min_tls_version', 
            'max_tls_version', 'setup', 'description', 'tags'
        ]
        widgets = {
            'setup': forms.Textarea(attrs={'rows': 10})
        }


class TerminationForm(NetBoxModelForm):
    class Meta:
        model = Termination
        fields = [
            'name', 'group', 'description', 'ipv4_vpn_ip_pool', 
            'ipv6_vpn_ip_pool', 'type', 'virtual_machine', 
            'vm_outside_interface', 'device', 'device_outside_interface', 
            'vpn_gateway_ip', 'tags'
        ]


class RemoteAccessTunnelForm(NetBoxModelForm):
    primary_dns = DynamicModelChoiceField(
        queryset=DNS.objects.all(),
        required=False,
        help_text="Primary DNS server (defaults to 1.1.1.1 if not specified)"
    )
    secondary_dns = DynamicModelChoiceField(
        queryset=DNS.objects.all(),
        required=False,
        help_text="Secondary DNS server (defaults to 8.8.8.8 if not specified)"
    )
    ipsec_profile = DynamicModelChoiceField(
        queryset=IPSecProfile.objects.all(),
        required=False,
        help_text="Required if technology is IPSec"
    )
    tls_profile = DynamicModelChoiceField(
        queryset=TLSProfile.objects.all(),
        required=False,
        help_text="Required if technology is TLS"
    )
    ipv4_routes_to_vpn = DynamicModelChoiceField(
        queryset=IPv4Routes.objects.all(),
        required=False,
        help_text="Routes to VPN (defaults to all traffic if not specified)"
    )
    ipv4_routes_to_local_breakout = DynamicModelChoiceField(
        queryset=IPv4Routes.objects.all(),
        required=False,
        help_text="Routes for local breakout"
    )
    ipv6_routes_to_vpn = DynamicModelChoiceField(
        queryset=IPv6Routes.objects.all(),
        required=False
    )
    ipv6_routes_to_local_breakout = DynamicModelChoiceField(
        queryset=IPv6Routes.objects.all(),
        required=False
    )
    terminations = DynamicModelMultipleChoiceField(
        queryset=Termination.objects.all(),
        required=False,
        help_text="VPN termination points (IP pool automatically split if not defined in termination)"
    )

    class Meta:
        model = RemoteAccessTunnel
        fields = [
            'name', 'group', 'server_certificate', 'technology',
            'ipsec_profile', 'tls_profile', 'status', 'primary_dns',
            'secondary_dns', 'ipv4_vpn_ip_pool', 'ipv6_vpn_ip_pool',
            'ipv4_routes_to_vpn', 'ipv4_routes_to_local_breakout',
            'ipv6_routes_to_vpn', 'ipv6_routes_to_local_breakout',
            'terminations', 'tags', 'tenant', 'contacts',
            'description', 'comments'
        ]
        widgets = {
            'server_certificate': forms.Textarea(attrs={'rows': 10}),
            'comments': forms.Textarea(attrs={'rows': 5})
        }
