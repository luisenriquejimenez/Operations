using System;

class MathOperations
{
    public static double Add(double a, double b) => a + b;
    public static double Subtract(double a, double b) => a - b;
    public static double Multiply(double a, double b) => a * b;
    public static double Divide(double a, double b)
    {
        if (b == 0)
        {
            Console.WriteLine("Error: División por cero no permitida.");
            return double.NaN;
        }
        return a / b;
    }
    
    static void Main()
    {
        Console.WriteLine("Ingrese el primer número:");
        double num1 = Convert.ToDouble(Console.ReadLine());
        
        Console.WriteLine("Ingrese el segundo número:");
        double num2 = Convert.ToDouble(Console.ReadLine());
        
        Console.WriteLine("Seleccione la operación (+, -, *, /):");
        char operation = Console.ReadLine()[0];
        
        double result = 0;
        switch (operation)
        {
            case '+':
                result = Add(num1, num2);
                break;
            case '-':
                result = Subtract(num1, num2);
                break;
            case '*':
                result = Multiply(num1, num2);
                break;
            case '/':
                result = Divide(num1, num2);
                break;
            default:
                Console.WriteLine("Operación no válida.");
                return;
        }
        
        Console.WriteLine($"Resultado: {result}");
    }
}
