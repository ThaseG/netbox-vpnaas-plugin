from django.core.validators import validate_ipv4_address, validate_ipv6_address
from django.db import models
from django.urls import reverse
from netbox.models import NetBoxModel
from utilities.choices import ChoiceSet


class TechnologyChoices(ChoiceSet):
    IPSEC = 'ipsec'
    TLS = 'tls'
    
    CHOICES = [
        (IPSEC, 'IPSec'),
        (TLS, 'TLS'),
    ]


class StatusChoices(ChoiceSet):
    ACTIVE = 'active'
    PLANNED = 'planned'
    DISABLED = 'disabled'
    
    CHOICES = [
        (ACTIVE, 'Active'),
        (PLANNED, 'Planned'),
        (DISABLED, 'Disabled'),
    ]


class ProtocolChoices(ChoiceSet):
    TCP = 'tcp'
    UDP = 'udp'
    
    CHOICES = [
        (TCP, 'TCP'),
        (UDP, 'UDP'),
    ]


class TLSVersionChoices(ChoiceSet):
    V1_2 = '1.2'
    V1_3 = '1.3'
    
    CHOICES = [
        (V1_2, 'TLS 1.2'),
        (V1_3, 'TLS 1.3'),
    ]


class TerminationTypeChoices(ChoiceSet):
    VIRTUAL_MACHINE = 'Virtual Machine'
    DEVICE = 'Device'
    
    CHOICES = [
        (VIRTUAL_MACHINE, 'Virtual Machine'),
        (DEVICE, 'Device'),
    ]


class DNS(NetBoxModel):
    """DNS configuration for VPN clients"""
    name = models.CharField(max_length=100)
    group = models.CharField(max_length=100, blank=True)
    ipv4 = models.GenericIPAddressField(
        protocol='IPv4',
        validators=[validate_ipv4_address],
        help_text="IPv4 DNS server address"
    )
    description = models.CharField(max_length=200, blank=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'DNS Server'
        verbose_name_plural = 'DNS Servers'

    def __str__(self):
        return f"{self.name} ({self.ipv4})"

    def get_absolute_url(self):
        return reverse('plugins:netbox_vpnaas:dns', args=[self.pk])


class IPv4Routes(NetBoxModel):
    """IPv4 routing configuration"""
    name = models.CharField(max_length=100)
    group = models.CharField(max_length=100, blank=True)
    ipv4_routes = models.TextField(
        help_text="IPv4 routes, one per line in CIDR format (e.g., 10.10.10.10/32)"
    )
    description = models.CharField(max_length=200, blank=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'IPv4 Routes'
        verbose_name_plural = 'IPv4 Routes'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('plugins:netbox_vpnaas:ipv4routes', args=[self.pk])


class IPv6Routes(NetBoxModel):
    """IPv6 routing configuration"""
    name = models.CharField(max_length=100)
    group = models.CharField(max_length=100, blank=True)
    ipv6_routes = models.TextField(
        help_text="IPv6 routes, one per line in CIDR format (e.g., ::/0)"
    )
    description = models.CharField(max_length=200, blank=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'IPv6 Routes'
        verbose_name_plural = 'IPv6 Routes'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('plugins:netbox_vpnaas:ipv6routes', args=[self.pk])


class IPSecProfile(NetBoxModel):
    """IPSec VPN profile configuration"""
    name = models.CharField(max_length=100)
    group = models.CharField(max_length=100, blank=True)
    setup = models.TextField(help_text="IPSec configuration setup")
    description = models.CharField(max_length=200, blank=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'IPSec Profile'
        verbose_name_plural = 'IPSec Profiles'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('plugins:netbox_vpnaas:ipsecprofile', args=[self.pk])


class TLSProfile(NetBoxModel):
    """TLS VPN profile configuration"""
    name = models.CharField(max_length=100)
    group = models.CharField(max_length=100, blank=True)
    protocol = models.CharField(
        max_length=10,
        choices=ProtocolChoices,
        blank=True,
        help_text="Transport protocol"
    )
    min_tls_version = models.CharField(
        max_length=10,
        choices=TLSVersionChoices,
        blank=True,
        help_text="Minimum TLS version"
    )
    max_tls_version = models.CharField(
        max_length=10,
        choices=TLSVersionChoices,
        blank=True,
        help_text="Maximum TLS version"
    )
    setup = models.TextField(help_text="TLS configuration setup")
    description = models.CharField(max_length=200, blank=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'TLS Profile'
        verbose_name_plural = 'TLS Profiles'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('plugins:netbox_vpnaas:tlsprofile', args=[self.pk])

    def clean(self):
        super().clean()
        # Validate TLS version consistency
        if self.min_tls_version == '1.3' and self.max_tls_version == '1.2':
            raise ValidationError("Maximum TLS version cannot be lower than minimum version")


class Termination(NetBoxModel):
    """VPN termination point configuration"""
    name = models.CharField(max_length=100)
    group = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=200, blank=True)
    
    # IP pools for this termination point
    ipv4_vpn_ip_pool = models.ForeignKey(
        'ipam.IPAddress',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='vpnaas_termination_ipv4',
        limit_choices_to={'family': 4}
    )
    ipv6_vpn_ip_pool = models.ForeignKey(
        'ipam.IPAddress',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='vpnaas_termination_ipv6',
        limit_choices_to={'family': 6}
    )
    
    # Termination type and target
    type = models.CharField(
        max_length=20,
        choices=TerminationTypeChoices,
        help_text="Type of termination endpoint"
    )
    
    # Virtual Machine fields
    virtual_machine = models.ForeignKey(
        'virtualization.VirtualMachine',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        help_text="Virtual machine for VPN termination"
    )
    vm_outside_interface = models.ForeignKey(
        'virtualization.VMInterface',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='vpnaas_termination_vm_interface',
        help_text="Outside interface on virtual machine"
    )
    
    # Device fields  
    device = models.ForeignKey(
        'dcim.Device',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        help_text="Device for VPN termination"
    )
    device_outside_interface = models.ForeignKey(
        'dcim.Interface',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='vpnaas_termination_device_interface',
        help_text="Outside interface on device"
    )
    
    # VPN Gateway IP
    vpn_gateway_ip = models.ForeignKey(
        'ipam.IPAddress',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='vpnaas_termination_gateway',
        help_text="VPN gateway IP address"
    )

    class Meta:
        ordering = ['name']
        verbose_name = 'VPN Termination'
        verbose_name_plural = 'VPN Terminations'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('plugins:netbox_vpnaas:termination', args=[self.pk])


class RemoteAccessTunnel(NetBoxModel):
    """Main Remote Access VPN tunnel configuration"""
    name = models.CharField(max_length=100)
    group = models.CharField(max_length=100, blank=True)
    
    # Certificate
    server_certificate = models.TextField(help_text="Server certificate (multi-line)")
    
    # Technology and profiles
    technology = models.CharField(
        max_length=10,
        choices=TechnologyChoices,
        help_text="VPN technology type"
    )
    ipsec_profile = models.ForeignKey(
        IPSecProfile,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        help_text="IPSec profile (required if technology is IPSec)"
    )
    tls_profile = models.ForeignKey(
        TLSProfile,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        help_text="TLS profile (required if technology is TLS)"
    )
    
    # Status
    status = models.CharField(
        max_length=10,
        choices=StatusChoices,
        help_text="Tunnel status"
    )
    
    # DNS configuration
    primary_dns = models.ForeignKey(
        DNS,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='tunnels_primary',
        help_text="Primary DNS server (defaults to 1.1.1.1)"
    )
    secondary_dns = models.ForeignKey(
        DNS,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='tunnels_secondary',
        help_text="Secondary DNS server (defaults to 8.8.8.8)"
    )
    
    # IP pools
    ipv4_vpn_ip_pool = models.ForeignKey(
        'ipam.IPAddress',
        on_delete=models.PROTECT,
        related_name='vpnaas_tunnel_ipv4',
        limit_choices_to={'family': 4},
        help_text="IPv4 IP pool for VPN clients"
    )
    ipv6_vpn_ip_pool = models.ForeignKey(
        'ipam.IPAddress',
        on_delete=models.PROTECT,
        related_name='vpnaas_tunnel_ipv6',
        limit_choices_to={'family': 6},
        help_text="IPv6 IP pool for VPN clients"
    )
    
    # Routing
    ipv4_routes_to_vpn = models.ForeignKey(
        IPv4Routes,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='tunnels_vpn_routes',
        help_text="IPv4 routes to VPN (defaults to all traffic)"
    )
    ipv4_routes_to_local_breakout = models.ForeignKey(
        IPv4Routes,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='tunnels_breakout_routes',
        help_text="IPv4 routes for local breakout"
    )
    ipv6_routes_to_vpn = models.ForeignKey(
        IPv6Routes,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='tunnels_vpn_routes_v6',
        help_text="IPv6 routes to VPN"
    )
    ipv6_routes_to_local_breakout = models.ForeignKey(
        IPv6Routes,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='tunnels_breakout_routes_v6',
        help_text="IPv6 routes for local breakout"
    )
    
    # Termination points
    terminations = models.ManyToManyField(
        Termination,
        blank=True,
        help_text="VPN termination points"
    )
    
    # NetBox standard fields
    tags = models.ManyToManyField(
        'extras.Tag',
        blank=True
    )
    tenant = models.ForeignKey(
        'tenancy.Tenant',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    contacts = models.ManyToManyField(
        'tenancy.Contact',
        blank=True
    )
    
    # Additional fields
    description = models.CharField(max_length=200, blank=True)
    comments = models.TextField(blank=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Remote Access VPN Tunnel'
        verbose_name_plural = 'Remote Access VPN Tunnels'

    def __str__(self):
        return f"{self.name} ({self.get_technology_display()})"

    def get_absolute_url(self):
        return reverse('plugins:netbox_vpnaas:remoteaccesstunnel', args=[self.pk])

    def clean(self):
        super().clean()
        # Validate profile selection based on technology
        if self.technology == TechnologyChoices.IPSEC and not self.ipsec_profile:
            raise ValidationError("IPSec profile is required when technology is IPSec")
        if self.technology == TechnologyChoices.TLS and not self.tls_profile:
            raise ValidationError("TLS profile is required when technology is TLS")
        if self.technology == TechnologyChoices.IPSEC and self.tls_profile:
            raise ValidationError("TLS profile should not be set when technology is IPSec")
        if self.technology == TechnologyChoices.TLS and self.ipsec_profile:
            raise ValidationError("IPSec profile should not be set when technology is TLS")