import xml.etree.ElementTree as ET
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

print(analyze_user_activity(load_users_data()))
