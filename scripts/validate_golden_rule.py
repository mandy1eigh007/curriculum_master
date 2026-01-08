#!/usr/bin/env python3
"""
Golden Rule Hours Validation Script

<<<<<<< HEAD
Validates that curriculum hours conform to the Golden Rule:
- Core curriculum (excluding Math): 240 hours
- Mathematics: 40 hours
- Total: 280 hours
=======
Validates that the curriculum hours match the Golden Rule:
- Core (excluding Math): 240 hours
- Math: 40 hours
- Total: 280 hours

Also validates that each bucket's subunits sum to the bucket's total.
>>>>>>> origin/main
"""

import sys
import yaml
from pathlib import Path


<<<<<<< HEAD
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
=======
def validate_golden_rule(yaml_path: Path) -> bool:
    """
    Validate the Golden Rule hours structure.
    
    Returns True if validation passes, False otherwise.
    """
    try:
        with open(yaml_path, 'r') as f:
            data = yaml.safe_load(f)
    except Exception as e:
        print(f"❌ Error reading YAML file: {e}")
        return False
    
    if 'buckets' not in data:
        print("❌ No 'buckets' key found in YAML")
        return False
    
    buckets = data['buckets']
    core_total = 0
    math_total = 0
    errors = []
    
    # Validate each bucket
    for bucket in buckets:
        name = bucket.get('name', 'Unknown')
        category = bucket.get('category', 'Unknown')
        hours_total = bucket.get('hours_total', 0)
        subunits = bucket.get('subunits', [])
        
        # Check subunits sum to bucket total
        subunit_sum = sum(subunit.get('hours', 0) for subunit in subunits)
        
        if subunit_sum != hours_total:
            errors.append(
                f"  Bucket '{name}': subunits sum to {subunit_sum} but hours_total is {hours_total}"
            )
        
        # Accumulate by category
        if category == 'core':
            core_total += hours_total
        elif category == 'math':
            math_total += hours_total
        else:
            errors.append(f"  Bucket '{name}': unknown category '{category}'")
    
    # Validate Golden Rule totals
    total = core_total + math_total
    
    print("=" * 60)
    print("Golden Rule Hours Validation")
    print("=" * 60)
    print(f"Core hours (excluding Math): {core_total} (expected: 240)")
    print(f"Math hours: {math_total} (expected: 40)")
    print(f"Total hours: {total} (expected: 280)")
    print("=" * 60)
    
    if errors:
        print("\n❌ Validation Errors:")
        for error in errors:
            print(error)
    
    # Check totals
    success = True
    if core_total != 240:
        print(f"❌ Core hours must equal 240, but got {core_total}")
        success = False
    
    if math_total != 40:
        print(f"❌ Math hours must equal 40, but got {math_total}")
        success = False
    
    if total != 280:
        print(f"❌ Total hours must equal 280, but got {total}")
        success = False
    
    if errors:
        success = False
    
    if success:
        print("\n✅ Golden Rule validation passed!")
    else:
        print("\n❌ Golden Rule validation failed!")
    
    return success


def main():
    """Main entry point."""
    # Default path relative to script location
    script_dir = Path(__file__).parent
    repo_root = script_dir.parent
    yaml_path = repo_root / 'curriculum_data' / 'golden_rule_hours.yaml'
    
    # Allow override via command line
    if len(sys.argv) > 1:
        yaml_path = Path(sys.argv[1])
    
    if not yaml_path.exists():
        print(f"❌ File not found: {yaml_path}")
        sys.exit(1)
    
    success = validate_golden_rule(yaml_path)
    sys.exit(0 if success else 1)
>>>>>>> origin/main


if __name__ == '__main__':
    main()
