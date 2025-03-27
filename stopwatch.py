import time

def stopwatch():
    print("Stopwatch started. Press Enter to stop.")
    start_time = time.time()
    input()
    elapsed_time = time.time() - start_time
    print(f"Elapsed time: {elapsed_time:.2f} seconds")

def timer(seconds):
    print(f"Timer set for {seconds} seconds.")
    time.sleep(seconds)
    print("Time's up!")

# Example usage
choice = input("Enter 's' for stopwatch or 't' for timer: ")
if choice == 's':
    stopwatch()
elif choice == 't':
    seconds = int(input("Enter seconds: "))
    timer(seconds)
else:
    print("Invalid choice.")
