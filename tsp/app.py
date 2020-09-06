from typing import List

import pandas as pd

from tsp.city import City


def load(data_path: str) -> List[City]:
    data = pd.read_csv(data_path, sep=' ')
    cities = []
    for x, y in data[['x', 'y']].values:
        cities.append(City(x, y))
    return cities


if __name__ == '__main__':
    pass
