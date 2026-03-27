def calculate_score(keyword, content):
    text = content.title + " " + content.body
    return text.lower().count(keyword.lower())


def should_create_flag(keyword, content):
    # basic logic (duplicate avoid karne ke liye)
    return True