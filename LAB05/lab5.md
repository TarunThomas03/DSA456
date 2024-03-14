## LAB 5 - Reflection

### For the big-O analysis:

__init__(self): o(1)
is_empty(self): O(1)
prepend(self, data): O(1)    
append(self, data): O(n) - When appending, we traverse the list to find the last node.    
insert_after(self, target, data): O(1) - Assuming we have a reference to the target node.    
delete(self, target): O(n) - We may need to traverse the list to find the target node to delete.    
search(self, data): O(n) - We may need to traverse the list to find the node with the given data.    
size(self): O(n) - We need to traverse the entire list to count the number of nodes.     
to_list(self): O(n) - We need to traverse the entire list to gather all the data.     
print(self): O(n) - We need to traverse the entire list to print all the elements.    




#### Initialization (__init__):    
     
Time Complexity: O(1)     
Explanation: Initializing an empty linked list involves setting up the initial state, which typically entails only setting the head pointer to None. This operation has a constant time complexity since it does not depend on the size of the list.     
    
is_empty(self) -> bool:    
    
Time Complexity: O(1)      
Explanation: Checking whether the linked list is empty requires accessing the head pointer, which takes constant time regardless of the size of the list.    
     
prepend(self, data: Any):    
     
Time Complexity: O(1)       
Explanation: Prepending a new node involves updating the head pointer to point to the new node. Since this operation does not depend on the size of the list, its time complexity is constant.       
     
append(self, data: Any):      
      
Time Complexity: O(n)      
Explanation: Appending a new node at the end of the list requires traversing the entire list to reach the last node. Therefore, its time complexity is linearly proportional to the size of the list.      
insert_after(self, target: Node, data: Any):      
      
Time Complexity: O(1)      
Explanation: Inserting a node after a given target node involves updating references and does not require traversing the list. Thus, its time complexity is constant.
       
delete(self, target: Node) -> bool:          
      
Time Complexity: O(n)       
Explanation: Deleting a node from the list may require traversing the list to find the node to be deleted. Therefore, the time complexity of deletion is linear in the worst case, where n is the size of the list.      
    
search(self, data: Any) -> Optional[Node]:     
       
Time Complexity: O(n)      
Explanation: Searching for a node with a specific value entails traversing the list until the desired node is found or reaching the end of the list. Thus, the time complexity of searching is linear in the size of the list.      
    
size(self) -> int:      
       
Time Complexity: O(n)     
Explanation: Calculating the size of the list requires traversing the entire list to count the number of nodes. Therefore, the time complexity is linearly proportional to the size of the list.     
       
to_list(self) -> List[Any]:      
        
Time Complexity: O(n)        
Explanation: Converting the linked list to a Python list involves traversing the entire list to gather all the data. Thus, the time complexity is linear in the size of the list.       
      
print(self):      
      
Time Complexity: O(n)       
Explanation: Printing all elements in the linked list requires traversing the entire list to access each node's data. Therefore, the time complexity is linear in the size of the list.       