

def find_combinations(budget, newspapers):
def backtrack(start, budget, curr, ans):
    if budget < 0:
        return
    if budget == 0:
        ans.append(curr)
        return
    for i in range(start, len(newspapers)):
        backtrack(i+1, budget-newspapers[i].prices[0], curr + [newspapers[i].name], ans)

ans = []
backtrack(0, budget, [], ans)
return ans

class Newspaper:
def __init__(self, name, prices):
    self.name = name
    self.prices = prices
e1 = Newspaper("TOI", [3,3,3,3,3,5,6])
e2 = Newspaper("Hindu", [2.5, 2.5, 2.5, 2.5, 2.5, 4, 4])
e3 = Newspaper("ET", [4, 4, 4, 4, 4, 4, 10])
e4 = Newspaper("BM", [1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5])
e5 = Newspaper("HT", [2, 2, 2, 2, 2, 4, 4])

newspapers = [e1,e2,e3,e4,e5]

budget = 40
combinations = find_combinations(budget, newspapers)

for comb in combinations:
print(comb)