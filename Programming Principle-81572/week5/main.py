from eircode_validator import has_eircode_shape

def main():
    examples= [
        "A65 F4E2",
        "D02 X285",
        "A65F4E2",
        "A65 F4",
        "",
    ]

    print("week5: Regex Expression with Unit tests")
    print("Eircode shape demonstration (3 characters + space + 4 characters):")
    print("\n")

    for value in examples:
        result = has_eircode_shape(value)
        print(f"{value!r:14} -> {result}")

if __name__ == "__main__":
    main()