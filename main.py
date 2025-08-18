def main():

	from stats import get_word_count, character_count, sorted

	from sys import argv, exit

	if len(argv) < 2:
		print("Usage: python3 main.py <path_to_book>")
		exit(1)

	path = argv[1]
	text = get_book_text(path)
	wc = get_word_count(text)
	letter_count = character_count(text)
	final_list = sorted(letter_count)

	print("============ BOOKBOT ============")
	print(f"analyzing book found at {path}")
	print("----------- Word Count ----------")
	print(f"Found {wc} total words")
	print("--------- Character Count -------")
	print()

	for item in final_list:
		if not item["char"].isalpha():
			continue
		print(f"{item['char']}: {item['num']} times")

	print("============= END ===============")

def get_book_text(path):
	with open(path) as f:
		return f.read()

main()
