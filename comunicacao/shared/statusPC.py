import psutil

def status():
    mem = psutil.virtual_memory()[2]
    CPU = psutil.cpu_percent()
    return {'ram':mem, 'cpu':CPU}