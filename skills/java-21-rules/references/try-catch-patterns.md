# Try-Catch Statements and Error Handling in Java 21

Modern Java requires clean and resource-safe error handling. Combine traditional exception handling with newer concurrency models carefully to prevent resource leaks and silent failures.

## Rules

### 1. Always Use Try-With-Resources

If a class implements `AutoCloseable`, it **must** be managed by a try-with-resources statement. This guarantees proper resource release (file handles, streams, network connections) even when an exception is thrown.

```java
// Bad: Manual close logic is prone to error and verbose
BufferedReader br = new BufferedReader(new FileReader("file.txt"));
try {
    return br.readLine();
} finally {
    if (br != null) br.close();
}

// Good: Try-with-resources
try (var br = new BufferedReader(new FileReader("file.txt"))) {
    return br.readLine();
} catch (IOException e) {
    // Handle specific exceptions logically
}
```

### 2. Multi-Catch Clauses

When handling multiple exceptions that share the same recovery logic, combine them using the multi-catch `|` operator instead of writing duplicate catch blocks.
```java
try {
    processData();
} catch (IOException | SQLException e) {
    logger.error("Failed to process data due to I/O or database error", e);
    throw new ProcessingException("Processing failed", e);
}
```

### 3. Handle Exceptions at the Edge of Virtual Threads

Because Virtual Threads run asynchronously and are so lightweight, unhandled exceptions can easily get lost or terminate the thread silently if not carefully managed by an executor or a structured task scope.

**When using `ExecutorService` (like `newVirtualThreadPerTaskExecutor`):**
Make sure you either submit tasks using `.submit()` and properly handle the resulting `Future`, or explicitly catch exceptions inside the `Runnable`/`Callable` passed to `.execute()`.

### 4. Throwing inside Structured Concurrency (Preview)

When using `StructuredTaskScope` in Java 21, the default scopes (`ShutdownOnFailure`, `ShutdownOnSuccess`) make error handling significantly safer across sub-tasks.

Use `.throwIfFailed()` to automatically bubble up exceptions from cancelled or failed sibling threads back to the parent thread's call stack.

```java
try (var scope = new StructuredTaskScope.ShutdownOnFailure()) {
    Supplier<String> task1 = scope.fork(() -> { throw new RuntimeException("Failed!"); });
    scope.join();
    
    // Throws an exception containing "Failed!" if task1 failed
    scope.throwIfFailed(); 
} catch (ExecutionException e) {
    // Correctly catching errors propagated from the structured scope
    logger.error("A subtask failed during structured execution", e);
} catch (InterruptedException e) {
    Thread.currentThread().interrupt(); // Restore interrupted status
}
```