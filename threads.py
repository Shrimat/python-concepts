import threading
import time
import concurrent.futures

def do_work(seconds):
    print("Starting work...")
    time.sleep(seconds)
    return "Work done!"

# threads = []
# for i in range(5):
#     thread = threading.Thread(target=do_work, args=(1,))
#     threads.append(thread)
#     thread.start()

# for thread in threads:
#     thread.join()

with concurrent.futures.ThreadPoolExecutor() as executor:
    results = [executor.submit(do_work, 1) for _ in range(10)]
    for f in concurrent.futures.as_completed(results):
        print(f.result())
