"""
    Project by: Rushikesh Patil;
    project: Bring out the factorial of input number n;
"""


def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n*factorial(n-1)


if __name__ == "__main__":
    n = int(input("Enter the number: "))
    print(f"The factorial of {n} is {factorial(n)}")
