class FiniteStateAutomaton:
    def _init_(self):
        self.state = 0  

    def transition(self, char):
        """Transitions the automaton based on input character"""
        if self.state == 0:
            if char == 'a':
                self.state = 1
            else:
                self.state = 0 
        elif self.state == 1:
            if char == 'b':
                self.state = 2  
            elif char == 'a':
                self.state = 1  
            else:
                self.state = 0  
        elif self.state == 2:
            if char == 'a':  
                self.state = 1
            else:
                self.state = 0  

    def is_accepted(self, input_string):
        self.state = 0  
        for char in input_string:
            self.transition(char)

        return self.state == 2 

fsa = FiniteStateAutomaton()
test_strings = ["ab", "aab", "baba", "abab", "abc", "xyz", "aaabb"]

for s in test_strings:
    result = "Accepted" if fsa.is_accepted(s) else "Rejected"
    print(f"Input: '{s}' -> {result}")
