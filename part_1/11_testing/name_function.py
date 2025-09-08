def get_formatted_name(first, last, middle=''): 
    # changing the code so that passes the test. Not chaing the test so that the
    # code runs 
    """Generate a neatly formatted full name."""
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()
