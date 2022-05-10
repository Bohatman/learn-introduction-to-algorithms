

import logging
import sys
logging.basicConfig(level=logging.DEBUG)
def merge_sort(array: list,start,end):
    if start < end:
        logging.debug(f"Input is {array} with arguments p={start} r={end}")
        half = (end + start) / 2
        half = int(half)
        merge_sort(array,start,half)
        merge_sort(array,half +1,end)
        merge(array,start,half,end)

def merge(array: list, start: int, half: int, end: int):
    logging.debug(f"Input is {array} with arguments p={start} half={half} r={end}")
    first_half_length = (half-start) + 1
    second_half_length = (end - half) +1
    first_half = array[start: start + first_half_length]
    # first_half.append(sys.maxsize)
    second_half = array[half +1 :half + second_half_length]
    # second_half.append(sys.maxsize)
    logging.debug(f"Source array is {array}")
    logging.debug(f"Frist half is {first_half}")
    logging.debug(f"Second half is {second_half}")
    i = j = 0        
    for k in range(start,end + 1):
        if i >= len(first_half):
            array[k] = second_half[j]
            j += 1
        elif j >= len(second_half):
            array[k] = first_half[i]
            i += 1
        elif first_half[i] <= second_half[j]:
            array[k] = first_half[i]
            i += 1
        else:
            array[k] = second_half[j]
            j += 1
    logging.debug(f"Result array is {array}")

# Input is [0, 1, 1, 2, 2, 3, 3, 4, 3, 4, 123, 4123, 4123, 22, 12, 334, 1123] with arguments p=12 r=13
# Input is [0, 1, 1, 2, 2, 3, 3, 4, 3, 4, 123, 4123, 4123, 22, 12, 334, 1123] with arguments p=12 half=12 r=13
# Source array is [0, 1, 1, 2, 2, 3, 3, 4, 3, 4, 123, 4123, 4123, 22, 12, 334, 1123]
# Frist half is [4123, 9223372036854775807]
# Second half is [22, 9223372036854775807]
# Result array is [0, 1, 1, 2, 2, 3, 3, 4, 3, 4, 123, 4123, 22, 22, 12, 334, 1123]
input = [0, 1, 1, 2, 2, 3, 3, 4, 3, 4, 123, 4123, 4123, 22, 12, 334, 1123] 
merge_sort(input,0,len(input) -1)
# merge(input,12,12,13)