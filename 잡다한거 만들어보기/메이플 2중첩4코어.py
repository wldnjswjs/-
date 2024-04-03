from itertools import permutations


# list 안의 list로 저장
def create_list_of_lists():
  num_1 = input("Enter the first name:")
  num_2 = input("Enter the second name:")
  num_3 = input("Enter the third name:")
  num_4 = input("Enter the fourth name:")
  num_5 = input("Enter the fifth name:")
  num_6 = input("Enter the sixth name:")
  convert_to_number = {
      1: num_1,
      2: num_2,
      3: num_3,
      4: num_4,
      5: num_5,
      6: num_6
  }

  print(
      f"Convert your name to number with following dictionary. {convert_to_number}"
  )
  return convert_to_number

create_list_of_lists()



lists_of_lists = [
  [1, 2, 3], [3, 6, 1], [2, 4, 5], [1, 5, 3], [6, 3, 4],
  [4, 1, 2], [2, 5, 6], [3, 1, 4], [5, 2, 6], [6, 3, 1],
  [1, 4, 6], [3, 5, 2], [2, 6, 4], [1, 3, 5], [4, 2, 6],
  [6, 5, 1], [2, 3, 4], [1, 6, 2], [5, 3, 4], [4, 1, 5],
  [3, 6, 2], [2, 4, 1], [1, 5, 6], [6, 2, 3], [3, 1, 2],
  [5, 4, 6], [4, 3, 2], [2, 6, 5], [1, 4, 3], [5, 1, 6]
]
'''

def get_lists(lists_of_lists):
  while True:
    user_input = input(
        "Enter a list of 3 numbers separated by space (or 'done' to finish): ")

    if user_input.lower() == 'done':
      break

    user_list = user_input.split()

    if len(user_list) != 3:
      print("Invalid input. Please enter exactly 3 numbers.")
      continue

    try:
      user_list = list(map(int, user_list))
    except ValueError:
      print("Invalid input. Please enter numeric values.")
      continue

    lists_of_lists.append(user_list)
  return lists_of_lists


get_lists(lists_of_lists)
'''

# 2중첩 inspector
def condition_no2_inspector(flattened_list, target_number, target_count):
  if flattened_list.count(target_number) == target_count:
    return False
  return True


# 2중첩(condition2) inspector
def condition_no2(flattened_list):
  target_count = 3
  for target_number in range(1, 7):
    if not condition_no2_inspector(flattened_list, target_number, target_count):
      break
  else:
    return True
  return False


def calculating_function(lists_of_lists):
  for i in range(len(lists_of_lists)):
    print(f"picked list : {lists_of_lists[i]}")
    first_picked_list = lists_of_lists[i]
    print(f"First picked list : {first_picked_list}")

    for j in range(i + 1, len(lists_of_lists)):
      print(f"Second picked list : {lists_of_lists[j]}")

      if first_picked_list[0] == lists_of_lists[j][0]:
        print(":(")
      else:
        print("Keep going")

        for k in range(j + 1, len(lists_of_lists)):
          print(f"Third picked list : {lists_of_lists[k]}")

          if first_picked_list[0] == lists_of_lists[k][0] or lists_of_lists[j][
              0] == lists_of_lists[k][0]:
            print(":(")
          else:
            print("finish")
            inspecting_3lists = [
                first_picked_list, lists_of_lists[j], lists_of_lists[k]
            ]
            flattened_list = [
                item for sublist in inspecting_3lists for item in sublist
            ]
            print(flattened_list)

            if condition_no2(flattened_list) == False:
              print("duplicated3")
            else:
              print("Keep going")

              for l in range(k + 1, len(lists_of_lists)):
                print(f"Fourth picked list : {lists_of_lists[l]}")

                if first_picked_list[0] == lists_of_lists[l][
                    0] or lists_of_lists[j][0] == lists_of_lists[l][
                        0] or lists_of_lists[k][0] == lists_of_lists[l][0]:
                  print("Same number in the same list")
                else:
                  print("Keep going")
                  inspecting_4lists = [
                      first_picked_list, lists_of_lists[j], lists_of_lists[k],
                      lists_of_lists[l]
                  ]
                  flattened_list = [
                      item for sublist in inspecting_4lists for item in sublist
                  ]

                  if condition_no2(flattened_list) == False:
                    print("duplicated4")
                  else:
                    result_list = [
                        first_picked_list, lists_of_lists[j],
                        lists_of_lists[k], lists_of_lists[l]
                    ]
                    print("Picked!")
                    result.append(result_list)


result = []
calculating_function(lists_of_lists)
print(result)

'''
def convert_number_to_name(convert_to_nummber):
'''

  
  
