"""
Created on Thu Jul  9 21:08:39 2020

@author: kach@microsoft.com
"""
import itertools

class apriori:
    def __init__(self, data, support=20, confidence=50):
        self.support = support
        self.confidence = confidence
        self.data = data #list / #handle other data types
        
    """apriori_gen function to compute candidate k-itemset, (Ck) , using frequent (k-1)-itemset, (Lk_1)"""
    def apriori_gen(self,Lk_1, k):
        length = k
        Ck = [] 
        for list1 in Lk_1:
            for list2 in Lk_1:
                count = 0
                c = []
                if list1 != list2:
                    while count < length-1:
                        if list1[count] != list2[count]:
                            break
                        else:
                            count += 1
                    else:
                        if list1[length-1] < list2[length-1]:
                            for item in list1:
                                c.append(item)
                            c.append(list2[length-1])
                            if not self.has_infrequent_subset(c, Lk_1, k):
                                Ck.append(c) 
                                c = []
        return Ck
    
    """function to compute 'm' element subsets of a set S"""    
    def findsubsets(self,S,m):
        return set(itertools.combinations(S, m))
    
    """has_infrequent_subsets function to determine if pruning is required to remove unfruitful candidates (c) using the Apriori property, with prior knowledge of frequent (k-1)-itemset (Lk_1)"""       
    def has_infrequent_subset(self,c, Lk_1, k):
        list = []
        list = self.findsubsets(c,k)
        for item in list: 
            s = []
            for l in item:
                s.append(l)
            s.sort()
            if s not in Lk_1:
                return True
        return False
    
    
    """frequent_itemsets function to compute all frequent itemsets"""    
    def frequent_itemsets(self):
        k = 2
        Lk_1 = []
        Lk = []
        L = []
        count = 0
        transactions = 0
        for item in self.L1:
            Lk_1.append(item)
        while Lk_1 != []:
            Ck = []
            Lk = []
            Ck = self.apriori_gen(Lk_1, k-1)
            #print "-------------------------CANDIDATE %d-ITEMSET---------------------" % k
            #print "Ck: %s" % Ck
            #print "------------------------------------------------------------------"
            for c in Ck:
                count = 0
                transactions = 0
                s = set(c)
                for T in self.data:
                    transactions += 1
                    t = set(T)
                    if s.issubset(t) == True:
                        count += 1
                if (100 * count/transactions) >= self.support:
                    c.sort()
                    Lk.append(c)
            Lk_1 = []
            print("-----------------------FREQUENT %d-ITEMSET------------------------" % k)
            print(Lk)
            print("------------------------------------------------------------------")
            for l in Lk:
                Lk_1.append(l)
            k += 1
            if Lk != []:
                L.append(Lk)        
        return L
         
            
    """generate_association_rules function to mine and print all the association rules with given support and confidence value"""    
    def generate_association_rules(self):
        #------------------------------------------------------------------
        """Compute candidate 1-itemset"""
        C1 = {}
        
        """total number of transactions contained in the file"""
        transactions = len(self.data)

        for transaction in self.data:
            for item in transaction:
                if item not in C1.keys():
                    C1[item]=1
                else:
                    count = C1[item]
                    C1[item] = count+1
        
        print('Total Transactions:',transactions)
        print('Unique Items:', len(C1))
        #self.C1=C1
        
        """Compute frequent 1-itemset"""
        L1 = []
        for key in C1:
            if (100 * C1[key]/transactions) >= self.support:
                list = []
                list.append(key)
                L1.append(list)

        self.L1=L1
        print("----------------------FREQUENT 1-ITEMSET-------------------------")
        print(L1)
        print("-----------------------------------------------------------------")
        #------------------------------------------------------------------
        
        s = []
        r = []
        length = 0
        count = 1
        inc1 = 0
        inc2 = 0
        num = 1
        m = []
        L= self.frequent_itemsets()
        print("---------------------ASSOCIATION RULES------------------")
        print("RULES \t SUPPORT \t CONFIDENCE")
        print("--------------------------------------------------------")
        for list in L:
            for l in list:
                length = len(l)
                count = 1
                while count < length: 
                    s = []
                    r = self.findsubsets(l,count)
                    count += 1
                    for item in r:
                        inc1 = 0
                        inc2 = 0
                        s = []
                        m = []
                        for i in item:
                            s.append(i)
                        for T in self.data:
                            if set(s).issubset(set(T)) == True:
                                inc1 += 1
                            if set(l).issubset(set(T)) == True:
                                inc2 += 1
                        if 100*inc2/inc1 >= self.confidence:
                            for index in l:
                                if index not in s:
                                    m.append(index)
                            print("Rule#  %d : %s ==> %s %d %d" %(num, s, m, 100*inc2/len(self.data), 100*inc2/inc1))
                            num += 1  
