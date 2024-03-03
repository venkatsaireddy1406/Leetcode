def main(s):
    cleaned_s = ''.join(char.lower() for char in s if char.isalnum())
    return cleaned_s == cleaned_s[::-1]


if __name__=="__main__":
    print(main(s = "A man, a plan, a canal: Panama"))