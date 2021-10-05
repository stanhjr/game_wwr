import json


class Score:
    """
    The dictionary is sorted by values of no more than 10 elements
    Returns a dictionary
    """

    def __init__(self, score=0, json_list=[], name='John Doe') -> list:
        self.score = score
        self.json_list = json_list
        self.name = name

    def calculation_of_points(self) -> list:
        list_scores = []
        new_dict = {}
        zip_list = [ind for ind in range(1, 11)]
        for i in self.search_user().values():
            list_scores.append(i)
        list_scores.append(self.score)
        list_scores.sort(reverse=True)
        new_res = dict(zip(zip_list, list_scores))
        new_dict[self.name] = new_res
        self.json_list.append(new_dict)
        return self.json_list

    def search_user(self) -> dict:
        for dictionary in self.json_list:
            for keys, value in dictionary.items():
                if keys == self.name:
                    dict_values = value
                    self.json_list.remove(dictionary)
                    return dict_values
        return {}

    def show_scores(self):
        with open('scores.txt', 'r') as f:
            json_show = json.loads(f.read())
            for elem in json_show:
                for key, value in elem.items():
                    if key == self.name:
                        for key, value in value.items():
                            print(self.name, ' ', 'points:  ', value)
                            return None
            return None








def search_user(json_list, name) -> list:
    for dictionary in json_list:
        for keys, value in dictionary.items():
            if keys == name:
                return value
    return []


def calculation_of_points(score, name, seach_user=[], test_list=[]) -> list:
    new_dict = {}
    seach_user.append(score)
    seach_user.sort(reverse=True)
    new_dict[name] = seach_user[:10]
    for elem in test_list:
        for key in elem.keys():
            if key == name:
                test_list.remove(elem)
    test_list.append(new_dict)
    return test_list


def show_scores():
    """Print of result, top - 10"""
    with open('scores.txt', 'r') as f:
        json_list = json.loads(f.read())
    result_dict = {}
    for dictionary in json_list:
        i = 0
        for keys, values in dictionary.items():
            for elem in values:
                i += 1
                result_dict[str(keys) + str(i)] = elem

    if len(result_dict) > 10:
        for i in range(10):
            for key, values in result_dict.items():
                if values == max(result_dict.values()):
                    print(key[:-1], values)
                    del result_dict[key]
                    break
    else:
        for i in range(len(result_dict)):
            for key, values in result_dict.items():
                if values == max(result_dict.values()):
                    print(key[:-1], values)
                    del result_dict[key]
                    break




dict_list = [{"John Doe": [15, 10, 10, 5]},
             {"Alice": [10, 5, 15, 10, 10, 10, 10]},
             {"Stan": [5, 25, 3]}]

name = 'Alice'
show_scores()
