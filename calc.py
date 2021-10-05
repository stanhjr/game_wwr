import json

a = [{"John Doe": {"1": 15, "2": 10, "3": 10, "4": 10, "5": 10, "6": 10, "7": 10, "8": 5, "9": 5, "10": 5}},
     {"Alice": {"1": 15, "2": 10}},
     {"Stan": {"1": 35, "2": 5}}
     ]


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



b = Score(20, a, 'Stan')
c = b.calculation_of_points()
print(c)
b.show_scores()

name = 'Alice'
with open('scores.txt', 'r') as f:
    json_show = json.loads(f.read())
    for elem in json_show:
        for key, value in elem.items():
            if key == name:
                for key, value in value.items():
                    print(name, ' ', 'points:  ', value)