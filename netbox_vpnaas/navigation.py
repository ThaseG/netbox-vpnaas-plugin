from netbox.plugins import PluginMenuButton, PluginMenuItem
from utilities.choices import ButtonColorChoices

menu_items = (
    PluginMenuItem(
        link='plugins:netbox_vpnaas:remoteaccesstunnel_list',
        link_text='Remote Access Tunnels',
        buttons=(
            PluginMenuButton(
                link='plugins:netbox_vpnaas:remoteaccesstunnel_add',
                title='Add',
                icon_class='mdi mdi-plus-thick',
                color=ButtonColorChoices.GREEN
            ),
        )
    ),
    PluginMenuItem(
        link='plugins:netbox_vpnaas:dns_list',
        link_text='DNS Servers',
        buttons=(
            PluginMenuButton(
                link='plugins:netbox_vpnaas:dns_add',
                title='Add',
                icon_class='mdi mdi-plus-thick',
                color=ButtonColorChoices.GREEN
            ),
        )
    ),
    PluginMenuItem(
        link='plugins:netbox_vpnaas:ipv4routes_list',
        link_text='IPv4 Routes',
        buttons=(
            PluginMenuButton(
                link='plugins:netbox_vpnaas:ipv4routes_add',
                title='Add',
                icon_class='mdi mdi-plus-thick',
                color=ButtonColorChoices.GREEN
            ),
        )
    ),
    PluginMenuItem(
        link='plugins:netbox_vpnaas:ipv6routes_list',
        link_text='IPv6 Routes',
        buttons=(
            PluginMenuButton(
                link='plugins:netbox_vpnaas:ipv6routes_add',
                title='Add',
                icon_class='mdi mdi-plus-thick',
                color=ButtonColorChoices.GREEN
            ),
        )
    ),
    PluginMenuItem(
        link='plugins:netbox_vpnaas:ipsecprofile_list',
        link_text='IPSec Profiles',
        buttons=(
            PluginMenuButton(
                link='plugins:netbox_vpnaas:ipsecprofile_add',
                title='Add',
                icon_class='mdi mdi-plus-thick',
                color=ButtonColorChoices.GREEN
            ),
        )
    ),
    PluginMenuItem(
        link='plugins:netbox_vpnaas:tlsprofile_list',
        link_text='TLS Profiles',
        buttons=(
            PluginMenuButton(
                link='plugins:netbox_vpnaas:tlsprofile_add',
                title='Add',
                icon_class='mdi mdi-plus-thick',
                color=ButtonColorChoices.GREEN
            ),
        )
    ),
    PluginMenuItem(
        link='plugins:netbox_vpnaas:termination_list',
        link_text='Terminations',
        buttons=(
            PluginMenuButton(
                link='plugins:netbox_vpnaas:termination_add',
                title='Add',
                icon_class='mdi mdi-plus-thick',
                color=ButtonColorChoices.GREEN
            ),
        )
    ),
)