using System;
namespace CalculatorApplication
{
	class numMunipulator
	{
		public int factorial(int num)
		{
			if (num==1)
				return 1;
			else 
				return factorial(num-1)*num;
		}
	}
	class test
	{
		static void Main(string[] args)
		{
			numMunipulator n=new numMunipulator();
			//int result7=n.factorial(7);
			int result4=n.factorial(4);
			//Console.WriteLine(result7);
			Console.WriteLine(result4);
			//Console.WriteLine("Factorial of 10:", n.factorial(10));
			Console.ReadLine();
		}
	}
}


