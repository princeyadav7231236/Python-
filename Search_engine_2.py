import random

def matchingWord(sentence1, sentence2):
    words1 = sentence1.strip().split()
    words2 = sentence2.strip().split()
    score = 0
    for word1 in words1:
        for word2 in words2:
            # print(f"Matching {word1} with {word2}")
            if word1.lower() == word2.lower():
                score += 1
    return score

if __name__ == '__main__':
    # print(matchingWord("This is good ", "Python is good"))
    sentences = ["Python is good", "This is good", "Devil is bad", "Hello programmer"]
    query = input("Please enter your query string \n")
    scores = [matchingWord(query, sentence) for sentence in sentences]
    # print(scores)

    sortedSentScores = [sentScore for sentScore in sorted(zip(scores, sentences), reverse=True) if sentScore != 0]
    # This will sort the list in reverse order if we will remove the if statement then also the list will be same
    # print(sortedSentScores)
    print(f"{len(sortedSentScores)} results found")
    for score, item in sortedSentScores:
        print(f"\"{item}\" : with the score of {score}")