def comparison(version_a, version_b):
    """Function which compares versions.

     Args:
         version_a: str - comparable version.
         version_b: str - needful version.

     Returns:
         int - if version is equal: 0, if version_a older: -1, if version_b older: 1
     """
    if version_a[-1] == '.':
        version_a += '0'
    if version_b[-1] == '.':
        version_b += '0'
    arr_a = list(map(int, version_a.split('.')))
    arr_b = list(map(int, version_b.split('.')))
    while len(arr_a) != len(arr_b):
        if len(arr_a) > len(arr_b):
            arr_b.append(0)
        elif len(arr_a) < len(arr_b):
            arr_a.append(0)
    for num_a, num_b in zip(arr_a, arr_b):
        if num_a < num_b:
            return -1
        if num_a > num_b:
            return 1
    return 0


if __name__ == '__main__':
    print(comparison('1.10.10', '1.10.10.0.0.0.0.0'))
