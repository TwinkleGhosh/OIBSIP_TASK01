from sklearn.tree import plot_tree
import matplotlib.pyplot as plt


def visualize_tree(model, feature_names, save_path):
    plt.figure(figsize=(12, 8))
    plot_tree(model, feature_names=feature_names, class_names=True, filled=True)
    plt.savefig(save_path)
    plt.show()
