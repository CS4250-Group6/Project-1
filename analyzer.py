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
   print("Number of unique words:", unique_word_count()) # prints number of unique words


def find_unique_words():
    fileNames = os.listdir("repository")
    # Parse through all file names in ./repository/
    for name in fileNames:
        if name[-5:] == ".html":  # Only open files labeled .html
            filePath = os.path.join("repository", name)
            with open(filePath, encoding="utf8") as f:
                rawHTML = f.read()  # Get the raw html

                # Get only the text in the raw html, then make it all lowercase. Then merge all of the texts into a single string.
                bs = BeautifulSoup(rawHTML, "lxml")
                words = bs.getText(" ").split()
                words = [
                    x.strip("0123456789~`^%$#@&*?!.;:'()[]{},/|\\><+=_- \"").lower()
                    for x in words
                ]
                unique_words = []
                for x in words:
                    if x not in unique_words:
                        unique_words.append(x)
                return unique_words


def unique_word_count():
    unique_count = len(find_unique_words())
    return unique_count


def getWordCounter() -> Counter:
    """
    Generates a Counter of words from all the .html files in the ./repository/ folder.

    Parameters:
        TODO language (str): a specific language to get the html files for.
    """
    fileNames = os.listdir("repository")
    wordCounter = Counter()
    # Parse through all file names in ./repository/
    for name in fileNames:
        if name[-5:] == ".html":  # Only open files labeled .html
            filePath = os.path.join("repository", name)
            with open(filePath) as f:
                rawHTML = f.read()  # Get the raw html

                # Get only the text in the raw html, then make it all lowercase. Then merge all of the texts into a single string.
                bs = BeautifulSoup(rawHTML, "lxml")
                words = bs.getText(" ").split()
                words = [
                    x.strip("0123456789~`^%$#@&*?!.;:'()[]{},/|\\><+=_- \"").lower()
                    for x in words
                ]
                wordCounter.update(words)  # Add words to wordCounter.

    del wordCounter[""]
    # TODO make sure wordCounter actually contains all the "textual content"

    return wordCounter


if __name__ == "__main__":
    
    zipfsLaw()
    heapsLaw()
  
  
    