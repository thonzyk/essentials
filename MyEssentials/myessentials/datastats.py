def abs_hist(data):
    """Returns x and y for bar-plot representing absolute histogram of the input list data"""
    hist_dict = dict()

    # Initialize dictionary for every class of elements in list
    classes = set(data)
    for element in classes:
        hist_dict[element] = 0

    # Count the instances
    for element in data:
        hist_dict[element] += 1

    x = [cls for cls in hist_dict]
    y = [hist_dict[cls] for cls in hist_dict]

    return x, y


if __name__ == '__main__':
    abs_hist(["a", "z", "b", "a", "b", "a"])
