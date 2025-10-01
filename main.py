class Stack:
    def __init__(self):
        self.items = []   # ใช้ list เป็นตัวเก็บข้อมูล

    def push(self, item):
        self.items.append(item)   # เพิ่มค่าที่ท้าย list

    def pop(self):
        if not self.is_empty():
            return self.items.pop()   # ลบตัวท้ายออก
        else:
            return "Stack is empty!"

    def peek(self):
        if not self.is_empty():
            return self.items[-1]   # ดูตัวท้าย แต่ไม่ลบ
        else:
            return "Stack is empty!"

    def is_empty(self):
        return len(self.items) == 0   # True ถ้าว่าง

    def size(self):
        return len(self.items)   # คืนจำนวนสมาชิก


# --------- ทดสอบ ---------
s = Stack()

# Push ค่า 1–5 เข้าไป
for i in range(1, 6):
    s.push(i)

print("Is empty?", s.is_empty())
print("Size after push:", s.size())
print("Top element:", s.peek())

print("Pop:", s.pop())
print("Pop:", s.pop())
print("Pop:", s.pop())
print("Pop:", s.pop())
print("Pop:", s.pop())

print("Is empty?", s.is_empty())
print("Pop from empty:", s.pop())