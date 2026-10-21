import numpy as np

def is_valid(arr, num_books, num_students, max_allowed_pages):
    students = 1
    pages = 0

    for i in range(num_books):
        if arr[i] > max_allowed_pages:
            return False

        if pages + arr[i] <= max_allowed_pages:
            pages += arr[i]
        else:
            students += 1
            pages = arr[i]

    return students <= num_students

def allocate_books(arr, num_books, num_students):
    if num_students > num_books:
        return -1

    start = 0
    end = np.sum(arr)
    ans = -1

    while start <= end:
        mid = start + (end - start) // 2

        if is_valid(arr, num_books, num_students, mid):
            ans = mid
            end = mid - 1
        else:
            start = mid + 1

    return ans

num_books = int(input("Enter the number of books: "))
num_students = int(input("Enter the number of students: "))

user_input = input("Enter the pages of books separated by space: ")

user_list = [int(x) for x in user_input.split()]
arr = np.array(user_list)

if len(arr) != num_books:
    print(f"Error: You entered {len(arr)} elements, but specified {num_books}.")
else:
    result = allocate_books(arr, num_books, num_students)
    print(f"Minimum possible maximum pages: {result}")