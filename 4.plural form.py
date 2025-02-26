class MorphologicalFSM:
    def __init__(self):
        self.state = "INITIAL" 

    def pluralize(self, noun):
        """Apply finite-state rules to generate the plural form of an English noun."""
        if noun.endswith(("s", "sh", "ch", "x", "z")):
            return noun + "es"  
        elif noun.endswith("y") and noun[-2] not in "aeiou":
            return noun[:-1] + "ies" 
        elif noun.endswith("f"):
            return noun[:-1] + "ves"  
        elif noun.endswith("fe"):
            return noun[:-2] + "ves"  
        else:
            return noun + "s"  

fsm = MorphologicalFSM()
test_nouns = ["cat", "dog", "box", "bus", "baby", "city", "leaf", "knife", "fox", "church"]

for noun in test_nouns:
    print(f"Singular: {noun} -> Plural: {fsm.pluralize(noun)}")
