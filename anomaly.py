import statistics
def detect_leak(flow_data,current_flow):
    if len(flow_data)<2:
        return False
    mean=statistics.mean(flow_data)
    std=statistics.stdev(flow_data)
    return current_flow> mean+2*std
