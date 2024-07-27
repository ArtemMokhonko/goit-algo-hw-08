import heapq

def cables_min_cost(cables):
    # Створити мін-кучу з довжин кабелів
    heapq.heapify(cables)
    
    total_cost = 0
    
    while len(cables) > 1:
        # Витягнути два найменші елементи
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)
        
        # Об'єднати їх
        new_cable = first + second
        
        # Додати новий кабель назад у купу
        heapq.heappush(cables, new_cable)
        
        # Додати вартість злиття до загальної вартості
        total_cost += new_cable
    
    return total_cost
"""
Загальна часова складність алгоритму становить O(N log k), де N - загальна кількість елементів у всіх списках, а k - кількість списків.
"""

# Приклад використання
cables = [7, 5, 1, 4, 3]
print("Мінімальні витрати на об'єднання кабелів:", cables_min_cost(cables))
