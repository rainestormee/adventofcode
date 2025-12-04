Completely first experiences using Rust.

Seeing how I cope with AOC.


# Day 1 Notes:

Really? not int? i32? sure okay 

SO string is funky. so is slicing them.

.split() just eats the thing i use to split it with. okay fine. but for regex as well? aw there goes my plan to match [LR].

Arrays and vectors are very different. 

Stop making me fix my types to your weird ones.

|x| is fun syntax. why not.

MODULO IS NOT WHAT I EXPECTED. thanks stackoverflow for rem_euclid.

was originally a `Vec<Vec<str>>` thanks for tuples


# Day 2 Notes:

looks like a substring search feels like a substring search

OOPS I SOLVED PART 2 BEFORE PART 1 BECAUSE I MISREAD THE CHALLENGE INFO. OH WELL

Didn't realise part 1 wanted a ONCE copy not an N copy. 

Okay so the int naming convention actually makes a lot of sense. 

I need to figure out if im being silly with casting the int to a bigger type i.e. u32 => u64. need to figure out if the .sum() can take a type and then cast itself 


i.e. `Vec<u32>.sum::<u64>()` would be nice.


# Day 3 notes:

smells like a time complexity problem

i want to do a search for biggest number, then only search the rest of the space to the right. but need to do the search less the last digit ofc so we're 2 digit.

I thought part 2 would be to do with indexes of the positions found, but instead is just do it for size (n) really. well i could probably cheat and do it for 12 but it's probably bad.

the solution i wanted to work ending up not working as well as i thought it would. 

iterable ranges don't go down lol, that's not a neat trick

also don't do a-b > 0 because that's always true. i guess it makes sense that unsigned ints are always positive but maybe i should have done something better. probably a > b is a cheaper calulation anyway.

