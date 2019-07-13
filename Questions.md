##### 1. How much time does it take to retrieve an element if stored in HashMap, Binary tree, and a Linked list? how it change if you have millions of records?
In HashMap it takes O(1) time, in the binary tree it takes O(logN) where N is a number of nodes in the tree and in linked list it takes O(n) time where n is a number of element in the list. Millions of records don't affect the performance if the data structure is working as expected e.g. HashMap has no or relatively less number of collision or binary tree is balanced. If that's not the case then their performance degrades as a number of records grows.
##### 2. What is the difference between Overriding and Overloading?
Overriding is resolved at runtime while overloading is compile time. Also, rules of overriding and overloading are different, for example in Java, method signature of the overloaded method must be different than original method, but in the case of overriding it must be exactly same as an overriding method.
##### 3. What is the difference between forking a process and spawning a thread? 
When you fork a process, the new process will run the same code as parent process but in different memory space, but when you spawn a new thread in existing process, it just creates another independent path of execution but share same memory space.
##### 4. What is a critical section?
A critical section is the part of a code, which is very important and in multi-threading must be exclusively modified by any thread. Semaphore or mutex is used to protect critical section. In Java, you can use synchronized keyword or ReentrantLock to protect a critical section.
##### 5. What is the difference between a value type and a reference type?
A value type is a more optimized type and always immutable e.g. primitive int, long, double and float in Java while a reference type points to an object, which can be mutable or Immutable. You can also say that value type points to a value while reference type points to an object.
##### 6. What is heap and stack in a process?
They are two separate areas of memory in the same process. Talking about Java, the stack is used to store primitive values and reference type to object but actual object is always created in heap. One critical difference between heap and stack is that heap memory is shared by all threads but each thread has their own stack.
##### 7. What is revision/version control?
Version control is software which is used to store code and manage versions of codebase e.g. SVN, CVS, Git, Perforce, and ClearCase. They are very effective while comparing code, reviewing code and creating a build from previous stable version. All professional development use some sort of revision or version control tool, without them, you cannot manage code effectively, especially if 20 developers are working on same code base at the same time. Version control tool plays very important role to keep code base consistent and resolving code conflicts.
##### 8. What is a strongly typed programming language?
In a strongly typed language compiler ensure type correctness, for example, you can not store the number in String or vice-versa. Java is a strongly typed language, that's why you have different data types e.g. int, float, String, char, boolean etc. You can only store compatible values in respective types. On the other hand, weakly typed language don't enforce type checking at compile time and they tree values based upon context. Python and Perl are two popular example of weakly typed programming language, where you can store a numeric string in number type.
##### 9. Can you describe the difference between valid and well-formed XML?
A well-formed XML is the one which has root element and all tags are closed properly, attributes are defined properly, their value is also quoted properly. On another hand, a valid XML is the one which can be validated against an XSD file or schema. So it's possible for an XML to be well-formed but not valid because they contain tags which may not be allowed by their schema.
##### 10. What is the difference between DOM and SAX parser?
DOM parser is an in-memory parser so it loads whole XML file in memory and create a DOM tree to parse. SAX parser is an event based parser, so it parses XML document based on the event received e.g. opening tag, closing tag, the start of attribute or end of the attribute. Because of their working methodology, DOM parser is not suitable for large XML file as they will take a lot of space in memory and your process may run out of memory, SAX is the one which should be used to parse large files. For small files, DOM is usually much faster than SAX.
##### 11. What is the relationship between threads and processes?
A process can have multiple threads but a thread always belongs to a single process. Two processes cannot share memory space until they are purposefully doing inter-process communication via shared memory but two threads from the same process always share the same memory.
##### 12. What is Immutable class mean?
A class is said to be Immutable if its state cannot be changed once created, for example, String in Java is immutable. Once you create a String say "Java", you cannot change its content. Any modification in this string e.g. converting into upper case,  c oncatenating with another String will result in the new object. An immutable object is very useful for concurrent programming because they can be shared between multiple threads without worrying about synchronization. In fact, the whole model of functional programming is built on top of Immutable objects.
##### 13. Why would you ever want to create a mock object?
A mock object is very useful to test an individual unit in your Software, in fact, stub and mocks a are a powerful tool for creating automated unit tests. Suppose you write a program to display currency conversion rates but you don't have a URL to connect to, now if you want to test your code, you can use mock objects. In Java world, there are a lot of frameworks which can create powerful mock objects for you e.g. Mockito and PowerMock.
##### 14. What is SQL injection?
SQL injection is a security vulnerability which allows an intruder to steal data from the system. Any system which takes input from the user and creates SQL query without validating or sanitizing that input is vulnerable to SQL injection. In such system, an intruder can inject SQL code instead of data to retrieve more than expected data. There are many instances on which sensitive information e.g. user id, password, and personal details are stolen by exploiting this vulnerability. In Java, you can avoid SQL injection by using Prepared statement.
##### 15. What is the difference between an inner join and a left join in SQL?
In SQL, there are mainly two types of joins, inner join, and outer join. Again outer joins can be two types right and left outer join. The main difference between inner join and left join is that in the case of former only matching records from both tables are selected while in the case of left join, all records from left table are selected in addition to matching records from both tables. Always watch out for queries which have "all" in it, they usually require left join e.g. to write SQL query to find all departments and a number of employees on it. If you use inner join to solve this query, you will miss empty departments where no one works.
##### 16. What does the V in MVC stand for, and what does it signify?
V stands for View in MVC pattern. The view is what user sees e.g. web pages. This is a very important design pattern of web development which is based upon segregation of concern so that each area can be modified without impacting other areas. In Java world, there are lots of open source framework which provides an implementation of MVC pattern e.g. Struts 2 and Spring MVC. By the way, M stands the for model and C stands the for controller. Modes are actual business objects e.g. User, Employee, Order; while the controller is used for the routing request to correct processor.
##### 17. What is the difference between a class and an object?
A class is a blueprint on which objects are created. A class has code and behavior but an object has both the state and behavior. You cannot create an object without creating a class to represent its structure. The class is also used to map an object in memory, in Java, JVM does that for you.
##### 18. What is loose-coupling?
Loose coupling is a desirable quality of software, which allows one part of the software to modify without affecting another part of the software. For example, in a loosely coupled software, a change in UI layout should not affect the back-end class structure.
##### 19. What is the difference between composition, aggregation, and association?
Association means two objects are related to each other but can exist without each other, Composition is a form of association where one object is composed of multiple objects, but they only exists together e.g. human body is the composition of organs, individual organs cannot live they only useful in the body. Aggregation is a collection of object e.g. city is an aggregation of citizens.
##### 20. What is the difference between an interface and an abstract class?
This is the most classical question of all programming interviews. An interface is the purest form of abstraction with nothing concrete in place while an abstract class is a combination of some abstraction and concrete things. The difference may vary depending upon language e.g. in Java you can extend multiple interface but you can only extend on the abstract class. For a more comprehensive discussion see the detailed answer.
##### 21. What is unit testing?
Unit testing is a way to test individual unit for their functionality instead of testing whole application. There are a lot of tools to do the unit testing in different programming language e.g. in Java, you can use JUnit or TestNG to write unit tests. It is often run automatically during the build process or in a continuous environment like Jenkins.
##### 22. Can you describe three different kinds of testing that might be performed on an application before it goes live?
unit testing, integration testing and smoke testing. Unit testing is used to test individual units to verify whether they are working as expected, integration testing is done to verify whether individually tested module can work together or not and smoke testing is a way to test whether most common functionality of software is working properly or not e.g. in a flight booking website, you should be able to book, cancel or change flights.
##### 23. What is the difference between iteration and recursion?
Iteration uses a loop to perform the same step again and again while recursion calls the function itself to do the repetitive task. Many times recursion result in a clear and concise solution to complex problem e.g. tower of Hanoi, reversing a linked list or reversing a String itself. One drawback of recursion is depth  since recursion stores intermediate result in the stack you can only go up to a certain depth, after that your program will die with StackOverFlowError, this is why iteration is preferred over recursion in production code.
##### 24. What is difference between & and && operator?
& is a bitwise operator while && is a logical operator. One difference between & and && is that bitwise operator (&) can be applied to both integer and boolean but logical operator (&&) can only be applied to boolean variables. When you do a & b then AND operator is applied to each bit of both integer number, while in the case of a && b, the second argument may or may not be evaluated, that's why it is also known as short circuit operator, at least in Java. I like this question and often asked it to junior or developer and college graduates.
##### 25. What is the result of 1 XOR 1?
The answer is zero because XOR returns 1 if two operands are distinct and zero if two operands are same, for example, 0 XOR 0 is also zero, but 0 XOR 1 or 1 XOR 0 is always 1.
##### 26. How do you get the last digit of an integer?
By using modulus operator, number % 10 returns the last digit of the number, for example, 2345%10 will return 5 and 567%10 will return 7.  Similarly, division operator can be used to get rid of the last digit of  a number e.g. 2345/10 will give 234 and 567/10 will return 56. This is an important technique to know and useful to solve problems like number palindrome or reversing numbers.
##### 27. What is test-driven development?
Test driven is one of the popular development methodologies in which tests are written before writing any function code. In fact, test drives the structure of your program. Purists never wrote a single line of application code without writing a test for that. It greatly improve code quality and often attributed as a quality of rockstar developers.
##### 28. What is the Liskov substitution principle?
Liskov substitution principle is one of the five principle introduced by Uncle Bob as SOLID design principles. It's the 'L' in SOLID. Liskov substitution principle asserts that every subtype should be able to work as the proxy for parent type. For example, if a method except object of Parent class then it should work as expected if you pass an object of the Child class. Any class which cannot stand in place of its parent violate LSP or Liskov substitution principle. This is actually a tough question to answer and if you do that you end up with creating a good impression on interviewers mind.
##### 29. What is the Open closed design principle?
Open closed is another principle from SOLID, which asserts that a system should be open for extension but closes for modification. Which means if a new functionality is required in a stable system then your tried and tested code should not be touched and new functionality should be provided by adding new classes only. 
##### 30. What is the difference between a binary tree and a binary search tree?
Binary search tree is an ordered binary tree, where the value of all nodes in the left tree are less than or equal to node and values of all nodes in right subtree is greater than or equal to the node (e.g. root). It's an important data structure and can be used to represent a sorted structure.
##### 31. Can you give a practical example of a recursive algorithm?
There are lots of places where recursive algorithm fits e.g. algorithm related to binary and linked list. A couple of examples of a recursive algorithm is reversing String and calculating Fibonacci series. Other examples include reversing linked list, tree traversal, and quick sort algorithm. 
##### 32. What is time complexity of an algorithm?
Time complexity specifies the ratio of time to the input. It shows how much time an algorithm will take to complete for a given number of input. It's approximated valued but enough to give you an indication that how your algorithm will perform if the number of input is increased from 10 to 10 million?
##### 33. What are some important differences between a linked list and an array?
linked list and array are two of the most important data structure in the programming world. The most significant difference between them is that array stores its element at the contiguous location while linked list stores its data anywhere in memory. This gives linked list enormous flexibility to expand itself because memory is always scattered. It's always possible that you wouldn't be able to create an array to store 1M integers but can do by using linked list because space is available but not as contiguous chunk. All other differences are the result of this fact. For example, you can search an element in array with O(1) time if you know the index but searching will take O(n) time in linked list. For more differences see the detailed answer.
##### 34. What is a couple of ways to resolve collision in the hash table? 
linear probing, double hashing, and chaining. In linear probing, if the bucket is already occupied then function check next bucket linearly until it finds an empty one, while in chaining, multiple elements are stored in same bucket location.
##### 35. What is a regular expression?
A regular expression is a way to perform pattern matching on text data. It's very powerful tool to find something e.g. some character in a long string e.g. finding if a book contains some word or not. Almost all major programming language supports regular expression but Perl has been renowned for its enormous capability. Java also supports Perl-like regular expression using java.util.regex package. You can use the regular expression to check if an email is valid or not, if a phone number is valid, or if a zip code is valid, or even an SSN number is valid or not. One of the simplest examples of the regular expression is to check if a String is a number or not.
##### 36. What is a stateless system?
A stateless system is a system which doesn't maintain any internal state. Such system will produce the same output for same input at any point of time. It's always easier to code and optimize a stateless system, so you should always strive for one if possible.
##### 37. Write SQL query to find second highest salary in employee table?
This is one of the classic questions from SQL interviews, the event it's quite old it is still interesting and has lots of follow-ups you can use to check the depth of candidate's knowledge. You can find second highest salary by using the correlated and non-correlated subquery. You can also use keyword's like TOP or LIMIT if you are using SQL Server or MySQL, given Interviewer allows you. The simplest way to find 2nd highest salary is following:
```
SELECT MAX(Salary) FROM Employee WHERE Salary NOT IN (SELECT MAX(Salary) FROM Employee)
```
This query first finds maximum salary and then exclude that from the list and again finds maximum salary. Obviously second time, it would be second highest salary.
##### 38. Can you describe the difference between correlated and non-correlated subquery?
In correlated sub-query, inner query depends upon the outer query and executes for each row in the outer query. While non-correlated subquery doesn't depend upon the outer query and can be executed independently. Due to this reason former is slow and later is fast. BTW, correlated subquery has some nice application, one of them is finding Nth highest salary in Employee table, as seen on previous SQL question as well.
##### 39. How do you find if a number is a power of two, without using arithmetic operator?
Assume it's a question of using the bitwise operator as soon as you hear restriction about not allowed to use arithmetic operator. If that restriction is not in place then you can easily check if a number is a power of two by using modulus and division operator. By the using bitwise operator, there is a nice trick to do this.  You can use following code to check if a number if power of two or not
```
public static boolean powerOfTwo(int x) {
        return (x & (x - 1)) == 0;
}
```
x & (x-1) is a nice trick to convert right most bit to zero if it's on, I learned from hackers delight book.


##### 40. How do you find a  running Java process on UNIX?
You can use the combination of 'ps' and 'grep' command to find any process running on UNIX machine. Suppose your Java process has a name or any text which you can use to match against just use following command.
```
ps -ef | grep "myJavaApp"
```
ps -e will list every process i.e. process from all user not just you and  ps -f will give you full details including PID, which will be required if you want to investigate more or would like to kill this process using kill command.


##### 41. How do you find large files in UNIX  e.g. more than 1GB?
You can easily find big files by using find command because it provides an option to search files based upon their size. Use this if your file system is full and your Java process is crashing with no more space. This command will list all files which are more than 1GB. You can tweak the size easily e.g. to find all files with more than 100 MB just use +100M.
```
find . - type f -size +1G -print
```

##### 42. What is the shell script?
A shell script is set of shell commands with some programming constructs e.g. if and for loop, which allow you to automate some repetitive task. For example, you can write a shell script to the daily cleanup of logs files,  for backing up data for historical use and for other housekeeping jobs, releases, and monitoring.
