import threading
import time

def create_file_with_delay(file_number):

    time.sleep(1) 
    filename = f"file_{file_number}.txt"
    with open(filename, 'w') as f:
        f.write("This is a test file.")

    print(f"File {filename} created.")

def run_without_multithreading():

    start_time = time.time()
    for i in range(100):
        create_file_with_delay(i)
    end_time = time.time()

    print(f"Time taken without multithreading: {end_time - start_time} seconds")

def run_with_multithreading():

    start_time = time.time()
    threads = []

    for i in range(1):

        thread = threading.Thread(target=create_file_with_delay, args=(i,))
        thread.start()
        threads.append(thread)

    for thread in threads:

        thread.join()
        end_time = time.time()

    print(f"Time taken with multithreading: {end_time - start_time} seconds")

if __name__ == "__main__":

    print("Running without multithreading:")
    run_without_multithreading()
    
    print("\nRunning with multithreading:")
    run_with_multithreading()
