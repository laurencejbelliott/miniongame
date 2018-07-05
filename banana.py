def minion_game(string):
    print("Each player must take turns to enter a substring of " + string +
          ".\nPlayer 1's substrings must start with consonants." +
          "\nPlayer 2's substrings must start with vowels." +
          "\nFor each occurance of a substring within the orginal string," +
          "\none point is awarded.")

    substrings = []
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    vowels = "AEIOU"
    consonants = [c for c in alphabet if c not in vowels]
    guessed = set()
    stu_guessed = set()
    kev_guessed = set()
    stu_points = 0
    kev_points = 0

    for i in range(0,len(string)):
        for j in range(i+1,len(string)+1):
            substrings.append(string[i:j])

    substrings_set = set(substrings)

    while True:
        stu_guess = raw_input("Player 1, enter a substring of "
                              + string + ": ").upper()
        if stu_guess == "":
            print "\nPlease enter a substring of " + string + "!\n"
        elif (stu_guess in substrings_set) & (stu_guess[0] in consonants) & (stu_guess not in guessed):
            stu_guessed.add(stu_guess)
            print ("Player 1 correctly guessed a substring of " + string +
                ", beginning with a consonant.")

            occurances = 0
            for i in range(0,len(substrings)):
                if stu_guess == substrings[i]:
                    occurances += 1
            print (stu_guess + " occurs " + str(occurances) + " time(s)."  +
                "\nPlayer 1 gains " + str(occurances) + " point(s).")
            stu_points += occurances
            print "Player 1 currently has " + str(stu_points) + " point(s)."
        else:
            if stu_guess in guessed:
                print stu_guess + " has already been guessed."
                print "Player 1 currently has " + str(stu_points) + " point(s)."
            else:
                print ("Player 1 guessed incorrectly. " + stu_guess +
                    " is not a substring of " + string +
                    " beginning with a consonant.")
                print "Player 1 currently has " + str(stu_points) + " point(s)."

        kev_guess = raw_input("Player 2, enter a substring of "
                              + string + ": ").upper()

        if kev_guess == "":
            print "\nPlease enter a substring of " + string + "!\n"
        elif (kev_guess in substrings_set) & (kev_guess[0] in vowels) & (kev_guess not in guessed):
            kev_guessed.add(kev_guess)
            print ("Player 2 correctly guessed a substring of " + string +
                ", beginning with a vowel.")

            occurances = 0
            for i in range(0,len(substrings)):
                if kev_guess == substrings[i]:
                    occurances += 1
            print (kev_guess + " occurs " + str(occurances) + " time(s)."  +
                "\nPlayer 2 gains " + str(occurances) + " point(s).")
            kev_points += occurances
            print "Player 2 currently has " + str(kev_points) + " point(s)."
        else:
            if kev_guess in guessed:
                print kev_guess + " has already been guessed."
                print "Player 2 currently has " + str(kev_points) + " point(s)."
            else:    
                print ("Player 2 guessed incorrectly. " + kev_guess +
                    " is not a substring of " + string +
                    " beginning with a vowel.")
                print "Player 2 currently has " + str(kev_points) + " point(s)."

        if stu_guess in substrings_set:
            guessed.add(stu_guess)
        if kev_guess in substrings_set:    
            guessed.add(kev_guess)
        print "\nGuessed substrings:\n" + "\n".join(guessed) + "\n"
        if guessed == substrings_set:
            break

    if stu_points > kev_points:
        print "Player 1 wins with " + str(stu_points) + " points!"
    elif kev_points > stu_points:
        print "Player 2 wins with " + str(kev_points) + " points!"
    else:
        print "Draw, you both scored " + str(stu_points) + " points!"
        
if __name__ == "__main__":
    s = (raw_input("Enter a word: ").upper()).replace(" ", "")
    minion_game(s)
