#!/usr/bin/env python3
"""
Golden Rule Hours Validation Script

Validates that curriculum hours conform to the Golden Rule:
- Core curriculum (excluding Math): 240 hours
- Mathematics: 40 hours
- Total: 280 hours
"""

import sys
import yaml
from pathlib import Path


def load_golden_rule_config(config_path):
    """Load the golden rule hours configuration."""
    with open(config_path, 'r') as f:
        return yaml.safe_load(f)


def validate_subunits(bucket_name, bucket_data):
    """Validate that subunits sum to the bucket's hours_total."""
    hours_total = bucket_data.get('hours_total')
    subunits = bucket_data.get('subunits', [])
    
    if hours_total is None:
        print(f"❌ ERROR: {bucket_name} missing 'hours_total'")
        return False
    
    if not subunits:
        print(f"❌ ERROR: {bucket_name} has no subunits")
        return False
    
    subunit_sum = sum(unit.get('hours', 0) for unit in subunits)
    
    if subunit_sum != hours_total:
        print(f"❌ ERROR: {bucket_name} subunits sum to {subunit_sum}, but hours_total is {hours_total}")
        return False
    
    print(f"✓ {bucket_name}: {subunit_sum} hours (subunits match total)")
    return True


def validate_components(bucket_name, bucket_data):
    """Validate that components sum to the bucket's hours_total."""
    hours_total = bucket_data.get('hours_total')
    components = bucket_data.get('components', [])
    
    if hours_total is None:
        print(f"❌ ERROR: {bucket_name} missing 'hours_total'")
        return False
    
    if not components:
        print(f"❌ ERROR: {bucket_name} has no components")
        return False
    
    component_sum = sum(comp.get('hours', 0) for comp in components)
    
    if component_sum != hours_total:
        print(f"❌ ERROR: {bucket_name} components sum to {component_sum}, but hours_total is {hours_total}")
        return False
    
    print(f"✓ {bucket_name}: {component_sum} hours (components match total)")
    return True


def validate_golden_rule(config):
    """Validate the Golden Rule hours constraints."""
    all_valid = True
    
    print("\n=== Golden Rule Hours Validation ===\n")
    
    # Validate core curriculum
    if 'core_curriculum' in config:
        if not validate_subunits('core_curriculum', config['core_curriculum']):
            all_valid = False
        
        core_hours = config['core_curriculum'].get('hours_total')
        if core_hours != 240:
            print(f"❌ ERROR: Core curriculum should be 240 hours, but is {core_hours}")
            all_valid = False
    else:
        print("❌ ERROR: Missing 'core_curriculum' section")
        all_valid = False
    
    # Validate mathematics
    if 'mathematics' in config:
        if not validate_subunits('mathematics', config['mathematics']):
            all_valid = False
        
        math_hours = config['mathematics'].get('hours_total')
        if math_hours != 40:
            print(f"❌ ERROR: Mathematics should be 40 hours, but is {math_hours}")
            all_valid = False
    else:
        print("❌ ERROR: Missing 'mathematics' section")
        all_valid = False
    
    # Validate total
    if 'total_curriculum' in config:
        if not validate_components('total_curriculum', config['total_curriculum']):
            all_valid = False
        
        total_hours = config['total_curriculum'].get('hours_total')
        if total_hours != 280:
            print(f"❌ ERROR: Total curriculum should be 280 hours, but is {total_hours}")
            all_valid = False
    else:
        print("❌ ERROR: Missing 'total_curriculum' section")
        all_valid = False
    
    print()
    if all_valid:
        print("✅ Golden Rule validation PASSED: All hour totals are correct!")
        print("   - Core (excluding Math): 240 hours")
        print("   - Mathematics: 40 hours")
        print("   - Total: 280 hours")
    else:
        print("❌ Golden Rule validation FAILED: Hour totals do not match requirements")
    
    return all_valid


def main():
    """Main entry point for the validation script."""
    config_path = Path(__file__).parent.parent / 'curriculum_data' / 'golden_rule_hours.yaml'
    
    if not config_path.exists():
        print(f"❌ ERROR: Configuration file not found: {config_path}")
        sys.exit(1)
    
    try:
        config = load_golden_rule_config(config_path)
        is_valid = validate_golden_rule(config)
        sys.exit(0 if is_valid else 1)
    except Exception as e:
        print(f"❌ ERROR: Failed to validate golden rule hours: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
