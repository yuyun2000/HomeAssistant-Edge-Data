"""
设备管理模块 - 处理设备相关的操作
"""
import random
from typing import List, Dict, Optional
from config import DEVICES, SERVICES


class DeviceManager:
    """设备管理器"""
    
    def __init__(self):
        self.devices = DEVICES
        self.services = SERVICES
    
    def get_all_devices_by_type(self, device_type: str) -> List[Dict]:
        """
        获取指定类型的所有设备
        
        Args:
            device_type: 设备类型 (light, cover, lock, fan, timer, vacuum, media_player)
            
        Returns:
            设备列表
        """
        return self.devices.get(device_type, [])
    
    def get_random_device(self, device_type: str) -> Optional[Dict]:
        """
        随机获取一个指定类型的设备
        
        Args:
            device_type: 设备类型
            
        Returns:
            设备信息字典
        """
        devices = self.get_all_devices_by_type(device_type)
        return random.choice(devices) if devices else None
    
    def get_random_devices(self, device_type: str, count: int) -> List[Dict]:
        """
        随机获取多个指定类型的设备
        
        Args:
            device_type: 设备类型
            count: 需要的设备数量
            
        Returns:
            设备列表
        """
        devices = self.get_all_devices_by_type(device_type)
        if not devices:
            return []
        
        # 如果请求数量大于可用设备数，返回所有设备
        count = min(count, len(devices))
        return random.sample(devices, count)
    
    def get_device_type(self, device_id: str) -> Optional[str]:
        """
        根据设备ID获取设备类型
        
        Args:
            device_id: 设备ID
            
        Returns:
            设备类型
        """
        for device_type, devices in self.devices.items():
            for device in devices:
                if device["id"] == device_id:
                    return device_type
        return None
    
    def get_all_device_types(self) -> List[str]:
        """获取所有设备类型"""
        return list(self.devices.keys())
    
    def format_devices_for_system_prompt(self) -> str:
        """
        格式化设备信息用于系统提示
        
        Returns:
            格式化的设备字符串
        """
        device_lines = []
        for device_type, devices in self.devices.items():
            for device in devices:
                device_lines.append(f"{device['id']} '{device['name']}'")
        return "\n".join(device_lines)
    
    def format_services_for_system_prompt(self, device_types: List[str] = None) -> str:
        """
        格式化服务信息用于系统提示（根据设备类型）
        
        Args:
            device_types: 设备类型列表，如果为None则返回所有服务
            
        Returns:
            格式化的服务字符串
        """
        if device_types is None:
            device_types = list(self.services.keys())
        
        all_services = []
        for device_type in device_types:
            if device_type in self.services:
                all_services.extend(self.services[device_type])
        
        # 去重并排序
        all_services = sorted(set(all_services))
        return ", ".join(all_services)
    
    def get_device_types_from_devices(self, devices: List[Dict]) -> List[str]:
        """
        从设备列表中提取设备类型
        
        Args:
            devices: 设备列表
            
        Returns:
            设备类型列表（去重）
        """
        device_types = set()
        for device in devices:
            device_type = self.get_device_type(device['id'])
            if device_type:
                device_types.add(device_type)
        return list(device_types)
