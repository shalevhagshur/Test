# tools/col.py

def zip_it(t1, t2):
    """
    Zips two collections (lists, tuples, etc.) together and returns the result.
    """
    zipped_result = []
    
    # Determine the minimum length of the two collections
    min_length = min(len(t1), len(t2))
    
    # Zip the collections
    for i in range(min_length):
        zipped_result.append((t1[i], t2[i]))
    
    return zipped_result
