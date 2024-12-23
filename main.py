def main():
    with open("/home/ilak/workspace/github.com/bankPanachai/bookbot/books/frankenstein.txt") as f:
        file_contents = f.read()
        to_lower = file_contents.lower()
        letters = {}
        sorted_list = []
        for i in to_lower:
            if i.isalpha():
                if(i not in letters):
                    letters[i] = 1
                else:
                    letters[i] += 1
        for i in letters:
            sorted_list.append(i)
        sorted_list.sort(reverse=False)
        for i in sorted_list:
            print(f"The '{i}' chracter was found {letters[i]}")
main()