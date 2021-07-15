def func_args(normal, *args, **student):
    print(normal)
    for item in args:
        print(item)

    for key, value in student.items():
        print(f"{key}  has a value {value}")


har = ["a", "b", "c", "d"]
var2 = {"a": 1, "b": 2}
var3 = " I am a DEVIL of my word"
func_args(var3, *har, **var2)
