"""Morphological and POS analysis script."""

import nltk

# Download required NLTK data
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# Morphological dictionaries

english_words = {
    "play": {
        "root": "play",
        "cat": "v",
        "gen": "NA",
        "num": "sg",
        "per": "NA",
        "case": "NA",
        "tense": "present"
    },

    "plays": {
        "root": "play",
        "cat": "v",
        "gen": "NA",
        "num": "sg",
        "per": "3",
        "case": "NA",
        "tense": "present"
    },

    "played": {
        "root": "play",
        "cat": "v",
        "gen": "NA",
        "num": "NA",
        "per": "NA",
        "case": "NA",
        "tense": "past"
    },

    "playing": {
        "root": "play",
        "cat": "v",
        "gen": "NA",
        "num": "NA",
        "per": "NA",
        "case": "NA",
        "tense": "present"
    },

    "boy": {
        "root": "boy",
        "cat": "n",
        "gen": "male",
        "num": "sg",
        "per": "NA",
        "case": "NA",
        "tense": "NA"
    },

    "boys": {
        "root": "boy",
        "cat": "n",
        "gen": "male",
        "num": "pl",
        "per": "NA",
        "case": "NA",
        "tense": "NA"
    },

    "happy": {
        "root": "happy",
        "cat": "adj",
        "gen": "NA",
        "num": "NA",
        "per": "NA",
        "case": "NA",
        "tense": "NA"
    },

    "happiness": {
        "root": "happy",
        "cat": "n",
        "gen": "NA",
        "num": "NA",
        "per": "NA",
        "case": "NA",
        "tense": "NA"
    }
}


hindi_words = {
    "लड़का": {
        "root": "लड़का",
        "cat": "n",
        "gen": "male",
        "num": "sg",
        "per": "NA",
        "case": "direct",
        "tense": "NA"
    },

    "लड़के": {
        "root": "लड़का",
        "cat": "n",
        "gen": "male",
        "num": "pl",
        "per": "NA",
        "case": "direct",
        "tense": "NA"
    },

    "लड़कों": {
        "root": "लड़का",
        "cat": "n",
        "gen": "male",
        "num": "pl",
        "per": "NA",
        "case": "oblique",
        "tense": "NA"
    },

    "लड़की": {
        "root": "लड़की",
        "cat": "n",
        "gen": "female",
        "num": "sg",
        "per": "NA",
        "case": "direct",
        "tense": "NA"
    },

    "लड़कियाँ": {
        "root": "लड़की",
        "cat": "n",
        "gen": "female",
        "num": "pl",
        "per": "NA",
        "case": "direct",
        "tense": "NA"
    },

    "खेल": {
        "root": "खेल",
        "cat": "v",
        "gen": "NA",
        "num": "NA",
        "per": "NA",
        "case": "NA",
        "tense": "present"
    },

    "खेला": {
        "root": "खेल",
        "cat": "v",
        "gen": "male",
        "num": "sg",
        "per": "3",
        "case": "NA",
        "tense": "past"
    },

    "खेली": {
        "root": "खेल",
        "cat": "v",
        "gen": "female",
        "num": "sg",
        "per": "3",
        "case": "NA",
        "tense": "past"
    },

    "खेलेंगे": {
        "root": "खेल",
        "cat": "v",
        "gen": "NA",
        "num": "pl",
        "per": "3",
        "case": "NA",
        "tense": "future"
    },

    "हंसी": {
        "root": "हंस",
        "cat": "v",
        "gen": "female",
        "num": "sg",
        "per": "3",
        "case": "NA",
        "tense": "past"
    }
}


# Display the analysis result

def analyze_word(word, language):
    """Prints morphological information for a given word.

    Args:
        word (str): The word to analyze.
        language (str): The language of the word, either 'English' or 'Hindi'.
    """
    if language == "English":
        data = english_words
    else:
        data = hindi_words

    if word not in data:
        print("\nWord not found in the morphological dictionary.")
        return

    result = data[word]

    print("\n--- Morphological Analysis ---")
    print("Word     :", word)
    print("Root     :", result["root"])
    print("Category :", result["cat"])
    print("Gender   :", result["gen"])
    print("Number   :", result["num"])
    print("Person   :", result["per"])
    print("Case     :", result["case"])
    print("Tense    :", result["tense"])
    print("-" * 30)


# NLTK POS tagger

def nltk_pos_analysis(sentence):
    """Tokenizes and prints part-of-speech tags for a sentence.

    Args:
        sentence (str): The English text to process.
    """
    print("\nNLTK POS Analysis:")

    tokens = nltk.word_tokenize(sentence)
    tagged_words = nltk.pos_tag(tokens)

    for word, tag in tagged_words:
        print(word, "->", tag)


# Main loop

def main():
    """Runs the interactive command line interface."""
    while True:

        print("\n=== Morphological Analyzer ===")

        print("1. English")
        print("2. Hindi")
        print("3. NLTK POS Tagging")
        print("4. Exit")

        choice = input("\nWhat would you like to do? ")

        # English
        if choice == "1":

            print("\nAvailable English words:")
            print(", ".join(english_words.keys()))

            word = input("\nEnter an English word: ").lower()

            analyze_word(word, "English")

        # Hindi
        elif choice == "2":

            print("\nAvailable Hindi words:")
            print(", ".join(hindi_words.keys()))

            word = input("\nEnter a Hindi word: ")

            analyze_word(word, "Hindi")

        # POS tagging
        elif choice == "3":

            sentence = input("\nEnter an English sentence: ")

            nltk_pos_analysis(sentence)

        # Exit
        elif choice == "4":

            print("\nBye!")
            break

        else:
            print("\nInvalid choice!")


# Run it

if __name__ == "__main__":
    main()