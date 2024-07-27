import heapq

def merge_k_lists_1(lists):
    min_heap = []
    
    # Додаємо перші елементи кожного списку в купу
    for i in range(len(lists)):
        if lists[i]:  # Перевірка, що список не порожній
            heapq.heappush(min_heap, (lists[i][0], i, 0))  # (значення, індекс списку, індекс елемента в списку)
    
    result = []
    
    # Поки є елементи в купі
    while min_heap:
        value, list_idx, element_idx = heapq.heappop(min_heap)
        result.append(value)
        
        # Додаємо наступний елемент з того ж списку в купу, якщо він існує
        if element_idx + 1 < len(lists[list_idx]):
            next_value = lists[list_idx][element_idx + 1]
            heapq.heappush(min_heap, (next_value, list_idx, element_idx + 1))
               
    return result


def merge_k_lists_2(lists):
    # Використовуємо heapq.merge для злиття всіх відсортованих списків
    merged = heapq.merge(*lists)
    
    # Перетворюємо ітератор у список
    return list(merged)


# Приклад використання
lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists_1(lists)
print("Відсортований список:", merged_list)

# Приклад використання

merged_list = merge_k_lists_2(lists)
print("Відсортований список:", merged_list)
