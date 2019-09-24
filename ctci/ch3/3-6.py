import unittest


class Stack:
    def __init__(self):
        self.values = []
        self.is_empty = True
        self.size = 0

    def push(self, value):
        self.values.append(value)
        self.size += 1
        self.is_empty = False

    def pop(self):
        if not self.is_empty:
            self.size -= 1
            if self.size == 0:
                self.is_empty = True
            return self.values.pop()


class Queue:
    def __init__(self):
        self.stack_one = Stack()
        self.stack_two = Stack()
        self.size = 0

    def enqueue(self, value):
        self.stack_one.push(value)
        self.size += 1

    def dequeue(self):
        if self.size > 0:
            current_val = None

            while not self.stack_one.is_empty:
                current_val = self.stack_one.pop()
                self.stack_two.push(current_val)

            self.stack_two.pop()

            while not self.stack_two.is_empty:
                self.stack_one.push(self.stack_two.pop())

            return current_val

    def peek(self):
        if self.size > 0:
            val = self.stack_one.pop()
            self.stack_one.push(val)
            return val


class AnimalShelter:
    def __init__(self):
        self.dogs = Queue()
        self.cats = Queue()
        self.num_dogs = 0
        self.num_cats = 0

    def enqueue(self, is_dog, arrival_time, name):
        if is_dog:
            self.dogs.enqueue((name, arrival_time))
            self.num_dogs += 1
        else:
            self.cats.enqueue((name, arrival_time))
            self.num_cats += 1

    def dequeue_dog(self):
        if self.num_dogs > 0:
            self.num_dogs -= 1
            return self.dogs.dequeue()[0]

    def dequeue_cat(self):
        if self.num_cat > 0:
            self.num_cats -= 1
            return self.cats.dequeue()[0]

    def dequeue_any(self):
        if self.num_dogs > 0 and self.num_cats > 0:
            if self.dogs.peek()[1] < self.cats.peek()[1]:
                self.num_dogs -= 1
                return self.dogs.dequeue()[0]
            else:
                self.num_cats -= 1
                return self.cats.dequeue()[0]
        elif self.num_cats > 0:
            return self.cats.dequeue()[0]
        else:
            return self.dogs.dequeue()[0]


class TestSolution(unittest.TestCase):
    def test_animal_shelter(self):
        animal_shelter = AnimalShelter()
        animal_shelter.enqueue(True, 0, 'Charlie')
        animal_shelter.enqueue(False, 1, 'Kitty')
        animal_shelter.enqueue(True, 3, 'Lucky')
        animal_shelter.enqueue(False, 2, 'Feline')
        self.assertEqual(animal_shelter.dequeue_dog(), 'Charlie')
        self.assertEqual(animal_shelter.dequeue_any(), 'Kitty')
        self.assertEqual(animal_shelter.dequeue_any(), 'Feline')
        self.assertEqual(animal_shelter.dequeue_any(), 'Lucky')


if __name__ == '__main__':
    unittest.main()
