import copy
import random


class Hat:
    """ take a variable number of keyword arguments as color = quantity
    at least 1 ball
    contets instance attribute containing colors """
    def __init__(self, **kwargs):
        self.stack = {x:y for x, y in kwargs.items() if y > 0}
        self.contents = [color for color, times in self.stack.items() for y in range(times)]
        self.color = [x for x in self.stack]

    def __check_balls_quantity(self):
        return sum(y for y in self.stack.values())

    def __check_for_zero_color(self, color):
        if self.stack[color] == 0:
            return False 
        else:
            return True 

    def __decrease_color_stack(self, color):
        self.stack[color] -= 1

    def draw(self, number):
        """ accepts an argument indicating the number of balls drawed from it
        should remove balls at random from contents
        return the balls as a list of strings
        if number exceeds available quantity, return all balls  """
        list_of_colors_taken = []
        if number >= self.__check_balls_quantity():
            return [color for color, times in self.stack.items() for y in range(times)]
        else:
            flag = number
            while flag:
                color = random.choice(self.color)
                if self.__check_for_zero_color(color):
                    self.__decrease_color_stack(color)
                    list_of_colors_taken.append(color)
                    flag -= 1
                else:
                    continue
            self.contents = [color for color, times in self.stack.items() for y in range(times)]
            return list_of_colors_taken
    
    @staticmethod
    def make_dict_from_list(lista):
        new_dict = {}
        for ob in lista:
            if ob in new_dict:
                new_dict[ob] += 1
            else:
                new_dict[ob] = 1 
        return new_dict

    @staticmethod
    def check_min_two_dicts(dict1, dict2):
        s1 = set(dict1)
        s2 = set(dict2)
        ds = s2.difference(s1)
        dict1.update({x:0 for x in ds})
        return all([dict1[color] >= dict2[color] for color in dict2])
        



def experiment(hat:Hat, expected_balls, num_balls_drawn, num_experiments):
    """ hat = hat object 
    expected_balls = group of balls to attempt drawing from the hat 
    num_balls_drawn = number of balls to draw out of the hat 
    num_experiments = number of experiments to perform 
    returns a probability """ 
    satisfied_attempts = 0
    for _ in range(num_experiments):
        new_hat = copy.deepcopy(hat)
        balls_taken = hat.make_dict_from_list(new_hat.draw(num_balls_drawn))
        if hat.check_min_two_dicts(balls_taken, expected_balls):
            satisfied_attempts += 1
        else:
            continue
    return satisfied_attempts/num_experiments


if __name__ == '__main__':

    h1  = Hat(yellow=3, blue=2, green=6)
    d2 = {'blue':2, 'yellow':2}
    d3 = {'blue':2, 'yellow':1, 'purple':2}
    """ print(h1.check_min_two_dicts(d3,d2)) """
    """ print([experiment(h1, d2, 4, 2000)*100 for _ in range(15)])
    print([experiment(h1, d2, 5, 2000)*100 for _ in range(15)]) """
    hat = Hat(red=3,blue=2)
    print(hat.contents)