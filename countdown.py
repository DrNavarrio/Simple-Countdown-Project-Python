import time

start_time = time.time()

for i in range(60, 0, -1):
    print(i)
    time.sleep(1)

end_time = time.time()

elapsed_time = end_time - start_time
print(f"Countdown completed in {elapsed_time:.2f} seconds.")
