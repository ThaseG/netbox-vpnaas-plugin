"""Netbox Plugin Configuration"""

from django.db.models.signals import post_migrate
from netbox.plugins import PluginConfig
from .utilities import create_webhook


class NetBoxVPNaaSConfig(PluginConfig):
    """Plugin Config Class"""

    name = "netbox_vpnaas_plugin"
    verbose_name = " NetBox VPNaaS Plugin"
    description = "Manage VPNaaS"
    version = "0.0.1"
    base_url = "vpnaas"
    min_version = "0.0.1"
    author = "Andrej Hyben <andrej@hyben.net>"
    author_email = "andrej@hyben.net"

    def ready(self):
        from . import signals  # pylint: disable=unused-import, import-outside-toplevel

        post_migrate.connect(create_webhook)

        super().ready()


# pylint: disable=C0103
config = NetBoxVPNaaSConfig
