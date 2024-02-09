from multiprocessing import Process
import subprocess


def run():
    subprocess.run("curl http://localhost:8000/cook_recipe?recipe_id=2")


for i in range(1, 100000):
    p = Process(target=run)
    p.start()


