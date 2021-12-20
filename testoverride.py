class Parent:
	def __init__(self) -> None:
		pass

	def test(self):
		print("parent")


class Child(Parent):
	def __init__(self) -> None:
		super().__init__()

	def test(self, string):
		print("this is child")


child = Child()
child.test("t")
parent = Parent()
parent.test()