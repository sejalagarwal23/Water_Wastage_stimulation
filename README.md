# Smart Water Usage Monitoring System

A Python-based simulation designed to monitor water usage, detect unattended taps, and identify potential pipe or tap leaks using historical flow analysis. This system serves as a foundational prototype for IoT-based smart home water management systems.

## Overview

The application simulates the real-time operation of smart water taps integrated with an automated monitoring service. It tracks flow rates, identifies if a tap has been left running unattended beyond a safe duration, and applies basic statistical anomaly detection to flag potential leaks.

However there is a developed part of this which is discussed in details inside this pdf link:
https://1drv.ms/b/c/af09d61bb0b79bdd/IQDjwcHMLJA3Sb7aa7lKBvthAQlzUWnhcgzvj_iPb4stwjY?e=5coMQa 

This is simple stimulation of project 

## System Components

The project structure comprises the following core modules:

- `tap.py`: Defines the `Tap` class, representing physical water outlets. Tracks state (ON/OFF), duration of usage, and current flow rate.
- `monitor.py`: Contains the `Monitor` service that tracks active taps and flags safety/wastage alerts (e.g., unattended running water).
- `anomaly.py`: Implements the leak detection algorithm (`detect_leak`) which compares current flow metrics against historical operational baselines.
- `main.py`: The primary simulation script orchestrating the components to demonstrate an end-to-end execution lifecycle.

## Features

- **State Tracking:** Programmatic control over tap states (`turn_on`, `turn_off`) with configurable flow rates.
- **Unattended Run Alerts:** Automated validation to check if a tap remains open without supervision over a simulated period.
- **Statistical Leak Detection:** Basic algorithmic approach comparing active flow data against a `flow_history` baseline to catch abnormal surges or drops indicative of a leak.

## Getting Started

### Prerequisites

- Python 3.6 or higher

### Project Setup

1. Ensure all core modules (`tap.py`, `monitor.py`, `anomaly.py`) are present in your working directory alongside the main runner script.
2. Structure your main execution file (e.g., `main.py`) as follows:

```python
import time
from tap import Tap
from monitor import Monitor
from anomaly import detect_leak

# Initialize Monitor and Taps
monitor = Monitor()
tap1 = Tap("Tap-1")
tap2 = Tap("Tap-2")

# Historical flow data baseline (in liters/minute or equivalent unit)
flow_history = [4.5, 5.0, 4.8, 5.2, 4.9]

print("Smart Water Usage Monitoring System Started\n")

# Simulate Turning ON Tap-1
tap1.turn_on(flow_rate=5.0)
print("Tap-1 turned ON")

# Simulate the passage of time
time.sleep(2)

# Check for unattended tap conditions
if monitor.check_unattended(tap1):
    print("ALERT: Tap-1 left unattended for too long")

# Execute Anomaly/Leak Detection
current_flow = tap1.flow_rate
if detect_leak(flow_history, current_flow):
    print("ALERT: Possible leak detected in Tap-1")
else:
    print("No leak detected in Tap-1")

# Simulate Turning OFF Tap-1
tap1.turn_off()
print("Tap-1 turned OFF")

print("\nSystem Execution Completed")
```

### Running the Simulation

Execute the main script via your terminal:

```bash
python main.py
```

## Expected Console Output

When running the simulation, the console output will look similar to the following:

```text
Smart Water Usage Monitoring System Started

Tap-1 turned ON
ALERT: Tap-1 left unattended for too long
No leak detected in Tap-1
Tap-1 turned OFF

System Execution Completed
```

## License

This project is open-source and available under the [MIT License](LICENSE).


