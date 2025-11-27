authors = {
    "e r eddison": ["The Worm Ouroboros", "Mistress of Mistresses"],
    "n k jemisin": ["The Fifth Season", "The Stone Sky"],
    "tamsyn muir": ["Gideon the Ninth", "Harrow the Ninth"],
    "j r r tolkien": ["The Hobbit", "The Silmarillion"],
    "j k rowling": ["Philosopher's Stone", "Chamber of Secrets"]
}

author_input = input("Enter an author name: ").lower().strip()

# safe lookup
books = authors.get(author_input)

if books:
    print("Books:", ", ".join(books))
else:
    print("Author not found, try again.")

