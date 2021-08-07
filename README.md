# Strong-Password-Generator
Hi , This is a Simple Strong Password Generator , I am also a beginner to python programming.
Explanation :
Nowadays it is very easy to hack your passwords , so it is safe that you always have a 
8 digit strong password or a passphrase , generally a stong password should contain
Numbers, Uppercase letters , Lowercase letters, Symbols. 
Code Explanation:
1) Import two default modules random and array
2) Initialize the lenght of the password as maxlen 
3) Initialize didits i.e numbers, lowercase alphabets , uppercase alphabets, symbols
4) A password should be  a combination of all these so initoialize combinedlist and add all these i.e
 digits,numbers,lowercase and uppercase.
5) Next we need to generate a password randomly , so lets use the function random to generate rand_digit,
rand_upper, rand_lower,rand_symbol. 
6)After shuffling these randomly we will add them up and keep in temp_pass.
7) now that we are sure we have at least one character from each ,set of characters we fill the rest of
the password length by selecting randomly from the combined list of character above.
8)convert temporary password into array and shuffle to prevent it from having a consistent pattern
 where the beginning of the password is predictable.
9) Then print the password 

 
