import pandas as pd
import io

if __name__ == '__main__':
    url = 'https://raw.githubusercontent.com/cathegit/CS471A3/refs/heads/main/SpamDetection.csv'  # grab the data
    df = pd.read_csv(url)

    print(df)  # displays the data

    prispam = 0
    priham = 0

    words_unique = {}  # dictionary to hold the unique words
    testing_data = []  # list to hold the testing data

    # Loop through the each row of the CSV file
    for index, row in df.iterrows():
        # print(index)
        message = row['data']  # get the message
        if index < 20: # training data
            message_type = row['Target']  # get the type of message

            if message_type == 'spam':  # increment the spam or ham count
                prispam += 1
            elif message_type == 'ham':
                priham += 1

            # Loop through each word in the message
            for word in message.split():
                # Check if the word is a unique word
                if word not in words_unique:
                    words_unique[word] = {'count': 1, 'type': message_type}
                else:
                    words_unique[word]['count'] += 1
        else:
            testing_data.append(message)  # add the message to the testing data

    prispam = prispam / 20  # final probabilities
    priham = priham / 20

    print("P(ham) =", priham)
    print("P(spam) =", prispam)

    words = {  # getting a list of unique words
        x for x in ' '.join(
            df.data.str.lower().tolist()
        ).split() if x.isalpha()

    }
    uniquewords = 0
    for x in words:  # calculating the number of unique words
        uniquewords += 1

    print(uniquewords)

    for x in testing_data:


    # for word, info in words_unique.items():
    #     print(f"Word: {word}, Count: {info['count']}, Type: {info['type']}")

    # for word in words_unique:
    #     # Calculate the probability of the word being spam or ham
    #     words_unique[word]['prob_spam'] = (words_unique[word]['count'] + 1) / (prispam + uniquewords)
    #     words_unique[word]['prob_ham'] = (words_unique[word]['count'] + 1) / (priham + uniquewords)