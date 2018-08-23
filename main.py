# pylint: disable=no-member

import NetworkManager

WIFI_INTERFACE = 'wlan0'
WIFI_INTERFACE = 'wlo1'

device = NetworkManager.NetworkManager.GetDeviceByIpIface(WIFI_INTERFACE)

print("=== Networks ==================")
for index, access_point in enumerate(device.AccessPoints):
    print('{:03d}: {}'.format(index, access_point.Ssid))

