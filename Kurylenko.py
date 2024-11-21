def bubble_sort(arr):
    """Бульбашкове сортування"""
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Міняємо місцями, якщо елемент більший за наступний
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def selection_sort(arr):
    """Сортування вибором"""
    n = len(arr)
    for i in range(n):
        # Знаходимо індекс мінімального елемента
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Міняємо місцями мінімальний елемент з першим у поточній підмножині
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


def insertion_sort(arr):
    """Сортування вставкою"""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Зсуваємо елементи, щоб знайти позицію для вставки
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


# Приклад використання:
if __name__ == "__main__":
    # Початковий список
    test_list = [64, 34, 25, 12, 22, 11, 90]

    print("Бульбашкове сортування:", bubble_sort(test_list.copy()))
    print("Сортування вибором:", selection_sort(test_list.copy()))
    print("Сортування вставкою:", insertion_sort(test_list.copy()))
