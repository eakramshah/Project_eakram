def calculate_love_score(name1, name2):
    # Step 1: Combine names and convert to lowercase
    combine = (name1 + name2).lower()

    # Step 2: Count letters in "TRUE"
    true_count = 0
    for letter in "true":
        true_count += combine.count(letter)

    # Step 3: Count letters in "LOVE"
    love_count = 0
    for letter in "love":
        love_count += combine.count(letter)

    # Step 4: Combine the two counts to form the love score
    love_score = int(str(true_count) + str(love_count))

    # Step 5: Print the result
    print(f"Love Score = {love_score}")


calculate_love_score(name1="ikram", name2="saleha")