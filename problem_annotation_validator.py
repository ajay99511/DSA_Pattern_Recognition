import os
import sys

REQUIRED_SECTIONS = [
    "## Problem Statement Summary",
    "## Recognition Signals",
    "## Step-by-Step Approach",
    "## Clean Python Solution",
    "## Complexity Analysis",
    "## Key Takeaways"
]

def validate_annotation(filepath):
    if not os.path.exists(filepath):
        print(f"Error: File {filepath} not found.")
        return False
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Check all required sections are present
    missing_sections = []
    for section in REQUIRED_SECTIONS:
        if section not in content:
            missing_sections.append(section)
            
    if missing_sections:
        print(f"Validation Failed for {filepath}: Missing sections: {', '.join(missing_sections)}")
        return False
        
    # Check for at least 3 key takeaways
    takeaways_section = content.split("## Key Takeaways")[-1]
    # Simple heuristic: count list items (starting with number or dash)
    lines = takeaways_section.strip().split('\\n')
    insight_count = sum(1 for line in lines if line.strip().startswith(('1.', '2.', '3.', '4.', '5.', '- ')))
    
    if insight_count < 3:
        print(f"Validation Failed for {filepath}: Found {insight_count} key takeaways, minimum 3 required.")
        return False
        
    print(f"Validation Passed for {filepath}.")
    return True

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python problem_annotation_validator.py <path_to_markdown_file>")
        sys.exit(1)
        
    file_to_validate = sys.argv[1]
    success = validate_annotation(file_to_validate)
    sys.exit(0 if success else 1)
