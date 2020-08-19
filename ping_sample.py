import pyping

ret = pyping.ping('google.com')

if ret:
    print("Available")
