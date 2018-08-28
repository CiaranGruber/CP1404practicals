from prac_06.programming_language import ProgrammingLanguage


def main():
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    print(ruby)
    print()
    print('The dynamic typed languages are:')
    for programming_language in [ruby, python, visual_basic]:
        if programming_language.typing == 'Dynamic':
            print(programming_language.name)



main()
