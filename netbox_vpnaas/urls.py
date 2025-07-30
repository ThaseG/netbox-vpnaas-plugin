from django.urls import path
from . import views

app_name = 'netbox_vpnaas'

urlpatterns = [
    # DNS URLs
    path('dns/', views.DNSListView.as_view(), name='dns_list'),
    path('dns/add/', views.DNSEditView.as_view(), name='dns_add'),
    path('dns/<int:pk>/', views.DNSView.as_view(), name='dns'),
    path('dns/<int:pk>/edit/', views.DNSEditView.as_view(), name='dns_edit'),
    path('dns/<int:pk>/delete/', views.DNSDeleteView.as_view(), name='dns_delete'),

    # IPv4 Routes URLs
    path('ipv4-routes/', views.IPv4RoutesListView.as_view(), name='ipv4routes_list'),
    path('ipv4-routes/add/', views.IPv4RoutesEditView.as_view(), name='ipv4routes_add'),
    path('ipv4-routes/<int:pk>/', views.IPv4RoutesView.as_view(), name='ipv4routes'),
    path('ipv4-routes/<int:pk>/edit/', views.IPv4RoutesEditView.as_view(), name='ipv4routes_edit'),
    path('ipv4-routes/<int:pk>/delete/', views.IPv4RoutesDeleteView.as_view(), name='ipv4routes_delete'),

    # IPv6 Routes URLs
    path('ipv6-routes/', views.IPv6RoutesListView.as_view(), name='ipv6routes_list'),
    path('ipv6-routes/add/', views.IPv6RoutesEditView.as_view(), name='ipv6routes_add'),
    path('ipv6-routes/<int:pk>/', views.IPv6RoutesView.as_view(), name='ipv6routes'),
    path('ipv6-routes/<int:pk>/edit/', views.IPv6RoutesEditView.as_view(), name='ipv6routes_edit'),
    path('ipv6-routes/<int:pk>/delete/', views.IPv6RoutesDeleteView.as_view(), name='ipv6routes_delete'),

    # IPSec Profile URLs
    path('ipsec-profiles/', views.IPSecProfileListView.as_view(), name='ipsecprofile_list'),
    path('ipsec-profiles/add/', views.IPSecProfileEditView.as_view(), name='ipsecprofile_add'),
    path('ipsec-profiles/<int:pk>/', views.IPSecProfileView.as_view(), name='ipsecprofile'),
    path('ipsec-profiles/<int:pk>/edit/', views.IPSecProfileEditView.as_view(), name='ipsecprofile_edit'),
    path('ipsec-profiles/<int:pk>/delete/', views.IPSecProfileDeleteView.as_view(), name='ipsecprofile_delete'),

    # TLS Profile URLs
    path('tls-profiles/', views.TLSProfileListView.as_view(), name='tlsprofile_list'),
    path('tls-profiles/add/', views.TLSProfileEditView.as_view(), name='tlsprofile_add'),
    path('tls-profiles/<int:pk>/', views.TLSProfileView.as_view(), name='tlsprofile'),
    path('tls-profiles/<int:pk>/edit/', views.TLSProfileEditView.as_view(), name='tlsprofile_edit'),
    path('tls-profiles/<int:pk>/delete/', views.TLSProfileDeleteView.as_view(), name='tlsprofile_delete'),

    # Termination URLs
    path('terminations/', views.TerminationListView.as_view(), name='termination_list'),
    path('terminations/add/', views.TerminationEditView.as_view(), name='termination_add'),
    path('terminations/<int:pk>/', views.TerminationView.as_view(), name='termination'),
    path('terminations/<int:pk>/edit/', views.TerminationEditView.as_view(), name='termination_edit'),
    path('terminations/<int:pk>/delete/', views.TerminationDeleteView.as_view(), name='termination_delete'),

    # Remote Access Tunnel URLs
    path('remote-access-tunnels/', views.RemoteAccessTunnelListView.as_view(), name='remoteaccesstunnel_list'),
    path('remote-access-tunnels/add/', views.RemoteAccessTunnelEditView.as_view(), name='remoteaccesstunnel_add'),
    path('remote-access-tunnels/<int:pk>/', views.RemoteAccessTunnelView.as_view(), name='remoteaccesstunnel'),
    path('remote-access-tunnels/<int:pk>/edit/', views.RemoteAccessTunnelEditView.as_view(), name='remoteaccesstunnel_edit'),
    path('remote-access-tunnels/<int:pk>/delete/', views.RemoteAccessTunnelDeleteView.as_view(), name='remoteaccesstunnel_delete'),
]
