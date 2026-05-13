import sys
from store.SqliteTodoStore import SqliteTodoStore
from service.todo_service import TodoService

store = SqliteTodoStore()
service = TodoService(store)

def print_usage():
    print("用法： ")
    print(" add <title>")
    print(" remove <id>")
    print(" list")
    print(" complete <id>")
    print(" update <id> <title>")
    print(" delete")
if len(sys.argv) < 2:
    print_usage()
    sys.exit(1)


command = sys.argv[1]
    
if command == "add":
    if len(sys.argv) < 3:
        print("错误：缺少 title")
        sys.exit(1)
    service.add(sys.argv[2])

elif command == "remove":
    if len(sys.argv) < 3:
        print("错误：缺少 id")
        sys.exit(1)
    try:
        id = int(sys.argv[2])
    except ValueError:
        print("错误：id 必须是数字")
        sys.exit(1)
    success = service.remove(id)
    if not success:
        print("找不到todo对象")
    
    
elif command =="list":
    for todo in service.list():
        print(todo)

elif command == "complete":
    if len(sys.argv) < 3:
        print("错误：缺少 id")
        sys.exit(1)
    try:
        id = int(sys.argv[2])
    except ValueError:
        print("错误：id 必须是数字")
        sys.exit(1)

    success = service.complete(id)
    if not success:
        print("找不到todo对象")

elif command == "update":
    if len(sys.argv) < 4:
        print("错误：缺少参数")
        sys.exit(1)
    try:
        id = int(sys.argv[2])
    except ValueError:
        print("错误：id 必须是数字")
        sys.exit(1)

    title = sys.argv[3]
    success = service.update(id,title)
    if not success:
        print("找不到todo对象")

elif command == "delete":
        service.delete_all()

else:
    print("未知命令")
    print_usage()



