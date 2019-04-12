# Predicting Stable Portfolios using Machine Learning / Deep Learning

This repo contains notebooks for the 4 modules described in the report linked here.

## Modules:
### **SEC Scraper**

Note: We have already scraped S&P 500 SEC filings. For testing purpose we are scraping the filings for just 2 tickers here as an example.

- `scraping_cleaning_sec.ipynb` notebook is used to scrape all data from SEC EDGAR website. It also takes care of cleaning and parsing HTML into raw text files and checkpoints its progress so extraction can resume later.

### **Sentiment Analyzer**

Notebooks for this module are located in `EDGAR-reports-Text-Analysis`.

- `Sentiment_Analysis_SEC.ipynb` contains all the code extract sentiment scores from SEC filings.
- `Sentiment_Stocks_Visualization.ipynb` is used to generate stock trends vs. the calculated sentiments.

### **Stock Predictor**

Note that feature engineering code is common across these notebooks.

- `lstmstocks-sentiments.ipynb` is used to train models with and without sentiments. This notebook also performs all the feature engineering such as windowing, cascading, merging and interpolation.\

- `lstmstocks-gww.ipynb` notebook constructs, trains and saves three models (no sentiments, positive and negative sentiments) for a single stock which can be changed.

- `generate-predictions-csv.ipynb` generates predicted dataframes using saved models from earlier traing.

### **Portfolio Generator and Optimizer**

- `generating_portfolio.ipynb` constructs stable portfolios using metrics such as correlation, covariance, Sharpe ratio and volatility. Also creates related visualizations that help select stable portfolios.

## Libraries and requirements:
- Jupyter
- NLTK VADER
- Keras
- Scikit-learn
- fastai datepart
- Pandas
- Numpy
- BeautifulSoup
- Stocker
- Quandl
- Plotly
- Tensorboard
