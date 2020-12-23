import json
import math
import sys

print(sys.version)
print(sys.executable)


items = json.loads(
    '[{"id":1,"text":"Item 1"},{"id":2,"text":"Item 2"},{"id":3,"text":"Item 3"}]'
)

for item in items:
    print(item["text"])


def greet(greeting, name):
    """Returns a greeting

    Args:
        greeting (string): A greet word
        name (string): A persons name

    Returns:
        strin: A greeting with a name
    """
    return f"{greeting} {name}"


print(greet("Hello", "World"))
