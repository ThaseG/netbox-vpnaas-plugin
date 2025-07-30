# NetBox VPNaaS Plugin

A comprehensive NetBox plugin that provides VPN-as-a-Service capabilities with support for Remote Access VPNs and Site-to-Site VPNs using containerized deployments with auto-scaling.

This plugin extends NetBox to manage and orchestrate VPN services, integrating network documentation with automated VPN provisioning and lifecycle management. It supports multiple VPN technologies deployed as scalable container workloads.

## Features

### Remote Access VPN
- **SSL/TLS VPNs**: OpenVPN and similar technologies
- **IKEv2/IPSec**: StrongSwan-based implementations
- **Multi-tenancy**: Support for multiple organizations and departments
- **Certificate Management**: Server certificate storage and management
- **Flexible Routing**: Configurable routes for VPN and local breakout traffic
- **DNS Configuration**: Custom DNS server assignments with defaults
- **IP Pool Management**: IPv4 and IPv6 address pool assignments
- **Termination Points**: Support for both virtual machines and physical devices

### Site-to-Site VPN (Planned)
- IPSec tunnels between network sites
- Automated provisioning based on NetBox data

### Management Features
- **API-driven**: Full REST API for external integrations
- **Web Interface**: Complete NetBox-style web interface
- **Multi-tenancy**: Tenant and contact assignment
- **Tagging**: Full NetBox tagging support
- **Filtering**: Advanced filtering and search capabilities

## API Endpoints

The plugin provides REST API endpoints matching your specification:

### Remote Access VPN
- `GET /api/plugins/vpnaas/ravpn/tunnel/` - List all tunnels
- `POST /api/plugins/vpnaas/ravpn/tunnel/` - Create new tunnel
- `GET /api/plugins/vpnaas/ravpn/tunnel/{id}/` - Get specific tunnel
- `PUT /api/plugins/vpnaas/ravpn/tunnel/{id}/` - Update tunnel
- `DELETE /api/plugins/vpnaas/ravpn/tunnel/{id}/` - Delete tunnel

### Supporting Resources
- `GET/POST/PUT/DELETE /api/plugins/vpnaas/ravpn/dns/` - DNS servers
- `GET/POST/PUT/DELETE /api/plugins/vpnaas/ravpn/ipv4_routes/` - IPv4 routing
- `GET/POST/PUT/DELETE /api/plugins/vpnaas/ravpn/ipv6_routes/` - IPv6 routing
- `GET/POST/PUT/DELETE /api/plugins/vpnaas/ravpn/termination/` - Termination points
- `GET/POST/PUT/DELETE /api/plugins/vpnaas/ravpn/ipsecprofile/` - IPSec profiles
- `GET/POST/PUT/DELETE /api/plugins/vpnaas/ravpn/tlsprofile/` - TLS profiles

## Installation

### Requirements
- NetBox 4.0+
- Python 3.10+
- Django 4.2+

### Installation Steps

#### Option 1: Install from PyPI (when published)
```bash
# Activate NetBox virtual environment
source /opt/netbox/venv/bin/activate

# Install the plugin
pip install netbox-vpnaas-plugin
```

#### Option 2: Install from GitHub
```bash
# Activate NetBox virtual environment
source /opt/netbox/venv/bin/activate

# Install directly from GitHub
pip install git+https://github.com/ThaseG/netbox-vpnaas-plugin.git
```

#### Option 3: Development Installation
```bash
# Clone the repository
git clone https://github.com/ThaseG/netbox-vpnaas-plugin.git
cd netbox-vpnaas-plugin

# Activate NetBox virtual environment
source /opt/netbox/venv/bin/activate

# Install in development mode
pip install -e .
```

### NetBox Configuration

1. Add the plugin to your `configuration.py` file:

```python
# configuration.py
PLUGINS = [
    'netbox_vpnaas',
    # ... other plugins
]

# Optional plugin configuration
PLUGINS_CONFIG = {
    'netbox_vpnaas': {
        'enable_remote_access': True,
        'enable_site_to_site': True,
        'auto_scaling_enabled': True,
        'default_dns_primary': '1.1.1.1',
        'default_dns_secondary': '8.8.8.8',
    }
}
```

2. Run database migrations:

```bash
cd /opt/netbox
source venv/bin/activate
python manage.py migrate netbox_vpnaas
```

3. Collect static files:

```bash
python manage.py collectstatic --no-input
```

4. Restart NetBox services:

```bash
sudo systemctl restart netbox netbox-rq
```

### Docker Installation (netbox-docker)

1. Add to your `plugin_requirements.txt`:
```
netbox-vpnaas-plugin
```

2. Add to your `plugins.py` configuration:
```python
PLUGINS = [
    'netbox_vpnaas',
]

PLUGINS_CONFIG = {
    'netbox_vpnaas': {
        'enable_remote_access': True,
        'enable_site_to_site': True,
    }
}
```

3. Rebuild and restart containers:
```bash
docker-compose down
docker-compose build --no-cache
docker-compose up -d
```

## Usage

### Creating a Remote Access VPN Tunnel

1. **Set up prerequisites**:
   - Create DNS servers (optional - defaults to 1.1.1.1 and 8.8.8.8)
   - Create IPv4/IPv6 route objects (optional - defaults to all traffic to VPN)
   - Create VPN profiles (IPSec or TLS)
   - Create termination points
   - Ensure IP address objects exist for VPN pools

2. **Create the tunnel**:
   - Navigate to **Plugins > VPN as a Service > Remote Access Tunnels**
   - Click **Add** to create a new tunnel
   - Fill in the required fields:
     - Name (required)
     - Server certificate (required)
     - Technology (IPSec or TLS) and corresponding profile
     - Status (Active, Planned, or Disabled)
     - IPv4 and IPv6 VPN IP pools (required)
   - Configure optional settings:
     - DNS servers
     - Routing rules
     - Termination points
     - Tenant and contacts

### API Usage Example

```python
import requests

# Create a new Remote Access VPN tunnel
tunnel_data = {
    "name": "Corporate VPN",
    "group": "Remote Access",
    "server_certificate": "-----BEGIN CERTIFICATE-----\n...\n-----END CERTIFICATE-----",
    "technology": "tls",
    "tls_profile": 1,  # ID of TLS profile
    "status": "active",
    "ipv4_vpn_ip_pool": 1,  # ID of IPv4 address object
    "ipv6_vpn_ip_pool": 2,  # ID of IPv6 address object
    "description": "Main corporate remote access VPN"
}

response = requests.post(
    'https://your-netbox.com/api/plugins/vpnaas/ravpn/tunnel/',
    json=tunnel_data,
    headers={'Authorization': 'Token your-api-token'}
)
```

## Data Model

The plugin implements the following models:

- **RemoteAccessTunnel**: Main VPN tunnel configuration
- **DNS**: DNS server configurations
- **IPv4Routes/IPv6Routes**: Routing table definitions
- **IPSecProfile**: IPSec-specific configurations
- **TLSProfile**: TLS/SSL-specific configurations
- **Termination**: VPN termination point definitions

## Development

### Project Structure
```
netbox_vpnaas/
├── __init__.py
├── config.py              # Plugin configuration
├── models.py              # Django models
├── admin.py               # Django admin
├── forms.py               # Web forms
├── views.py               # Web views
├── tables.py              # Display tables
├── urls.py                # URL routing
├── navigation.py          # Menu items
├── filtersets.py          # Filtering
├── api/
│   ├── serializers.py     # API serializers
│   ├── views.py           # API viewsets
│   └── urls.py            # API URLs
├── migrations/            # Database migrations
└── templates/             # HTML templates
    └── netbox_vpnaas/
```

### Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the BSD 3-Clause License - see the [LICENSE](LICENSE) file for details.

## Support

- **Documentation**: [GitHub Repository](https://github.com/ThaseG/netbox-vpnaas-plugin)
- **Issues**: [GitHub Issues](https://github.com/ThaseG/netbox-vpnaas-plugin/issues)
- **Email**: [andrej@hyben.net](mailto:andrej@hyben.net)

## Acknowledgments

- NetBox community for the excellent platform
- Contributors and maintainers of this project

---

**Disclaimer**: This plugin is designed for production use but should be thoroughly tested in your environment before deployment. Always follow security best practices when deploying VPN services.