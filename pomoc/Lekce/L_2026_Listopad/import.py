import math

print(f"math.pi = {math.pi}")
print(f"sin 90 angle: {math.sin(math.pi/2)}")


def safe_divide(a, b):
    try:
        answer = a / b
    except ZeroDivisionError as there:
        print(f"Error: {there}")
        answer = None
    except Exception as e:
        text = f"Can't divide object {a} by {b}: {e}"
        raise Exception(text)
    finally:
        print("safe_divide() finished")
        print(f"this is the finally block, it will always run")
    return answer


print(safe_divide(10, 2))