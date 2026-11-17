"""Existing finite abstract pickup/place planner, without grid geometry."""
from collections import deque


def plan_abstract(sites, initial_robot, initial_objects, object_goals):
    names = sorted(initial_objects)
    initial = (initial_robot, tuple(initial_objects[name] for name in names), None)
    previous = {initial: None}
    pending = deque([initial])
    while pending:
        state = pending.popleft()
        robot, places, held = state
        if held is None and all(places[names.index(name)] == target
                                for name, target in object_goals.items()):
            result = []
            while previous[state] is not None:
                state, action = previous[state]
                result.append(action)
            return result[::-1]
        alternatives = []
        for target in sites:
            if target != robot:
                alternatives.append(((target, places, held), ['move', target]))
        if held is None:
            for index, place in enumerate(places):
                if place == robot:
                    updated = list(places)
                    updated[index] = None
                    alternatives.append(((robot, tuple(updated), index), ['pick', names[index]]))
        else:
            updated = list(places)
            updated[held] = robot
            alternatives.append(((robot, tuple(updated), None), ['place', names[held]]))
        for other, action in alternatives:
            if other not in previous:
                previous[other] = state, action
                pending.append(other)
    return None
