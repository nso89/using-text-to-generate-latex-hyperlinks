

def verify(parameter: str, name: str) -> None:
    """
    Verify if parameter is blank, if so, raise ValueError.
    """
    if not parameter or parameter.isspace():
        raise ValueError(f"{name} cannot be blank!")
    if parameter.startswith(" ") or parameter.endswith(" "):
        raise ValueError(f"{name} cannot begin or end with an empty space!")


def main():

    try:
        
        text = input("Text: ").strip()
        verify(parameter = text, name = "Text")

        link = input("Link: ").strip()
        verify(parameter = link, name = "Hyperlink")

        print(f"Output: \href{{{link}}}{{{text}}}")
    
    except(ValueError) as e:
        print(e)

if __name__ == "__main__":
    main()
