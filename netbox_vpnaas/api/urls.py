from netbox.api.routers import NetBoxRouter
from . import views

app_name = 'netbox_vpnaas-api'

router = NetBoxRouter()

# Remote Access VPN endpoints
router.register('ravpn/tunnel', views.RemoteAccessTunnelViewSet, basename='remoteaccesstunnel')
router.register('ravpn/dns', views.DNSViewSet, basename='dns')
router.register('ravpn/ipv4_routes', views.IPv4RoutesViewSet, basename='ipv4routes')
router.register('ravpn/ipv6_routes', views.IPv6RoutesViewSet, basename='ipv6routes')
router.register('ravpn/termination', views.TerminationViewSet, basename='termination')
router.register('ravpn/ipsecprofile', views.IPSecProfileViewSet, basename='ipsecprofile')
router.register('ravpn/tlsprofile', views.TLSProfileViewSet, basename='tlsprofile')

urlpatterns = router.urls