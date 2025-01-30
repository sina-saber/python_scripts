from copy import copy

#___________1. Used for creating a string representing a Multiset___________#


def repeat_element_at_list(list_element,element_count):
    return copy([list_element])*element_count

#______________________2. Simple Multiset Permutation_______________________#


def multiset_permutation(permutations,sample_list,start,end):
    final_permutations=copy(permutations)
    for i in range(start,end,-1):
        #to_append will be added to final_permutations
        to_append=[]
        for j in final_permutations:
            new_word=copy(j)
            for k in range(i,len(sample_list)-1,1):
                if new_word[k]==new_word[k+1]:
                    break
                try:
                    new_word[k],new_word[k+1]=new_word[k+1],new_word[k]
                except:
                    pass
                to_append.append(copy(new_word))
        final_permutations.extend(to_append)
    return final_permutations

#___________________________3. Setting the inputs___________________________#

objects=["a1","a2","a3"]
object_counts=[1,2,1]

#_______________4. Constructing a base list for permutations________________#

c=list(map(repeat_element_at_list,objects,object_counts))
word=[]
for i in c:
    word.extend(i)

#______________________5. Creating the list of answers______________________#

if objects and object_counts:
    produced_perms=multiset_permutation([word],word,len(word)-1,-1)

print(produced_perms)