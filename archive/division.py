import argparse

def divide(numerator: float, denominator: float) -> float:
    """Return numerator / denominator, raising ValueError on division by zero."""
    if denominator == 0:
        raise ValueError("denominator cannot be zero")
    return numerator / denominator

def main() -> None:
    parser = argparse.ArgumentParser(description='Divide two numbers.')
    parser.add_argument("numerator", type=float, help="First number (numerator)")
    parser.add_argument("denominator", type=float, help="Second number (denominator)")
    args = parser.parse_args()

    try:
        result = divide(args.numerator, args.denominator)
    except ValueError as e:
        print(f"Error: {e}")

    print(result)

if __name__ == "__main__":
    main()