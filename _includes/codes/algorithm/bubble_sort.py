def bubble_sort(num_list):
    n=len(num_list)
    flag=True
    for i in range(n-1):
        for j in range(n-1-i):
            if num_list[j]>num_list[j+1]:
                num_list[j],num_list[j+1]=num_list[j+1],num_list[j]
                flag=False
        if flag:
            break
def main():
    num_list=[1,2,3,4,5,8,7,6,3,2,1]
    print('original list: ', num_list)
    bubble_sort(num_list)
    print('sorted list: ', num_list)

if __name__=='__main__':
    main()
