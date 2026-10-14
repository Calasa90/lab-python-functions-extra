import string


def get_unique_list_f(lst):
	return list(set(lst))


def count_case_f(text):
	upper = 0
	lower = 0

	for character in text:
		if character.isupper():
			upper += 1
		elif character.islower():
			lower += 1

	return upper, lower


def remove_punctuation_f(sentence):
	clean_sentence = []

	for character in sentence:
		if character not in string.punctuation:
			clean_sentence.append(character)

	return "".join(clean_sentence)


def word_count_f(sentence):
	clean_sentence = remove_punctuation_f(sentence)
	words = clean_sentence.split()
	return len(words)
