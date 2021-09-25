import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import os
from collections import Counter


def zipfsLaw():
    wordCounter = getWordCounter()
    totalWordCount = sum(wordCounter.values())

    # Make an array, sorted by word rank. So, index is rank.
    wordRanks = sorted(wordCounter, key=lambda x: wordCounter[x], reverse=True)

    # Calculate the probability of each word
    wordFrequencies = []
    for w in wordRanks:
        wordFrequencies.append(wordCounter[w])

    # for i in range(len(wordRanks)):
    #     print(i*wordProbabilities[i])

    # Plot the Ziph's Law line.
    ziphLineY = []
    K = 0.1 * totalWordCount
    ziphLineY.extend([K / (x + 1) for x in range(len(wordRanks))])
    plt.plot(range(1, len(wordRanks) + 1), ziphLineY, label="Zipf", c="g")

    # Graph the probabilities vs rank:
    plt.scatter(range(1, len(wordRanks) + 1), wordFrequencies, s=5, label="Data", c="r")
    # plt.locator_params(nbins=10)

    # Naming stuff
    plt.xlabel("Rank\n(by decreasing frequency)")
    plt.ylabel("Frequency")
    plt.title("Zipf's Law")

    # Make x and y scale log base 10
    plt.yscale("log", base=10)
    plt.xscale("log", base=10)
    plt.legend()  # Display the legend
    plt.show()


def heapsLaw():
    pass


def getWordCounter() -> Counter:
    """
    Generates a Counter of words from all the .html files in the ./repository/ folder.

    Parameters:
        TODO language (str): a specific language to get the html files for.
    """
    fileNames = os.listdir("./repository")
    wordCounter = Counter()
    # Parse through all file names in ./repository/
    for name in fileNames:
        if name[-5:] == ".html":  # Only open files labeled .html
            with open("./repository/" + name) as f:
                rawHTML = f.read()  # Get the raw html

                # Get only the text in the raw html, then make it all lowercase. Then merge all of the texts into a single string.
                bs = BeautifulSoup(rawHTML, "lxml")
                cleanText = "".join(bs.getText(" ").lower())
                wordCounter.update(cleanText.split())  # Add words to wordCounter.

    # TODO handle words that aren't words or that could contain non-letter characters, such as ,()[]{}\|-_=~ etc
    # TODO make sure wordCounter actually contains all the "textual content"

    return wordCounter


if __name__ == "__main__":
    zipfsLaw()
    heapsLaw()
