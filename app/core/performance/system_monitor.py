import psutil

class SystemMonitor:

    def get_cpu_usage(self):
        return psutil.cpu_percent(interval=None)

    def get_memory_info(self):
        memory = psutil.virtual_memory()

        return {
            "percent": memory.percent,
            "used_gb": memory.used / 1024**3,
            "total_gb": memory.total / 1024**3,
        }

    def get_disk_info(self):
        disk = psutil.disk_usage("C:\\")

        return {
            "percent": disk.percent,
            "used_gb": disk.used / 1024**3,
            "total_gb": disk.total / 1024**3,
        }

    def get_network_info(self):
        network = psutil.net_io_counters()

        return {
            "bytes_sent": network.bytes_sent,
            "bytes_received": network.bytes_recv,
        }
        
    def get_cpu_temperature(self):

        try:
            temperatures = psutil.sensors_temperatures()

            if not temperatures:
                return None

            for entries in temperatures.values():

                for entry in entries:

                    if entry.current:
                        return entry.current

        except Exception:
            pass

        return None    