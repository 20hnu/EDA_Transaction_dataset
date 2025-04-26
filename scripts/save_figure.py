import matplotlib.pyplot as plt

IMAGES_PATH = "/home/bishnu/project/EDA_transaction_data/visuals/plots" # Make directory if it doesn't exist

def save_fig(fig_id, tight_layout=True, fig_extension="png", resolution=1000):
    path = IMAGES_PATH + "/" + f"{fig_id}.{fig_extension}"
    if tight_layout:
        plt.tight_layout()
    plt.savefig(path, format=fig_extension, dpi=resolution)