# Purpose - Receive the call for testing a page from the Chrome extension and return the result (SAFE/PHISHING)
# for display. This file calls all the different components of the project (The ML model, features_extraction) and
# consolidates the result.

import joblib
import features_extraction
import sys
import numpy as np
import re
from features_extraction import LOCALHOST_PATH, DIRECTORY_NAME


def get_prediction_from_url(test_url):
    features_test = features_extraction.main(test_url)
    # Due to updates to scikit-learn, we now need a 2D array as a parameter to the predict function.
    features_test = np.array(features_test).reshape((1, -1))

    clf = joblib.load(LOCALHOST_PATH + DIRECTORY_NAME + '/classifier/random_forest.pkl')
    print(clf)
    #red = clf.predict(features_test)
    #return int(pred[0])
def Find(string): 
  regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
  url = re.findall(regex,string)       
  return [x[0] for x in url] 

def main():
    url = "https://www.google.com"
    if(url):
        prediction = get_prediction_from_url(url)
        if prediction == 1:
            print("Its Safe")
        elif prediction == -1:
            print("Sounds Like Phishing")
    else:
        print("fuck")

if __name__ == "__main__":
    main()
