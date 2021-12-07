import random
from db import DB
import constants as const

def main():
    print(const.TITLE)
    db = DB()
    db.init_new_db()
    do_hat_trick(db, 'The Girls', age='kids', gender='f')
    do_hat_trick(db, 'The Boys', age='kids', gender='m')
    do_hat_trick(db, 'The Ladies', age='adults', gender='f')
    do_hat_trick(db, 'The Guys', age='adults', gender='m')
    do_hat_trick(db, 'The Kids', age='kids')
    do_hat_trick(db, 'The Grownups', age='adults')
    do_hat_trick(db, 'Everyone')
    do_hat_trick(db, 'All Females', gender='f')
    do_hat_trick(db, 'All Males', gender='m')

def do_hat_trick(db, title, age = '', gender = ''):
    hs_with_names = db.get_households_with_names(age = age, gender = gender)
    final_names = get_final_names(db, hs_with_names)
    pretty_print_names(final_names, title)

def pretty_print_names(names, title):
    print(f"\n{title}")
    print('--------------------')
    for key, val in names.items():
        left_name = key.ljust(8)
        right_name = val.ljust(8)
        print(f"{left_name} |  {right_name}")
    print('--------------------')

def get_final_names(db, hs_with_names):
    final_names = {}
    max_tries = 100
    count = 0
    while not final_names and count < max_tries:
        final_names = execute_hat_trick(db, hs_with_names)
        count += 1
    return final_names

def execute_hat_trick(db, hs_with_names):
    used_names = []  # names we can no longer use
    hat_trick_final_picks = {}
    try:
        for key_outer, val_outer in hs_with_names.items():
            allowed_list = []
            # initialize the allowed list
            for key_inner, val_inner in hs_with_names.items():
                if key_outer != key_inner:
                    allowed_list.extend(val_inner)
                    
            # remove any names we have already used
            for used_name in used_names:
                if used_name in allowed_list:
                    allowed_list.remove(used_name)

            # now loop through all of the names for the current household
            # and begin pulling names from the allowed list
            for name in val_outer:
                # lets see if the db object found any excludes for this name
                excludes = db.get_excludes(name)

                # draw our first name to initialize
                name_index = random.randint(0, len(allowed_list) - 1)
                draw_name = allowed_list[name_index]
                # if we have exludes, we don't want to actually remove them from
                # the allowed list, we just want to not pick them, but we must also
                # only honor the excludes if there are enough picks left in the list
                # to make it work
                if excludes and len(excludes) < len(allowed_list) and draw_name in excludes:
                    while draw_name in excludes:
                        name_index = random.randint(0, len(allowed_list) - 1)
                        draw_name = allowed_list[name_index]
                hat_trick_final_picks[name] = draw_name
                used_names.append(draw_name)
                # remove this name from the hat for this household
                allowed_list.remove(draw_name)
    except:
        hat_trick_final_picks = {}
    return hat_trick_final_picks
    
if __name__ == "__main__":
    main()