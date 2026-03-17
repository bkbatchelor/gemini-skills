# Handling Gradle Multi-Module Projects

When a project has a `settings.gradle` or `settings.gradle.kts` file, it might be a multi-module project.

## Discovery Steps
1. **Identify Subprojects:** Read `settings.gradle` or `settings.gradle.kts`. Look for `include` statements. E.g. `include 'app'`, `include 'core'`, `include 'domain'`.
2. **Analyze Root Build File:** The `build.gradle` or `build.gradle.kts` at the root defines common plugins and configurations via `allprojects { }` or `subprojects { }`.
3. **Analyze Subprojects:** Iterate through each included directory. Read its `build.gradle` or `build.gradle.kts` to identify:
    - Dependencies: specifically `implementation`, `api`, `testImplementation`
    - Plugins: `id "org.springframework.boot"`, `kotlin("jvm")`, etc.
    - Functionality: A brief summary based on the module name and its dependencies.

## Output Structure
For the generated README, document each module in a 'Modules' or 'Architecture' section. Each module should have a description and a list of key dependencies.