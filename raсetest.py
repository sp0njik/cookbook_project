# from threading import Thread, Lock


# class Counter:
#     def __init__(self):
#         self.value = 0
#         self.lock = Lock()

#     def change(self):
#         with self.lock:
#             self.value += int(1)


# def work(counter: Counter, operations: int):
#     for _ in range(operations):
#         counter.change()


# def run_threads(counter: Counter, threads_count: int, operations: int):
#     threads = []
#     for _ in range(threads_count):
#         thread = Thread(target=work, args=(counter, operations))
#         thread.start()
#         threads.append(thread)
#     for thread in threads:
#         thread.join()


# if __name__ == "__main__":
#     threads_count = 3
#     operations = 1_000_000
#     counter = Counter()
#     expected_value = threads_count * operations
#     run_threads(counter, threads_count, operations)
#     print(counter.value, expected_value)
    