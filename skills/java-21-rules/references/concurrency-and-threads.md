# Concurrency, Threading, Virtual Threads, and Pinning

Java 21 introduces significant enhancements to concurrency, most notably through Virtual Threads. Follow these rules and guidelines when developing concurrently.

## General Threading Rules

1. **Prefer `await()` over `sleep()`:** When a thread needs to wait for a state change or condition, use `Condition.await()` (with `ReentrantLock`) instead of `Thread.sleep()`. `Thread.sleep()` is non-responsive to state changes and can lead to inefficient execution or race conditions. Using `await()` allows the thread to be efficiently suspended and woken up exactly when the condition it is waiting for becomes true.
   ```java
   // Bad: Sleeping to wait for a condition
   while (!ready) {
       Thread.sleep(100); 
   }

   // Good: Using await() to wait efficiently
   lock.lock();
   try {
       while (!ready) {
           condition.await();
       }
   } finally {
       lock.unlock();
   }
   ```

## Virtual Threads

Virtual Threads (`java.lang.Thread.Builder.OfVirtual`) are lightweight threads managed by the JVM rather than the OS. They drastically reduce the overhead of creating and scheduling threads.

### Rules

1. **Do Not Pool Virtual Threads:** Virtual threads are cheap to create and destroy. Never pool them. Instead, create a new virtual thread for each concurrent task.
   ```java
   // Bad: Pooling virtual threads
   ExecutorService executor = Executors.newFixedThreadPool(10);
   
   // Good: Using an executor that spawns a new virtual thread for each task
   try (var executor = Executors.newVirtualThreadPerTaskExecutor()) {
       executor.submit(() -> doWork());
   }
   ```

2. **Prefer Virtual Threads for I/O-Bound Work:** Virtual threads excel in scenarios involving blocking I/O (e.g., HTTP requests, database calls).
3. **Avoid Virtual Threads for CPU-Bound Work:** CPU-intensive tasks should continue to rely on platform threads or parallel streams since virtual threads do not magically increase the number of available CPU cores.

## Thread Pinning

"Pinning" occurs when a virtual thread is blocked while holding a monitor lock (e.g., inside a `synchronized` block) or executing a native method. When pinned, the virtual thread prevents the underlying OS carrier thread from executing other virtual threads, reducing scalability.

### Rules

1. **Avoid `synchronized` in I/O Blocking Sections:** Replace `synchronized` blocks with `ReentrantLock` when the critical section involves blocking I/O operations.
   ```java
   // Bad: Pinning risk if networkCall() blocks
   synchronized(this) {
       networkCall(); 
   }

   // Good: ReentrantLock avoids pinning
   private final ReentrantLock lock = new ReentrantLock();
   lock.lock();
   try {
       networkCall();
   } finally {
       lock.unlock();
   }
   ```
2. **Keep Synchronized Blocks Fast:** Using `synchronized` is still perfectly acceptable for fast, CPU-bound critical sections (like updating a counter or a small memory state). Just avoid blocking I/O inside them.

## Structured Concurrency (Preview in Java 21)

Though a preview feature in Java 21, Structured Concurrency (`StructuredTaskScope`) provides a robust way to treat multiple concurrent tasks as a single unit of work.

### Rules

1. **Scope Lifecycles:** Use try-with-resources to cleanly start and join concurrent subtasks. If one task fails, others can be automatically cancelled, preventing thread leaks.
   ```java
   try (var scope = new StructuredTaskScope.ShutdownOnFailure()) {
       Supplier<String> user = scope.fork(() -> fetchUser());
       Supplier<String> order = scope.fork(() -> fetchOrder());

       scope.join(); // Wait for both to finish
       scope.throwIfFailed(); // Propagate errors if any task failed

       return new Response(user.get(), order.get());
   }
   ```
