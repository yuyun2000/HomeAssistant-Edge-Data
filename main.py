"""
主程序 - 用于生成智能家居控制数据
"""
import json
import argparse
from typing import List, Dict
from generators import SequentialGenerator, BatchGenerator, LightControlGenerator, MixedGenerator


class DataGenerator:
    """数据生成主类"""
    
    def __init__(self):
        self.sequential_generator = SequentialGenerator()
        self.batch_generator = BatchGenerator()
        self.light_control_generator = LightControlGenerator()
        self.mixed_generator = MixedGenerator()
    
    def generate_sequential_data(self, count: int = 10, 
                                 operation_count: int = None) -> List[Dict]:
        """
        生成连续操作数据
        
        Args:
            count: 生成数量
            operation_count: 每条数据的操作数量
            
        Returns:
            生成的数据列表
        """
        print(f"正在生成 {count} 条连续操作数据...")
        data = self.sequential_generator.generate(count, operation_count)
        print(f"✓ 成功生成 {len(data)} 条连续操作数据")
        return data
    
    def generate_batch_data(self, count: int = 10, 
                           device_type: str = None) -> List[Dict]:
        """
        生成统一操作数据
        
        Args:
            count: 生成数量
            device_type: 设备类型
            
        Returns:
            生成的数据列表
        """
        print(f"正在生成 {count} 条统一操作数据...")
        data = self.batch_generator.generate(count, device_type)
        print(f"✓ 成功生成 {len(data)} 条统一操作数据")
        return data
    
    def generate_light_control_data(self, count: int = 10,
                                   change_type: str = None) -> List[Dict]:
        """
        生成灯光控制数据（颜色/亮度调整）
        
        Args:
            count: 生成数量
            change_type: 改变类型 ('color', 'brightness', 'both')
            
        Returns:
            生成的数据列表
        """
        print(f"正在生成 {count} 条灯光控制数据...")
        data = self.light_control_generator.generate(count, change_type)
        print(f"✓ 成功生成 {len(data)} 条灯光控制数据")
        return data
    
    def generate_combined_operation_data(self, count: int = 10) -> List[Dict]:
        """
        生成混合操作数据（统一操作+单独操作混合在一起）
        例如：打开所有的灯并把窗帘拉上
        
        Args:
            count: 生成数量
            
        Returns:
            生成的数据列表
        """
        print(f"正在生成 {count} 条混合操作数据...")
        data = self.mixed_generator.generate(count)
        print(f"✓ 成功生成 {len(data)} 条混合操作数据")
        return data
    
    def generate_mixed_data(self, sequential_count: int = 10, 
                           batch_count: int = 10,
                           light_control_count: int = 10,
                           combined_count: int = 10) -> List[Dict]:
        """
        生成混合数据（包含所有类型：连续操作 + 统一操作 + 灯光控制 + 混合操作）
        
        Args:
            sequential_count: 连续操作数据数量
            batch_count: 统一操作数据数量
            light_control_count: 灯光控制数据数量
            combined_count: 混合操作数据数量
            
        Returns:
            生成的数据列表
        """
        print(f"正在生成混合数据...")
        data = []
        data.extend(self.generate_sequential_data(sequential_count))
        data.extend(self.generate_batch_data(batch_count))
        data.extend(self.generate_light_control_data(light_control_count))
        data.extend(self.generate_combined_operation_data(combined_count))
        print(f"✓ 总共生成 {len(data)} 条数据")
        return data
    
    def save_to_file(self, data: List[Dict], filename: str = "generated_data.json"):
        """
        保存数据到文件
        
        Args:
            data: 数据列表
            filename: 输出文件名
        """
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"✓ 数据已保存到 {filename}")
    
    def preview_data(self, data: List[Dict], count: int = 2):
        """
        预览生成的数据
        
        Args:
            data: 数据列表
            count: 预览数量
        """
        print(f"\n{'='*60}")
        print(f"数据预览 (前 {min(count, len(data))} 条)")
        print(f"{'='*60}\n")
        
        for i, item in enumerate(data[:count], 1):
            print(f"--- 数据 {i} ---")
            print(f"用户: {item['messages'][1]['content']}")
            print(f"助手: {item['messages'][2]['content']}")
            print()


def main():
    """主函数"""
    parser = argparse.ArgumentParser(description='智能家居数据生成器')
    parser.add_argument('--type', '-t', 
                       choices=['sequential', 'batch', 'light', 'combined', 'mixed'],
                       default='mixed',
                       help='数据类型: sequential(连续操作), batch(统一操作), light(灯光控制), combined(混合操作), mixed(全部混合)')
    parser.add_argument('--count', '-c', 
                       type=int, 
                       default=30,
                       help='生成数量（mixed模式下为总数）')
    parser.add_argument('--output', '-o', 
                       default='generated_data.json',
                       help='输出文件名')
    parser.add_argument('--preview', '-p', 
                       action='store_true',
                       help='预览生成的数据')
    parser.add_argument('--operations', 
                       type=int,
                       help='连续操作模式下，每条数据的操作数量')
    parser.add_argument('--device-type', 
                       choices=['light', 'cover', 'lock', 'fan', 'vacuum', 'media_player', 'timer','switch'],
                       help='统一操作模式下，指定设备类型')
    parser.add_argument('--change-type',
                       choices=['color', 'brightness', 'both'],
                       help='灯光控制模式下，指定改变类型')
    
    args = parser.parse_args()
    
    # 创建生成器
    generator = DataGenerator()
    
    # 生成数据
    if args.type == 'sequential':
        data = generator.generate_sequential_data(args.count, args.operations)
    elif args.type == 'batch':
        data = generator.generate_batch_data(args.count, args.device_type)
    elif args.type == 'light':
        data = generator.generate_light_control_data(args.count, args.change_type)
    elif args.type == 'combined':
        data = generator.generate_combined_operation_data(args.count)
    else:  # mixed
        # mixed模式下，平均分配数量
        seq_count = args.count // 4
        batch_count = args.count // 4
        light_count = args.count // 4
        combined_count = args.count - seq_count - batch_count - light_count
        data = generator.generate_mixed_data(seq_count, batch_count, light_count, combined_count)
    
    # 预览数据
    if args.preview:
        generator.preview_data(data)
    
    # 保存数据
    generator.save_to_file(data, args.output)
    
    print(f"\n✓ 完成！共生成 {len(data)} 条数据")


if __name__ == '__main__':
    main()
