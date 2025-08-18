def get_word_count(text):
	words = text.split()
	return len(words)

def character_count(text):
	ch_count = {}
	for c in text:
		low_word = c.lower()
		if low_word in ch_count:
			ch_count[low_word] += 1
		else:
			ch_count[low_word] = 1
	return ch_count

def sort_list(items):
	return items["num"]

def sorted(ch_count):
	sorted_list = []
	for ch in ch_count:
		sorted_list.append({"char": ch, "num": ch_count[ch]})
	sorted_list.sort(reverse=True, key=sort_list)
	return sorted_list
