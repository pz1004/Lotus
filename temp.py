from lotus.libero.benchmark.libero_suite_task_map import libero_task_map
libero_100 = libero_task_map['libero_100']
task_orders_25 = [0, 1, 2, 6, 7, 11, 12, 13, 18, 19, 20, 22, 23, 24, 28, 29, 30, 33, 35, 36, 38, 40, 41, 92, 93]
task_orders_30 = task_orders_25 + [3, 4, 5, 8, 9]
task_orders_35 = task_orders_30 + [10, 14, 15, 16, 17]
task_orders_40 = task_orders_35 + [21, 25, 26, 27, 31]
task_orders_45 = task_orders_40 + [32, 34, 37, 39, 42]
task_orders_50 = task_orders_45 + [43, 44, 45, 98, 99]

Dataset_Name_List_25 = [
    f"../datasets/libero_100/{libero_100[i]}_demo" for i in task_orders_25
]

print(Dataset_Name_List_25)