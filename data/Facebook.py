#############################################################################
#   Facebook
#############################################################################
# Group Email IDs 
# given a list of map, find if any of the id has any duplicated email 
# output a list of groups of IDs

# Input 
# [
#     {id = 10, email = ["a","b"]},
#     {id = 20, email = ["b","d"]},
#     {id = 30, email = ["a","c"]},
#     {id = 40, email = ["e"]},
# ]

# Output
# [[10,20,30], [40]] 
#############################################################################
def groupEmails(email_dict):

    email_map = {}  # map email to a set of IDs 

    # 1 map email to ID 
    for dictionary in email_dict:
        for email in dictionary["email"]:
            if email not in email_map:
                email_map[email] = set([dictionary["id"]])
            else:
                email_map[email].add(dictionary["id"])

    # email_map = {a-> 10 30  b->10 20  c->30    d->20   e->40}
    # [[10 30] [10 20] [30] [20] [40]]

    # 2  merge overlaping list in a list    ==  find connected component 
    res = []
    count = 0
    for _, id_set in email_map.items(): 
        if count == 0:
            res.append(id_set)
        else:
            for i in range(len(res)):
                if res[i] & id_set == set():
                    res.append(id_set)
                else:
                    res.append((id_set | res[i]))
                    res.pop(i)
        count += 1

    return res


email_dict = [
    {"id":10, "email":["a","b"]},
    {"id":20, "email":["b","d"]},
    {"id":30, "email":["a","c"]},
    {"id":40, "email":["e"]},
]
print(groupEmails(email_dict))


#####################################################
# 721. Accounts Merge
# Example 1:
# Input:  accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], 
#                     ["John", "johnnybravo@mail.com"], 
#                     ["John", "johnsmith@mail.com", "john_newyork@mail.com"], 
#                     ["Mary", "mary@mail.com"]]
# Output: [   ["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],  
#             ["John", "johnnybravo@mail.com"], 
#             ["Mary", "mary@mail.com"]]
#####################################################


from collections import defaultdict

def accountsMerge(accounts: List[List[str]]) -> List[List[str]]:
    '''
    FB intern 面试真题 稍微修改了题目   没想到dfs 也不会unionfind 妥妥的跪了 
    1   Use two different structure to store email to name AND email to emails 
    2   Run dfs on the graph for email to email to find all connected components 
    3   concatenate all names to the list of connected components 
    '''
    email_to_name = {}              # map email to name  
    email_graph = defaultdict(set)        # map email to a set of its connected emails, including itself   
    visited = set()                 # visited set for dfs traversal
    res = [] 
    
    # 1 build the email graph  and construct the email_to_name map 
    for email_pairs in accounts:
        name = email_pairs[0]
        for email in email_pairs[1:]:
            # build the undirected email_graph to hold all emails
            email_graph[email_pairs[1]].add(email)
            email_graph[email].add(email_pairs[1])
            # map email to name
            email_to_name[email] = name

    def dfs(email, cc):
        # visit current node and add to the connected_components
        visited.add(email)
        cc.append(email)
        for neighbour in email_graph[email]:
            if neighbour not in visited:
                dfs(neighbour, cc)

    # 2 run dfs on the graph and find all connected component
    for email in email_graph:
        if email not in visited:
            cc = []  
            dfs(email, cc)
            # form the solution, cc has to be in sorted order
            res.append([email_to_name[email]]+ sorted(cc))

    return res 
        
