import psutil
import time
import os
from datetime import datetime

def bytes_to_gb(bytes_value):
    """Конвертирует байты в гигабайты с округлением до 2 знаков."""
    return round(bytes_value / (1024 ** 3), 2)


