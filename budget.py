class Category:

    def __init__(self, category):   #class created passed in name of the category 
        self.category = category
        self.ledger = []   #instance variable called ledger(list) 
        self.total_withdraw = 0 

    def deposit(self, amount, description=''):
        #accepts an amount and description(optional)
        deposit_info = {'amount':amount, 'description':description}
        self.ledger.append(deposit_info)        

    def withdraw(self, amount, description=''):
        #same es deposit but with negative number 
        if self.__check_funds(amount):
            self.deposit(-amount, description)
            self.total_withdraw += amount
            return True 
        else:
            return False 

    def get_balance(self):
        #return current balance
        return sum(x['amount'] for x in self.ledger)

    def transfer(self, amount, target):       #accept amount and another budget category
        if self.__check_funds(amount):
            description_to = 'Transfer to {}'.format(target.category)
            self.withdraw(amount, description_to)
            description_from = 'Transfer from {}'.format(self.category)
            target.deposit(amount, description_from)
            return True 
        else:
            return False 
  

    def __check_funds(self, amount):
        #False if amount greater than the balance, True otherwise 
        total_balance = self.get_balance()
        if amount > total_balance:
            return False 
        else:
            return True 

    def __str__(self):
        first_line =  format(self.category, '*^30')
        followed_lines = [first_line]
        for x in self.ledger:
            string = x['description'][:23].ljust(23) + '{:.2f}'.format(x['amount']).rjust(7)
            followed_lines.append(string)
        final_line = 'Total:'+str(self.get_balance()).rjust(7)
        followed_lines.append(final_line)
        return '\n'.join(followed_lines)

    @staticmethod
    def format_category_name(list_of_names):
        max_len_name = max(map(lambda x: len(x), list_of_names))
        formated_list = []
        for x in list_of_names:
            if len(x) < max_len_name:
                new_name = x + ' '*(max_len_name - len(x))
                formated_list.append(new_name)
            else:
                formated_list.append(x)
        return formated_list

    @staticmethod
    def calculate_percent_withdraw(category_list):
        withdraws = [x.total_withdraw for x in category_list]
        sum_withdraws = sum(withdraws)
        percent_withdraw = [x/sum_withdraws for x in withdraws]
        str_decimals =  ['{:f}'.format(x) for x in percent_withdraw]
        return [int(float(x[:3])*100) for x in str_decimals]

def create_spend_chart(categories_list):
    print('Percentage spent by category')
    categories_list_len = len(categories_list)
    list_cat_names = [x.category for x in categories_list]
    max_len_name = max(map(lambda x: len(x), list_cat_names))
    lines_list = []
    for x in range(100, -1, -10):
        lines_list.append(str(x).rjust(3)+'|')
    lines_list.append(' '*4 + '-'*3*categories_list_len + '-')
    categories_list_formated = Category.format_category_name(list_cat_names)
    for x in range(max_len_name):
        string = ' '*4 + ''.join([categories_list_formated[y][x].center(3) for y in range(len(categories_list))])
        lines_list.append(string)
    pertcent_list = Category.calculate_percent_withdraw(categories_list)
    for line in range(10, -1, -1):
        for number in pertcent_list:
            if int(lines_list[line][:3]) <= number:
                lines_list[line] = lines_list[line] + ('o'.center(3))
            else:
                lines_list[line] = lines_list[line] + (' '*3)
    return '\n'.join(lines_list)





if __name__ == '__main__':
    food = Category("Food")
    entertainment = Category("Entertainment")
    business = Category("Business")
    food.deposit(900, "deposit")
    entertainment.deposit(900, "deposit")
    business.deposit(900, "deposit")
    food.withdraw(105.55)
    entertainment.withdraw(33.40)
    business.withdraw(10.99)
    print(create_spend_chart([business, food, entertainment]))
    expected = "Percentage spent by category\n100|          \n 90|          \n 80|          \n 70|    o     \n 60|    o     \n 50|    o     \n 40|    o     \n 30|    o     \n 20|    o  o  \n 10|    o  o  \n  0| o  o  o  \n    ----------\n     B  F  E  \n     u  o  n  \n     s  o  t  \n     i  d  e  \n     n     r  \n     e     t  \n     s     a  \n     s     i  \n           n  \n           m  \n           e  \n           n  \n           t  "
    print(expected)