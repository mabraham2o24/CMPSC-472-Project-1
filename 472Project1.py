import threading
import multiprocessing
import timeit
import os


# Class to represent a Thread
class Thread:
    def __init__(self, tid):
        # Initialize a thread with an ID and default status 'Running'
        self.tid = tid
        self.status = "Running"  


# Class to represent a Process
class Process:
    def __init__(self, pid):
        # Initialize a process with a Process ID (PID) and an empty list to store threads
        self.pid = pid
        self.threads = []  


# Class to manage Processes and Threads
class ProcessManager:
    def __init__(self):
        # Initialize the Process Manager with an empty list to store processes
        self.processes = []  

    # Create a new process with given PID
    def create_process(self, pid):
        new_process = Process(pid)  # Create a new Process object
        self.processes.append(new_process)  # Add the process to the list
        print(f"Process {pid} created.")

    # Create a new thread within a process with given PID and TID
    def create_thread(self, pid, tid):
        # Find the process with the given PID
        for process in self.processes:
            if process.pid == pid:
                new_thread = Thread(tid)  # Create a new Thread object
                process.threads.append(new_thread)  # Add the thread to the process
                print(f"Thread {tid} created for Process {pid}.")
                return
        print(f"Process {pid} not found.")

    # Display information about processes and threads
    def display_processes(self):
        print("\n=== Process and Thread Manager ===")
        # Iterate through each process and its associated threads
        for process in self.processes:
            print(f"Process ID: {process.pid}")
            print("Threads:")
            for thread in process.threads:
                print(f" - Thread ID: {thread.tid}, Status: {thread.status}")
            print()

    # Kill a process with given PID
    def kill_process(self, pid):
        for process in self.processes:
            if process.pid == pid:
                self.processes.remove(process)  # Remove the process from the list
                print(f"Process {pid} killed.")
                return
        print(f"Process {pid} not found.")

    # Kill a thread within a process with given PID and TID
    def kill_thread(self, pid, tid):
        for process in self.processes:
            if process.pid == pid:
                for thread in process.threads:
                    if thread.tid == tid:
                        process.threads.remove(thread)  # Remove the thread from the process
                        print(f"Thread {tid} killed for Process {pid}.")
                        return
                print(f"Thread {tid} not found for Process {pid}.")
                return
        print(f"Process {pid} not found.")

    # Suspend a thread within a process with given PID and TID
    def suspend_thread(self, pid, tid):
        for process in self.processes:
            if process.pid == pid:
                for thread in process.threads:
                    if thread.tid == tid:
                        thread.status = "Suspended"  # Update the thread status
                        print(f"Thread {tid} suspended for Process {pid}.")
                        return
                print(f"Thread {tid} not found for Process {pid}.")
                return
        print(f"Process {pid} not found.")

    # Resume a suspended thread within a process with given PID and TID
    def resume_thread(self, pid, tid):
        for process in self.processes:
            if process.pid == pid:
                for thread in process.threads:
                    if thread.tid == tid:
                        thread.status = "Running"  # Update the thread status
                        print(f"Thread {tid} resumed for Process {pid}.")
                        return
                print(f"Thread {tid} not found for Process {pid}.")
                return
        print(f"Process {pid} not found.")


# Function to test the Multi-Process and Thread Manager feature
def test_multi_process_and_thread_manager():
    manager = ProcessManager()

    while True:
        # Display the menu options
        print("\n=== Multi-Process and Thread Manager ===")
        print("1. Create a Process")
        print("2. Create a Thread")
        print("3. Display Processes and Threads")
        print("4. Kill a Process")
        print("5. Kill a Thread")
        print("6. Suspend a Thread")
        print("7. Resume a Thread")
        print("8. Exit")

        # Get user input for the selected option
        choice = input("Select an option: ")

        # Perform actions based on user choice
        if choice == '1':
            pid = input("Enter Process ID: ")
            manager.create_process(pid)
        elif choice == '2':
            pid = input("Enter Process ID: ")
            tid = input("Enter Thread ID: ")
            manager.create_thread(pid, tid)
        elif choice == '3':
            manager.display_processes()
        elif choice == '4':
            pid = input("Enter Process ID to kill: ")
            manager.kill_process(pid)
        elif choice == '5':
            pid = input("Enter Process ID: ")
            tid = input("Enter Thread ID to kill: ")
            manager.kill_thread(pid, tid)
        elif choice == '6':
            pid = input("Enter Process ID: ")
            tid = input("Enter Thread ID to suspend: ")
            manager.suspend_thread(pid, tid)
        elif choice == '7':
            pid = input("Enter Process ID: ")
            tid = input("Enter Thread ID to resume: ")
            manager.resume_thread(pid, tid)
        elif choice == '8':
            print("Exiting the Multi-Process and Thread Manager...")
            break
        else:
            print("Invalid choice. Please select a valid option.")

# Class to manage inter-process communication
class IPCManager:
    def __init__(self):
        self.shared_memory = {}  # Dictionary to simulate shared memory
        self.message_queue = []  # List to simulate message passing

    # Send a message from sender to receiver
    def send_message(self, sender, receiver, message):
        start_time = timeit.default_timer()  # Record the start time
        # Simulate message passing
        self.message_queue.append((sender, receiver, message))
        end_time = timeit.default_timer()  # Record the end time
        print(f"Message sent: From {sender} to {receiver}: {message}. Time taken: {end_time - start_time:.6f} seconds")

    # Receive a message intended for the receiver
    def receive_message(self, receiver):
        start_time = timeit.default_timer()  # Record the start time
        # Simulate message receiving
        for idx, (sender, recv, message) in enumerate(self.message_queue):
            if recv == receiver:
                del self.message_queue[idx]
                end_time = timeit.default_timer()  # Record the end time
                print(f"Message received by {receiver}: From {sender}: {message}. Time taken: {end_time - start_time:.6f} seconds")
                return message
        return None

    # Write data to shared memory
    def write_to_shared_memory(self, key, data):
        # Simulate writing to shared memory
        self.shared_memory[key] = data

    # Read data from shared memory
    def read_from_shared_memory(self, key):
        # Simulate reading from shared memory
        return self.shared_memory.get(key)

# Class to represent a process in parallel text file processing
class TextFileProcessor:
    def __init__(self, filename):
        self.filename = filename
        self.file_content = ""  # Store the content of the text file

    # Load the content of the text file into memory
    def load_file(self):
        with open(self.filename, 'r') as file:
            self.file_content = file.read()

    # Convert characters to uppercase within a given segment of the file content
    def convert_to_uppercase(self, start, end):
        segment_content = self.file_content[start:end]
        self.file_content = self.file_content[:start] + segment_content.upper() + self.file_content[end:]

    # Count occurrences of each character
    def count_character_occurrences(self):
        """
        Counts the occurrences of each alphabetical character in the file content.

        Returns:
            character_count (dict): A dictionary containing character counts.
        """
        character_count = {}  # Initialize an empty dictionary to store character counts
        for char in self.file_content:
            if char.isalpha():  # Check if the character is alphabetical
                if char in character_count:  # If the character is already in the dictionary
                    character_count[char] += 1  # Increment its count
                else:
                    character_count[char] = 1  # Otherwise, add it to the dictionary with a count of 1
        return character_count  # Return the dictionary containing character counts

# Function to process a large text file
def process_large_text_file(filename):
    processor = TextFileProcessor(filename)
    processor.load_file()

    start_time = timeit.default_timer()

    # Perform text processing operations
    processor.convert_to_uppercase(0, len(processor.file_content))
    character_count = processor.count_character_occurrences()

    end_time = timeit.default_timer()
    execution_time = end_time - start_time

    # Print proof of processing and performance metrics
    print("Sample of converted text:")
    print(processor.file_content[:100])  # Print the first 100 characters
    print("Character occurrences:", character_count)
    print(f"Execution time: {execution_time:.6f} seconds")

# Function to test IPC mechanisms
def test_ipc():
    # Test case: Few short messages
    print("\nTesting IPC with few short messages...")
    ipc = IPCManager()  # Create an IPCManager instance
    # Send 3 short messages from one process to another
    ipc.send_message("Process A", "Process B", "Short Message 1")
    ipc.send_message("Process C", "Process D", "Short Message 2")
    ipc.send_message("Process E", "Process F", "Short Message 3")
    # Receive 3 short messages in the receiving process
    ipc.receive_message("Process B")
    ipc.receive_message("Process D")
    ipc.receive_message("Process F")

    # Test case: Few long messages
    print("\nTesting IPC with few long messages...")
    ipc.send_message("Process G", "Process H", "This is a long message containing more text.")
    ipc.send_message("Process I", "Process J", "Another long message to test the IPC mechanism.")
    ipc.receive_message("Process H")
    ipc.receive_message("Process J")

# Main function to provide a menu-based user interface
def main():
    while True:
        # Display the menu options
        print("\n=== Simple User Interface ===")
        print("1. Test Multi-Process and Thread Manager")
        print("2. Test Inter-Process Communication (IPC)")
        print("3. Test Parallel Text File Processing")
        print("4. Exit")

        # Get user input for the selected option
        choice = input("Select an option: ")

        # Perform actions based on user choice
        if choice == '1':
          test_multi_process_and_thread_manager()
        elif choice == '2':
            print("\n=== Testing Inter-Process Communication (IPC) ===")
            test_ipc()
        elif choice == '3':
            print("\n=== Testing Parallel Text File Processing ===")
            process_large_text_file("data.txt")
        elif choice == '4':
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    # Start the program
    main()
