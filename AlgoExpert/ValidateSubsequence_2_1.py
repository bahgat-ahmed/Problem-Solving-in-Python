# O(n) time | O(1) space - where n is the length of the sequence
def isValidSubsequence(array, sequence):
    if len(sequence) == 1:
        if sequence[0] in array:
            return True
        else:
            return False
    elif len(sequence) == len(array):
        if sequence == array:
            return True
        else:
            return False
    else:
        # try except blocks to catch the ValueError when a value in the
        # sequence is not found in the given array
        try:
            idx = array.index(sequence[0])
        except ValueError:
            return False
        # start looping from the second item in the sequence
        for item in sequence[1:]:
            try:
                # start searching for the index from the last obtained index
                new_idx = array.index(item, idx+1)
                if new_idx > idx:
                    # update index value
                    idx = new_idx
                else:
                    return False
            except ValueError:
                return False

        return True
