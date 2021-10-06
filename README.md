# CS 4250 Web Search and Recommender Systems Project 1

## Assignment Details

Implement a web crawler and do analysis on 3 different crawls (each one a different language). <br>
Analysis includes graphing to compare to Zipf's Law and Heap's Law. <br>
Crawling included downloading the raw HTML content for each page and saving it to the `repository` folder.

## Install

```console
# Clone the repo 
$ git clone https://github.com/CS4250-Group6/Project-1.git

# Install the requirements
$ python3 -m pip install -r requirements.txt
```

## Use

1. Modify the seed URL and crawl language according to the accepted languages in [langdetect](https://pypi.org/project/langdetect/)
2. Make a `repository` folder and `repository/<lang>` folders according to the selected language ISO 639-1 code
3. `python3 crawler.py`
4. Modify `analyzer.py` for the correct language name and code
5. `python3 analyzer.py`
