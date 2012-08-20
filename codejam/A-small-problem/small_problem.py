from itertools import *

class SmallProblem:

    def __init__ (self,input_string):
        self.input_array = self.set_input_array(input_string)
        self.cases = self.set_cases()
        self.credits = self.set_credits()
        self.prices = self.set_prices()
        self.items = self.select_items()

    def get_input_array(self):
        return self.input_array

    def get_cases(self):
        return self.cases

    def get_credits(self):
        return self.credits

    def get_prices(self):
        return self.prices

    def set_input_array(self,input_string):
        return input_string.split('\n')

    def set_cases(self):
        try:
            return int(self.input_array[0])
        except ValueError:
            return 0

    def set_credits(self):
        case_array = []
        for i in islice(self.input_array,1,None,3):
            try:
                case_array.append(int(i))
            except ValueError:
                print "value of i is %s" % (i)
        return case_array
    
    def set_prices(self):
        price_array =[]
        for i in islice(self.input_array,3,None,3):
            price_array.append(list(imap(int,i.split(' '))))
        return price_array

    def select_items(self):
        item_list = []
        for i, price_list in enumerate(self.prices):
            for price_combo in combinations(price_list,2):
                if reduce(lambda x , y: x + y ,price_combo) == self.get_credits()[i]:
                    index_arr = [price_list.index(price_combo[0]) + 1,price_list.index(price_combo[1]) + 1]
                    if index_arr[0] != index_arr[1]:
                        item_list.append(index_arr)
                    else:
                        item_list.append(self.find_indexes(price_list,price_combo[0]))
                        
        for i in item_list:
            i.sort()
        return item_list
        
    def print_results(self):
        results = ""
        for i,item in enumerate(self.items):
            results += "Case #%d: %s\n" % ((i + 1),(' '.join(imap(str,item))))
        return results
    
    def find_indexes(self,arr,target):
        index_arr = []
        for i, val in enumerate(arr):
            if val == target:
                index_arr.append(i + 1)
        return index_arr
                
