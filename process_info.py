import spacy
nlp = spacy.load('en')

# doc = nlp("My daughter is at the party")
# print([(ch.text, ch.root.dep_) for ch in doc.noun_chunks])

# doc = nlp("Where is my daughter?")
# print([(ch.text, ch.dep_) for ch in doc])



def my_to_your(message):
    # Change my --> your
    ms1 = message.replace(" my "," your ")
    ms2 = ms1.replace("My ","Your ")
    ms3 = ms2.replace(" I ", " you ")
    ms4 = ms3.replace("I ","You ")
    ms5 = ms4.replace("my","your")
    return ms5

def find_keyword(message):
    doc = nlp(message)
    lst = [(ch.text, ch.root.dep_) for ch in doc.noun_chunks]
    has_dobj = False
    for (text,dep) in lst:
        if "dobj" in dep:
            has_dobj = True
            return text
    if not has_dobj:
        for (text,dep) in lst:
            if "nsubj" in dep:
                return text
    else:
        return "error"

