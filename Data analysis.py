import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("database.csv", sep=",")

def data_info(data):
    print(data.head())
    print(data.info())
    print(data.describe())

data_info(data)

# Получение уникальных дат
unique_dates = sorted(data["event_date"].unique())

print (f"Уникальные даты: {len(unique_dates)}")

print(unique_dates)

print(data[data["event_date"] == "2020-05-21"])



# Преобразование даты
data["event_date"] = pd.to_datetime(data["event_date"])

# Сортировка по дате
attendance_by_date = data.groupby(data['event_date'].dt.date)['is_attend'].mean()

# График средняя посещаемость по дням
plt.figure(figsize=(10, 5))
plt.plot(attendance_by_date.index, attendance_by_date.values, marker='o', linestyle='-')
plt.xlabel('Дата')
plt.ylabel('Средняя посещаемость')
plt.title('Средняя посещаемость по дням')
plt.grid(True)
plt.xticks(rotation=45)

# plt.savefig('attendance_by_date.png')
plt.show()



# В какие дни недели чаще всего посещали мероприятия

# Добавление столбца с днем недели
data['day_of_week'] = data['event_date'].dt.day_name()

# Группировка по дням недели
attendance_by_day = data.groupby('day_of_week')['is_attend'].sum().reindex(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']).fillna(0).astype(int)
palette = sns.color_palette("husl", len(attendance_by_day))

# График посещаемости по дням недели
plt.figure(figsize=(10, 5))
basr_day = plt.bar(attendance_by_day.index, attendance_by_day.values, color=palette)
plt.xlabel('День недели')
plt.ylabel('Количество посещений')
plt.title('Посещаемость по дням недели')
# plt.grid(axis='y')

labels = [f'{day}: {visits} посещений' for day, visits in zip(attendance_by_day.index, attendance_by_day.values)]
legend = plt.legend(basr_day, labels, loc='upper left')

plt.tight_layout()
# plt.savefig('attendance_by_day.png')
plt.show()

# print(data[data["day_of_week"] == "Sunday"])



# Какие клиенты посещают мероприятия чаще других

attendance_by_customer = data.groupby('customer_id')['is_attend'].sum()
attendance_by_customer_sorted = attendance_by_customer.sort_values(ascending=False).head(10)
palette = sns.color_palette("husl", len(attendance_by_customer_sorted))


plt.figure(figsize=(12, 6))
bars_customer = plt.bar(attendance_by_customer_sorted.index, attendance_by_customer_sorted.values, color=palette, width=8)
plt.xlabel('ID клиента')
plt.ylabel('Количество посещений')
plt.title('Топ-10 клиентов по посещаемости')
# plt.grid(axis='y')
plt.tight_layout()

plt.xticks(attendance_by_customer_sorted.index, attendance_by_customer_sorted.index, rotation=0)
labels = [f'Клиент {customer_id}: {visits} посещений' for customer_id, visits in zip(attendance_by_customer_sorted.index, attendance_by_customer_sorted.values)]
plt.legend(bars_customer, labels, loc='center left', bbox_to_anchor=(1, 0.5))


plt.show()



# Какие учетиля проводят мероприятия чаще других

attendance_by_teacher = data.groupby('teacher_ids')['is_attend'].sum()
attendance_by_teacher_sorted = attendance_by_teacher.sort_values(ascending=False).head(10)
palette = sns.color_palette("husl", len(attendance_by_teacher_sorted))


plt.figure(figsize=(12, 6))
bars_teaher = plt.bar(attendance_by_teacher_sorted.index, attendance_by_teacher_sorted.values, color=palette, width=0.5)
plt.xlabel('ID учителя')
plt.ylabel('Количество посещений')
plt.title('Топ-10 учителей по посещаемости')
# plt.grid(axis='y')
plt.xticks(attendance_by_teacher_sorted.index, attendance_by_teacher_sorted.index, rotation=0)
labels = [f'Учитель {teacher_id}: {visits} посещений' for teacher_id, visits in zip(attendance_by_teacher_sorted.index, attendance_by_teacher_sorted.values)]
legend = plt.legend(bars_teaher, labels, loc='upper left')

plt.tight_layout()
plt.show()



# Какие группы посещают мероприятия чаще других

attendance_by_group = data.groupby('group_ids')['is_attend'].sum()
attendance_by_group_sorted = attendance_by_group.sort_values(ascending=False).head(10)

plt.figure(figsize=(12, 6))
# plt.bar(attendance_by_teacher_sorted.index, attendance_by_teacher_sorted.values, color='skyblue', width=0.5)

palette = sns.color_palette("husl", len(attendance_by_group_sorted))

bars_group = plt.bar(attendance_by_group_sorted.index, attendance_by_group_sorted.values, color=palette, width=0.5)
plt.xlabel('ID группы')
plt.ylabel('Количество посещений')
plt.title('Популярность групп мероприятий по посещаемости')
# plt.grid(axis='y')
plt.xticks(attendance_by_group_sorted.index, attendance_by_group_sorted.index, rotation=0)

labels = [f'Группа {group_id}: {visits} посещений' for group_id, visits in zip(attendance_by_group_sorted.index, attendance_by_group_sorted.values)]
plt.legend(bars_group, labels, loc='upper left')

plt.tight_layout()
plt.show()

unique_grops = sorted(data["group_ids"].unique())
