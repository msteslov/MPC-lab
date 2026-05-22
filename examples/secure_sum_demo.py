from secure_aggregation import secure_average, secure_sum


P = 2089


def main() -> None:
    values = [120, 340, 75, 220]

    print("Private participant values:", values)
    print("Secure sum:", secure_sum(values, P))
    print("Secure average:", secure_average(values, P))


if __name__ == "__main__":
    main()
