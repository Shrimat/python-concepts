import multiprocessing
import time

def do_work(string, seconds):
    print(f"Starting work for {string}")
    time.sleep(seconds)
    print(f"Work for {string} done!")

if __name__ == "__main__":
    args = ["Shrimat", "Kapoor", "Python"]
    processes = [multiprocessing.Process(target=do_work, args=(arg, 1)) for arg in args]

    for p in processes:
        p.start()

    for p in processes:
        p.join()