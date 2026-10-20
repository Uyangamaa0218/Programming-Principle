from simple_checkout import run as run_simple_checkout
from complex_checkout import run as run_complex_checkout
def main() -> None:
    print("this is the simple checkout")
    run_simple_checkout()
    print("This is the complex checkout")
    run_complex_checkout()

if __name__ == "__main__":
    main()

