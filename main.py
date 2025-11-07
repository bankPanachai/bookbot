import sys
from stats import get_book_text, word_count, charactor_count, char_num, only_alpha




def main():
  if len(sys.argv) != 2 :
    print(f"Usage: python3 main.py <path_to_book>")
    return sys.exit(1)
  
  path = sys.argv[1]

  content = get_book_text(path) # 
  total_word = word_count(content)
  total_charactor = charactor_count(content)
  char_num_lists = char_num(total_charactor)
  #print(total_word) # 75767
  #print(total_charactor) # {'t': 29493, 'h': 19176, 'e': 44538, ......}
  #print(char_num_lists) # [{'char': 't', 'num': 29493}, {'char': 'h', 'num': 19176}, {'char': 'e', 'num': 44538}....]
  result = only_alpha(char_num_lists) # [{'char': 't', 'num': 29493}, {'char': 'h', 'num': 19176}, {'char': 'e', 'num': 44538}....] no space !
  result.sort(reverse=True, key=sort_on) # sort
  #display(result) # Charactor count
  print(f"============ BOOKBOT ============")
  print(f"Analyzing book found at books/frankenstein.txt...")
  print(f"----------- Word Count ----------")
  print(f"Found {total_word} total words")
  print(f"--------- Character Count -------")
  display(result)


def sort_on(item):
  return item["num"]

def display(arr):
  for a in arr:
    print(f"{a["char"]}: {a["num"]}")


main()
