# Projects
Contains the Machine learning and other Data Science related projects

**1) INVESTMENT ASSIGNMENT** :  Spark Funds, an asset management company wants to make investments in a few companies. Spark Funds has two minor constraints for investments:
- It wants to invest between 5 to 15 million USD per round of investment
- It wants to invest only in English-speaking countries because of the ease of communication with the companies it would invest in.

**Objective**: The objective is to identify the best sectors, countries, and a suitable investment type for making investments. The overall strategy is to invest where others are investing, implying that the 'best' sectors and countries are the ones 'where most investors are investing'.
 
 
**2) CASE STUDY[Lending Club]** : A consumer finance company which specialises in lending various types of loans to urban customers has to make a decision for loan approval based on the applicant’s profile. Two types of risks are associated with the bank’s decision:
- If the applicant is likely to repay the loan, then not approving the loan results in a loss of business to the company
- If the applicant is not likely to repay the loan, i.e. he/she is likely to default, then approving the loan may lead to a financial loss for the company

**Objective**: The company wants to understand the driving factors (or driver variables) behind loan default, i.e. the variables which are strong indicators of default


**3) CAR PRICE PREDICTION**: A Chinese automobile company Geely Auto aspires to enter the US market by setting up their manufacturing unit there and producing cars locally to give competition to their US and European counterparts. Specifically, they want to understand the factors affecting the pricing of cars in the American market, since those may be very different from the Chinese market. The company wants to know:
- Which variables are significant in predicting the price of a car
- How well those variables describe the price of a car

**Objective**: Build a multiple linear regression model for the prediction of car prices with the available independent variables


**4) TELECOM CHURN CASE STUDY**: In the telecom industry, customers are able to choose from multiple service providers and actively switch from one operator to another. In this highly competitive market, the telecommunications industry experiences an average of 15-25% annual churn rate. Given the fact that it costs 5-10 times more to acquire a new customer than to retain an existing one, customer retention has now become even more important than customer acquisition. For many incumbent operators, retaining high profitable customers is the number one business goal.
To reduce customer churn, telecom companies need to predict which customers are at high risk of churn.

**Objective**: Analyse customer-level data of a leading telecom firm, build predictive models to identify customers at high risk of churn and identify the main indicators of churn.
Here we will use the usage-based definition to define churn.

**5) Syntactic Analysis [POS Tagging for unknown words]**: The vanilla Viterbi algorithm when encountered an unknown word (i.e. not present in the training set, such as 'Twitter'), it assigned an incorrect tag arbitrarily. This is because, for unknown words, the emission probabilities for all candidate tags are 0, so the algorithm arbitrarily chooses (the first) tag.
Here we use the Penn Treebank dataset of NLTK with the 'universal' tagset

**Objective**: Solving the problem of unknown words using 2 modifications: 
- Using weighted transition probabilities 
- Using rule based tagging

**6) Chatbot**: An Indian startup named 'Foodie' wants to build a conversational bot (chatbot) which can help users discover restaurants across several Indian cities(Tier 1 and 2) 

**Objective**: The bot should take city, cuisine and budget as input and  should display the top 5 restaurants in a sorted order (descending) of the average Zomato user rating. It should also send an optional mail to the user
Below are the files and its usage:
1) nlu_model.py - Part of rasa nlu for understanding user messages and extracting useful information from the text. Load the data, train it using spacy_sklearn pipeline and finally save the model in models/nlu
2) train_init.py - Part of rasa core. Uses the Memoization and Keras policies to train the model using the stories
3) dialogue_management_model.py - Part of rasa core whihc holds the conversations and decides the next step
4) rasa-nlu-trainer can be used to create data with entities and intents online
5) train_online.py - Used to train the model online to tell the bot what the next action should be and create stories
