def calculate_love_score(name1,name2):
    combined_names=(name1+name2).lower()
    true_count=sum(combined_names.count(letter)for letter in "true")
    love_count= sum(combined_names.count(letter) for letter in "love")

    love_score=int(f"{true_count}{love_count}")
    print(f"Love score={love_score}")
calculate_love_score("kanye west","Kim kardashian")