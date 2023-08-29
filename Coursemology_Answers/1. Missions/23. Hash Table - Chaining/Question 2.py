class SongRecord:
    def __init__(self, SongID, SongTitle):
        self.SongID = SongID
        self.SongTitle = SongTitle
        self.next = None
        
class HashTable:
    def __init__(self, size):
        #initialises Size attribute with value size
        #Size : integer
        
        #initialises Array attribute to store size number of Python lists
        #Array : ARRAY[0:size-1] OF LIST
        
        #resolve aliasing
        self.Size = size
        self.Array = [None]*size
        
    def Hash(self, SongID):
        #sums the ASCII value of each character in SongID
        #returns the remainder when the sum is divided by the size of Array
        sum = 0
        for i in SongID:
            sum += ord(i)
        return sum%self.Size
    
    def Display(self):
        #displays the content of Array neatly
        print("INDEX\tSONG ID\t\tSONG TITLE")
        for i in range(self.Size):
            print(str(i)+"\t"+str(self.Array[i]))
        print()
        
    def Add(self, SongID, SongTitle):
        #instantiates a SongRecord object with SongID and SongTitle to Array
        #inserts the new object into Array
        #uses chaining to handle collisions
        index = self.Hash(SongID)
        if self.Array[index] == None:
            self.Array[index] = SongRecord(SongID,SongTitle)
        else:
            temp = self.Array[index]
            while temp.next != None:
                temp = temp.next
            temp.next = SongRecord(SongID,SongTitle)

    def Remove(self, SongID):
        #deletes the SongRecord with SongID from Array
        index = self.Hash(SongID)
        if self.Array[index] == None:
            return
        else:
            temp = self.Array[index]
            if temp.SongID == SongID:
                self.Array[index] = temp.next
            else:
                while temp.next != None:
                    if temp.next.SongID == SongID:
                        temp.next = temp.next.next
                        return
                    temp = temp.next
        
    def Search(self, SongID):
        #uses hash table search to find the SongRecord with SongID in Array
        #returns the associated SongTitle if found or "NONE" if not found
        index = self.Hash(SongID)
        if self.Array[index] == None:
            return "NONE"
        else:
            temp = self.Array[index]
            while temp != None:
                if temp.SongID == SongID:
                    return temp.SongTitle
                temp = temp.next
            return "NONE"
        
#DO NOT EDIT OR DELETE THE FOLLOWING CODE
#========================================
hta1 = HashTable(13) #hash table of size 13
hta1.Add("EL0078","Hotel California")
hta1.Add("CL0123","K-King")
hta1.Add("CL0010","Red Bean")
hta1.Add("EL7810","Lady in Red")
hta1.Add("CL2310","Ninja")
hta1.Add("EL1610","Tears in Heaven")
hta1.Add("CL3210","Beach")
hta1.Add("EL0611","Unchained Melody")

hta1.Remove("CL2310")
hta1.Remove("EL0078")
hta1.Add("EL0870","Witulah")

a = hta1.Search("CL3210")
b = hta1.Search("CL2310")
c = hta1.Search("EL1610")
d = hta1.Search("EL0611")
e = hta1.Search("EL0870")