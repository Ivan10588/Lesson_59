import psutil
import time
import os
from datetime import datetime

def bytes_to_gb(bytes_value):
    """Конвертирует байты в гигабайты с округлением до 2 знаков."""
    return round(bytes_value / (1024 ** 3), 2)

def get_cpu_info(use_interval_none=False):
    """
    Собирает информацию о загрузке CPU.
    Если use_interval_none=True, использует интервал None (дельта с прошлого замера).
    Иначе делает замер с интервалом 1 сек.
    Возвращает словарь с текущей загрузкой и средними значениями (если доступны).
    """
    if use_interval_none:
        current_percent = psutil.cpu_percent(interval=None)
    else:
        current_percent = psutil.cpu_percent(interval=1)

    avg1, avg5, avg15 = "N/A", "N/A", "N/A"
    try:
        load_avg = psutil.getloadavg()
        avg1, avg5, avg15 = [round(x, 1) for x in load_avg]
    except AttributeError:
        pass

    return {
        "current_percent": current_percent,
        "avg1": avg1,
        "avg5": avg5,
        "avg15": avg15,
    }

def get_memory_info():
    """Собирает информацию об использовании памяти (RAM)."""
    mem = psutil.virtual_memory()
    return {
        "total_gb": bytes_to_gb(mem.total),
        "available_gb": bytes_to_gb(mem.available),
        "used_gb": bytes_to_gb(mem.used),
        "percent_used": round(mem.percent, 1),
    }

def get_disk_info(path=None):
    """Собирает информацию об использовании диска."""
    if path is None:
        path = "C:" if os.name == "nt" else "/"
    disk = psutil.disk_usage(path)
    return {
        "path": path,
        "total_gb": bytes_to_gb(disk.total),
        "free_gb": bytes_to_gb(disk.free),
        "used_gb": bytes_to_gb(disk.used),
        "percent_used": round(disk.percent, 1),
    }

def get_network_info():
    """Собирает информацию об использовании сети (накопленные байты)."""
    net = psutil.net_io_counters()
    return {
        "bytes_sent": net.bytes_sent,
        "bytes_recv": net.bytes_recv,
    }

