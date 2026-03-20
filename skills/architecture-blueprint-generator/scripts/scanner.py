#!/usr/bin/env python3
import os
import json
import argparse
import sys

def detect_project_type(root_dir):
    indicators = {
        'package.json': 'Node.js / JavaScript / TypeScript',
        'requirements.txt': 'Python',
        'pyproject.toml': 'Python',
        'pom.xml': 'Java (Maven)',
        'build.gradle': 'Java (Gradle)',
        'build.gradle.kts': 'Kotlin (Gradle)',
        'Cargo.toml': 'Rust',
        'go.mod': 'Go',
        'Gemfile': 'Ruby',
        'composer.json': 'PHP',
        'Program.cs': '.NET (C#)',
        'App.xaml': '.NET (WPF/UWP)'
    }
    
    project_types = []
    
    # Check for frontend frameworks in package.json
    package_json_path = os.path.join(root_dir, 'package.json')
    if os.path.exists(package_json_path):
        try:
            with open(package_json_path, 'r') as f:
                data = json.load(f)
                deps = list(data.get('dependencies', {}).keys()) + list(data.get('devDependencies', {}).keys())
                if 'react' in deps:
                    project_types.append('React')
                if 'vue' in deps:
                    project_types.append('Vue')
                if '@angular/core' in deps:
                    project_types.append('Angular')
                if 'next' in deps:
                    project_types.append('Next.js')
                if 'nuxt' in deps:
                    project_types.append('Nuxt.js')
                if 'svelte' in deps:
                    project_types.append('Svelte')
        except Exception:
            pass

    # Check root for general indicators
    for item in os.listdir(root_dir):
        if item in indicators:
            pt = indicators[item]
            if pt not in project_types:
                project_types.append(pt)
                
    # Check for .csproj files
    for item in os.listdir(root_dir):
        if item.endswith('.csproj'):
            if '.NET (C#)' not in project_types:
                project_types.append('.NET (C#)')
                
    if not project_types:
        return "Unknown"
    return ", ".join(project_types)

def detect_architecture(root_dir):
    # Basic heuristic based on folder names
    patterns = {
        'MVC': ['controllers', 'models', 'views'],
        'Hexagonal / Clean Architecture': ['domain', 'infrastructure', 'application', 'adapters', 'core', 'usecases'],
        'Microservices': ['services', 'api-gateway', 'eureka', 'discovery'],
        'Serverless': ['functions', 'lambdas', 'handlers', 'serverless.yml']
    }
    
    found_dirs = set()
    for root, dirs, files in os.walk(root_dir):
        # Ignore common hidden/build dirs
        dirs[:] = [d for d in dirs if not d.startswith('.') and d not in ('node_modules', 'venv', 'env', 'build', 'dist', 'target', 'out')]
        for d in dirs:
            found_dirs.add(d.lower())
            
    scores = {pattern: 0 for pattern in patterns}
    
    for pattern, indicators in patterns.items():
        for indicator in indicators:
            if indicator in found_dirs:
                scores[pattern] += 1
                
    # Find the pattern with the highest score
    best_pattern = max(scores, key=scores.get)
    if scores[best_pattern] > 0:
        return best_pattern
    else:
        return "Unclear / Monolithic"

def main():
    parser = argparse.ArgumentParser(description="Scan codebase for project type and architecture.")
    parser.add_argument("dir", nargs="?", default=".", help="Directory to scan")
    args = parser.parse_args()
    
    root_dir = os.path.abspath(args.dir)
    if not os.path.isdir(root_dir):
        print(f"Error: Directory '{root_dir}' not found.", file=sys.stderr)
        sys.exit(1)
        
    project_type = detect_project_type(root_dir)
    arch_pattern = detect_architecture(root_dir)
    
    result = {
        "project_type": project_type,
        "architecture_pattern": arch_pattern
    }
    
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
