# This program groups together similar anagrams passed as a list.


def groupAnagrams(strs):
    ana_dict = {};
    for i in strs:
        alpha_w = ''.join(sorted(i))
        print("alpha word ", alpha_w)
        if alpha_w in ana_dict.keys():
            ana_dict[alpha_w].append(i)
        else:
            ana_dict[alpha_w] = [i]
    print("ana dict is ", ana_dict)
    return [value for value in ana_dict.values()]

#Example:
#print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
#output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
