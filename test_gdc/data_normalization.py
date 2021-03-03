import re


# We noticed that data normalization is not straighforward using only formatting transformation.
# If we assume that only 2 categories are possible we can use an algorithm to normalize data
# using the closest string (cf edit distance algorithm) or clusteting techniques

#Dictionnary for data normalization
hardcoded_normalization_dic = {
    "relestate": "realestate",
    "relestat": "realestate",
    "M.": "F",
    "Mr": "M",
}

#Regex normalization
def regex_rule_normalize(text):
    # Keep only lower-cased text and numbers by applying a regex
    return re.sub("[^a-z0-9] ", "", text.lower())


#Function that returns normalized version of text if text belongs to hardcoded_normalization_dic keys
def hardcoded_rule_normalize(text):
    if text in hardcoded_normalization_dic:
        return hardcoded_normalization_dic[text]
    return text
