try: # Try to run the code below
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["key"])
except FileNotFoundError: # It is executed if FileNotFound error were found
    file = open("a_file.txt", "w")
    file.write("Something")
except KeyError as error_message:
    print(f"The key {error_message} does not exist.")
else: # only if the except were not executed
    content = file.read()
    print(content)
finally: # This will be executed anyway
    file.close()
    print("File was closed.")
# if x > 3:
    # raise ValueError("X cannot be greater than 3")
    # raise statement creates a error