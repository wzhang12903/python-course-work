import matplotlib.pyplot as plt

def plot_scores(df):
    plt.figure()
    plt.bar(df["Name"], df["Score"])
    plt.title("Student Scores")
    plt.xlabel("Students")
    plt.ylabel("Score")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_distribution(df):
    plt.figure()
    plt.hist(df["Score"])
    plt.title("Score Distribution")
    plt.xlabel("Score")
    plt.ylabel("Frequency")
    plt.show()
    