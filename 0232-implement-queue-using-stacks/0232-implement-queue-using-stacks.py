class MyQueue:                                         
    def __init__(self):                                
        self.ins = []                                  
        self.outs = []                                 
                                                       
    def push(self, x: int) -> None:                    
        self.ins.append(x)                             
                                                       
    def pop(self) -> int:                              
        if self.empty():                               
            return None                                
        else:                                          
            self.peek()                                
            poped = self.outs.pop()                    
            return poped                               
                                                       
    def peek(self) -> int:                             
        if not self.outs:                              
            while self.ins:                            
                self.outs.append(self.ins.pop())       
        return self.outs[-1]                         
                                                       
    def empty(self) -> bool:                           
        if not self.ins and not self.outs:             
            return True                                
        else:                                          
            return False                               
                                                       


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
          