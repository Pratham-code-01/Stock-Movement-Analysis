# Stock Movement Prediction Using Reddit Sentiment Analysis #
### Project Overview
This project aims to predict stock market movements using Reddit sentiment data. The model classifies whether the stock price will go "up" or "down" based on sentiment extracted from Reddit posts in specific subreddits related to stock market discussions.

### Key Features
___Data Scraping___: The project uses the PRAW library to scrape Reddit posts from stock-related subreddits.\
___Sentiment Analysis___: Extracted Reddit posts are processed and analyzed to determine the sentiment (positive or negative) expressed in them.\
___Stock Movement Prediction___: A classification model is trained using Reddit sentiment data and historical stock data to predict stock movements ("up" or "down").\
___Evaluation Metrics___: The model is evaluated using classification metrics such as accuracy, precision, recall, and F1-score.

### Installation and Setup
1. __Clone the repository__\
Start by cloning the repository to your local machine:
git clone <repository_link>
cd project_name

2. ___Set up the environment___\
Create and activate a virtual environment:
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. ___Install dependencies___\
Install the required Python libraries:
___pip install -r requirements.txt___

The requirements.txt file includes the necessary libraries for this project, such as:
___pandas
praw
scikit-learn
matplotlib
seaborn
joblib___

### Run the Code

Follow these steps to run the code for the Stock Movement Prediction project:

1. ___Clone the Repository___\
Firstly, clone the repository to your local machine:
    ``` 
    git clone <repository_link>
    cd project_name
    ```

2. ___Set Up the Environment___\
Create a virtual environment to keep the dependencies isolated:
    ```
    python3 -m venv venv
    source venv/bin/activate # For mac

    venv\Scripts\activate  # For windows
    ```

3. ___Install Dependencies___\
Install the required libraries using ___pip___:
    ```
    pip install -r requirements.txt
    ```

4. Scrape Reddit Data\
To scrape Reddit Data for sentiment analysis, run the following command:
    ```
    python Scripts/stock_scraper.ipynb
    ```
    This will collect Reddit posts related to stock discussion using PRAW API. Make sure you have Reddit API Credentials (Client ID, Client Secret and User_Agent) set up in the script.

5. ___Data Analysis___\
To perform sentiment analysis, run the following command:
    ```
    python Scripts/data_analysis.ipynb
    ```
    This will performs three major tasks: analyzing sentiment, classifying it into labels like positive, negative, and extracting stock ticker symbols.

6. ___Preparing Data___\
To preprocess the Reddit sentiment data and stock data, run the following command
    ```
    python Scripts/data_prep.ipynb
    ```
    This will bridges the gap by merging the sentiment analyzed reddit data with historical stock prices, providing a dataset enriched with both social and financial features.

7. ___Train the Model___\
To train the machine learning model, run the following command
    ```
    python Scripts/model_training.ipynb
    ```
    This will train a classification model to predict stock movements. The model and preprocessing pipeline (scaler) will be saced as ___.pkl___ files in the ___Models___ folder

8. ___Run User Interface___\
To run the frontend, run the following command:
    ```
    python App/app.py
    ```
    This will run the frontend of the project and then fill the form and click on the predict button. Then it will give the output as the stock goes ___'up'___ or ___'down'___


### How It Works
___Reddit Data Scraping___: Using the PRAW library, the script scrapes data from relevant stock-related subreddits (e.g., r/stocks, r/investing). It extracts post titles and comments to analyze the sentiment.\
___Data Preprocessing___: The Reddit text data is cleaned and transformed into numerical features that can be fed into machine learning models.\
___Sentiment Analysis___: Each post’s sentiment is evaluated to understand the general mood about the stock in question (positive or negative).\
___Model Training___: A machine learning model (Random Forest or another classifier) is trained using the Reddit sentiment data and stock market information to predict stock movements.\
___Prediction___: The trained model is used to predict stock price trends based on real-time Reddit sentiment.

### Future Work and Improvements
Integrating Multiple Data Sources: Future work could involve incorporating other data sources such as financial news, stock indicators, or technical analysis.
Real-Time Predictions: Real-time stock predictions could be integrated by continuously scraping new Reddit posts and predicting stock trends on the fly.
Model Improvement: Exploring additional machine learning models and feature engineering could improve prediction accuracy.

### Acknowledgments
___Pandas___: For data manipulation and analysis.\
___PRAW___: For Reddit data scraping.\
___Scikit-Learn___: For machine learning tools and evaluation metrics.\
___Matplotlib___: For visualizations and charts.


Let me know if you need any changes or additional details added!


## Credits
- ### Developer : Pratham Sharma