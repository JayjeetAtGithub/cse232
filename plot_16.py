import json
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

if __name__ == "__main__":
    server = [800, 1000, 1200, 1400, 1600, 2000]

    plt_data = list()
    with open("results_16/pq_2000_2000.json", "r") as f:
        data = json.loads(f.read())
        for lat in data["1"]:
            plt_data.append({'mhz': "2000**", 'lat': lat})

    for mhz in reversed(server):
        with open("results_16/sk_2000_{}.json".format(mhz)) as f:
            data = json.loads(f.read())
            for lat in data["1"]:
                plt_data.append({'mhz': str(mhz), 'lat': lat})



    sns.set(style="whitegrid")
    plot = sns.barplot(x="mhz", y="lat", data=pd.DataFrame(plt_data), palette="Blues")
    plot.set_xlabel("Frequency (MHz)", fontsize = 14)
    plot.set_ylabel("Latency (s)", fontsize = 14)
    plt.tick_params(axis='both', which='major', labelsize=14)
    plt.title('16 Storage Servers', fontsize = 14)
    plt.savefig('plot_16.pdf')
