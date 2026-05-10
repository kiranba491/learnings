class NotImplemented(Exception):
    pass


class Action:
    _registry = {}
    
    @classmethod
    def register(cls, cls_name):
        def wrapper(obj):
            cls._registry[cls_name] = obj
        return wrapper
        
    @classmethod
    def create(cls, cls_name):
        try:
            return cls._registry[cls_name]
        except KeyError as error:
            raise NotImplemented(f"Class name {cls_name} not registered.")


@Action.register("test-action-1")
class TestAction1:
    def run():
        print("run - TestAction1")


@Action.register("test-action-2")
class TestAction2:
    def run():
        print("run - TestAction2")


print(Action._registry)

t1 = Action.create("test-action-1")
t1.run()

t2 = Action.create("test-action-2")
t2.run()

t3 = Action.create("test-action-3")
t3.run()
