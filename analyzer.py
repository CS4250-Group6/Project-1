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

    # Plot the Zipf's Law line.
    zipfLineY = []
    K = 0.1 * totalWordCount
    zipfLineY.extend([K / (x + 1) for x in range(len(wordRanks))])
    plt.plot(range(1, len(wordRanks) + 1), zipfLineY, label="Zipf", c="g")

    # Graph the probabilities vs rank:
    plt.scatter(range(1, len(wordRanks) + 1), wordFrequencies, s=5, label="Data", c="r")

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
    # num_of_words = getWordCounter()
    # totalWordCount = sum(num_of_words.values()) # total number of words

    # Make arrays to plot data
    unique_so_far = []
    for word in find_unique_words():
        unique_so_far.append(word)

    totalWords_so_far = []
    # for w in allWords(): ?
    for w in range(0, len(unique_so_far)):
        totalWords_so_far.append(w)

    vocabList = getVocabList()

    # Graph Labels
    plt.xlabel("Words in Collection")  # this is N; total number of words
    plt.ylabel("Words in Vocabulary")  # this is Vocab size (number of unique words)
    plt.title("Heap's Law")

    # define scale of x and y axis on graph
    # plt.yscale("log", base=10)
    # plt.xscale("log", base=10)

    # plot corresponding data
    # Plot the Heap's Law line
    plt.plot(range(len(vocabList)), vocabList, label="Data", c="g")
    plt.legend()  # Display the legend
    plt.show()  # show graph


def getVocabList() -> list[int]:
    path = os.path.join("repository", selectedLanguage)
    fileNames = os.listdir(path)
    uniqueWords = set()
    vocabList = []
    # Parse through all file names in ./repository/
    for name in fileNames:
        if name[-5:] == ".html":  # Only open files labeled .html
            filePath = os.path.join(path, name)
            with open(filePath) as f:
                rawHTML = f.read()  # Get the raw html

                # Get only the text in the raw html, then make it all lowercase. Then merge all of the texts into a single string.
                bs = BeautifulSoup(rawHTML, "lxml")
                words = bs.getText(" ").split()
                words = [
                    x.strip("0123456789~`^%$#@&*?!.;:'()[]{},/|\\><+=_- \"").lower()
                    for x in words
                ]

                for word in words:
                    if word not in uniqueWords:
                        uniqueWords.add(word)

                    vocabList.append(len(uniqueWords))

    return vocabList


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


# used to fill the totalWords_sofar array, not sure if useful
# returns bigger number than totalWordCount
def allWords():
    """
    List of words from all the .html files in the ./repository/ folder.

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
                all_words = []
                for a in words:
                    all_words.append(a)
                return all_words


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
    global selectedLanguage
    selectedLanguage = "fr"
    # zipfsLaw()
    heapsLaw()
