import time
from tap import Tap
from monitor import Monitor
from anomaly import detect_leak
monitor=Monitor()
tap1 = Tap("Tap-1")
tap2 = Tap("Tap-2")
# Historical flow data (simulation)
flow_history = [4.5, 5.0, 4.8, 5.2, 4.9]
print("Smart Water Usage Monitoring System Started\n")
# Turn ON tap1
tap1.turn_on(flow_rate=5.0)
print("Tap-1 turned ON")
# Simulate time passing
time.sleep(2)
# Check unattended tap
if monitor.check_unattended(tap1):
    print("ALERT: Tap-1 left unattended for too long")
# Leak detection
current_flow = tap1.flow_rate
if detect_leak(flow_history,current_flow):
    print("ALERT: Possible leak detected in Tap-1")
else:
    print("No leak detected in Tap-1")
# Turn OFF tap
tap1.turn_off()
print("Tap-1 turned OFF")
print("\nSystem Execution Completed")
