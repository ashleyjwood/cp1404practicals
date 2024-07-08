"""
Estimated time: 30 minutes
Actual time: 45 minutes
"""

from prac_06.programming_language import ProgrammingLanguage

python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
print(python)

programming_languages = [python, ruby, visual_basic]
dynamic_languages = [language.name for language in programming_languages if language.is_dynamic()]
print(f"The dynamically typed languages are: \n{'\n'.join(dynamic_languages)}")
