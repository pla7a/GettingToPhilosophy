import wikipedia

score = 0


def start_game():
    # Displays the ascii art on the first boot of the game
    f = open("ascii_art.txt","r")
    print(f.read())
    print("-"*60)
    intro()



def intro():
    inp = str(input("[1] Start the game\n[2] See high scores\n[3] Read the idea for this game\n[4] Read instructions\n[q] Quit the game\n "))
    print("-"*60)
    if inp == "1":
        # Begins the game
        random_page()
    elif inp == "2":
        # Fetches high scores from the text file
        f = open("hs.txt", "r")
        print(f.read())
        print("-"*60)
        intro()
    elif inp == "3":
        # Fetches info about the game from the text file
        f = open("idea.txt","r")
        print(f.read())
        print("-"*60)
        intro()
    elif inp == "4":
        f = open("instructions.txt","r")
        print(f.read())
        print("-"*60)
        intro()
    elif inp == "q":
        # Quits the game
        exit()
    else:
        # Alerts user that they have entered an incorrect command
        print("Sorry, command not recognized. Please try again.")
        intro()

def random_page():
    # Fetches a random page from wikipedia
    try:
        page = wikipedia.page(wikipedia.random())
        print(page.links)
        show_links(page)

    # Deals with wiki disambiguation error
    except wikipedia.exceptions.DisambiguationError:
        random_page()



def show_links(page):
    # Keeps track of the user's score
    global score
    score += 1

    print("You got the page: {0}" .format(page.title))
    links = []
    for link in page.links:
        links.append(link)

    for i in range(0,len(links)):
        # Prints all of the possible links from the random page
        print("[{0}] - {1}" .format(i,links[i]))

    # Brings up info for new article of the chosen link
    new_page = links[choose_art(len(links), page.title)]
    if str(new_page) == "Philosophy" or str(new_page) == "philosophy":
        print("Well done. You completed the game in {0} moves." .format(score))
        print("Score: {0}" .format(score))
        submit(score)
    else:
        new_article(new_page, page)



def choose_art(len_links, title):
    a = str(input("Pick a number: "))

    # Ensures the user chooses a valid link
    if a in [str(x) for x in range(len_links)]:
        return int(a)
    elif a == "q":
        exit()
    elif a == "s":
        print("\n{0}\n".format(wikipedia.summary(title)))
        return(choose_art(len_links,title))
    else:
        print("Sorry. The index is out of range. Choose another number.")
        return(choose_art(len_links, title))


def new_article(new_title, old_title):
# Function takes 2 arguments (current page title and old page title). This is incase of disambiguation and the user needs to choose another link.
    try:
        new_page = wikipedia.page(new_title)
        show_links(new_page)

    # Deals with wiki disambiguation error
    except wikipedia.exceptions.DisambiguationError:
        print("An error occurred (due to disambiguation), please choose another link.")
        show_links(wikipedia.page(old_title))


# Needs changing to only allow unique submissions for each name (with possibility of overwrite)
def submit(score):
    name = str(input("What is your name? "))
    if len(name) > 20:
        print("Name too long. Try again.")
        submit(score)
    else:
        file_a = open("hs.txt","a")
        file_r = open("hs.txt","r")
        file_a.write("Name: {0:25} Score: {1:3}\n" .format(name,score))



start_game()
