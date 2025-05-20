def add(a, b):
    try:
        if isinstance(a, int) and isinstance(b, int):
            return a + b
        else:
            raise ValueError
    except ValueError as e:
        print(f"خطا: {e}")
        return None
