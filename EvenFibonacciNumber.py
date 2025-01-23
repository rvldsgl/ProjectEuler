def generate_fibonacci(limit):
    fib_list = [1, 2]  # Initialize the Fibonacci sequence
    i = 0

    while True:
        next_value = fib_list[i] + fib_list[i + 1]
        if next_value > limit:
            break
        fib_list.append(next_value)
        i += 1

    return fib_list

def sum_even_numbers(sequence):
    return sum(number for number in sequence if number % 2 == 0)

def main():
    limit = 4000000  
    fib_sequence = generate_fibonacci(limit)
    even_sum = sum_even_numbers(fib_sequence)

    print("Fibonacci Sequence:", fib_sequence)
    print("Sum of even numbers:", even_sum)

if __name__ == "__main__":
    main()
