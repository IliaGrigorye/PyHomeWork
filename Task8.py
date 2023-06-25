def combinations(items, max_weight):
    if not items:
        return [[]]
    else:
        result = []
        item, weight = items[0]  # первый предмет в списке
        rest = items[1:]  # остальные предметы в списке
        if weight > max_weight:
            # пропускаем элемент, если его масса больше максимальной грузоподъёмности
            result = combinations(rest, max_weight)
        else:
            # две рекурсивные ветви:
            # 1) добавляем первый предмет и ищем все возможные комбинации для оставшихся предметов
            # 2) не добавляем первый предмет и ищем все возможные комбинации для оставшихся предметов
            with_item = [[item] + c for c in combinations(rest, max_weight - weight)]
            without_item = combinations(rest, max_weight)
            result = with_item + without_item
        return result

# пример использования:
items = {"спальник": 1.2, "палатка": 2.3, "котелок": 0.5, "продукты": 4.7, "карта": 0.1}
max_weight = 5.0  # максимальная грузоподъемность рюкзака
items_list = [(k, v) for k, v in items.items()]  # конвертируем словарь в список кортежей (ключ, значение)
combs = combinations(items_list, max_weight)  # ищем все возможные комбинации
for c in combs:
    print(c)
