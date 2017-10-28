#### Pair Problem

*This is a classical question and a version of this problem was given to a Metis grad in an interview for a data scientist position on April 16, 2015.*

#### Take 1 ####
In programming languages, and especially in Lisps, there can be a lot of parentheses. The parentheses have to be "balanced" to be valid. For example, `()(())` is balanced, but `()())` is not balanced. Also, `)((())` is not balanced.

Write a function that takes a string and returns `True` if the string's parentheses are balanced, `False` if they are not.

What's the time and space complexity of your code? Can you improve it?

We can do this with **O(N)** time.  
We can do this with **O(1)** additional space.  

Here are examples to test your function with:

 * `(()()()())` should return `True`
 * `(((())))` should return `True`
 * `(()((())()))` should return `True`
 * `((((((())` should return `False`
 * `()))` should return `False`
 * `(()()))(()` should return `False`

#### Take 2 ####
In a real programming language, you will have different types of brackets, eg. `{{[]()(()){}[]}}`.   
Does your existing code handle the multiple brackets well? If not, extend your code to work with the multiple brackets.   

Create some test cases to check your code.  



