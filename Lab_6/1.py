import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
def load_users_data():
    try:
        users_tree = ET.parse('users.xml')
        users = []
        for user_elem in users_tree.getroot().findall('user'):
            user = {
                'user_id': int(user_elem.find('user_id').text),
                'name': user_elem.find('name').text,
                'age': int(user_elem.find('age').text),
                'weight': int(user_elem.find('weight').text),
                'fitness_level': user_elem.find('fitness_level').text,
                'workouts': []
            }
            users.append(user)
        return users
    except FileNotFoundError:
        print("Файл не найден")
        return []
def load_workouts_data():
    try:
        workouts_tree = ET.parse('workouts.xml')
        workouts = []
        for workout_elem in workouts_tree.getroot().findall('workout'):
            workout = {
                'workout_id': int(workout_elem.find('workout_id').text),
                'user_id': int(workout_elem.find('user_id').text),
                'type': workout_elem.find('type').text,
                'duration': int(workout_elem.find('duration').text),
                'distance': float(workout_elem.find('distance').text),
                'calories': int(workout_elem.find('calories').text),
                'avg_heart_rate': int(workout_elem.find('avg_heart_rate').text),
                'intensity': workout_elem.find('intensity').text,

            }
            workouts.append(workout)
        return workouts
    except FileNotFoundError:
        print("Файл не найден")
        return []
users = load_users_data()
workouts = load_workouts_data()
users_dict = {u['user_id']: u for u in users}
for w in workouts:
    u_id = w['user_id']
    if u_id in users_dict:
        users_dict[u_id]['workouts'].append(w)

def get_stats(users, workouts):
    total_workouts = len(workouts)
    total_users = len(users)
    total_calories = sum(w['calories'] for w in workouts)
    total_hours = sum(w['duration'] for w in workouts) / 60
    total_distance = sum(w['distance'] for w in workouts)
    print("\nОБЩАЯ СТАТИСТИКА")
    print("===================")
    print(f"Всего тренировок: {total_workouts}")
    print(f"Всего пользователей: {total_users}")
    print(f"Сожжено калорий: {total_calories}")
    print(f"Общее время: {total_hours:.1f} часов")
    print(f"Пройдено дистанции: {total_distance:.1f} км")

def analyze_user_activity(users):
    user_stats = []
    for user in users:
        u_workouts = user['workouts']
        count = len(u_workouts)
        calories = sum(w['calories'] for w in u_workouts)
        hours = sum(w['duration'] for w in u_workouts) / 60
        user_stats.append({
            'name': user['name'],
            'level': user['fitness_level'],
            'count': count,
            'calories': calories,
            'hours': hours
        })
    sorted_users = sorted(user_stats, key=lambda x: x['calories'], reverse=True)[:3]
    print("\nТОП-3 АКТИВНЫХ ПОЛЬЗОВАТЕЛЕЙ:")
    for i, u in enumerate(sorted_users, 1):
        print(f"{i}. {u['name']} ({u['level']}):")
        print(f"   Тренировок: {u['count']}")
        print(f"   Калорий: {u['calories']}")
        print(f"   Время: {u['hours']:.1f} часов")
def analyze_workout_types(workouts):
    types_stats = {}
    total_count = len(workouts)

    for w in workouts:
        w_type = w['type']
        if w_type not in types_stats:
            types_stats[w_type] = {'count': 0, 'duration': 0, 'calories': 0}
        
        types_stats[w_type]['count'] += 1
        types_stats[w_type]['duration'] += w['duration']
        types_stats[w_type]['calories'] += w['calories']

    print("\nРАСПРЕДЕЛЕНИЕ ПО ТИПАМ ТРЕНИРОВОК:")
    for w_type, stats in types_stats.items():
        percent = (stats['count'] / total_count) * 100
        avg_dur = stats['duration'] / stats['count']
        avg_cal = stats['calories'] / stats['count']
        
        print(f"{w_type.capitalize()}: {stats['count']} тренировок ({percent:.1f}%)")
        print(f"   Средняя длительность: {avg_dur:.0f} мин")
        print(f"   Средние калории: {avg_cal:.0f} ккал")
def find_user_workouts(users, user_name):
    target_user = next((u for u in users if u['name'].lower() == user_name.lower()), None)
    if target_user:
        return target_user['workouts']
    return []
def analyze_user(user, user_workouts):
    if not user:
        print("\nПользователь не найден.")
        return

    count = len(user_workouts)
    calories = sum(w['calories'] for w in user_workouts)
    hours = sum(w['duration'] for w in user_workouts) / 60
    distance = sum(w['distance'] for w in user_workouts)
    avg_cal = calories / count if count > 0 else 0
    
    type_counts = {}
    for w in user_workouts:
        type_counts[w['type']] = type_counts.get(w['type'], 0) + 1
    fav_type = max(type_counts, key=type_counts.get) if type_counts else "нет"

    print(f"\nДЕТАЛЬНЫЙ АНАЛИЗ ДЛЯ ПОЛЬЗОВАТЕЛЯ: {user['name']}")
    print(f"Возраст: {user['age']} лет, Вес: {user['weight']} кг")
    print(f"Уровень: {user['fitness_level']}")
    print(f"Тренировок: {count}")
    print(f"Сожжено калорий: {calories}")
    print(f"Общее время: {hours:.1f} часов")
    print(f"Пройдено дистанции: {distance:.1f} км")
    print(f"Средние калории за тренировку: {avg_cal:.0f}")
    print(f"Любимый тип тренировки: {fav_type}")
target_name = "Анна"
user_obj = next((u for u in users if u['name'] == target_name), None)
if user_obj:
    analyze_user(user_obj, user_obj['workouts'])



