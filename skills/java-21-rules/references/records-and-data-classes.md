# Records and Data Classes in Java 21

Java 16+ (and fully supported in 21) introduces **Records**, which are a concise way to model immutable data. They should be preferred over traditional POJOs for simple data carriers.

## Rules

### 1. Prefer Records over POJOs for Data Carriers
If a class is primarily used to hold data (a "data carrier") and its fields are immutable, use a `record`. Records automatically provide `equals()`, `hashCode()`, `toString()`, and accessor methods.

```java
// Bad: Verbose POJO
public class User {
    private final String name;
    private final int age;

    public User(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public String getName() { return name; }
    public int getAge() { return age; }
    // plus boilerplate equals, hashCode, toString...
}

// Good: Concise Record
public record User(String name, int age) {}
```

### 2. Immutability by Default
Records are shallowly immutable. All fields are `final`. If you need mutable state, a traditional class (POJO) is still appropriate, but aim for immutability whenever possible.

### 3. Use Compact Constructors for Validation
If you need to validate data in a record, use a compact constructor. It avoids repeating the record's components.

```java
public record User(String name, int age) {
    public User {
        if (age < 0) {
            throw new IllegalArgumentException("Age cannot be negative");
        }
    }
}
```

### 4. Pattern Matching for Records
Java 21 enhances pattern matching for records, allowing you to deconstruct them in `instanceof` and `switch` statements.

```java
if (obj instanceof User(String name, int age)) {
    System.out.println("User: " + name + ", Age: " + age);
}
```
