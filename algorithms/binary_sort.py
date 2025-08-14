
def binary_sort(list: list[any], target: any) -> list[any]:
    low = 0
    high = len(list) - 1
    while low <= high: 
        mid = (low + high) // 2
        if list[mid] == target:
            return mid
        elif list[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return None
