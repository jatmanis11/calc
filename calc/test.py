n=89.9
def inti(n):
    n=str(n)
    a="1234567890."
    for i in n:
        if i not in a:
            return False
    return True
print(inti(90.02))