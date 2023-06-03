from joblib import Parallel, delayed
from tqdm import tqdm # to show a progress bar

def calcula(num):
    # do some processing here
    print("Calculando {}".format(num))

Parallel(n_jobs=3)(delayed(calcula)(i) for i in tqdm(range(10)))

# python3 -m pip install joblib
# python3 -m pip install tqdm 