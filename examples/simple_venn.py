from hypervenn import plot_venn

if __name__ == "__main__":
    sets = {
        "A": {1, 2, 3, 4},
        "B": {3, 4, 5, 6},
        "C": {4, 5, 7},
    }
    plot_venn(sets)
