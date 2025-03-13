<h1>Binary Calculator</h1>

<h2>Description</h2>
The **Binary Calculator** is a simple Java program that performs basic arithmetic operations (addition, subtraction, multiplication, and division) on binary numbers. The program allows users to input two binary numbers, selects the operation they want to perform, and then outputs the result as a binary number.

This project demonstrates fundamental Java programming concepts, such as user input handling, binary number manipulation, and the implementation of basic mathematical operations.

<br />

<h2>Languages and Tools Used</h2>

- <b>Java</b>
- <b>Scanner Class</b> (for user input)
- <b>Integer.parseInt()</b> (for converting binary strings to integers)
- <b>Integer.toBinaryString()</b> (for converting integers back to binary strings)

<h2>Program Walk-through</h2>

1. **Prompt User for Binary Numbers**:
   - The program asks the user to enter two binary numbers.
   - The input is captured using a `Scanner` object.

2. **Prompt User for Operation**:
   - The program presents the user with a choice of operations: addition, subtraction, multiplication, or division.

3. **Convert Binary to Decimal**:
   - The binary numbers are converted to decimal integers using `Integer.parseInt(binaryString, 2)`.

4. **Perform the Selected Operation**:
   - The appropriate mathematical operation (addition, subtraction, multiplication, or division) is performed on the decimal equivalents.

5. **Convert Decimal Result Back to Binary**:
   - The result of the operation is converted back to binary using `Integer.toBinaryString()`.

6. **Display the Result**:
   - The result of the operation is printed in binary format for the user.

<h2>Example Code</h2>

```java
import java.util.Scanner;

class BinaryCalculator {
    public static void main(String[] args) {
        Scanner keyboard = new Scanner(System.in);

        System.out.print("Enter the first binary number: ");
        String binary1 = keyboard.nextLine();
        
        System.out.print("Enter the second binary number: ");
        String binary2 = keyboard.nextLine();
        
        System.out.println("Choose an operation (1: Add, 2: Subtract, 3: Multiply, 4: Divide): ");
        int operation = keyboard.nextInt();

        int num1 = Integer.parseInt(binary1, 2);
        int num2 = Integer.parseInt(binary2, 2);
        int result = 0;

        switch (operation) {
            case 1: // Addition
                result = num1 + num2;
                break;
            case 2: // Subtraction
                result = num1 - num2;
                break;
            case 3: // Multiplication
                result = num1 * num2;
                break;
            case 4: // Division
                if (num2 != 0) {
                    result = num1 / num2;
                } else {
                    System.out.println("Error: Division by zero is not allowed.");
                    return;
                }
                break;
            default:
                System.out.println("Invalid operation");
                return;
        }

        String resultBinary = Integer.toBinaryString(result);
        System.out.println("The result in binary is: " + resultBinary);
    }
}
