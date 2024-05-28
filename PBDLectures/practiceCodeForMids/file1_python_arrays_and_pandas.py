import pandas as pd
from array import array
import numpy as np

def main():
    arr = array('i', [1, 3, 5, 7, 9])
    print(type(arr))
    print(arr)
    for i in range(len(arr)):
        print(arr[i], end=' ')
    print()
    np_arr = np.array(arr)
    print(np_arr[0::2])
    pd_series = pd.Series(np_arr)
    print(pd_series)

if __name__ == '__main__':
    main()