# pylint: disable=no-member

import NetworkManager

print("=== Networks ==================")
for dev in NetworkManager.NetworkManager.GetDevices():
    if dev.DeviceType != NetworkManager.NM_DEVICE_TYPE_WIFI:
        continue
    for ap in dev.GetAccessPoints():
        print('%-30s %dMHz %d%%' % (ap.Ssid, ap.Frequency, ap.Strength))
