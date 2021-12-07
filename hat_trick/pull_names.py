import random
from db import DB
import constants as const

def main():
    print(const.TITLE)
    db = DB()
    db.init_new_db()
    hs_with_names_kids = db.get_households_with_names(age = 'kids')
    final_names_kids = get_final_names(hs_with_names_kids)
    hs_with_names_adults = db.get_households_with_names(age = 'adults')
    final_names_adults = get_final_names(hs_with_names_adults)

    pretty_print_names(final_names_kids, 'Kids')
    pretty_print_names(final_names_adults, 'Adults')

def pretty_print_names(names, title):
    print(f"\n{title}")
    print('--------------------')
    for key, val in names.items():
        left_name = key.ljust(8)
        right_name = val.ljust(8)
        print(f"{left_name} |  {right_name}")
    print('--------------------')

def get_final_names(hs_with_names):
    final_names = {}
    max_tries = 100
    count = 0
    while not final_names and count < max_tries:
        final_names = execute_hat_trick(hs_with_names)
        count += 1
    return final_names

def execute_hat_trick(hs_with_names):
     # Build allowed lists
    names_with_allowed_lists = {}
    used_names = []
    hat_trick_final_picks = {}
    try:
        for key_outer, val_outer in hs_with_names.items():
            allowed_list = []
            # initialize the allowed list
            for key_inner, val_inner in hs_with_names.items():
                if key_outer != key_inner:
                    for val in val_inner:
                        # make sure we only add the names if there
                        # and exclude list available
                        actual_val = ''
                        if isinstance(val, dict):
                            actual_val = list(val.keys())[0]
                        else:
                            actual_val = val
                        allowed_list.append(actual_val)
            # remove any names we have already used
            for used_name in used_names:
                if used_name in allowed_list:
                    allowed_list.remove(used_name)
            # now loop through all of the names for the current household
            # and begin pulling names from the allowed list
            for name in val_outer:
                actual_name = ''
                excludes = []
                # if there are any excludes for this name, now is the time
                # to grab them
                if isinstance(name, dict):
                    actual_name = list(name.keys())[0]
                    excludes = name[actual_name]
                else:
                    actual_name = name
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
                hat_trick_final_picks[actual_name] = draw_name
                used_names.append(draw_name)
                # remove this name from the hat for this household
                allowed_list.remove(draw_name)
                names_with_allowed_lists[actual_name] = allowed_list
    except:
        hat_trick_final_picks = {}
    return hat_trick_final_picks


if __name__ == "__main__":
    main()