using System;
namespace ArrayApplication
{
	class MyArray
	{
		static void Main(string[] args)
		{
			int [] n = new int[10];
			for (int i=0;i<10;i++)
			{
				n[i]=i+100;
			}
//			for (j=0;j<10;j++)
//			{
//				Console.WriteLine("Element[{0}]={1}:",j, n[j]);
//			}
			foreach (int j in n)
			{
				int i = j-100;
				Console.WriteLine("Element[{0}]={1}:",i, j);
			}

			Console.ReadKey();
		}
	}
}

