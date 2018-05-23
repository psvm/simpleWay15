#
def half_division(sequence, checked_number, iteration_count):
    left_border = 0
    right_border = len(sequence) - 1

    while left_border <= right_border:
        iteration_count [0] = iteration_count[0] + 1
        center = left_border + (right_border - left_border) // 2
        if checked_number == sequence[center]:
            return center
        elif checked_number > sequence[center]:
            right_border = center - 1
        else:
            left_border = center + 1
    return None

sequence = [10, 9, 7, 5, 4, 1, 0, -50, -100, -101, -102, -103, -104, -105, -106]
checked_number = 10
iteration_count  = [0]
result = half_division(sequence, checked_number, iteration_count)
print("Index of checked number in sequence is " + str(result))
print(str(iteration_count[0]) + " iterations done")
