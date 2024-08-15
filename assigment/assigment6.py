def getMetric(metric, ListVal):
    sum = 0

    for val in ListVal:
        sum += val
    mean_v = sum / len(ListVal)

    sorted_list = sorted(ListVal)  # 7 9 14 17 43 56 81
    div = len(ListVal) // 2
    if len(ListVal) % 2 == 0:
        median_v = (ListVal[div + 1] + ListVal[div]) / 2
    else:
        median_v = ListVal[div]
    new_dict = dict()
    new_dict["mean"] = mean_v
    new_dict["median"] = median_v
    new_dict["max"] = max(ListVal)
    new_dict["min"] = min(ListVal)
    return new_dict[metric]


vals = [7, 14, 81, 56, 9, 17, 43]
mean = getMetric("mean", vals)
med = getMetric("median", vals)
max_value = getMetric("max", vals)
min_value = getMetric("min", vals)
print(f"mean {mean}")
print(f"med {med}")
print(f"max_value {max_value}")
print(f"min_value {min_value}")

