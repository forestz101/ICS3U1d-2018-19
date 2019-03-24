
def cigar_party(cigars):
    if cigars >= 40:
        return True
    else:
        return False


a = cigar_party(30)


if a:
    print("True")
else:
    print("False")
