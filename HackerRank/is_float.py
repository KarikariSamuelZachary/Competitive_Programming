if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        N = input()
        try:
            N == float(N)
            if "." in N:
                print("True")
            else:
                print("False")
        except ValueError:
            print("False")
    