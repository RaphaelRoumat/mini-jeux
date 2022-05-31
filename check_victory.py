
def start_check(coordy, coordx, coins, player):
    nbr_aligned = 1

    if 0 <= coordx + 1 <= 6:
        nbr_aligned += check_case(coordy, coordx + 1, coins, player, [0, 1])
    if 0 <= coordx - 1 <= 6:
        nbr_aligned += check_case(coordy, coordx - 1, coins, player, [0, -1])

    if nbr_aligned < 4:
        nbr_aligned = 1
        if 0 <= coordy + 1 <= 5:
            nbr_aligned += check_case(coordy + 1, coordx, coins, player, [1, 0])
        if 0 <= coordy - 1 <= 5:
            nbr_aligned += check_case(coordy - 1, coordx, coins, player, [-1, 0])

    if nbr_aligned < 4:
        nbr_aligned = 1
        if 0 <= coordy + 1 <= 5 and 0 <= coordx + 1 <= 6:
            nbr_aligned += check_case(coordy + 1, coordx + 1, coins, player, [1, 1])
        if 0 <= coordy - 1 <= 5 and 0 <= coordx - 1 <= 6:
            nbr_aligned += check_case(coordy - 1, coordx - 1, coins, player, [-1, -1])

    if nbr_aligned < 4:
        nbr_aligned = 1
        if 0 <= coordy + 1 <= 5 and 0 <= coordx - 1 <= 6:
            nbr_aligned += check_case(coordy + 1, coordx - 1, coins, player, [1, -1])
        if 0 <= coordy - 1 <= 5 and 0 <= coordx + 1 <= 6:
            nbr_aligned += check_case(coordy - 1, coordx + 1, coins, player, [-1, 1])

    if nbr_aligned >= 4:
        return True
    else:
        return False


def check_case(coordy, coordx, coins, player, direction):
    nbr_aligned = 0
    if coins[coordy][coordx] == player:
        nbr_aligned += 1

        if 0 <= coordy + direction[0] <= 5 and 0 <= coordx + direction[1] <= 6:
            nbr_aligned += check_case(coordy + direction[0], coordx + direction[1], coins, player, direction)
    return nbr_aligned
