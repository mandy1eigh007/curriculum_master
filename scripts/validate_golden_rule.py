#!/usr/bin/env python3
"""
Golden Rule Hours Validation Script

Validates that the curriculum hours match the Golden Rule:
- Core (excluding Math): 240 hours
- Math: 40 hours
- Total: 280 hours

Also validates that each bucket's subunits sum to the bucket's total.
"""

import sys
import yaml
from pathlib import Path


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


if __name__ == '__main__':
    main()
