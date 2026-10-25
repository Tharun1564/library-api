def normalize_isbn(value: str) -> str:
    """Remove hyphens and spaces, and uppercase the check charcter."""
    return value.replace("-","").replace(" ","").upper()


def is_valid_isbn(isbn: str) -> bool:
    #ISBN-13: 13 digits, weights alternate 1 and 3
    if len(isbn)==13 and isbn.isdigit():
        total = sum(int(d) * (1 if i % 2==0 else 3) for i, d in enumerate (isbn[:12]))
        check = (10 - total % 10) % 10
        return check == int(isbn[12])

    if len(isbn)==10 and isbn[:9].isdigit() and (isbn[9].isdigit() or isbn[9]=="x"):
        total = sum(int(d) * (10 - i) for i, d in enumerate(isbn[:9]))
        total += 10 if isbn[9]=="x" else int(isbn[9])
        return total % 11 == 0
    return False
