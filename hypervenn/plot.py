import matplotlib.pyplot as plt

def plot_venn(sets):
    labels = list(sets.keys())
    sizes = [len(v) for v in sets.values()]
    plt.pie(sizes, labels=labels, autopct='%1.1f%%')
    plt.title("HyperVenn - Simple View")
    plt.show()
