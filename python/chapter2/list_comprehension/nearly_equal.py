"""Write a function nearly_equal to test whether two strings are nearly equal. Two strings a and b are nearly equal
 when a can be generated by a single mutation on b."""

import mutate

def nearly_equal(word,word2):
	if word2 in mutate.mutate(word):
		return True


print nearly_equal("perl","pearl")