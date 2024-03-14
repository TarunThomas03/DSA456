## LAB 5 - Reflection

### For the big-O analysis:

is_empty(self): O(1)
prepend(self, data): O(1)    
append(self, data): O(n) - When appending, we traverse the list to find the last node.    
insert_after(self, target, data): O(1) - Assuming we have a reference to the target node.    
delete(self, target): O(n) - We may need to traverse the list to find the target node to delete.    
search(self, data): O(n) - We may need to traverse the list to find the node with the given data.    
size(self): O(n) - We need to traverse the entire list to count the number of nodes.     
to_list(self): O(n) - We need to traverse the entire list to gather all the data.     
print(self): O(n) - We need to traverse the entire list to print all the elements.    


