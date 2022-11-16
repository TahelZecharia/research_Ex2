class List(list):
    """
    The List class inherits from python's List.
    in order for it to be able to access the items with syntax of a multidimensional array,
    updated its __getitem__ and __getitem__ function.
    """
    def __init__(self, items):

        super().__init__(items)

    def __getitem__(self, args):
        
        if type(args) is tuple:

            curr = super(List, self).__getitem__(args[0])
            for item in args[1:]:
                curr = curr.__getitem__(item)
            return curr

        return super(List, self).__getitem__(args)
        
    def __setitem__(self, key, value):
        
        if type(key) is tuple:
            self.__getitem__(key[:-1]).__setitem__(key[-1], value)

        else:
            super(List, self).__setitem__(key,  value)



if __name__ == '__main__':

    my_list1 = List([[[1, 2, 3], [4, 5, 6]],
               [[7, 8, 9], [10, 11, 12]]])

    regular_list1 = [[[1, 2, 3], [4, 5, 6]],
               [[7, 8, 9], [10, 11, 12]]]

    assert (type(my_list1) is List)
    assert (type(my_list1) is not type(regular_list1))
    assert (my_list1[0, 1, 0] == 4) # get func
    assert (my_list1[0][1][0] == 4) # get func
    assert (my_list1[1] == [[7, 8, 9], [10, 11, 12]]) # Acts like a list

    my_list1.append([13, 14, 15, 16])
    assert (my_list1[len(my_list1) - 1] == [13, 14, 15, 16])

    my_list1[0, 1, 0] = 100 # set func
    assert (my_list1[0, 1, 0] == 100)
    assert (my_list1[0][1][0] == 100)

    my_list2 = List([[["aa", "bb"], ["cc", "dd"], ["ee", "ff"], ["gg", "hh"]],
                     [["ii", "jj"], ["kk", "ll"], ["mm", "nn"], ["oo", "pp"]],
                     [["qq", "rr"], ["ss", "tt"], ["uu", "vv"], ["ww", "xx"]]])

    assert (type(my_list2) is List)
    assert (my_list2[1, 3, 0] == "oo")

    my_list2[0].append(123)
    assert (my_list2[0] == [["aa", "bb"], ["cc", "dd"], ["ee", "ff"], ["gg", "hh"], 123]) # add to the middle of the list

    my_list2[2, 3, 0] = my_list2[2, 3, 1].upper() # set func
    assert (my_list2[2, 3] == ["XX", "xx"])

