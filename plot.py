import json
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

if __name__ == "__main__":
    server = [800, 1000, 1200, 1400, 1600, 1800, 2000]

    plt_data = list()

    for mhz in server:
        with open("results_16/sk_2000_{}.json".format(mhz)) as f:
            data = json.loads(f.read())
            for lat in data["1"]:
                plt_data.append({'mhz': mhz, 'lat': lat})

    sns.set(style="whitegrid")
    plot = sns.barplot(x="mhz", y="lat", data=pd.DataFrame(plt_data))
    plt.savefig('plot_16.png')
