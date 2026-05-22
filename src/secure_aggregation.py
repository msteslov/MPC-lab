from additive_sharing import reconstruct_secret, split_secret


def secure_sum(values: list[int], p: int) -> int:
    if not values:
        raise ValueError("values must not be empty")

    n = len(values)
    participant_shares = [split_secret(value, n, p) for value in values]
    aggregate_shares = [0] * n

    for shares in participant_shares:
        for i in range(n):
            aggregate_shares[i] = (aggregate_shares[i] + shares[i]) % p

    return reconstruct_secret(aggregate_shares, p)


def secure_average(values: list[int], p: int) -> float:
    return secure_sum(values, p) / len(values)
