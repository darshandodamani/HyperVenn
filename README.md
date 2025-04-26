# HyperVenn

**HyperVenn** is an open-source Python library to create beautiful, scalable Venn diagrams for up to 10 sets.

🔵 Scalable to multiple classes  
🔵 Easy to use  
🔵 Designed for Data Science, Machine Learning, Visualization

## Quickstart

```python
from hypervenn import plot_venn

sets = {
    "A": {1, 2, 3, 4},
    "B": {3, 4, 5, 6},
    "C": {4, 5, 7},
}

plot_venn(sets)
