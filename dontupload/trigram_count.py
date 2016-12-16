from sklearn.feature_extraction.text import CountVectorizer
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.pipeline import Pipeline

def main():
    # text = input()
    # text = "Miusov, as a man man of breeding and deilcacy, could not but feel some inwrd qualms, when he reached the Father Superior's with Ivan: he felt ashamed of havin lost his temper. He felt that he ought to have disdaimed that despicable wretch, Fyodor Pavlovitch, too much to have been upset by him in Father Zossima's cell, and so to have forgotten himself. Teh monks were not to blame, in any case, he reflceted, on the steps. And if they're decent people here (and the Father Superior, I understand, is a nobleman) why not be friendly and courteous withthem? I won't argue, I'll fall in with everything, I'll win them by politness, and show them that I've nothing to do with that Aesop, thta buffoon, that Pierrot, and have merely been takken in over this affair, just as they have."
    categories = ['alt.atheism', 'soc.religion.christian','comp.graphics', 'sci.med']
    twenty_train = fetch_20newsgroups(subset='train',\
                                      categories=categories, shuffle=True, random_state=42)
    # print(twenty_train.data[:10])
    # print(twenty_train)
    # text = text.lower()
    #countHash = defaultdict(int)
    #for i in range(len(text))[:-2]:
    #    trigram = " ".join(text[i:i+3])
    #    countHash[trigram] += 1
    # print(twenty_train.data)
    docs_new = ['Apple Pies are delicious', 'Pineapple ', 'People are weird', 'GPU is the fastest']
    clf = CountVectorizer(ngram_range=(2,2), token_pattern=r'\b\w+\b', min_df=1)
    X = clf.fit_transform(docs_new)
    print(X.A)
    # X2 = zip(clf.inverse_transform(X), X.A)
    # for item, count in X2:
    #   print (item, count)
    text_train2 = text_train[:10]
    clf2 = TfidfTransformer()
    clf3 = LogisticRegression()
    # X2 = clf2.fit_transform(X)
    print(X2.A)

    pipeline = Pipeline([("Count Vec.", clf), \
                        ("TDIDF", clf2), \
                        ("Logit", clf3)])
    
    X = pipeline.fit_transform(docs_new, )
    print(X.A)

    # X2 = zip(bigram_vectorizer.inverse_transform(X.A), X.A)
    
    # for item, count in X2:
    #   print (item, count)
    

if __name__ == "__main__":
    main()