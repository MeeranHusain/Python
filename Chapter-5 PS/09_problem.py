# Can you change the values inside a list which is contained in set S? 

s = {8, 7, 12, "Harry", [1,2]}

# No, because a list cannot be an element of a set. Lists are mutable and unhashable, so Python raises TypeError: unhashable type: 'list'.