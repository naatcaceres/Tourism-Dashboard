# Tourism-Dashboard
## Abstract ##
This repository contains the complete development of an interactive tourism dashboard using Python. 
The repository contains five notebooks:

- 01.scraping_vars.ipynb: Shows the web scraping process for several variables of our dataset, through the use of Selenium and XPath
- 02.etl.ipynb: Shows the loading and preprocessing of all data in the raw file, and it then stores the clean datasets inside the data/processed folder
- 03.eda.ipynb: Conducts an exploratory analysis of our already processed data to gain a better understanding of the information we have available
- 04.ranking.ipynb: Conducts an analysis of our available data, establishing the baseline for our dashboard's correct functioning. It also creates the final datasets in the proper format to feed our dashboard

## Dependencies ##
- Python
- streamlit

## Quick Guide ##
To follow along the complete process, the reader should go to the four notebooks in order. If, instead, the user would like to access the tool directly, they could simply run dashboard.py using the following command in their terminal: streamlit run dashboard.py
