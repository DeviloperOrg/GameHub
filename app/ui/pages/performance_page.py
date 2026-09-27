import platform
import psutil
import subprocess

from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QGridLayout,
    QLabel,
    QFrame,
    QProgressBar,
)

from app.core.performance.system_monitor import SystemMonitor

class MetricCard(QFrame):

    def __init__(
        self,
        title,
        icon,
        parent=None
    ):
        super().__init__(parent)

        self.setObjectName("StatCard")

        layout = QVBoxLayout(self)

        layout.setContentsMargins(
            18, 16, 18, 16
        )

        layout.setSpacing(8)

        # Header
        header = QHBoxLayout()

        title_label = QLabel(title)

        title_label.setObjectName(
            "StatTitle"
        )

        icon_label = QLabel(icon)

        icon_label.setObjectName(
            "StatIcon"
        )

        header.addWidget(
            title_label
        )

        header.addStretch()

        header.addWidget(
            icon_label
        )

        layout.addLayout(
            header
        )

        # Main value
        self.value = QLabel("0%")

        self.value.setObjectName(
            "StatValue"
        )

        layout.addWidget(
            self.value
        )

        # Progress
        self.progress = QProgressBar()

        self.progress.setRange(
            0,
            100
        )

        self.progress.setValue(0)

        self.progress.setTextVisible(
            False
        )

        self.progress.setFixedHeight(5)

        self.progress.setStyleSheet("""
            QProgressBar {
                background-color: #1A1E27;
                border: none;
                border-radius: 2px;
            }

            QProgressBar::chunk {
                background-color: #8B5CF6;
                border-radius: 2px;
            }
        """)

        layout.addWidget(
            self.progress
        )

        # Extra information
        self.extra = QLabel("Waiting...")

        self.extra.setObjectName(
            "StatExtra"
        )

        layout.addWidget(
            self.extra
        )

    def update_metric(
        self,
        value,
        extra=""
    ):

        value = max(
            0,
            min(100, int(value))
        )

        self.value.setText(
            f"{value}%"
        )

        self.progress.setValue(
            value
        )

        self.extra.setText(
            extra
        )


class PerformancePage(QWidget):

    def __init__(self):

        super().__init__()
        
        self.monitor = SystemMonitor()

        self._build_ui()

        self._setup_timer()

        self.update_metrics()

    # ==================================================
    # UI
    # ==================================================

    def _build_ui(self):

        layout = QVBoxLayout(self)

        layout.setContentsMargins(
            34,
            28,
            34,
            28
        )

        layout.setSpacing(22)

        # ------------------------------------------
        # HEADER
        # ------------------------------------------

        header = QHBoxLayout()

        title_box = QVBoxLayout()

        title = QLabel(
            "Performance Monitor"
        )

        title.setObjectName(
            "PageTitle"
        )

        subtitle = QLabel(
            "Monitor your system in real time."
        )

        subtitle.setObjectName(
            "PageSubtitle"
        )

        title_box.addWidget(title)
        title_box.addWidget(subtitle)

        header.addLayout(
            title_box
        )

        header.addStretch()

        self.status = QLabel(
            "● LIVE"
        )

        self.status.setStyleSheet("""
            QLabel {
                color: #A78BFA;
                font-size: 11px;
                font-weight: 700;
            }
        """)

        header.addWidget(
            self.status
        )

        layout.addLayout(
            header
        )

        # ------------------------------------------
        # METRICS
        # ------------------------------------------

        metrics = QGridLayout()

        metrics.setSpacing(14)

        self.cpu_card = MetricCard(
            "CPU",
            "◉"
        )

        self.gpu_card = MetricCard(
            "GPU",
            "◈"
        )

        self.ram_card = MetricCard(
            "MEMORY",
            "▣"
        )

        self.disk_card = MetricCard(
            "DISK",
            "◫"
        )

        metrics.addWidget(
            self.cpu_card,
            0,
            0
        )

        metrics.addWidget(
            self.gpu_card,
            0,
            1
        )

        metrics.addWidget(
            self.ram_card,
            0,
            2
        )

        metrics.addWidget(
            self.disk_card,
            1,
            0
        )

        layout.addLayout(
            metrics
        )

        # ------------------------------------------
        # SYSTEM INFO
        # ------------------------------------------

        section_title = QLabel(
            "System Information"
        )

        section_title.setObjectName(
            "SectionTitle"
        )

        layout.addWidget(
            section_title
        )

        info_card = QFrame()

        info_card.setObjectName(
            "StatCard"
        )

        info_layout = QGridLayout(
            info_card
        )

        info_layout.setContentsMargins(
            20,
            18,
            20,
            18
        )

        self.cpu_info = self._create_info(
            info_layout,
            "CPU",
            0,
            0
        )

        self.ram_info = self._create_info(
            info_layout,
            "RAM",
            0,
            1
        )

        self.os_info = self._create_info(
            info_layout,
            "Operating System",
            1,
            0
        )

        self.hostname_info = self._create_info(
            info_layout,
            "Computer",
            1,
            1
        )

        layout.addWidget(
            info_card
        )

        # ------------------------------------------
        # NETWORK
        # ------------------------------------------

        network_title = QLabel(
            "Network"
        )

        network_title.setObjectName(
            "SectionTitle"
        )

        layout.addWidget(
            network_title
        )

        network_card = QFrame()

        network_card.setObjectName(
            "StatCard"
        )

        network_layout = QHBoxLayout(
            network_card
        )

        network_layout.setContentsMargins(
            20,
            18,
            20,
            18
        )

        self.download_label = QLabel(
            "↓ 0 KB/s"
        )

        self.download_label.setStyleSheet("""
            QLabel {
                color: #FFFFFF;
                font-size: 14px;
                font-weight: 700;
            }
        """)

        self.upload_label = QLabel(
            "↑ 0 KB/s"
        )

        self.upload_label.setStyleSheet("""
            QLabel {
                color: #FFFFFF;
                font-size: 14px;
                font-weight: 700;
            }
        """)

        network_layout.addWidget(
            self.download_label
        )

        network_layout.addStretch()

        network_layout.addWidget(
            self.upload_label
        )

        layout.addWidget(
            network_card
        )

        layout.addStretch()

    # ==================================================
    # INFO ITEM
    # ==================================================

    def _create_info(
        self,
        parent_layout,
        title,
        row,
        column
    ):

        container = QVBoxLayout()

        title_label = QLabel(
            title
        )

        title_label.setObjectName(
            "StatTitle"
        )

        value_label = QLabel(
            "Detecting..."
        )

        value_label.setStyleSheet("""
            QLabel {
                color: #FFFFFF;
                font-size: 13px;
                font-weight: 600;
            }
        """)

        container.addWidget(
            title_label
        )

        container.addWidget(
            value_label
        )

        parent_layout.addLayout(
            container,
            row,
            column
        )

        return value_label

    # ==================================================
    # TIMER
    # ==================================================

    def _setup_timer(self):

        self.timer = QTimer(self)

        self.timer.setInterval(
            1000
        )

        self.timer.timeout.connect(
            self.update_metrics
        )

        self.timer.start()

    # ==================================================
    # UPDATE
    # ==================================================

    def update_metrics(self):

    # CPU
        cpu_name = "Unknown CPU"

        try:
            result = subprocess.check_output(
                [
                    "wmic",
                    "cpu",
                    "get",
                    "name"
                ],
                text=True
            )

            lines = [
                line.strip()
                for line in result.splitlines()
                if line.strip() and line.strip().lower() != "name"
            ]

            if lines:
                cpu_name = lines[0]

        except Exception:
            pass

        self.cpu_info.setText(cpu_name)
        
        cpu = self.monitor.get_cpu_usage()

        cpu_temperature = self.monitor.get_cpu_temperature()
        
        if cpu_temperature is not None:
            cpu_extra = f"{cpu_temperature:.0f}°C"
        else:
            cpu_extra = "Temperature unavailable"
            
        self.cpu_card.update_metric(
            cpu,
            cpu_extra
        )        
        
        # RAM
        memory = self.monitor.get_memory_info()

        self.ram_card.update_metric(
            memory["percent"],
            f"{memory['used_gb']:.1f} GB / "
            f"{memory['total_gb']:.1f} GB"
        )

        # Disk
        disk = self.monitor.get_disk_info()

        self.disk_card.update_metric(
            disk["percent"],
            f"{disk['used_gb']:.0f} GB / "
            f"{disk['total_gb']:.0f} GB"
        )

        # GPU
        gpu_usage, gpu_extra = self._get_gpu_info()

        self.gpu_card.update_metric(
            gpu_usage,
            gpu_extra
        )

        # System information
        
        self.ram_info.setText(
            f"{memory['total_gb']:.1f} GB"
        )

        self.os_info.setText(
            f"{platform.system()} {platform.release()}"
        )

        self.hostname_info.setText(
            platform.node()
        )

        # Network
        self._update_network()

    # ==================================================
    # GPU
    # ==================================================

    def _get_gpu_info(self):

        try:

            import subprocess

            result = subprocess.run(
                [
                    "nvidia-smi",
                    "--query-gpu=utilization.gpu,"
                    "memory.used,memory.total",
                    "--format=csv,noheader,nounits"
                ],
                capture_output=True,
                text=True,
                timeout=1
            )

            if result.returncode != 0:
                return 0, "NVIDIA GPU unavailable"

            line = result.stdout.strip()

            if not line:
                return 0, "GPU data unavailable"

            parts = [
                x.strip()
                for x in line.split(",")
            ]

            usage = int(
                float(parts[0])
            )

            memory_used = float(
                parts[1]
            )

            memory_total = float(
                parts[2]
            )

            return (
                usage,
                f"{memory_used:.0f} MB / "
                f"{memory_total:.0f} MB VRAM"
            )

        except Exception:

            return (
                0,
                "NVIDIA GPU unavailable"
            )

    # ==================================================
    # NETWORK
    # ==================================================

    def _update_network(self):

        current = (
            psutil.net_io_counters()
        )

        if not hasattr(
            self,
            "_previous_network"
        ):

            self._previous_network = current

            return

        previous = (
            self._previous_network
        )

        download = (
            current.bytes_recv
            - previous.bytes_recv
        )

        upload = (
            current.bytes_sent
            - previous.bytes_sent
        )

        self._previous_network = current

        download_kb = download / 1024
        upload_kb = upload / 1024

        self.download_label.setText(
            f"↓ {download_kb:.1f} KB/s"
        )

        self.upload_label.setText(
            f"↑ {upload_kb:.1f} KB/s"
        )