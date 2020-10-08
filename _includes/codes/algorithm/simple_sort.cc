#include<iostream>
using namespace std;

void  tem_swap(int array[], int i, int j)
{
	int tem=array[i];
	array[i]=array[j];
	array[j]=tem;
}

void select_sort(int array[], int n)
{
	for(int i=0;i<n-1;i++)
	{
		int min_index=i;
		for (int j=i;j<n;j++)
		{
			if (array[min_index]>array[j])
				min_index=j;
		}
		if (min_index!=i)
			tem_swap(array,i,min_index);
	}
}

int main()
{
	int a[5]={1,5,4,3,8};
	select_sort(a,5);
	for(int i=0;i<5;i++)
	{
		cout<<a[i]<<"  ";
	}
	cout<<endl;
	return 0;
}

