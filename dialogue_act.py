import nltk
# Trains a  nltk NaiveBayesClassifier to recognize different types of dialogue.
# the classifier can distinguish between ['ynQuestion', 'System', 'Statement', 'Emotion',
# 'Greet', 'whQuestion', 'Emphasis', 'nAnswer', 'Clarify', 'Continuer', 'Accept', 
#'Reject', 'Bye', 'yAnswer', 'Other']
# 
# We use it to identify whether the user is asking a question or issuing a statement.

posts = nltk.corpus.nps_chat.xml_posts()[:10000]

def dialogue_act_features(post):
    features = {}
    for word in nltk.word_tokenize(post):
        features['contains({})'.format(word.lower())] = True
    return features

featuresets = [(dialogue_act_features(post.text), post.get('class'))
                for post in posts]
size = int(len(featuresets) * 0.1)
train_set, test_set = featuresets[size:], featuresets[:size]
classifier = nltk.NaiveBayesClassifier.train(train_set)

def is_yn_question(text):
    label = classifier.classify(dialogue_act_features(text))
    if label == 'ynQuestion' or ('?' in text):
        return True
    else:
        return False

def is_wh_question(text):
    label = classifier.classify(dialogue_act_features(text))
    if label == 'whQuestion' or ('?' in text):
        return True
    else:
        return False

