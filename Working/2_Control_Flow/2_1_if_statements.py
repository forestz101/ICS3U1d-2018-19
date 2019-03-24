def cigar_party(cigars, is_weekend):
    if 40 >= cigars <= 60 and not is_weekend:
        return True
    elif cigars >= 40 and is_weekend:
        return True
    else:
        return False


if cigar_party(70, False):
    print("True")
else:
    print("False")


