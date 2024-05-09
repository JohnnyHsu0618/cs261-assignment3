# Name:CHE-HAN HSU
# OSU Email:hsuche@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment:assignment 2
# Due Date: 29,04,2024
# Description:This program a DynamicArray which adds functionality to the underlying StaticArray


from static_array import StaticArray


class DynamicArrayException(Exception):
    """
    Custom exception class to be used by Dynamic Array
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class DynamicArray:
    def __init__(self, start_array=None):
        """
        Initialize new dynamic array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._size = 0
        self._capacity = 4
        self._data = StaticArray(self._capacity)

        # populate dynamic array with initial values (if provided)
        # before using this feature, implement append() method
        if start_array is not None:
            for value in start_array:
                self.append(value)

    def __str__(self) -> str:
        """
        Return content of dynamic array in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "DYN_ARR Size/Cap: "
        out += str(self._size) + "/" + str(self._capacity) + ' ['
        out += ', '.join([str(self._data[_]) for _ in range(self._size)])
        return out + ']'

    def __iter__(self):
        """
        Create iterator for loop
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._index = 0
        return self

    def __next__(self):
        """
        Obtain next value and advance iterator
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        try:
            value = self[self._index]
        except DynamicArrayException:
            raise StopIteration

        self._index += 1
        return value

    def get_at_index(self, index: int) -> object:
        """
        Return value from given index position
        Invalid index raises DynamicArrayException
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if index < 0 or index >= self._size:
            raise DynamicArrayException
        return self._data[index]

    def set_at_index(self, index: int, value: object) -> None:
        """
        Store value at given index in the array
        Invalid index raises DynamicArrayException
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        print("a,d,w,efe,fef")
        print(self._size,index,value)
        print(StaticArray)
        if index < 0 or index >= self._size:
            raise DynamicArrayException
        self._data[index] = value

    def __getitem__(self, index) -> object:
        """
        Same functionality as get_at_index() method above,
        but called using array[index] syntax
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.get_at_index(index)

    def __setitem__(self, index, value) -> None:
        """
        Same functionality as set_at_index() method above,
        but called using array[index] syntax
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.set_at_index(index, value)

    def is_empty(self) -> bool:
        """
        Return True is array is empty / False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._size == 0

    def length(self) -> int:
        """
        Return number of elements stored in array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._size

    def get_capacity(self) -> int:
        """
        Return the capacity of the array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._capacity

    def print_da_variables(self) -> None:
        """
        Print information contained in the dynamic array.
        Used for testing purposes.
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        print(f"Length: {self._size}, Capacity: {self._capacity}, {self._data}")

    # -----------------------------------------------------------------------

    def resize(self, new_capacity: int) -> None:


        if new_capacity <= 0 or new_capacity < self._size:  # Exit if new_capacity is not positive or less than current size
            return

        resized_array = StaticArray(new_capacity)  # Create a new array with the specified capacity

        for curr_index in range(self.length()):
            resized_array.set(curr_index, self.get_at_index(curr_index))

        self._capacity = new_capacity  # update
        self._data = resized_array  #update




    def append(self, value: object) -> None:

        if self._size >= self._capacity:     # Double the capacity if the internal storage is full or less
            self._resize(2 * self._capacity)

        self._size += 1
        self.set_at_index(self._size , value)  # Add the new value at the end of the array



    def insert_at_index(self, index: int, value: object) -> None:

        if not (0 <= index <= self.length):
            raise DynamicArrayException

        if self.length >= self.cap_acity:
            self.resize(2 * self.capacity)  # Double the capacity


        for i in range(self.length, index, -1):    # Shift elements to make space for the new value
            self.data[i] = self.data[i - 1]


        self.data[index] = value   # Insert the new value



    def remove_at_index(self, index: int) -> None:

            if index < 0 or index >= self._size:   # Check if the provided index is valid
                raise DynamicArrayException


            if self._size < self._capacity // 4 and self._capacity > 10:  # Check if capacity reduction is needed
                new_capacity = max(10, 2 * self._size)
                self._resize(new_capacity)


            for i in range(index, self._size - 1):  # Remove the element at the specified index
                self._data.set(i, self._data.get(i + 1))


            self._size -= 1   # Decrement the size of the dynamic array






    def slice(self, start_index: int, size: int) -> "DynamicArray":
        if start_index < 0 or start_index >= self._size:   # Check if the provided start index is valid
            raise DynamicArrayException


        if size < 0:                      # Check if the provided size is valid
            raise DynamicArrayException


        if start_index + size > self._size:   # Check if there are enough elements from the start index to the end of the array
            raise DynamicArrayException


        sliced_array = DynamicArray(size)               # Create a new DynamicArray object to store the slice
        for i in range(start_index, start_index + size):
            sliced_array.append(self._data.get(i))

        return sliced_array




    def map(self, map_func) -> "DynamicArray":

        mapped_array = DynamicArray(self._size)  # Create a new DynamicArray object to store the mapped values
        for i in range(self._size):
            mapped_array.append(map_func(self._data.get(i)))

            return mapped_array



    def filter(self, filter_func) -> "DynamicArray":

        filtered_array = DynamicArray()  # Create a new DynamicArray object to store the filtered values

        for i in range(self._size):
            if filter_func(self._data.get(i)):
                filtered_array.append(self._data.get(i))

        return filtered_array



    def reduce(self, reduce_func, initializer=None) -> object:

        if not dynamic_array:
            return initializer  # Return initializer (or None if not provided)

        result = dynamic_array[0] if initializer is None else initializer
        for element in dynamic_array[1:]:
            result = reduce_func(result, element)

        return result




def chunk(arr: DynamicArray) -> "DynamicArray":
    chunks = []  # Initialize a list to store the chunked subsequences
    current_chunk = DynamicArray()  # Initialize a DynamicArray to store the current subsequence

    for i in range(input_array.length()):  # Iterate over the values in the input DynamicArray
        value = input_array.get_at_index(i)

        # If the current_chunk is empty or the current value is greater than or equal to the last value in current_chunk,
        # append the value to current_chunk
        if current_chunk.length() == 0 or value >= current_chunk.get_at_index(
                -1):  # If the current_chunk is empty or the current value is greater than or equal to the last value in current_chunk,append the value to current_chunk
            current_chunk.append(value)


        else:  # If the current value is less than the last value in current_chunk, append current_chunk to chunks and start a new subsequence
            chunks.append(current_chunk)
            current_chunk = DynamicArray()
            current_chunk.append(value)

    chunks.append(current_chunk)  # Append the last subsequence to chunks

    chunked_array = DynamicArray(len(chunks))  # Convert the list of subsequences to a DynamicArray
    for chunk in chunks:
        chunked_array.append(chunk)

    return chunked_array





def find_mode(arr: DynamicArray) -> tuple[DynamicArray, int]:
    mode = DynamicArray()
    max_frequency = 0
    current_value = None
    current_frequency = 0

    for i in range(input_array.length()):  # Iterate over the values in the input DynamicArray
        value = input_array.get_at_index(i)

        if value != current_value:  # If it's a different value than the current one, update current_value and reset current_frequency
            current_value = value
            current_frequency = 1
        else:
            current_frequency += 1

        if current_frequency > max_frequency:  # Update mode and max_frequency if current_frequency is greater
            mode = DynamicArray()
            mode.append(current_value)
            max_frequency = current_frequency
        elif current_frequency == max_frequency:
            mode.append(current_value)

    return (mode, max_frequency)



# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# resize - example 1")
    da = DynamicArray()

    # print dynamic array's size, capacity and the contents
    # of the underlying static array (data)
    da.print_da_variables()
    da.resize(8)
    da.print_da_variables()
    da.resize(2)
    da.print_da_variables()
    da.resize(0)
    da.print_da_variables()

    print("\n# resize - example 2")
    da = DynamicArray([1, 2, 3, 4, 5, 6, 7, 8])
    print(da)
    da.resize(20)
    print(da)
    da.resize(4)
    print(da)

    print("\n# append - example 1")
    da = DynamicArray()
    da.print_da_variables()
    da.append(1)
    da.print_da_variables()
    print(da)

    print("\n# append - example 2")
    da = DynamicArray()
    for i in range(9):
        da.append(i + 101)
        print(da)

    print("\n# append - example 3")
    da = DynamicArray()
    for i in range(600):
        da.append(i)
    print(da.length())
    print(da.get_capacity())

    print("\n# insert_at_index - example 1")
    da = DynamicArray([100])
    print(da)
    da.insert_at_index(0, 200)
    da.insert_at_index(0, 300)
    da.insert_at_index(0, 400)
    print(da)
    da.insert_at_index(3, 500)
    print(da)
    da.insert_at_index(1, 600)
    print(da)

    print("\n# insert_at_index example 2")
    da = DynamicArray()
    try:
        da.insert_at_index(-1, 100)
    except Exception as e:
        print("Exception raised:", type(e))
    da.insert_at_index(0, 200)
    try:
        da.insert_at_index(2, 300)
    except Exception as e:
        print("Exception raised:", type(e))
    print(da)

    print("\n# insert at index example 3")
    da = DynamicArray()
    for i in range(1, 10):
        index, value = i - 4, i * 10
        try:
            da.insert_at_index(index, value)
        except Exception as e:
            print("Cannot insert value", value, "at index", index)
    print(da)

    print("\n# remove_at_index - example 1")
    da = DynamicArray([10, 20, 30, 40, 50, 60, 70, 80])
    print(da)
    da.remove_at_index(0)
    print(da)
    da.remove_at_index(6)
    print(da)
    da.remove_at_index(2)
    print(da)

    print("\n# remove_at_index - example 2")
    da = DynamicArray([1024])
    print(da)
    for i in range(17):
        da.insert_at_index(i, i)
    print(da.length(), da.get_capacity())
    for i in range(16, -1, -1):
        da.remove_at_index(0)
    print(da)

    print("\n# remove_at_index - example 3")
    da = DynamicArray()
    print(da.length(), da.get_capacity())
    [da.append(1) for i in range(100)]  # step 1 - add 100 elements
    print(da.length(), da.get_capacity())
    [da.remove_at_index(0) for i in range(68)]  # step 2 - remove 68 elements
    print(da.length(), da.get_capacity())
    da.remove_at_index(0)  # step 3 - remove 1 element
    print(da.length(), da.get_capacity())
    da.remove_at_index(0)  # step 4 - remove 1 element
    print(da.length(), da.get_capacity())
    [da.remove_at_index(0) for i in range(14)]  # step 5 - remove 14 elements
    print(da.length(), da.get_capacity())
    da.remove_at_index(0)  # step 6 - remove 1 element
    print(da.length(), da.get_capacity())
    da.remove_at_index(0)  # step 7 - remove 1 element
    print(da.length(), da.get_capacity())

    for i in range(14):
        print("Before remove_at_index(): ", da.length(), da.get_capacity(), end="")
        da.remove_at_index(0)
        print(" After remove_at_index(): ", da.length(), da.get_capacity())

    print("\n# remove at index - example 4")
    da = DynamicArray([1, 2, 3, 4, 5])
    print(da)
    for _ in range(5):
        da.remove_at_index(0)
        print(da)

    print("\n# slice example 1")
    da = DynamicArray([1, 2, 3, 4, 5, 6, 7, 8, 9])
    da_slice = da.slice(1, 3)
    print(da, da_slice, sep="\n")
    da_slice.remove_at_index(0)
    print(da, da_slice, sep="\n")

    print("\n# slice example 2")
    da = DynamicArray([10, 11, 12, 13, 14, 15, 16])
    print("SOURCE:", da)
    slices = [(0, 7), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3), (6, 1), (6, -1)]
    for i, cnt in slices:
        print("Slice", i, "/", cnt, end="")
        try:
            print(" --- OK: ", da.slice(i, cnt))
        except:
            print(" --- exception occurred.")

    print("\n# map example 1")
    da = DynamicArray([1, 5, 10, 15, 20, 25])
    print(da)
    print(da.map(lambda x: x ** 2))

    print("\n# map example 2")


    def double(value):
        return value * 2


    def square(value):
        return value ** 2


    def cube(value):
        return value ** 3


    def plus_one(value):
        return value + 1


    da = DynamicArray([plus_one, double, square, cube])
    for value in [1, 10, 20]:
        print(da.map(lambda x: x(value)))

    print("\n# filter example 1")


    def filter_a(e):
        return e > 10


    da = DynamicArray([1, 5, 10, 15, 20, 25])
    print(da)
    result = da.filter(filter_a)
    print(result)
    print(da.filter(lambda x: (10 <= x <= 20)))

    print("\n# filter example 2")


    def is_long_word(word, length):
        return len(word) > length


    da = DynamicArray("This is a sentence with some long words".split())
    print(da)
    for length in [3, 4, 7]:
        print(da.filter(lambda word: is_long_word(word, length)))

    print("\n# reduce example 1")
    values = [100, 5, 10, 15, 20, 25]
    da = DynamicArray(values)
    print(da)
    print(da.reduce(lambda x, y: (x // 5 + y ** 2)))
    print(da.reduce(lambda x, y: (x + y ** 2), -1))

    print("\n# reduce example 2")
    da = DynamicArray([100])
    print(da.reduce(lambda x, y: x + y ** 2))
    print(da.reduce(lambda x, y: x + y ** 2, -1))
    da.remove_at_index(0)
    print(da.reduce(lambda x, y: x + y ** 2))
    print(da.reduce(lambda x, y: x + y ** 2, -1))

    def print_chunked_da(arr: DynamicArray):
        if len(str(arr)) <= 100:
            print(arr)
        else:
            print(f"DYN_ARR Size/Cap: {arr.length()}/{arr.get_capacity()}")
            print('[\n' + ',\n'.join(f'\t{chunk}' for chunk in arr) + '\n]')

    print("\n# chunk example 1")
    test_cases = [
        [10, 20, 30, 30, 5, 10, 1, 2, 3, 4],
        ['App', 'Async', 'Cloud', 'Data', 'Deploy',
         'C', 'Java', 'Python', 'Git', 'GitHub',
         'Class', 'Method', 'Heap']
    ]

    for case in test_cases:
        da = DynamicArray(case)
        chunked_da = chunk(da)
        print(da)
        print_chunked_da(chunked_da)

    print("\n# chunk example 2")
    test_cases = [[], [261], [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]]

    for case in test_cases:
        da = DynamicArray(case)
        chunked_da = chunk(da)
        print(da)
        print_chunked_da(chunked_da)

    print("\n# find_mode - example 1")
    test_cases = (
        [1, 1, 2, 3, 3, 4],
        [1, 2, 3, 4, 5],
        ["Apple", "Banana", "Banana", "Carrot", "Carrot",
         "Date", "Date", "Date", "Eggplant", "Eggplant", "Eggplant",
         "Fig", "Fig", "Grape"]
    )

    for case in test_cases:
        da = DynamicArray(case)
        mode, frequency = find_mode(da)
        print(f"{da}\nMode: {mode}, Frequency: {frequency}\n")

    case = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
    da = DynamicArray()
    for x in range(len(case)):
        da.append(case[x])
        mode, frequency = find_mode(da)
        print(f"{da}\nMode: {mode}, Frequency: {frequency}")

