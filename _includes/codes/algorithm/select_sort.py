def select_sort(num_list):
    n=len(num_list)
    for i in range(n):
        min_index=i
        for j in range(i+1, n):
            if num_list[j]<num_list[min_index]:
                min_index=j
        if min_index!=i:
            num_list[min_index],num_list[i]=num_list[i],num_list[min_index]
def main():
    num_list=[1,3,5,8,6,7,5,1,2]
    print('original list: ', num_list)
    select_sort(num_list)
    print('sorted list: ', num_list)

if __name__=='__main__':
    main()

            


