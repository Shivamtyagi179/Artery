"""
Artery System Monitor Package
Advanced Screen Intelligence Module
"""

from system_monitor.tracker import ScreenTracker
from system_monitor.analyzer import ScreenAnalyzer
from system_monitor.controller import ScreenController
from system_monitor.memory_bridge import MemoryBridge
from system_monitor.screen_intelligence import ScreenIntelligence

__all__ = [
    "ScreenTracker",
    "ScreenAnalyzer",
    "ScreenController",
    "MemoryBridge",
    "ScreenIntelligence"
]

PACKAGE_NAME = "Artery System Monitor"
VERSION = "2.0"