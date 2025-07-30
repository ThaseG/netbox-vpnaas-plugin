# VPNaaS NetBox Plugin

A comprehensive NetBox plugin that provides VPN-as-a-Service capabilities with support for Site-to-Site (S2S) and Remote Access VPNs using containerized deployments with auto-scaling.

## Overview

This plugin extends NetBox to manage and orchestrate VPN services, integrating network documentation with automated VPN provisioning and lifecycle management. It supports multiple VPN technologies deployed as scalable container workloads.

## Features

### VPN Types Supported
- **Site-to-Site VPNs**: IPSec tunnels between network sites
- **Remote Access VPNs**: Client-to-site connectivity for remote users using 
  - **SSL/TLS VPNs**: OpenVPN and similar technologies
  - **IKEv2/IPSec**: StrongSwan-based implementations

### Core Capabilities
- **Automated Provisioning**: Deploy VPN instances based on NetBox data
- **Auto-scaling**: Dynamic scaling based on connection load and metrics
- **Multi-tenancy**: Support for multiple organizations and departments
- **Certificate Management**: Automated PKI and certificate lifecycle
- **Load Balancing**: Distribute VPN connections across multiple instances
- **Monitoring Integration**: Prometheus metrics and Grafana dashboards
- **API-driven**: Full REST API for external integrations

### Container Technologies
- **NetBox Docker Plugin**: Primary orchestration platform [Using NetBox Docker Plugin]() & [NetBox Docker Agent]()
- **Container Services**: Planned orchestration platform using Public Cloud services
- **Kubernetes**: Planned orchestration platform using Public Cloud services

## Architecture

TBA

## Installation

### Prerequisites
TBA

### Plugin Installation

TBA

## Usage

TBA

## Supported VPN Technologies

| Technology | S2S Support | Remote Access | Container Image | Auto-scaling |
|------------|-------------|---------------|-----------------|--------------|
| StrongSwan | ✅ | ✅ | `strongswan/strongswan:latest` | ✅ |
| OpenVPN    | ✅ | ✅ | `openvpn/openvpn-as:latest` | ✅ |
| Site-to-Site IPSEC | ✅ | ✅ | `custom/ipsec:latest` | ✅ |

## Roadmap

TBA

## License

This project is licensed under the BSD 3-Clause License - see the [LICENSE](LICENSE) file for details.

## Support

- **Documentation**: [This Github Repo](https://github.com/ThaseG/netbox-vpnaas-plugin)
- **Issues**: [GitHub Issues](https://github.com/ThaseG/netbox-vpnaas-plugin/issues)
- **Email**: andrej@hyben.net

## Acknowledgments

- NetBox community for the excellent platform
- Kubernetes community for container orchestration
- StrongSwan and OpenVPN projects for VPN implementations
- Contributors and maintainers of this project

---

**Disclaimer**: This plugin is designed for production use but should be thoroughly tested in your environment before deployment. Always follow security best practices when deploying VPN services.