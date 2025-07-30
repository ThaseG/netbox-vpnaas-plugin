from netbox.plugins import PluginConfig

class VPNaaSConfig(PluginConfig):
    name = 'netbox_vpnaas'
    verbose_name = 'VPN as a Service'
    description = 'VPN-as-a-Service plugin for NetBox'
    version = '0.1.0'
    author = 'Andrej Hyben'
    author_email = 'andrej@hyben.net'
    base_url = 'vpnaas'
    required_settings = []
    default_settings = {
        'enable_remote_access': True,
        'enable_site_to_site': True,
        'auto_scaling_enabled': True,
        'default_dns_primary': '1.1.1.1',
        'default_dns_secondary': '8.8.8.8',
    }
    caching_config = {}

config = VPNaaSConfig