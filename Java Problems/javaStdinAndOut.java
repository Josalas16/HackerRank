// Problem
// Java Stdin and Stdout 1

// One popular way to read input from stdin is by using the Scanner class and Specifying the input Stream as System.in.
// For Example
// Scanner scanner = new Scanner(Systen.in);
// String myString = scanner.next();
// int myInt = scanner.nextInt();
// scanner.close();

// System.out.println("mystring is: " + myString);
// System.out.println("myInt is: " + myInt);

// The code above creates a Scanner object named scanner and uses it tot read a
// String and an int. it then closes the Scannerobject because there is no more input to
// read, and pritnes to stdout using System.out.println(String). So, if our input is:
// Hi 5

// Our code will print:
// myString is: Hi
// myInt is: 5
// Alteratively, You can used the BufferedReader class

// Task
// In this challenge, you must read 3 integers from stdin and then print them to stdout.
// Each integer must be printed on a new line. To make the problem a little easier, a
// portion of the code is provided for you in the editor below.

// Input Format:
// There are 3 lines of input , and each line contains a single integer.

// Sample Input
// 42
// 100
// 125

// Sample Output
// 42
// 100
// 125

import java.util.*;
public class javaStdinAndOut {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int a = scan.nextInt();
       

        System.out.println(a);
        
    }
}