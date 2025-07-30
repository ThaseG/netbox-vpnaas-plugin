import django_tables2 as tables
from netbox.tables import NetBoxTable, ChoiceFieldColumn
from .models import (
    DNS, IPv4Routes, IPv6Routes, IPSecProfile, TLSProfile,
    Termination, RemoteAccessTunnel
)


class DNSTable(NetBoxTable):
    name = tables.Column(
        linkify=True
    )
    ipv4 = tables.Column()
    group = tables.Column()

    class Meta(NetBoxTable.Meta):
        model = DNS
        fields = ('pk', 'id', 'name', 'group', 'ipv4', 'description', 'actions')
        default_columns = ('name', 'group', 'ipv4', 'description')


class IPv4RoutesTable(NetBoxTable):
    name = tables.Column(
        linkify=True
    )
    group = tables.Column()
    route_count = tables.Column(
        accessor='ipv4_routes',
        verbose_name='Route Count',
        orderable=False
    )

    def render_route_count(self, value):
        if value:
            return len([line.strip() for line in value.split('\n') if line.strip()])
        return 0

    class Meta(NetBoxTable.Meta):
        model = IPv4Routes
        fields = ('pk', 'id', 'name', 'group', 'route_count', 'description', 'actions')
        default_columns = ('name', 'group', 'route_count', 'description')


class IPv6RoutesTable(NetBoxTable):
    name = tables.Column(
        linkify=True
    )
    group = tables.Column()
    route_count = tables.Column(
        accessor='ipv6_routes',
        verbose_name='Route Count',
        orderable=False
    )

    def render_route_count(self, value):
        if value:
            return len([line.strip() for line in value.split('\n') if line.strip()])
        return 0

    class Meta(NetBoxTable.Meta):
        model = IPv6Routes
        fields = ('pk', 'id', 'name', 'group', 'route_count', 'description', 'actions')
        default_columns = ('name', 'group', 'route_count', 'description')


class IPSecProfileTable(NetBoxTable):
    name = tables.Column(
        linkify=True
    )
    group = tables.Column()

    class Meta(NetBoxTable.Meta):
        model = IPSecProfile
        fields = ('pk', 'id', 'name', 'group', 'description', 'actions')
        default_columns = ('name', 'group', 'description')


class TLSProfileTable(NetBoxTable):
    name = tables.Column(
        linkify=True
    )
    group = tables.Column()
    protocol = ChoiceFieldColumn()
    min_tls_version = tables.Column(
        verbose_name='Min TLS'
    )
    max_tls_version = tables.Column(
        verbose_name='Max TLS'
    )

    class Meta(NetBoxTable.Meta):
        model = TLSProfile
        fields = ('pk', 'id', 'name', 'group', 'protocol', 'min_tls_version', 'max_tls_version', 'description', 'actions')
        default_columns = ('name', 'group', 'protocol', 'min_tls_version', 'max_tls_version', 'description')


class TerminationTable(NetBoxTable):
    name = tables.Column(
        linkify=True
    )
    group = tables.Column()
    type = ChoiceFieldColumn()
    target = tables.Column(
        orderable=False,
        verbose_name='Target'
    )
    gateway_ip = tables.Column(
        accessor='vpn_gateway_ip',
        verbose_name='Gateway IP'
    )

    def render_target(self, record):
        if record.type == 'Virtual Machine' and record.virtual_machine:
            return record.virtual_machine
        elif record.type == 'Device' and record.device:
            return record.device
        return '-'

    class Meta(NetBoxTable.Meta):
        model = Termination
        fields = ('pk', 'id', 'name', 'group', 'type', 'target', 'gateway_ip', 'description', 'actions')
        default_columns = ('name', 'group', 'type', 'target', 'gateway_ip', 'description')


class RemoteAccessTunnelTable(NetBoxTable):
    name = tables.Column(
        linkify=True
    )
    group = tables.Column()
    technology = ChoiceFieldColumn()
    status = ChoiceFieldColumn()
    profile = tables.Column(
        orderable=False,
        verbose_name='Profile'
    )
    termination_count = tables.Column(
        accessor='terminations',
        verbose_name='Terminations',
        orderable=False
    )
    tenant = tables.Column(
        linkify=True
    )

    def render_profile(self, record):
        if record.technology == 'ipsec' and record.ipsec_profile:
            return record.ipsec_profile
        elif record.technology == 'tls' and record.tls_profile:
            return record.tls_profile
        return '-'

    def render_termination_count(self, value):
        return value.count()

    class Meta(NetBoxTable.Meta):
        model = RemoteAccessTunnel
        fields = (
            'pk', 'id', 'name', 'group', 'technology', 'status', 'profile', 
            'termination_count', 'tenant', 'description', 'actions'
        )
        default_columns = (
            'name', 'group', 'technology', 'status', 'profile', 
            'termination_count', 'tenant', 'description'
        )