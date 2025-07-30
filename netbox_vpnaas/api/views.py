from netbox.api.viewsets import NetBoxModelViewSet
from ..models import (
    DNS, IPv4Routes, IPv6Routes, IPSecProfile, TLSProfile,
    Termination, RemoteAccessTunnel
)
from .serializers import (
    DNSSerializer, IPv4RoutesSerializer, IPv6RoutesSerializer,
    IPSecProfileSerializer, TLSProfileSerializer, TerminationSerializer,
    RemoteAccessTunnelSerializer
)


class DNSViewSet(NetBoxModelViewSet):
    queryset = DNS.objects.all()
    serializer_class = DNSSerializer


class IPv4RoutesViewSet(NetBoxModelViewSet):
    queryset = IPv4Routes.objects.all()
    serializer_class = IPv4RoutesSerializer


class IPv6RoutesViewSet(NetBoxModelViewSet):
    queryset = IPv6Routes.objects.all()
    serializer_class = IPv6RoutesSerializer


class IPSecProfileViewSet(NetBoxModelViewSet):
    queryset = IPSecProfile.objects.all()
    serializer_class = IPSecProfileSerializer


class TLSProfileViewSet(NetBoxModelViewSet):
    queryset = TLSProfile.objects.all()
    serializer_class = TLSProfileSerializer


class TerminationViewSet(NetBoxModelViewSet):
    queryset = Termination.objects.all()
    serializer_class = TerminationSerializer


class RemoteAccessTunnelViewSet(NetBoxModelViewSet):
    queryset = RemoteAccessTunnel.objects.all()
    serializer_class = RemoteAccessTunnelSerializer
