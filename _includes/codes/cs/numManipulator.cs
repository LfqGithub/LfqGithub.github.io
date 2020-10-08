using System;
namespace CalculatorApplication
{
	class NumberManipulator
	{
		public int FindMax(int num1, int num2)
		{
			if (num1>=num2)
				return num1;
			else
				return num2;
		}
	}
	class test
	{
		static void Main(string[] args)
		{
			int a=100;
			int b=200;
			int ret;
			NumberManipulator n=new NumberManipulator();
			ret=n.FindMax(a,b);
			Console.WriteLine(ret);
			Console.ReadLine();
		}
	}
}
		

