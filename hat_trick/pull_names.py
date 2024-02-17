"""
Auther: Robert Rallison
Description: This tool is simply to simulate pulling names from a hat
for a gift exchange.
"""
import sys
import random
from db import DB
import constants as const


def main(argv):
    """
    Run this sucker
    """
    print(const.TITLE)
    db = DB()
    db.init_new_db()
    hat_trick_collection = {}
    #do_hat_trick(db, 'The Girls', age=const.KIDS, gender=const.GIRLS)
    #do_hat_trick(db, 'The Boys', age=const.KIDS, gender=const.BOYS)
    #do_hat_trick(db, 'The Ladies', age=const.ADULTS, gender=const.GIRLS)
    #do_hat_trick(db, 'The Guys', age=const.ADULTS, gender=const.BOYS)
    title, names = do_hat_trick(db, 'The Kids', age=const.KIDS)
    hat_trick_collection[title] = names
    title, names = do_hat_trick(db, 'The Grownups', age=const.ADULTS)
    hat_trick_collection[title] = names
    #do_hat_trick(db, 'Everyone')
    #do_hat_trick(db, 'All Females', gender=const.GIRLS)
    #do_hat_trick(db, 'All Males', gender=const.BOYS)
    if '-excludes' in argv:
        print(db.get_excludes())
    print(argv)

    pretty_print_multiple_to_file(hat_trick_collection)

def do_hat_trick(db, title, age = '', gender = ''):
    """
    1. Query the database for the list of names based on parameters.
    2. Draw the names.
    3. Print the results in a human readable format.
    4. Return the results in case we want to do more.

    Args:
        db (DB): The instance of the database class
        title (str): For pretty print purposes, the title of the list we are making.
        age (str, optional): If we specify an age (kids/adults). Defaults to ''.
        gender (str, optional): If we specify a gender (f/m). Defaults to ''.
    
    Returns:
        str: Title with spaces as underscores
        Dictionary: Names
    """
    hs_with_names = db.get_households_with_names(age = age, gender = gender)
    final_names = get_final_names(db, hs_with_names)
    pretty_print_names(final_names, title)
    return title.replace(' ', '_'), final_names

def pretty_print_names(names, title):
    """
    Prints the list in a human readable format with a title.

    Args:
        names (Dictionary): The names with their drawn assignments.
        title (str): Describes the list we created.
    """
    print(f"\n{title}")
    print('--------------------')
    for key, val in names.items():
        left_name = key.ljust(8)
        right_name = val.ljust(8)
        print(f"{left_name} |  {right_name}")
    print('--------------------')

def pretty_print_multiple_to_file(names_and_titles):
    """
    Prints the list in a human readable format with a title to a file.

    Args:
        names_and_titles (Dictionary): The names with their drawn assignments and titles for printing.
    """
    out = open(f'{const.PATH}\\names.txt', "w")
    out.write(const.TITLE)
    for title, names in names_and_titles.items():
        out.write(f"\n{title}\n")
        out.write('--------------------\n')
        for key, val in names.items():
            left_name = key.ljust(8)
            right_name = val.ljust(8)
            out.write(f"{left_name} |  {right_name}\n")
        out.write('--------------------\n')
    out.close()

def get_final_names(db, hs_with_names, max = 100):
    """
    This function is a little special in that it will keep trying, up to the max tries,
    to perform the hat trick successfully. Sometimes as we eliminate names from the pool
    we don't have enough leftover to keep drawing. So if the hat trick fails and returns
    an empty dictionary, we try again up to a limit.

    Args:
        db (DB): The instance of the database class
        hs_with_names (Dictionary): Where the keys are the households and the values are lists of names
        max (int, optional): If we ever want to specify the max tries. Defaults to 100.

    Returns:
        Dictionary: The names of each person with their drawn assignment. If it fails, it will be empty.
    """
    final_names = {}
    max_tries = max
    count = 0
    # Continue looping until it succeeds or we exceed the max tries
    while not final_names and count < max_tries:
        final_names = execute_hat_trick(db, hs_with_names)
        count += 1
    return final_names

def execute_hat_trick(db, hs_with_names):
    """
    This is it! Here is where the name drawing finally happens. To do this we build allowed lists
    for each household. This is basically all people in all other households as the number one
    rule is you can't get someone in your own household.

    1. Build allowed list for this household
    2. Remove names that have already been chosen from the allowed list
    3. Loop through all names in this household and randomly draw an assignment
    4. Check if the name is an exclusion. If so, try again.
    5. With each assignment, remove the name from the allowed list.
    6. Add the name to the used list for the next household iteration

    Args:
        db (DB): The instance of the database class
        hs_with_names (Dictionary): Where the keys are the households and the values are lists of names

    Returns:
        Dictionary: The names of each person with their drawn assignment.
    """
    used_names = []  # names we can no longer use
    hat_trick_final_picks = {}
    try:
        for key_outer, val_outer in hs_with_names.items():
            allowed_list = []
            # 1. initialize the allowed list
            for key_inner, val_inner in hs_with_names.items():
                if key_outer != key_inner:
                    allowed_list.extend(val_inner)
                    
            # 2. remove any names we have already used
            for used_name in used_names:
                if used_name in allowed_list:
                    allowed_list.remove(used_name)

            # 3. now loop through all of the names for the current household
            #    and begin pulling names from the allowed list
            for name in val_outer:
                # lets see if the db object found any excludes for this name
                excludes = db.get_excludes(name)

                # draw our first name to initialize
                name_index = random.randint(0, len(allowed_list) - 1)
                draw_name = allowed_list[name_index]
                # 4. if we have exludes, we don't want to actually remove them from
                # the allowed list, we just want to not pick them, but we must also
                # only honor the excludes if there are enough picks left in the list
                # to make it work
                if excludes and len(excludes) < len(allowed_list) and draw_name in excludes:
                    while draw_name in excludes:
                        name_index = random.randint(0, len(allowed_list) - 1)
                        draw_name = allowed_list[name_index]
                hat_trick_final_picks[name] = draw_name
                # 5. remove this name from the hat for this household
                allowed_list.remove(draw_name)
                # 6. add it to the used names so we don't try to use it again
                used_names.append(draw_name)
    except:
        # if we ever find ourselves unable to draw a name, we fail and return an empty dictionary
        # this happens when the used list depletes the allowed list before we can finish drawying
        # names for a household
        hat_trick_final_picks = {}
    return hat_trick_final_picks

if __name__ == "__main__":
    main(sys.argv[1:])