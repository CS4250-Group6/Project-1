import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import os
from collections import Counter
import re


def zipfsLaw():
    wordCounter = getWordCounter()
    totalWordCount = sum(wordCounter.values())

    # Make an array, sorted by word rank. So, index is rank.
    wordRanks = sorted(wordCounter, key=lambda x: wordCounter[x], reverse=True)

    # Calculate the probability of each word
    wordFrequencies = []
    for w in wordRanks:
        wordFrequencies.append(wordCounter[w])

    # Plot the Zipf's Law line.
    zipfLineY = []
    K = 0.1 * totalWordCount
    zipfLineY.extend([K / (x + 1) for x in range(len(wordRanks))])
    plt.plot(range(1, len(wordRanks) + 1), zipfLineY, label="Zipf", c="g")

    # Graph the probabilities vs rank:
    plt.scatter(range(1, len(wordRanks) + 1), wordFrequencies, s=5, label="Data", c="r")

    # Naming stuff
    plt.xlabel("Rank")
    plt.ylabel("Frequency")
    plt.title("Zipf's Law " + languageName)

    # Make x and y scale log base 10
    plt.yscale("log", base=10)
    plt.xscale("log", base=10)
    plt.legend()  # Display the legend
    plt.savefig(f"Zipfs{selectedLanguage}.png")
    plt.close()
    # plt.show()


def heapsLaw():
    vocabList = getVocabList()

    # Graph Labels
    plt.xlabel("Words in Collection")  # this is the total number of words
    plt.ylabel(
        "Words in Vocabulary"
    )  # this is the vocabulary size (number of unique words)
    plt.title("Heap's Law " + languageName)

    # scale of x and y axis on graph is normal

    # plot corresponding data using a line to represent Heap's Law implementation
    plt.plot(range(len(vocabList)), vocabList, label="Data", c="b")
    plt.legend()  # Display the legend
    plt.savefig(f"Heaps{selectedLanguage}.png")
    print(vocabList[-1])
    plt.close()
    # plt.show()  # show graph


def getVocabList() -> list[int]:
    path = os.path.join("repository", selectedLanguage)
    fileNames = os.listdir(path)
    uniqueWords = set()
    vocabList = []
    # Parse through all file names in ./repository/
    for name in fileNames:
        if name[-5:] == ".html":  # Only open files labeled .html
            filePath = os.path.join(path, name)
            with open(filePath, encoding="utf8") as f:
                rawHTML = f.read()  # Get the raw html

                # Get only the text in the raw html, then make it all lowercase. Then merge all of the texts into a single string.
                bs = BeautifulSoup(rawHTML, "lxml")
                words = re.findall(
                    "[^\W_\d]+",
                    bs.getText(" ").lower(),
                    flags=re.UNICODE | re.IGNORECASE,
                )

                for word in words:
                    if word not in uniqueWords:
                        uniqueWords.add(word)

                    vocabList.append(len(uniqueWords))

    return vocabList


def getWordCounter() -> Counter:
    """
    Generates a Counter of words from all the .html files in the ./repository/ folder.

    Parameters:
        TODO language (str): a specific language to get the html files for.
    """
    path = os.path.join("repository", selectedLanguage)
    fileNames = os.listdir(path)
    wordCounter = Counter()
    # Parse through all file names in ./repository/
    for name in fileNames:
        if name[-5:] == ".html":  # Only open files labeled .html
            filePath = os.path.join(path, name)
            with open(filePath) as f:
                rawHTML = f.read()  # Get the raw html

                # Get only the text in the raw html, then make it all lowercase. Then merge all of the texts into a single string.
                bs = BeautifulSoup(rawHTML, "lxml")
                words = re.findall(
                    "[^\W_\d]+",
                    bs.getText(" ").lower(),
                    flags=re.UNICODE | re.IGNORECASE,
                )
                wordCounter.update(words)  # Add words to wordCounter.

    del wordCounter[""]
    # TODO make sure wordCounter actually contains all the "textual content"

    return wordCounter


def topHundredWords():
    words = getWordCounter()
    wordL = words.most_common()
    outStr = ""
    for i in range(0, 100):
        if i == 99:
            outStr += wordL[i][0]
        else:
            outStr += wordL[i][0] + ", "
    print(outStr)


if __name__ == "__main__":
    global selectedLanguage
    global languageName
    selectedLanguage = "fr"
    languageName = "French"
    zipfsLaw()
    heapsLaw()
    # topHundredWords()
