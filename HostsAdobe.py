import tkinter as tk
from elevate import elevate
import os
import ctypes

# Attempt to elevate to administrative privileges
elevated = True
# try:
#     elevate()
# except OSError as e:
#     if e.winerror == 1223:  # The operation was canceled by the user
#         elevated = False

# Check for administrative privileges
def is_admin():
    try:
        return os.getuid() == 0
    except AttributeError:
        return ctypes.windll.shell32.IsUserAnAdmin() != 0

# Function to center the window on the screen and set its width 10% larger than its content
def center_window(root, width_increase_ratio=0.1):
    root.update_idletasks()
    
    # Calculate the required width and height
    required_width = root.winfo_reqwidth()
    required_height = root.winfo_reqheight()

    # Increase the width by the specified ratio
    increased_width = int(required_width * (1 + width_increase_ratio))

    # Get screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Calculate position x and y coordinates
    x = (screen_width - increased_width) // 2
    y = (screen_height - required_height) // 2

    root.geometry(f'{increased_width}x{required_height}+{x}+{y}')
    root.minsize(increased_width, required_height)

# Create the main window
root = tk.Tk()
root.iconbitmap("D:\\Desktop\\hostsadobe\\logo.ico")
root.title("Adobe hosts blocker/unblocker")
hosts_path = r"C:\Windows\System32\drivers\etc\hosts" if os.name == 'nt' else "/etc/hosts"

def update_label(message):
    result_label.config(text=message)

# Define the functions to be triggered
def block():
    text_to_write = """
# Copyright (c) 1993-2009 Microsoft Corp.
#
# This is a sample HOSTS file used by Microsoft TCP/IP for Windows.
#
# This file contains the mappings of IP addresses to host names. Each
# entry should be kept on an individual line. The IP address should
# be placed in the first column followed by the corresponding host name.
# The IP address and the host name should be separated by at least one
# space.
#
# Additionally, comments (such as these) may be inserted on individual
# lines or following the machine name denoted by a '#' symbol.
#
# For example:
#
#      102.54.94.97     rhino.acme.com          # source server
#       38.25.63.10     x.acme.com              # x client host

# localhost name resolution is handled within DNS itself.
#	127.0.0.1       localhost
#	::1             localhost

#New Ver 25.7
127.0.0.1 adobe.io
127.0.0.1 5amul9liob.adobestats.io
127.0.0.1 cc-api-data.adobe.io
127.0.0.1 lcs-robs.adobe.io
127.0.0.1 lcs-cops.adobe.io
127.0.0.1 crs.cr.adobe.com
127.0.0.1 36ai1uk1z7.adobestats.io
127.0.0.1 cctypekit.adobe.io
127.0.0.1 guzg78logz.adobe.io
127.0.0.1 1hzopx6nz7.adobe.io
127.0.0.1 ij0gdyrfka.adobe.io
#IPs
127.0.0.1 3.233.129.217
127.0.0.1 192.150.14.69
127.0.0.1 192.150.18.101
127.0.0.1 192.150.18.108
127.0.0.1 192.150.22.40
127.0.0.1 192.150.8.100
127.0.0.1 192.150.8.118
127.0.0.1 199.7.52.190
127.0.0.1 199.7.54.72
127.0.0.1 209-34-83-73.ood.opsource.net
127.0.0.1 209.34.83.67
127.0.0.1 209.34.83.73
127.0.0.1 18.207.85.246
127.0.0.1 52.6.155.20
127.0.0.1 52.10.49.85
127.0.0.1 23.22.30.141
127.0.0.1 34.215.42.13
127.0.0.1 52.84.156.37
127.0.0.1 65.8.207.109
127.0.0.1 3.220.11.113
127.0.0.1 3.221.72.231
127.0.0.1 3.216.32.253
127.0.0.1 3.208.248.199
127.0.0.1 3.219.243.226
127.0.0.1 13.227.103.57
127.0.0.1 34.192.151.90
127.0.0.1 34.237.241.83
127.0.0.1 44.240.189.42
127.0.0.1 52.20.222.155
127.0.0.1 52.208.86.132
127.0.0.1 54.208.86.132
127.0.0.1 63.140.38.120
127.0.0.1 63.140.38.160
127.0.0.1 63.140.38.169
127.0.0.1 63.140.38.219
127.0.0.1 18.228.243.121
127.0.0.1 18.230.164.221
127.0.0.1 54.156.135.114
127.0.0.1 54.221.228.134
127.0.0.1 54.224.241.105
127.0.0.1 100.24.211.130
127.0.0.1 162.247.242.20
#domain names
0.0.0.0 ic.adobe.io
0.0.0.0 b5kbg2ggog.adobe.io
127.0.0.1 3dns-1.adobe.com
127.0.0.1 3dns-2.adobe.com
127.0.0.1 3dns-3.adobe.com
127.0.0.1 3dns-4.adobe.com
127.0.0.1 3dns-5.adobe.com
127.0.0.1 3dns.adobe.com
127.0.0.1 activate-sea.adobe.com
127.0.0.1 activate-sea.adobe.de
127.0.0.1 activate-sjc0.adobe.com
127.0.0.1 activate-sjc0.adobe.de
127.0.0.1 activate.adobe.com
127.0.0.1 activate.adobe.de
127.0.0.1 activate.wip.adobe.com
127.0.0.1 activate.wip1.adobe.com
127.0.0.1 activate.wip2.adobe.com
127.0.0.1 activate.wip3.adobe.com
127.0.0.1 activate.wip3.adobe.de
127.0.0.1 activate.wip4.adobe.com
127.0.0.1 adobe-dns-1.adobe.com
127.0.0.1 adobe-dns-2.adobe.com
127.0.0.1 adobe-dns-2.adobe.de
127.0.0.1 adobe-dns-3.adobe.com
127.0.0.1 adobe-dns-3.adobe.de
127.0.0.1 adobe-dns-4.adobe.com
127.0.0.1 adobe-dns.adobe.com
127.0.0.1 adobe-dns.adobe.de
127.0.0.1 adobe.activate.com
127.0.0.1 adobeereg.com
127.0.0.1 cmdls.adobe.com
127.0.0.1 crl.verisign.net
127.0.0.1 ereg.adobe.com
127.0.0.1 ereg.adobe.de
127.0.0.1 ereg.wip.adobe.com
127.0.0.1 ereg.wip1.adobe.com
127.0.0.1 ereg.wip2.adobe.com
127.0.0.1 ereg.wip3.adobe.com
127.0.0.1 ereg.wip4.adobe.com
127.0.0.1 genuine.adobe.com
127.0.0.1 hlrcv.stage.adobe.com
127.0.0.1 hl2rcv.adobe.com
127.0.0.1 hl2rcv.adobe.de
127.0.0.1 ims-na1-prprod.adobelogin.com
127.0.0.1 lm.licenses.adobe.com
127.0.0.1 lmlicenses.wip4.adobe.com
127.0.0.1 na1r.services.adobe.com
127.0.0.1 na2m-pr.licenses.adobe.com
127.0.0.1 na2m-stg2.licenses.adobe.com
127.0.0.1 na4r.services.adobe.com
127.0.0.1 ocsp.spo1.verisign.com
127.0.0.1 ood.opsource.net
127.0.0.1 practivate.adobe
127.0.0.1 practivate.adobe.
127.0.0.1 practivate.adobe.com
127.0.0.1 practivate.adobe.de
127.0.0.1 practivate.adobe.ipp
127.0.0.1 practivate.adobe.newoa
127.0.0.1 practivate.adobe.ntp
127.0.0.1 prod-rel-ffc-ccm.oobesaas.adobe.com
127.0.0.1 s-2.adobe.com
127.0.0.1 s-3.adobe.com
127.0.0.1 tss-geotrust-crl.thawte.com
127.0.0.1 uds.licenses.adobe.com
127.0.0.1 dxyeyf6ecy.adobe.io
127.0.0.1 1hzopx6nz7.adobe.io
127.0.0.1 ic.adobe.io
127.0.0.1 p13n.adobe.io
127.0.0.1 wip1.adobe.com
127.0.0.1 wip2.adobe.com
127.0.0.1 wip3.adobe.com
127.0.0.1 wip4.adobe.com
127.0.0.1 wwis-dubc1-vip100.adobe.com
127.0.0.1 wwis-dubc1-vip101.adobe.com
127.0.0.1 wwis-dubc1-vip102.adobe.com
127.0.0.1 wwis-dubc1-vip103.adobe.com
127.0.0.1 wwis-dubc1-vip104.adobe.com
127.0.0.1 wwis-dubc1-vip105.adobe.com
127.0.0.1 wwis-dubc1-vip106.adobe.com
127.0.0.1 wwis-dubc1-vip107.adobe.com
127.0.0.1 wwis-dubc1-vip108.adobe.com
127.0.0.1 wwis-dubc1-vip109.adobe.com
127.0.0.1 wwis-dubc1-vip110.adobe.com
127.0.0.1 wwis-dubc1-vip111.adobe.com
127.0.0.1 wwis-dubc1-vip112.adobe.com
127.0.0.1 wwis-dubc1-vip113.adobe.com
127.0.0.1 wwis-dubc1-vip114.adobe.com
127.0.0.1 wwis-dubc1-vip115.adobe.com
127.0.0.1 wwis-dubc1-vip116.adobe.com
127.0.0.1 wwis-dubc1-vip117.adobe.com
127.0.0.1 wwis-dubc1-vip118.adobe.com
127.0.0.1 wwis-dubc1-vip119.adobe.com
127.0.0.1 wwis-dubc1-vip120.adobe.com
127.0.0.1 wwis-dubc1-vip121.adobe.com
127.0.0.1 wwis-dubc1-vip122.adobe.com
127.0.0.1 wwis-dubc1-vip123.adobe.com
127.0.0.1 wwis-dubc1-vip124.adobe.com
127.0.0.1 wwis-dubc1-vip125.adobe.com
127.0.0.1 wwis-dubc1-vip30.adobe.com
127.0.0.1 wwis-dubc1-vip31.adobe.com
127.0.0.1 wwis-dubc1-vip32.adobe.com
127.0.0.1 wwis-dubc1-vip33.adobe.com
127.0.0.1 wwis-dubc1-vip34.adobe.com
127.0.0.1 wwis-dubc1-vip35.adobe.com
127.0.0.1 wwis-dubc1-vip36.adobe.com
127.0.0.1 wwis-dubc1-vip37.adobe.com
127.0.0.1 wwis-dubc1-vip38.adobe.com
127.0.0.1 wwis-dubc1-vip39.adobe.com
127.0.0.1 wwis-dubc1-vip40.adobe.com
127.0.0.1 wwis-dubc1-vip41.adobe.com
127.0.0.1 wwis-dubc1-vip42.adobe.com
127.0.0.1 wwis-dubc1-vip43.adobe.com
127.0.0.1 wwis-dubc1-vip44.adobe.com
127.0.0.1 wwis-dubc1-vip45.adobe.com
127.0.0.1 wwis-dubc1-vip46.adobe.com
127.0.0.1 wwis-dubc1-vip47.adobe.com
127.0.0.1 wwis-dubc1-vip48.adobe.com
127.0.0.1 wwis-dubc1-vip49.adobe.com
127.0.0.1 wwis-dubc1-vip50.adobe.com
127.0.0.1 wwis-dubc1-vip51.adobe.com
127.0.0.1 wwis-dubc1-vip52.adobe.com
127.0.0.1 wwis-dubc1-vip53.adobe.com
127.0.0.1 wwis-dubc1-vip54.adobe.com
127.0.0.1 wwis-dubc1-vip55.adobe.com
127.0.0.1 wwis-dubc1-vip56.adobe.com
127.0.0.1 wwis-dubc1-vip57.adobe.com
127.0.0.1 wwis-dubc1-vip58.adobe.com
127.0.0.1 wwis-dubc1-vip59.adobe.com
127.0.0.1 wwis-dubc1-vip60.adobe.com
127.0.0.1 wwis-dubc1-vip60.adobe.de
127.0.0.1 wwis-dubc1-vip61.adobe.com
127.0.0.1 wwis-dubc1-vip62.adobe.com
127.0.0.1 wwis-dubc1-vip63.adobe.com
127.0.0.1 wwis-dubc1-vip64.adobe.com
127.0.0.1 wwis-dubc1-vip65.adobe.com
127.0.0.1 wwis-dubc1-vip66.adobe.com
127.0.0.1 wwis-dubc1-vip67.adobe.com
127.0.0.1 wwis-dubc1-vip68.adobe.com
127.0.0.1 wwis-dubc1-vip69.adobe.com
127.0.0.1 wwis-dubc1-vip70.adobe.com
127.0.0.1 wwis-dubc1-vip71.adobe.com
127.0.0.1 wwis-dubc1-vip72.adobe.com
127.0.0.1 wwis-dubc1-vip73.adobe.com
127.0.0.1 wwis-dubc1-vip74.adobe.com
127.0.0.1 wwis-dubc1-vip75.adobe.com
127.0.0.1 wwis-dubc1-vip76.adobe.com
127.0.0.1 wwis-dubc1-vip77.adobe.com
127.0.0.1 wwis-dubc1-vip78.adobe.com
127.0.0.1 wwis-dubc1-vip79.adobe.com
127.0.0.1 wwis-dubc1-vip80.adobe.com
127.0.0.1 wwis-dubc1-vip81.adobe.com
127.0.0.1 wwis-dubc1-vip82.adobe.com
127.0.0.1 wwis-dubc1-vip83.adobe.com
127.0.0.1 wwis-dubc1-vip84.adobe.com
127.0.0.1 wwis-dubc1-vip85.adobe.com
127.0.0.1 wwis-dubc1-vip86.adobe.com
127.0.0.1 wwis-dubc1-vip87.adobe.com
127.0.0.1 wwis-dubc1-vip88.adobe.com
127.0.0.1 wwis-dubc1-vip89.adobe.com
127.0.0.1 wwis-dubc1-vip90.adobe.com
127.0.0.1 wwis-dubc1-vip91.adobe.com
127.0.0.1 wwis-dubc1-vip92.adobe.com
127.0.0.1 wwis-dubc1-vip93.adobe.com
127.0.0.1 wwis-dubc1-vip94.adobe.com
127.0.0.1 wwis-dubc1-vip95.adobe.com
127.0.0.1 wwis-dubc1-vip96.adobe.com
127.0.0.1 wwis-dubc1-vip97.adobe.com
127.0.0.1 wwis-dubc1-vip98.adobe.com
127.0.0.1 wwis-dubc1-vip99.adobe.com
127.0.0.1 www.adobeereg.com
127.0.0.1 cc-api-data.adobe.io
127.0.0.1 prod.adobegenuine.com
127.0.0.1 assets.adobedtm.com
127.0.0.1 4vzokhpsbs.adobe.io
127.0.0.1 69tu0xswvq.adobe.io
127.0.0.1 5zgzzv92gn.adobe.io
127.0.0.1 dyzt55url8.adobe.io
127.0.0.1 gw8gfjbs05.adobe.io
127.0.0.1 wip.adobe.com
127.0.0.1 199.232.114.137
127.0.0.1 www.wip.adobe.com
127.0.0.1 www.wip1.adobe.com
127.0.0.1 www.wip2.adobe.com
127.0.0.1 www.wip3.adobe.com
127.0.0.1 www.wip4.adobe.com
127.0.0.1 workflow-ui-prod.licensingstack.com
127.0.0.1 1b9khekel6.adobe.io
127.0.0.1 adobe-dns-01.adobe.com
127.0.0.1 adobe.demdex.net
127.0.0.1 adobe.tt.omtrdc.net
127.0.0.1 adobedc.demdex.net
127.0.0.1 adobeid-na1.services.adobe.com
127.0.0.1 auth-cloudfront.prod.ims.adobejanus.com
127.0.0.1 auth.services.adobe.com
127.0.0.1 cai-splunk-proxy.adobe.io
127.0.0.1 cc-cdn.adobe.com
127.0.0.1 cc-cdn.adobe.com.edgekey.net
127.0.0.1 cclibraries-defaults-cdn.adobe.com
127.0.0.1 cclibraries-defaults-cdn.adobe.com.edgekey.net
127.0.0.1 cn-assets.adobedtm.com.edgekey.net
127.0.0.1 crlog-crcn.adobe.com
127.0.0.1 crs.cr.adobe.com
127.0.0.1 edgeproxy-irl1.cloud.adobe.io
127.0.0.1 ethos.ethos02-prod-irl1.ethos.adobe.net
127.0.0.1 geo2.adobe.com
127.0.0.1 lcs-cops.adobe.io
127.0.0.1 lcs-robs.adobe.io
127.0.0.1 pv2bqhsp36w.prod.cloud.adobe.io
127.0.0.1 services.prod.ims.adobejanus.com
127.0.0.1 ssl-delivery.adobe.com.edgekey.net
127.0.0.1 sstats.adobe.com
127.0.0.1 stls.adobe.com-cn.edgesuite.net
127.0.0.1 stls.adobe.com-cn.edgesuite.net.globalredir.akadns.net
127.0.0.1 use-stls.adobe.com.edgesuite.net
127.0.0.1 9ngulmtgqi.adobe.io
    """
    try:
        with open(hosts_path, 'w') as hosts_file:
            hosts_file.write(text_to_write)
        message = "Hosts file was updated! Adobe hosts blocked."
    except PermissionError:
        message = "Permission denied. Run the script as an administrator."
    except Exception as e:
        message = f"An error occurred: {e}"
    update_label(message)

def unblock():
    text_to_write = """
# Copyright (c) 1993-2009 Microsoft Corp.
#
# This is a sample HOSTS file used by Microsoft TCP/IP for Windows.
#
# This file contains the mappings of IP addresses to host names. Each
# entry should be kept on an individual line. The IP address should
# be placed in the first column followed by the corresponding host name.
# The IP address and the host name should be separated by at least one
# space.
#
# Additionally, comments (such as these) may be inserted on individual
# lines or following the machine name denoted by a '#' symbol.
#
# For example:
#
#      102.54.94.97     rhino.acme.com          # source server
#       38.25.63.10     x.acme.com              # x client host

# localhost name resolution is handled within DNS itself.
#	127.0.0.1       localhost
#	::1             localhost
    """
    try:
        with open(hosts_path, 'w') as hosts_file:
            hosts_file.write(text_to_write)
        message = "Hosts file was updated! Adobe hosts unblocked."
    except PermissionError:
        message = "Permission denied. Run the script as an administrator."
    except Exception as e:
        message = f"An error occurred: {e}"
    update_label(message)

def button1_click():
    block()

def button2_click():
    unblock()

# Create a frame to hold the buttons and center it
button_frame = tk.Frame(root)
button_frame.pack(expand=True)

# Create the buttons
button1 = tk.Button(button_frame, text="Enable cracked Adobe", command=button1_click)
button2 = tk.Button(button_frame, text="  Enable legit Adobe  ", command=button2_click)

# Position the buttons in the frame
button1.pack(side=tk.LEFT, padx=20, pady=20)
button2.pack(side=tk.RIGHT, padx=20, pady=20)

# Create a label to display the result at the bottom
result_label = tk.Label(root, text="", height=2, relief=tk.SUNKEN)
result_label.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=10)

# Check for administrative privileges
if not elevated or not is_admin():
    button1.config(state=tk.DISABLED)
    button2.config(state=tk.DISABLED)
    update_label("You need to run with administrative privileges.")
    root.deiconify()  # Ensure the window is shown and not minimized

# Center the window and set the minimum size
center_window(root)

# Run the application
root.mainloop()
