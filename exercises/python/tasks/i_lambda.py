"""
Write lambda function that checks if string starts with letter (not case-sensitive)

“Hello”, “h” -> True
“Hi”, “b” -> False
"""

if __name__ == "__main__":
    lambda_function = lambda word, first_letter: word.lower().startswith(
        first_letter.lower()
    )
    print(lambda_function("Hello", "h"))
    print(lambda_function("Hi", "b"))
