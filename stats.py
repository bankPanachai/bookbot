def get_book_text(file_path):
  with open(file_path) as f:
    return f.read()


def word_count(text):
  return len(text.split())

def charactor_count(text):
  my_dict = {}
  words = text.lower()
  for w in words:
    if w not in my_dict:
      my_dict[w] = 1
    else:
      my_dict[w] = my_dict[w] + 1
  return my_dict

def char_num(lists):
  char_num_lists = []
  for list in lists:
      char_num_lists.append({
        "char": list,
        "num": lists[list]
      })
  return char_num_lists

def only_alpha(char_num_lists):
  only_alpha = []
  for char in char_num_lists:
    if char["char"].isalpha() == True:
      only_alpha.append(char)
  return only_alpha


