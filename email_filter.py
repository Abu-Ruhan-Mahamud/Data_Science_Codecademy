from sklearn.datasets import fetch_20newsgroups
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer

emails = fetch_20newsgroups()

emails = fetch_20newsgroups(categories=['rec.sport.baseball', 'rec.sport.hockey'])

print("Sample Email:")
print(emails.data[5])


train_emails = fetch_20newsgroups(categories=['rec.sport.baseball', 'rec.sport.hockey'], subset='train', shuffle=True, random_state=108)
test_emails = fetch_20newsgroups(categories=['rec.sport.baseball', 'rec.sport.hockey'], subset='test', shuffle=True, random_state=108)

# Save the training and test labels
train_labels = train_emails.target
test_labels = test_emails.target

# Counting Words using CountVectorizer
counter = CountVectorizer()
counter.fit(test_emails.data + train_emails.data)

# Save the training and test counts
train_counts = counter.transform(train_emails.data)
test_counts = counter.transform(test_emails.data)


# Create and train a Naive Bayes Classifier
classifier = MultinomialNB()
classifier.fit(train_counts, train_labels)

accuracy = classifier.score(test_counts, test_labels)
print(f"The accuracy of the classifier on the test data is {accuracy:.3f}")


print("\nTesting with a different dataset:")

# Split the dataset into training and test sets
train_emails = fetch_20newsgroups(categories=['comp.sys.ibm.pc.hardware', 'rec.sport.hockey'], subset='train', shuffle=True, random_state=108)
test_emails = fetch_20newsgroups(categories=['comp.sys.ibm.pc.hardware', 'rec.sport.hockey'], subset='test', shuffle=True, random_state=108)

# Save the training and test labels
train_labels = train_emails.target
test_labels = test_emails.target

# Counting Words using CountVectorizer
counter = CountVectorizer()
counter.fit(test_emails.data + train_emails.data)

# Save the training and test counts
train_counts = counter.transform(train_emails.data)
test_counts = counter.transform(test_emails.data)

# Create and train a Naive Bayes Classifier
classifier = MultinomialNB()
classifier.fit(train_counts, train_labels)

# Evaluate the classifier's accuracy on the test data
accuracy = classifier.score(test_counts, test_labels)
print(f"The accuracy of the classifier on the test data is {accuracy:.3f}")

