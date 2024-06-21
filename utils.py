import matplotlib.pyplot as plt

def plot_statistics(stats):
    plt.figure()
    plt.plot(stats['games'], stats['wins'], label='Wins')
    plt.plot(stats['games'], stats['losses'], label='Losses')
    plt.xlabel('Games')
    plt.ylabel('Count')
    plt.legend()
    plt.show()