import matplotlib.pyplot as plt

def generate_pie_chart(labels, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    plt.savefig('pie.png')
    plt.close()
